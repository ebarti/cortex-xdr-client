import gzip
import hashlib
import json
import re
from pathlib import Path

import pytest
import requests

from cortex_xdr_client.api.authentication import Authentication, AuthenticationType
from cortex_xdr_client.api.models.alerts import AlertSeverity
from cortex_xdr_client.api.models.endpoints import EndpointPlatform, EndpointStatus, IsolateStatus, ScanStatus
from cortex_xdr_client.api.models.exceptions import UnsuccessfulQueryStatusException
from cortex_xdr_client.api.models.ioc import IoC, IoCSeverity
from cortex_xdr_client.api.version import APIVersion
from cortex_xdr_client.client import CortexXDRClient


ORIGIN = 'https://api-tenant.example.com'
FIXTURES = Path(__file__).parent / 'fixtures'
RESPONSES = json.loads((FIXTURES / 'core_responses.json').read_text())
OPERATIONS = json.loads((FIXTURES / 'openapi_operations.json').read_text())


def documented_operation(version, path, method):
    return any(method in methods and re.fullmatch(re.sub(r'\{[^}]+\}', '[^/]+', template), path)
               for spec in OPERATIONS if spec['product_version'] == version
               for template, methods in spec['operations'].items())


@pytest.fixture(params=[3, 5])
def client(request, auth):
    return CortexXDRClient(auth, 'tenant.example.com', api_version=request.param)


@pytest.mark.parametrize('fqdn', ['tenant.example.com', 'api-tenant.example.com',
                                  'https://api-tenant.example.com/'])
def test_tenant_and_default_version(fqdn, auth, requests_mock):
    client = CortexXDRClient(auth, fqdn)
    requests_mock.post(ORIGIN + '/public_api/v1/endpoints/get_endpoints', json={'reply': []})
    assert client.api_version == APIVersion.V3
    assert client.endpoints_api.get_all_endpoints().reply == []


@pytest.mark.parametrize('version', [0, 1, 4, 6, 'v5', None])
def test_invalid_version(version, auth):
    with pytest.raises(ValueError):
        CortexXDRClient(auth, 'tenant.example.com', api_version=version)


@pytest.mark.parametrize('fqdn', ['http://tenant.example.com', 'https://tenant.example.com/path',
                                  'https://user:secret@tenant.example.com', 'tenant.example.com/path', ''])
def test_invalid_tenant(fqdn, auth):
    with pytest.raises(ValueError):
        CortexXDRClient(auth, fqdn)


def test_version_guards(auth, requests_mock):
    v3 = CortexXDRClient(auth, 'tenant.example.com')
    v5 = CortexXDRClient(auth, 'tenant.example.com', api_version=5)
    for call, hint in [(v5.alerts_api.get_alerts, 'issues_api'),
                       (v5.incidents_api.get_incidents, 'cases_api'),
                       (v3.cases_api.get_cases, '5.x'),
                       (v3.issues_api.get_issues, '5.x'),
                       (lambda: v3.issues_api.create_issue({}), '5.x'),
                       (lambda: v5.incidents_api.get_incident_extra_data('1'), 'cases_api')]:
        with pytest.raises(NotImplementedError, match=hint):
            call()
    assert not requests_mock.called


@pytest.mark.parametrize('auth_type', list(AuthenticationType))
def test_authentication_headers(auth_type, client, requests_mock):
    auth = Authentication('test-key', 12, auth_type)
    client = CortexXDRClient(auth, 'tenant.example.com', api_version=client.api_version)
    requests_mock.post(ORIGIN + '/public_api/v1/endpoints/get_endpoints', json={'reply': []})
    client.endpoints_api.get_all_endpoints()
    first = requests_mock.last_request.headers
    assert first['x-xdr-auth-id'] == '12'
    if auth_type == AuthenticationType.STANDARD:
        assert first['Authorization'] == 'test-key'
    else:
        assert len(first['x-xdr-nonce']) == 64
        assert len(first['x-xdr-timestamp']) == 13
        value = 'test-key' + first['x-xdr-nonce'] + first['x-xdr-timestamp']
        assert first['Authorization'] == hashlib.sha256(value.encode()).hexdigest()
        client.endpoints_api.get_all_endpoints()
        assert requests_mock.last_request.headers['x-xdr-nonce'] != first['x-xdr-nonce']


