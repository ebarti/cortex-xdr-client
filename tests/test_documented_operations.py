"""Exercise every indexed operation through its public client entry point.

Expected paths, fields, and success media come from the pinned GitBook OpenAPI
blocks, independently of the module generator's normalized contract output.
"""

import inspect
import json
import re
from pathlib import Path
from unittest.mock import patch
from urllib.parse import quote

import pytest
from requests import Response
import requests

from cortex_xdr_client.broker_appliance_client import BrokerApplianceClient
from cortex_xdr_client.client import CortexXDRClient
from cortex_xdr_client.api.authentication import Authentication, AuthenticationType
from cortex_xdr_client.api.version import APIVersion


ROOT = Path(__file__).resolve().parents[1]
CATALOG = json.loads((ROOT / 'cortex_xdr_client/api/operation_catalog.json').read_text())
SNAPSHOT = json.loads((ROOT / 'tests/fixtures/indexed_openapi_blocks.json').read_text())
SOURCE = {}
for page in SNAPSHOT['pages']:
    version = 3 if '/xdr-3-api/' in page['url'] else 5
    for block in page['blocks']:
        for path, methods in block.get('paths', {}).items():
            for method, operation in methods.items():
                if method in {'get', 'post', 'put', 'patch', 'delete', 'head', 'options'}:
                    key = (version, path, method)
                    assert key not in SOURCE
                    SOURCE[key] = (operation, block)
NEW = [entry for entry in CATALOG if 'source' in entry]
INITIAL = [entry for entry in CATALOG if 'source' not in entry]


def dereference(schema, spec):
    for _ in range(12):
        if not isinstance(schema, dict) or '$ref' not in schema:
            break
        ref = schema['$ref']
        assert ref.startswith('#/')
        value = spec
        for part in ref[2:].split('/'):
            value = value[part.replace('~1', '/').replace('~0', '~')]
        schema = value
    if isinstance(schema, dict) and 'allOf' in schema:
        merged = {}
        for part in schema['allOf']:
            resolved = dereference(part, spec)
            merged.update({key: value for key, value in resolved.get('properties', {}).items()
                           if not (value.get('readOnly') and
                                   'omitted on insert' in value.get('description', '').lower())})
        schema = {'type': 'object', 'properties': merged}
    return schema


def vendor_fields(operation, spec, path):
    if path == '/public_api/v1/compliance/edit_assessment_profile':
        # The literal source has an empty-string property name. The public
        # method accepts the whole object without guessing its envelope.
        return {'raw_body:body': {'type': 'object'}}, None, 'application/json'
    fields = {}
    for parameter in operation.get('parameters', []):
        parameter = dereference(parameter, spec)
        location, name = parameter.get('in'), parameter.get('name')
        if location == 'header' and name.lower() in {
                'authorization', 'x-xdr-auth-id', 'x-xdr-timestamp', 'x-xdr-nonce', 'content-type'}:
            continue
        if location in {'path', 'query', 'header'} and name:
            fields[f'{location}:{name}'] = dereference(parameter.get('schema', {}), spec)
    for name in re.findall(r'\{([^{}]+)\}', path):
        fields.setdefault(f'path:{name}', {'type': 'string'})
    request_body = dereference(operation.get('requestBody', {}), spec)
    content = request_body.get('content', {})
    media = next(iter(content), None)
    body = dereference(content.get(media, {}).get('schema', {}), spec) if media else {}
    envelope = None
    if len(body.get('properties', {})) == 1:
        possible = next(iter(body['properties']))
        if possible in {'request', 'request_data'}:
            envelope = possible
            body = dereference(body['properties'][possible], spec)
    if body.get('properties'):
        for name, schema in body['properties'].items():
            fields[f'body:{name}'] = dereference(schema, spec)
    elif media and not (body.get('type') == 'object' and
                        (envelope or 'empty' in body.get('description', '').lower()) and
                        not body.get('additionalProperties')):
        fields['raw_body:payload'] = body
    return fields, envelope, media


def sample(schema):
    kind = schema.get('type') if isinstance(schema, dict) else None
    if isinstance(kind, list):
        kind = next((x for x in kind if x != 'null'), None)
    return {'string': 'value/with space', 'integer': 0, 'number': 0.0,
            'boolean': False, 'array': ['first', 'second'],
            'object': {'nested': 1}}.get(kind, {'nested': 1})


def expected_wire_scalar(value):
    if isinstance(value, bool):
        return 'true' if value else 'false'
    if value is None:
        return ''
    return str(value)


