import pytest

from cortex_xdr_client.client import CortexXDRClient
from tests.test_versions import ORIGIN, documented_operation


@pytest.fixture
def client(auth):
    return CortexXDRClient(auth, 'tenant.example.com', api_version=5)


def test_search_cases(client, requests_mock):
    path = '/public_api/v1/case/search'
    assert documented_operation(5, path, 'post')
    requests_mock.post(ORIGIN + path, json={'reply': {
        'TOTAL_COUNT': 2, 'FILTER_COUNT': 1, 'DATA': [{
            'case_id': 42, 'case_name': 'Malware', 'status_progress': 'Custom tenant status',
            'severity': 'high', 'resolve_reason': None, 'issue_ids': [123],
            'custom_fields': {'owner': 'team'}, 'future_field': True}]}})
    filters = [{'field': 'case_id', 'operator': 'in', 'value': [42]}]
    result = client.cases_api.get_cases(filters, 0, 1, {'field': 'case_id', 'keyword': 'desc'})
    assert result.reply.total_count == 2
    assert result.reply.filter_count == 1
    assert result.reply.data[0].case_id == 42
    assert result.reply.data[0].future_field is True
    assert result.reply.data[0].custom_fields == {'owner': 'team'}
    assert requests_mock.last_request.json() == {'request_data': {
        'filters': filters, 'search_from': 0, 'search_to': 1,
        'sort': {'field': 'case_id', 'keyword': 'desc'}}}


def test_search_issues(client, requests_mock):
    path = '/public_api/v1/issue/search'
    assert documented_operation(5, path, 'post')
    requests_mock.post(ORIGIN + path, json={'reply': {
        'TOTAL_COUNT': 1, 'FILTER_COUNT': 1, 'DATA': [{
            'id': 123, 'severity': 'CRITICAL', '_insert_time': 1000,
            'detection.method': 'TRAPS', 'status.progress': 'New',
            'status.resolution_reason': None, 'case_ids': [42],
            'normalized_fields': {'xdm.source.host.hostname': 'test'},
            'custom_fields': {'ticket': 'T-1'}, 'new_field': 'preserved'}]}})
    result = client.issues_api.get_issues(search_from=0, search_to=10,
                                         include_fields=['normalized_fields', 'custom_fields'],
                                         include_evidences=False, include_actions=True)
    issue = result.reply.data[0]
    assert issue.insert_time == 1000
    assert issue.detection_method == 'TRAPS'
    assert issue.status_progress == 'New'
    assert issue.new_field == 'preserved'
    assert issue.model_dump(by_alias=True)['status.resolution_reason'] is None
    assert issue.normalized_fields == {'xdm.source.host.hostname': 'test'}
    assert requests_mock.last_request.json() == {'request_data': {
        'search_from': 0, 'search_to': 10, 'include_fields': ['normalized_fields', 'custom_fields'],
        'include_evidences': False, 'include_actions': True}}


@pytest.mark.parametrize('api,method,path,update', [
    ('cases_api', 'update_case', '/public_api/v1/case/update/42',
     {'status_progress': 'Resolved', 'resolve_reason': 'Resolved - True Positive'}),
    ('issues_api', 'update_issue', '/public_api/v1/issue/42',
     {'status': 'Resolved', 'status_resolution_reason': 'Resolved - Threat Handled'}),
])
def test_updates_have_no_json_response(client, requests_mock, api, method, path, update):
    assert documented_operation(5, path, 'post')
    requests_mock.post(ORIGIN + path, status_code=204)
    assert getattr(getattr(client, api), method)(42, update) is None
    assert requests_mock.last_request.json() == {'request_data': {'update_data': update}}


def test_create_issue(client, requests_mock):
    path = '/public_api/v1/issue'
    assert documented_operation(5, path, 'post')
    requests_mock.post(ORIGIN + path, status_code=202,
                       json={'external_id': 'external', 'detection_method': 'Custom Issue'})
    issue = {'name': 'Example', 'description': 'Test', 'severity': 'HIGH',
             'observation_time': 1234, 'issue_domain': 'Security', 'category': 'MALWARE'}
    assert client.issues_api.create_issue(issue)['external_id'] == 'external'
    assert requests_mock.last_request.json() == {'request_data': {'issue': issue}}


@pytest.mark.parametrize('api,method,args,path,http_method,response', [
    ('cases_api', 'get_case_artifacts', (42,), '/public_api/v1/case/artifacts/42/', 'get',
     [{'case_id': 42, 'file_artifacts': {'DATA': [], 'TOTAL_COUNT': 0}}]),
    ('cases_api', 'get_cases_schema', (), '/public_api/v1/case/schema', 'get', {'reply': []}),
    ('cases_api', 'get_case_timeline', (42,), '/public_api/v1/case/timeline/42/', 'post',
     {'reply': {'DATA': [], 'TOTAL_COUNT': 0}}),
    ('cases_api', 'add_case_timeline_record', (42, {'record_type': 'Detection', 'record_name': 'Test', 'occurred_at': 1}),
     '/public_api/v1/case/timeline/42/add_record/', 'post', {'reply': {'record_id': 'record', 'case_id': 42}}),
    ('issues_api', 'get_issues_schema', (), '/public_api/v1/issue/schema/', 'post', {'reply': {'DATA': []}}),
    ('issues_api', 'create_issue_exception', ({'name': 'Exception'},), '/public_api/v1/issue_exceptions/',
     'post', {'reply': {'exception_id': 1}}),
    ('issues_api', 'disable_issue_exception', (1,), '/public_api/v1/issue_exceptions/disable/',
     'post', {'reply': {'rows_affected': 1, 'status': 'DISABLED'}}),
    ('issues_api', 'get_issue_exceptions', (), '/public_api/v1/issue_exceptions/search/',
     'post', {'reply': {'exceptions': []}}),
])
def test_additional_v5_methods(client, requests_mock, api, method, args, path, http_method, response):
    assert documented_operation(5, path, http_method)
    requests_mock.register_uri(http_method, ORIGIN + path, json=response)
    assert getattr(getattr(client, api), method)(*args) == response


def test_exception_search_preserves_special_filters(client, requests_mock):
    requests_mock.post(ORIGIN + '/public_api/v1/issue_exceptions/search/', json={'reply': {'exceptions': []}})
    filters = {'AND': [{'SEARCH_FIELD': 'STATUS', 'SEARCH_TYPE': 'EQ', 'SEARCH_VALUE': 'APPROVED'}]}
    client.issues_api.get_issue_exceptions(filters=filters, search_from=0, search_to=10)
    assert requests_mock.last_request.json()['request_data']['filters'] == filters