# These URLs and examples come from the vendor specs, independently of _get_url.
@pytest.mark.parametrize('api,method,call,args,example', [
    ('endpoints', 'get_all_endpoints', 'get_endpoints', (), 'example-1'),
    ('endpoints', 'get_endpoint', 'get_endpoint', (), None),
    ('endpoints', 'isolate_endpoints', 'isolate', (['endpoint'],), 'Example 1'),
    ('endpoints', 'unisolate_endpoints', 'unisolate', (['endpoint'],), 'example-1'),
    ('endpoints', 'quarantine_file', 'quarantine', (['endpoint'], '/tmp/test', 'a' * 64), 'example-1'),
    ('actions', 'get_action_status', 'get_action_status', (1,), 'example-1'),
    ('actions', 'get_file_retrieval_details', 'file_retrieval_details', (1,), 'Example 1'),
    ('scripts', 'get_scripts', 'get_scripts', (), 'example-1'),
    ('scripts', 'get_script_metadata', 'get_script_metadata', ('script',), 'When entry_point is returned as run'),
    ('scripts', 'get_script_execution_status', 'get_script_execution_status', (1,), 'example-1'),
    ('scripts', 'get_script_execution_results', 'get_script_execution_results', (1,), 'example-1'),
    ('scripts', 'get_script_execution_result_files', 'get_script_execution_results_files', (1, 'endpoint'), 'example-1'),
    ('scripts', 'run_script', 'run_script', ('script', {}, ['endpoint']), 'example-1'),
    ('scripts', 'run_snippet_code_script', 'run_snippet_code_script', ('print(1)', ['endpoint']), 'example-1'),
    ('xql', 'start_xql_query', 'start_xql_query', ('dataset = xdr_data',), 'Example 1'),
    ('xql', 'get_query_results', 'get_query_results', ('query',), 'Up to 1,000 results, JSON format, Single Tenant Investigation'),
])
def test_current_core_examples(client, requests_mock, api, method, call, args, example):
    version = str(client.api_version.value)
    path = '/public_api/v1/' + api + '/' + call
    if example is None:
        example = 'Example 2' if version == '3' else 'Example 1'
    assert documented_operation(int(version), path, 'post')
    response = RESPONSES[version][path][example]
    requests_mock.post(ORIGIN + path, json=response)
    result = getattr(getattr(client, api + '_api'), method)(*args)
    assert result is not None
    if method == 'get_endpoint':
        endpoint = result.reply.endpoints[0]
        assert endpoint.endpoint_id == response['reply']['endpoints'][0]['endpoint_id']
        assert endpoint.operating_system == response['reply']['endpoints'][0]['operating_system']
        if version == '5':
            assert endpoint.operational_status_details == response['reply']['endpoints'][0]['operational_status_details']
    if method.startswith('run_'):
        assert 'incident_id' not in requests_mock.last_request.json()['request_data']


def test_alert_severity(auth, requests_mock):
    client = CortexXDRClient(auth, 'tenant.example.com')
    requests_mock.post(ORIGIN + '/public_api/v1/alerts/get_alerts_multi_events',
                       json={'reply': {'alerts': [{'alert_id': '12', 'severity': 'critical', 'description': 'test', 'events': []}]}})
    result = client.alerts_api.get_alerts(severities=[AlertSeverity.HIGH, AlertSeverity.CRITICAL], search_from=0)
    assert result.reply.alerts[0].severity == AlertSeverity.CRITICAL
    assert requests_mock.last_request.json() == {'request_data': {
        'filters': [{'field': 'severity', 'operator': 'in', 'value': ['high', 'critical']}], 'search_from': 0}}