def fake_response(status=200, media='application/json', payload=b'{"ok":true}'):
    response = Response()
    response.status_code = status
    response._content = payload
    if media:
        response.headers['Content-Type'] = media
    return response


def client_for(entry):
    if entry['api'] == 'broker_appliance':
        return BrokerApplianceClient('https://broker.example.local', token='local-token')
    auth = Authentication('tenant-key', 7, AuthenticationType.STANDARD)
    return CortexXDRClient(auth, 'tenant.example', api_version=APIVersion(entry['version']))


@pytest.mark.parametrize('entry', NEW, ids=lambda e: f"{e['version']} {e['http_method']} {e['path']}")
def test_indexed_operation_wire_contract_and_success_response(entry):
    key = entry['version'], entry['path'], entry['http_method']
    operation, spec = SOURCE[key]
    vendor, envelope, _ = vendor_fields(operation, spec, entry['path'])
    assert set(entry['arguments']) == set(vendor), key
    client = client_for(entry)
    api = client if entry['api'] == 'broker_appliance' else getattr(client, entry['api'])
    method = getattr(api, entry['method'])
    signature = inspect.signature(method)
    assert all(parameter.kind == inspect.Parameter.KEYWORD_ONLY for parameter in signature.parameters.values())
    supplied = {entry['arguments'][field]: sample(schema) for field, schema in vendor.items()}
    response_specs = operation.get('responses', {})
    status = next((int(code) for code in response_specs if code.isdigit() and 200 <= int(code) < 300), 200)
    response_media = next(iter(response_specs.get(str(status), {}).get('content', {})), None)
    if status in (204, 205):
        payload = b''
    elif response_media and response_media.split(';')[0] == 'application/json':
        payload = b'{"ok":true}'
    else:
        payload = b'payload-bytes'
    response = fake_response(status, response_media, payload)
    with patch('requests.request', return_value=response) as request:
        result = method(**supplied)
    assert request.call_count == 1
    args, kwargs = request.call_args
    assert args[0] == entry['http_method']
    expected_path = entry['wire_path']
    for wire, py in ((field[5:], name) for field, name in entry['arguments'].items() if field.startswith('path:')):
        expected_path = expected_path.replace('{' + wire + '}', quote(str(supplied[py]), safe=''))
    origin = 'https://broker.example.local' if entry['api'] == 'broker_appliance' else 'https://api-tenant.example'
    assert args[1] == origin + expected_path
    assert kwargs['timeout'] == (10, 60)
    assert kwargs['allow_redirects'] is False
    headers = kwargs['headers']
    if entry['api'] == 'broker_appliance':
        assert 'x-xdr-auth-id' not in headers
        assert headers.get('Authorization') == (None if entry['path'].startswith('/public_api/v1/auth/')
                                                else 'Bearer local-token')
    else:
        assert headers['Authorization'] == 'tenant-key'
        assert headers['x-xdr-auth-id'] == '7'
    for field, schema in vendor.items():
        location, wire = field.split(':', 1)
        value = supplied[entry['arguments'][field]]
        if location == 'body':
            body = kwargs['json']
            if envelope:
                body = body[envelope]
            assert body[wire] == value
        elif location == 'raw_body':
            assert kwargs['json'] == ({envelope: value} if envelope else value)
        elif location == 'header':
            assert headers[wire] == str(value)
        elif location == 'query':
            assert wire in dict(kwargs['params'])
    if status in (204, 205):
        assert result is None
    elif response_media and response_media.split(';')[0] == 'application/json':
        assert result == {'ok': True}
    else:
        assert result == payload


def test_catalog_covers_all_indexed_operations_and_four_download_only_operations():
    keys = {(e['version'], e['path'], e['http_method']) for e in CATALOG}
    assert len(keys) == len(CATALOG) == 510
    assert set(SOURCE).issubset(keys)
    assert keys - set(SOURCE) == {
        (3, '/public_api/v1/automations/get_automation_rules', 'post'),
        (3, '/public_api/v1/endpoints/terminate_causality', 'post'),
        (3, '/public_api/v1/endpoints/terminate_process', 'post'),
        (5, '/public_api/appsec/v1/operational-risk', 'get'),
    }


