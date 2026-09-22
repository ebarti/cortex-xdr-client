"""Outgoing requests checked independently of the client's URL/filter helpers."""
from copy import deepcopy

import pytest

from cortex_xdr_client.api.models.incidents import IncidentStatus
from tests.test_versions import ORIGIN, client


@pytest.mark.parametrize('incident_id', [None, 'case-or-incident-42'])
@pytest.mark.parametrize('parameters', [None, {'x': 'input text', 'y': 0}])
def test_run_script_request(client, requests_mock, incident_id, parameters):
    requests_mock.post(ORIGIN + '/public_api/v1/scripts/run_script',
                       json={'reply': {'action_id': 'action-42', 'endpoints_count': 2}})
    targets = ['endpoint-1', 'endpoint-2']
    original_parameters = deepcopy(parameters)
    result = client.scripts_api.run_script('script-uid-42', parameters, targets,
                                           timeout=123, incident_id=incident_id)
    expected = {'filters': [{'field': 'endpoint_id_list', 'operator': 'in',
                             'value': ['endpoint-1', 'endpoint-2']}],
                'script_uid': 'script-uid-42', 'timeout': 123}
    if parameters is not None:
        expected['parameters_values'] = {'x': 'input text', 'y': 0}
    if incident_id is not None:
        expected['incident_id'] = 'case-or-incident-42'
    assert requests_mock.last_request.json() == {'request_data': expected}
    assert requests_mock.call_count == 1
    assert result == {'action_id': 'action-42', 'endpoints_count': 2}
    assert targets == ['endpoint-1', 'endpoint-2']
    assert parameters == original_parameters


@pytest.mark.parametrize('incident_id', [None, 'case-or-incident-42'])
def test_run_snippet_request(client, requests_mock, incident_id):
    requests_mock.post(ORIGIN + '/public_api/v1/scripts/run_snippet_code_script',
                       json={'reply': {'action_id': 'action-43', 'endpoints_count': 2}})
    result = client.scripts_api.run_snippet_code_script('print("test")', ['endpoint-1', 'endpoint-2'],
                                                        timeout=321, incident_id=incident_id)
    expected = {'filters': [{'field': 'endpoint_id_list', 'operator': 'in',
                             'value': ['endpoint-1', 'endpoint-2']}],
                'snippet_code': 'print("test")', 'timeout': 321}
    if incident_id is not None:
        expected['incident_id'] = 'case-or-incident-42'
    assert requests_mock.last_request.json() == {'request_data': expected}
    assert requests_mock.call_count == 1
    assert result['action_id'] == 'action-43'


@pytest.mark.parametrize('method,args,path,expected,response', [
    ('get_script_metadata', ('script-uid-42',), 'get_script_metadata',
     {'script_uid': 'script-uid-42'}, {'script_id': 'script-42'}),
    ('get_script_execution_status', (42,), 'get_script_execution_status',
     {'action_id': 42}, {'general_status': 'COMPLETED_SUCCESSFULLY'}),
    ('get_script_execution_results', (43,), 'get_script_execution_results',
     {'action_id': 43}, {'results': []}),
    ('get_script_execution_result_files', (44, 'endpoint-2'), 'get_script_execution_results_files',
     {'action_id': 44, 'endpoint_id': 'endpoint-2'}, {'DATA': 'https://download.example/files.zip'}),
])
def test_script_lookup_identity(client, requests_mock, method, args, path, expected, response):
    requests_mock.post(ORIGIN + '/public_api/v1/scripts/' + path, json={'reply': response})
    getattr(client.scripts_api, method)(*args)
    assert requests_mock.last_request.json() == {'request_data': expected}
    assert requests_mock.call_count == 1


@pytest.mark.parametrize('method', ['get_action_status', 'get_file_retrieval_details'])
def test_action_lookup_identity(client, requests_mock, method):
    path = 'get_action_status' if method == 'get_action_status' else 'file_retrieval_details'
    requests_mock.post(ORIGIN + '/public_api/v1/actions/' + path,
                       json={'reply': {'data': {'endpoint-1': 'PENDING'}}})
    getattr(client.actions_api, method)(42)
    assert requests_mock.last_request.json() == {'request_data': {'group_action_id': 42}}


@pytest.mark.parametrize('method,path', [('isolate_endpoints', 'isolate'),
                                        ('unisolate_endpoints', 'unisolate'),
                                        ('scan_endpoints', 'scan')])
def test_response_action_targets(client, requests_mock, method, path):
    requests_mock.post(ORIGIN + '/public_api/v1/endpoints/' + path,
                       json={'reply': {'action_id': 'action-42', 'endpoints_count': 2}})
    result = getattr(client.endpoints_api, method)(['endpoint-1', 'endpoint-2'])
    assert requests_mock.last_request.json() == {'request_data': {
        'filters': [{'field': 'endpoint_id_list', 'operator': 'in', 'value': ['endpoint-1', 'endpoint-2']}]}}
    assert result.reply.action_id == 'action-42'
    assert result.reply.endpoints_count == 2


@pytest.mark.parametrize('kwargs,timeframe', [
    ({'time_period': 3600000}, {'relativeTime': 3600000}),
    ({'from_date': 0, 'to_date': 1700000000000}, {'from': 0, 'to': 1700000000000}),
    ({'time_period': 3600000, 'from_date': 0, 'to_date': 1700000000000},
     {'from': 0, 'to': 1700000000000}),
])
def test_xql_query_and_timeframe(client, requests_mock, kwargs, timeframe):
    requests_mock.post(ORIGIN + '/public_api/v1/xql/start_xql_query', json={'reply': 'query-42'})
    result = client.xql_api.start_xql_query('dataset = xdr_data | limit 5', tenants=['tenant-1'], **kwargs)
    assert requests_mock.last_request.json() == {'request_data': {
        'query': 'dataset = xdr_data | limit 5', 'tenants': ['tenant-1'], 'timeframe': timeframe}}
    assert result == 'query-42'


@pytest.mark.parametrize('after,equal,time_operator,status_operator', [
    (True, True, 'gte', 'eq'), (False, False, 'lte', 'neq'),
])
def test_incident_filters_and_pagination(cortex_client, requests_mock, after, equal,
                                          time_operator, status_operator):
    requests_mock.post('https://api-a_fqdn/public_api/v1/incidents/get_incidents',
                       json={'reply': {'incidents': []}})
    cortex_client.incidents_api.get_incidents(
        modification_time=0, after_modification=after, creation_time=100, after_creation=after,
        incident_id_list=['42'], description='example', description_contains=True,
        alert_sources=['XDR Agent'], status=IncidentStatus.NEW, status_equal=equal,
        search_from=0, search_to=25, sort={'field': 'creation_time', 'keyword': 'asc'})
    assert requests_mock.last_request.json() == {'request_data': {
        'filters': [
            {'field': 'modification_time', 'operator': time_operator, 'value': 0},
            {'field': 'creation_time', 'operator': time_operator, 'value': 100},
            {'field': 'incident_id_list', 'operator': 'in', 'value': ['42']},
            {'field': 'description', 'operator': 'contains', 'value': 'example'},
            {'field': 'alert_sources', 'operator': 'in', 'value': ['XDR Agent']},
            {'field': 'status', 'operator': status_operator, 'value': 'new'}],
        'search_from': 0, 'search_to': 25, 'sort': {'field': 'creation_time', 'keyword': 'asc'}}}