def test_endpoint_filters(client, requests_mock):
    requests_mock.post(ORIGIN + '/public_api/v1/endpoints/get_endpoint', json={'reply': {'endpoints': []}})
    client.endpoints_api.get_endpoint(endpoint_status=[EndpointStatus.uninstalled],
                                      platform=[EndpointPlatform.windows], isolate=[IsolateStatus.unisolated],
                                      scan_status=[ScanStatus.none], public_ip_list=['192.0.2.1'])
    filters = {f['field']: f['value'] for f in requests_mock.last_request.json()['request_data']['filters']}
    assert filters == {'endpoint_status': ['uninstalled'], 'platform': ['windows'],
                       'isolate': ['unisolated'], 'scan_status': ['none'], 'public_ip_list': ['192.0.2.1']}


def test_cloud_filters(auth, requests_mock):
    v5 = CortexXDRClient(auth, 'tenant.example.com', api_version=5)
    requests_mock.post(ORIGIN + '/public_api/v1/endpoints/get_endpoint', json={'reply': {'endpoints': []}})
    v5.endpoints_api.get_endpoint(cloud_provider=['aws'], cloud_region=['us-east-1'])
    assert requests_mock.last_request.json()['request_data']['filters'] == [
        {'field': 'cloud_provider', 'operator': 'in', 'value': ['aws']},
        {'field': 'cloud_region', 'operator': 'in', 'value': ['us-east-1']}]
    with pytest.raises(NotImplementedError):
        CortexXDRClient(auth, 'tenant.example.com').endpoints_api.get_endpoint(cloud_provider=['aws'])


def test_retrieve_file_payload(client, requests_mock):
    requests_mock.post(ORIGIN + '/public_api/v1/endpoints/file_retrieval', json={'reply': {'action_id': '1'}})
    files = {'linux': ['/tmp/file']}
    client.endpoints_api.retrieve_file(['endpoint'], files, '123')
    assert requests_mock.last_request.json() == {'request_data': {
        'filters': [{'field': 'endpoint_id_list', 'operator': 'in', 'value': ['endpoint']}],
        'files': files, 'incident_id': '123'}}
    assert files == {'linux': ['/tmp/file']}
    with pytest.raises(ValueError):
        client.endpoints_api.retrieve_file(['endpoint'], {'invalid': ['/tmp/file']})


def test_quarantine_payload(client, requests_mock):
    requests_mock.post(ORIGIN + '/public_api/v1/endpoints/quarantine', json={'reply': {'action_id': '1'}})
    client.endpoints_api.quarantine_file(['endpoint'], '/tmp/file', 'a' * 64, '123')
    body = requests_mock.last_request.json()
    assert body['request_data']['incident_id'] == '123'
    assert 'incident_id' not in body


def test_script_filters(client, requests_mock):
    requests_mock.post(ORIGIN + '/public_api/v1/scripts/get_scripts', json={'reply': {'scripts': []}})
    client.scripts_api.get_scripts(is_high_risk=False, windows_supported=True, modification_time=0)
    assert requests_mock.last_request.json() == {'request_data': {'filters': [
        {'field': 'modification_date', 'operator': 'lte', 'value': 0},
        {'field': 'windows_supported', 'operator': 'in', 'value': ['true']},
        {'field': 'is_high_risk', 'operator': 'in', 'value': ['false']}]}}
    client.scripts_api.get_scripts()
    expected = {'filters': ['all']} if client.api_version == APIVersion.V3 else {}
    assert requests_mock.last_request.json() == {'request_data': expected}


def test_script_output_for_every_endpoint(client, requests_mock):
    requests_mock.post(ORIGIN + '/public_api/v1/scripts/get_script_execution_results', json={'reply': {
        'results': [{'_return_value': None}, {'_return_value': ['second']}, {'_return_value': ''}]}})
    results = client.scripts_api.get_script_execution_results(1).results
    assert [result.standard_output for result in results] == [None, ['second'], '']