@pytest.mark.parametrize('entry', INITIAL, ids=lambda e: f"{e['version']} {e['http_method']} {e['path']}")
def test_initial_operation_uses_documented_route_through_public_client(entry):
    """Exercise the checkpoint's 342 mappings against independently pinned fields."""
    client = client_for(entry)
    method = getattr(getattr(client, entry['api']), entry['method'])
    key = entry['version'], entry['path'], entry['http_method']
    operation, spec = SOURCE[key] if key in SOURCE else ({}, {})
    vendor, envelope, _ = vendor_fields(operation, spec, entry['path'])
    supplied = {name: 'probe' for name, parameter in inspect.signature(method).parameters.items()
                if parameter.default is inspect.Parameter.empty}
    for field, name in entry['arguments'].items():
        if field in vendor:
            supplied[name] = sample(vendor[field])
        elif field.startswith('payload:'):
            supplied[name] = {'nested': 1}
        elif field.startswith('outer:'):
            supplied[name] = False
        elif field.startswith('file:'):
            supplied[name] = ('upload.txt', b'content')
        elif field.startswith('header:'):
            supplied[name] = 'gzip'
    # The published legacy header spelling is malformed; both compatibility
    # arguments map to one valid Accept-Encoding field and cannot be combined.
    if 'accept_encoding_gzip' in supplied:
        supplied.pop('accept_encoding', None)
        supplied['accept_encoding_gzip'] = 'gzip'
    with patch('requests.request', return_value=fake_response(payload=b'{"reply":{}}')) as request:
        method(**supplied)
    assert request.call_count == 1
    args, kwargs = request.call_args
    expected_path = entry['wire_path']
    for field, name in entry['arguments'].items():
        if field.startswith('path:'):
            expected_path = expected_path.replace('{' + field[5:] + '}',
                                                  quote(str(supplied[name]), safe=''))
    assert args[:2] == (entry['http_method'], 'https://api-tenant.example' + expected_path)
    assert kwargs['allow_redirects'] is False
    assert kwargs['timeout'] == (10, 60)
    if envelope:
        assert envelope in kwargs['json']
    for field, schema in vendor.items():
        location, wire = field.split(':', 1)
        name = entry['arguments'].get(field)
        if location in {'path', 'query', 'header', 'body'}:
            assert name or (location == 'body' and any(
                prefix + wire in entry['arguments'] for prefix in ('payload:', 'outer:', 'file:'))), field
        if location == 'body':
            name = name or entry['arguments'].get('payload:' + wire)
            name = name or entry['arguments'].get('outer:' + wire)
            if name:
                body = kwargs['json'][envelope] if envelope else kwargs['json']
                assert body[wire] == supplied[name]
            elif 'file:' + wire in entry['arguments']:
                assert kwargs['files'][wire] == supplied[entry['arguments']['file:' + wire]]
        elif location == 'raw_body':
            name = entry['arguments'].get('payload:body')
            name = name or entry['arguments'].get('payload:request_data')
            if name:
                body = kwargs['json'][envelope] if envelope else kwargs['json']
                assert body == supplied[name]
        elif location == 'header' and name:
            if wire == '\'Accept-Encoding: gzip\' : " "':
                assert kwargs['headers']['Accept-Encoding'] == 'gzip'
            elif name in supplied:
                assert kwargs['headers'][wire] == expected_wire_scalar(supplied[name])
        elif location == 'query' and name:
            values = [value for key, value in kwargs['params'] if key == wire]
            value = supplied[name]
            parameter = next(p for p in operation['parameters']
                             if p.get('in') == 'query' and p.get('name') == wire)
            if isinstance(value, list):
                items = [expected_wire_scalar(item) for item in value]
                expected = items if parameter.get('explode', True) else [','.join(items)]
            else:
                expected = [expected_wire_scalar(value)]
            assert values == expected, (entry['path'], wire)
    if envelope and 'payload:body' in entry['arguments']:
        assert kwargs['json'] == {envelope: supplied[entry['arguments']['payload:body']]}
    if envelope and 'payload:' + envelope in entry['arguments']:
        assert kwargs['json'][envelope] == supplied[entry['arguments']['payload:' + envelope]]


def test_unset_is_distinct_from_null_false_zero_and_empty_array():
    client = client_for({'api': 'agent_configurations_api', 'version': 5})
    with patch('requests.request', return_value=fake_response()) as request:
        client.agent_configurations_api.set_content_management(
            enable_bandwidth_control=False, bandwidth_in_mbps=0,
            enable_minor_content_version_updates=None)
    assert request.call_args.kwargs['json'] == {'request_data': {
        'enable_bandwidth_control': False, 'bandwidth_in_mbps': 0,
        'enable_minor_content_version_updates': None}}
    with patch('requests.request', return_value=fake_response()) as request:
        client.api_keys_api.get_api_keys(filters=[])
    assert request.call_args.kwargs['json'] == {'request_data': {'filters': []}}