@pytest.mark.parametrize('wire_format', ['gzip-file', 'http-gzip', 'plain'])
def test_xql_stream_encoding(client, requests_mock, wire_format):
    data = b'{"row": 1}\n\n{"row": 2}\n'
    content = gzip.compress(data) if wire_format != 'plain' else data
    headers = {'Content-Encoding': 'gzip'} if wire_format == 'http-gzip' else {}
    requests_mock.post(ORIGIN + '/public_api/v1/xql/get_query_results_stream', content=content, headers=headers)
    assert client.xql_api.get_query_results_stream('stream') == {'data': [{'row': 1}, {'row': 2}]}


def test_xql_uses_stream_id_and_preserves_limit(client, requests_mock):
    requests_mock.post(ORIGIN + '/public_api/v1/xql/get_query_results', json={'reply': {
        'status': 'SUCCESS', 'number_of_results': 1, 'results': {'stream_id': 'stream'}}})
    requests_mock.post(ORIGIN + '/public_api/v1/xql/get_query_results_stream', content=b'{"row": 1}\n')
    assert client.xql_api.get_query_results('query', limit=2000) == {'data': [{'row': 1}]}
    assert requests_mock.request_history[0].json()['request_data']['limit'] == 2000


def test_xql_pending_status(client, requests_mock):
    requests_mock.post(ORIGIN + '/public_api/v1/xql/get_query_results', json={'reply': {'status': 'PENDING'}})
    with pytest.raises(UnsuccessfulQueryStatusException, match='PENDING'):
        client.xql_api.get_query_results('query')


def test_ioc_minimal_payload(client, requests_mock):
    requests_mock.post(ORIGIN + '/public_api/v1/indicators/insert_jsons', json={'reply': {'success': True}})
    indicator = IoC(indicator='192.0.2.1', type='IP', severity=IoCSeverity.informational)
    assert client.ioc_api.insert_json([indicator]).reply.success
    assert requests_mock.last_request.json() == {'request_data': [
        {'indicator': '192.0.2.1', 'type': 'IP', 'severity': 'INFO'}], 'validate': True}


def test_ioc_unknown_version_difference(auth, requests_mock):
    requests_mock.post(ORIGIN + '/public_api/v1/indicators/insert_jsons', json={'reply': True})
    indicator = IoC(indicator='192.0.2.1', type='IP', severity=IoCSeverity.unknown)
    assert CortexXDRClient(auth, 'tenant.example.com').ioc_api.insert_json([indicator], validate=False).reply is True
    assert requests_mock.last_request.json()['request_data'][0]['severity'] == 'unknown'
    with pytest.raises(ValueError):
        CortexXDRClient(auth, 'tenant.example.com', api_version=5).ioc_api.insert_json([indicator])
    assert requests_mock.call_count == 1


@pytest.mark.parametrize('value', ['file-id', '/public_api/v1/download/file-id',
                                   ORIGIN + '/public_api/v1/download/file-id'])
def test_download(client, requests_mock, value):
    requests_mock.post(ORIGIN + '/public_api/v1/download/file-id', content=b'zip-bytes')
    assert client.download_api.download_file(value) == b'zip-bytes'


def test_download_rejects_other_tenants(client, requests_mock):
    with pytest.raises(ValueError):
        client.download_api.download_file('https://api-other.example.com/public_api/v1/download/file')
    assert not requests_mock.called