def test_query_arrays_aliases_and_path_quoting():
    client = client_for({'api': 'appsec_api', 'version': 5})
    with patch('requests.request', return_value=fake_response()) as request:
        client.appsec_api.get_rules(enabled=False, categories=['a', 'b'],
                                    sub_categories=['x', 'y'], offset=0)
    assert request.call_args.kwargs['params'] == [
        ('enabled', 'false'), ('categories', 'a,b'), ('subCategories', 'x'),
        ('subCategories', 'y'), ('offset', '0')]
    with patch('requests.request', return_value=fake_response()) as request:
        client.iam_api.get_api_key_by_id(api_key_id=17)
    assert request.call_args.args[1].endswith('/platform/iam/v1/api-key/17')
    with patch('requests.request', return_value=fake_response()) as request:
        client.brokers_v5_api.get_applet(device_id='a/b c', applet_name='wec')
    assert request.call_args.args[1].endswith('/brokers/a%2Fb%20c/applets/wec/')


def test_multipart_raw_csv_binary_text_and_empty_responses():
    client = client_for({'api': 'playbooks_api', 'version': 5})
    with patch('requests.request', return_value=fake_response()) as request:
        client.playbooks_api.insert(file=('playbook.yml', b'content'))
    assert request.call_args.kwargs['files'] == {'file': ('playbook.yml', b'content')}
    assert request.call_args.kwargs['json'] is None
    with patch('requests.request', return_value=fake_response()) as request:
        client.ioc_api.insert_csv(request_data='type,value\nIP,1.2.3.4', validate=False)
    assert request.call_args.kwargs['json'] == {
        'request_data': 'type,value\nIP,1.2.3.4', 'validate': False}
    appliance = BrokerApplianceClient('https://broker.example.local', token='short-lived')
    with patch('requests.request', return_value=fake_response(media='application/octet-stream',
                                                              payload=b'PK\x03\x04')):
        assert appliance.issue_log_bundle() == b'PK\x03\x04'
    with patch('requests.request', return_value=fake_response(media='text/plain', payload=b'hello')):
        assert appliance.issue_log_bundle() == 'hello'
    with patch('requests.request', return_value=fake_response(status=204, media=None, payload=b'')):
        assert appliance.set_internal_subnet(docker_subnet='172.16.0.0/16') is None


def test_appliance_authentication_is_explicit_and_isolated_from_tenant_keys():
    with patch('requests.request') as request:
        appliance = BrokerApplianceClient('https://broker.example.local')
    request.assert_not_called()
    with patch('requests.request', return_value=fake_response()) as request:
        appliance.reset_initial_password(current_password='factory', new_password='changed')
    assert 'Authorization' not in request.call_args.kwargs['headers']
    with patch('requests.request', return_value=fake_response(payload=b'{"reply":{"api_key":"local-token"}}')) as request:
        reply = appliance.generate_token(password='changed')
    assert reply['reply']['api_key'] == 'local-token'
    assert 'Authorization' not in request.call_args.kwargs['headers']
    with pytest.raises(ValueError, match='Bearer token'):
        appliance.issue_log_bundle()
    appliance.set_token(reply['reply']['api_key'])
    with patch('requests.request', return_value=fake_response()) as request:
        appliance.register_broker(token='opaque')
    assert request.call_args.kwargs['headers']['Authorization'] == 'Bearer local-token'
    assert 'x-xdr-auth-id' not in request.call_args.kwargs['headers']
    appliance.clear_token()
    with pytest.raises(ValueError, match='Bearer token'):
        appliance.issue_log_bundle()
    with pytest.raises(ValueError, match='HTTPS origin'):
        BrokerApplianceClient('http://broker.example.local')
    with pytest.raises(ValueError, match='HTTPS origin'):
        BrokerApplianceClient('https://broker.example.local/path')


def test_errors_redirects_timeouts_and_version_guards_propagate():
    client = client_for({'api': 'iam_api', 'version': 5})
    error = fake_response(status=403, payload=b'{}')
    with patch('requests.request', return_value=error), pytest.raises(requests.HTTPError):
        client.iam_api.list_roles()
    redirect = fake_response(status=302, payload=b'')
    redirect.headers['Location'] = 'https://attacker.example'
    with patch('requests.request', return_value=redirect), pytest.raises(requests.HTTPError, match='redirect'):
        client.iam_api.list_roles()
    with patch('requests.request', side_effect=requests.Timeout), pytest.raises(requests.Timeout):
        client.iam_api.list_roles()
    legacy = client_for({'api': 'iam_api', 'version': 3})
    with patch('requests.request') as request, pytest.raises(NotImplementedError):
        legacy.iam_api.list_roles()
    request.assert_not_called()
    with patch('requests.request') as request, pytest.raises(ValueError, match='not supported'):
        client.ioc_api.insert_csv(accept_encoding='gzip')
    request.assert_not_called()