@pytest.mark.parametrize('version,path,method,body,params', [
    (3, '/public_api/v1/brokers/', 'get', {'name': ['broker-eu-01']}, None),
    (5, '/public_api/v1/configurations/agent/content_management', 'post', None, None),
    (5, '/public_api/appsec/v1/application/app-1', 'delete', None, None),
    (5, '/public_api/appsec/v1/rules/rule-1', 'patch', {'labels': ['reviewed']}, None),
    (5, '/public_api/appsec/v1/repositories', 'get', None, {'limit': 10}),
    (5, '/public_api/v1/compliance/get_asset', 'post', {'request_data': {'asset_id': 'asset'}}, None),
    (5, '/platform/notifications/v1/update-rule-status/rule-1', 'patch', {'request_data': {'status': 'enable'}}, None),
    (5, '/public_api/v2/xql/delete_dataset', 'post', {'request_data': {'dataset_name': 'lookup'}}, None),
])
def test_additional_api_transports(auth, requests_mock, version, path, method, body, params):
    assert documented_operation(version, path, method)
    client = CortexXDRClient(auth, 'tenant.example.com', api_version=version)
    requests_mock.register_uri(method, ORIGIN + path, status_code=204)
    response = client.request(path, method=method.upper(), json_value=body, params=params)
    assert response.status_code == 204
    if body is not None:
        assert requests_mock.last_request.json() == body
    if params:
        assert requests_mock.last_request.qs == {'limit': ['10']}


def test_multipart_transport(client, requests_mock):
    requests_mock.post(ORIGIN + '/public_api/v1/indicators/insert_csv', json={'reply': True})
    client.request('/public_api/v1/indicators/insert_csv', files={'file': ('ioc.csv', b'indicator,type\n')})
    request = requests_mock.last_request
    assert request.headers['Content-Type'].startswith('multipart/form-data; boundary=')
    assert b'filename="ioc.csv"' in request.body
    assert b'indicator,type' in request.body


@pytest.mark.parametrize('method', ['get', 'post', 'put', 'patch', 'delete'])
def test_query_and_body_on_all_methods(client, requests_mock, method):
    requests_mock.register_uri(method, ORIGIN + '/public_api/test', json={})
    client.request('/public_api/test', method=method, params={'page': 2}, json_value={'data': 1})
    assert requests_mock.last_request.qs == {'page': ['2']}
    assert requests_mock.last_request.json() == {'data': 1}


@pytest.mark.parametrize('status', [400, 401, 403, 404, 429, 500])
def test_http_errors(client, requests_mock, status):
    requests_mock.get(ORIGIN + '/public_api/v1/healthcheck', status_code=status)
    with pytest.raises(requests.HTTPError) as exc:
        client.request('/public_api/v1/healthcheck', method='get')
    assert exc.value.response.status_code == status
    assert requests_mock.call_count == 1


@pytest.mark.parametrize('path', ['https://other.example/path', '//other.example/path',
                                  '/path?query=value', '/path#fragment', '/path/../other'])
def test_invalid_raw_path(client, requests_mock, path):
    with pytest.raises(ValueError):
        client.request(path)
    assert not requests_mock.called


def test_redirects_do_not_forward_credentials(client, requests_mock):
    requests_mock.post(ORIGIN + '/public_api/test', status_code=307,
                       headers={'Location': 'https://other.example/test'})
    with pytest.raises(requests.HTTPError, match='redirect'):
        client.request('/public_api/test')
    assert requests_mock.call_count == 1


def test_timeouts_propagate(auth, monkeypatch):
    def request(method, url, **kwargs):
        assert kwargs['timeout'] == (2, 7)
        raise requests.Timeout()
    monkeypatch.setattr(requests, 'request', request)
    client = CortexXDRClient(auth, 'tenant.example.com', (2, 7), api_version=5)
    with pytest.raises(requests.Timeout):
        client.endpoints_api.get_all_endpoints()


@pytest.mark.parametrize('script_id', [12, '0012', 'script-uuid'])
def test_script_id_types_preserved(client, requests_mock, script_id):
    requests_mock.post(ORIGIN + '/public_api/v1/scripts/get_script_metadata', json={'reply': {'script_id': script_id}})
    result = client.scripts_api.get_script_metadata('uid')
    assert result.script_id == script_id
    assert type(result.script_id) is type(script_id)


def test_conflicting_body_types_rejected(client, requests_mock):
    with pytest.raises(ValueError, match='either'):
        client.request('/public_api/test', json_value={'a': 1}, data={'b': 2})
    assert not requests_mock.called