def test_legacy_stream_gzip_header_uses_valid_http_header_name():
    legacy = client_for({'api': 'xql_api', 'version': 3})
    with patch('requests.request', return_value=fake_response(media='application/octet-stream',
                                                              payload=b'\x1f\x8b')) as request:
        assert legacy.xql_api.get_query_results_stream_request(
            accept_encoding_gzip='gzip', stream_id='s-1') == b'\x1f\x8b'
    headers = request.call_args.kwargs['headers']
    assert headers['Accept-Encoding'] == 'gzip'
    assert all(':' not in name for name in headers)
    prepared = requests.Request('POST', request.call_args.args[1], headers=headers).prepare()
    assert prepared.headers['Accept-Encoding'] == 'gzip'
    with pytest.raises(ValueError, match='one Accept-Encoding'):
        legacy.xql_api.get_query_results_stream_request(accept_encoding='identity',
                                                        accept_encoding_gzip='gzip')


def test_forensics_policy_and_cwp_use_configured_origin_and_literal_headers():
    client = client_for({'api': 'forensics_api', 'version': 5})
    with patch('requests.request', return_value=fake_response()) as request:
        client.forensics_api.get_forensics_investigations()
    assert request.call_args.args[1] == 'https://api-tenant.example/public_api/v1/forensics/investigations'
    assert request.call_args.kwargs['json'] == {'request_data': {}}
    with patch('requests.request', return_value=fake_response()) as request:
        client.cloud_security_policies_api.list_cloud_security_policies()
    assert request.call_args.args[1] == 'https://api-tenant.example/public_api/v1/policy/search'
    with patch('requests.request', return_value=fake_response()) as request:
        client.cloud_workload_protection_api.get_unmanaged_registry_connector_public_api(
            connector_id='connector/42', authentication='registry-secret')
    assert request.call_args.args[1] == (
        'https://api-tenant.example/public_api/v1/cwp/registry_onboarding/instances/connector%2F42')
    assert request.call_args.kwargs['headers']['Authentication'] == 'registry-secret'
    assert request.call_args.kwargs['headers']['Authorization'] == 'tenant-key'
    assert request.call_args.kwargs['headers']['x-xdr-auth-id'] == '7'


def test_ambiguous_compliance_edit_body_is_sent_unchanged():
    client = client_for({'api': 'compliance_controls_api', 'version': 5})
    body = {'request_data': {'id': 'profile-7', 'enabled': False}}
    with patch('requests.request', return_value=fake_response()) as request:
        client.compliance_controls_api.edit_assessment_profile(body=body)
    assert request.call_args.args[:2] == (
        'post', 'https://api-tenant.example/public_api/v1/compliance/edit_assessment_profile')
    assert request.call_args.kwargs['json'] == body
    assert '' not in request.call_args.kwargs['json']


@pytest.mark.parametrize('api,method,arguments,inner,v3_unwrapped', [
    ('profiles_api', 'prevention_add', {'name': 'profile-1', 'modules': {}},
     {'name': 'profile-1', 'modules': {}}, True),
    ('profiles_api', 'add_signer_cn_to_allowlist',
     {'profile_name': 'profile-1', 'signers': ['CN=Example']},
     {'profile_name': 'profile-1', 'signers': ['CN=Example']}, True),
    ('profiles_api', 'prevention_edit', {'profile_id': 0, 'update_data': {'enabled': False}},
     {'profile_id': 0, 'update_data': {'enabled': False}}, True),
    ('profiles_api', 'prevention_get_modules', {'profile_type': 'endpoint', 'platform': 'linux'},
     {'profile_type': 'endpoint', 'platform': 'linux'}, True),
    ('system_api', 'assets', {'filters': [], 'search_from': 0},
     {'filters': [], 'search_from': 0}, False),
    ('rbac_api', 'get_users', {'body': {'filters': []}}, {'filters': []}, True),
])
def test_version_specific_request_data_envelopes(api, method, arguments, inner, v3_unwrapped):
    client = client_for({'api': api, 'version': 5})
    with patch('requests.request', return_value=fake_response()) as request:
        getattr(getattr(client, api), method)(**arguments)
    assert request.call_args.kwargs['json'] == {'request_data': inner}
    if v3_unwrapped:
        legacy = client_for({'api': api, 'version': 3})
        with patch('requests.request', return_value=fake_response()) as request:
            getattr(getattr(legacy, api), method)(**arguments)
        assert request.call_args.kwargs['json'] == inner
