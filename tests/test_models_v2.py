import json

import pytest
from pydantic import ValidationError

from cortex_xdr_client.api.models.action_status import ActionStatuStr, GetActionStatus
from cortex_xdr_client.api.models.alerts import Alert, AlertSeverity, Event, GetAlertsResponse
from cortex_xdr_client.api.models.cases import Case, GetCasesResponseItem
from cortex_xdr_client.api.models.endpoints import Endpoint, EndpointStatus, IsolateStatus
from cortex_xdr_client.api.models.incidents import Incident, IncidentStatus
from cortex_xdr_client.api.models.ioc import IoC
from cortex_xdr_client.api.models.issues import GetIssuesResponseItem, Issue
from cortex_xdr_client.api.models.scripts import GetScriptExecutionResults, ScriptExecutionResult


def test_sparse_responses_keep_optional_defaults():
    assert Event().event_id is None
    assert Case().case_id is None
    assert Issue().id is None
    assert GetScriptExecutionResults().results is None
    assert ScriptExecutionResult().standard_output is None
    assert Endpoint(endpoint_status='CONNECTED', is_isolated='AGENT_UNISOLATED').users is None
    assert Incident(status='new').incident_id is None


def test_required_response_structure_still_validates():
    with pytest.raises(ValidationError):
        GetAlertsResponse.model_validate({})
    with pytest.raises(ValidationError):
        Alert.model_validate({'description': 'Missing events'})
    with pytest.raises(ValidationError):
        Endpoint.model_validate({'is_isolated': 'AGENT_UNISOLATED'})


def test_unknown_fields_preserved_at_every_response_level():
    response = GetAlertsResponse.model_validate({'new_envelope_field': 'top', 'reply': {
        'new_page_field': 'page', 'alerts': [{
            'description': 'Example', 'events': [{'new_event_field': {'nested': [1, 2]}}],
            'new_alert_field': ['value']}]}})
    assert response.new_envelope_field == 'top'
    assert response.reply.new_page_field == 'page'
    assert response.reply.alerts[0].new_alert_field == ['value']
    assert response.reply.alerts[0].events[0].new_event_field == {'nested': [1, 2]}
    assert response.model_dump()['reply']['alerts'][0]['events'][0]['new_event_field'] == {'nested': [1, 2]}


def test_response_enums_retain_existing_types():
    endpoint = Endpoint(endpoint_status='CONNECTED', is_isolated='AGENT_UNISOLATED')
    assert endpoint.endpoint_status is EndpointStatus.connected
    assert endpoint.is_isolated is IsolateStatus.unisolated
    assert endpoint.model_dump()['endpoint_status'] is EndpointStatus.connected
    assert endpoint.model_dump(mode='json')['endpoint_status'] == 'CONNECTED'
    assert Incident(status='new').status is IncidentStatus.NEW
    # Alerts already exposed string enum values before this migration.
    alert = Alert(description='Example', events=[], severity=AlertSeverity.HIGH)
    assert type(alert.severity) is str
    assert alert.severity == 'high'


@pytest.mark.parametrize('model', [GetCasesResponseItem, GetIssuesResponseItem])
def test_aliases_accept_python_and_wire_names(model):
    python = model(total_count=2, filter_count=0, data=[])
    wire = model.model_validate({'TOTAL_COUNT': 2, 'FILTER_COUNT': 0, 'DATA': []})
    assert python == wire
    assert python.model_dump(by_alias=True) == {'TOTAL_COUNT': 2, 'FILTER_COUNT': 0, 'DATA': []}


def test_dotted_aliases_round_trip_without_data_loss():
    issue = Issue(id=1, insert_time=100, status_progress='New', detection_method='TRAPS',
                  custom_fields={'ticket': '001'}, additional_payload={'data': [1]})
    dumped = issue.model_dump(mode='json', by_alias=True, exclude_none=True)
    assert dumped == {'id': 1, '_insert_time': 100, 'status.progress': 'New',
                      'detection.method': 'TRAPS', 'custom_fields': {'ticket': '001'},
                      'additional_payload': {'data': [1]}}
    assert Issue.model_validate_json(json.dumps(dumped)) == issue


def test_structured_strings_and_lists_are_not_stringified():
    output = ScriptExecutionResult(standard_output=['line one', 'line two'])
    assert output.standard_output == ['line one', 'line two']
    alert = Alert(description=[{'pretty_name': 'Example', 'render_type': 'text'}], events=[])
    assert alert.description[0].pretty_name == 'Example'
    assert isinstance(alert.model_dump()['description'], list)
    with pytest.raises(ValidationError):
        ScriptExecutionResult(standard_output={'unexpected': 'object'})
    with pytest.raises(ValidationError):
        Issue(name={'unexpected': 'object'})


def test_action_status_root_model_preserves_wire_shape():
    payload = {'reply': {'data': {'endpoint-1': 'COMPLETED_SUCCESSFULLY', 'endpoint-2': None}}}
    response = GetActionStatus.model_validate(payload)
    assert response.reply.data.root == payload['reply']['data']
    assert response.model_dump() == payload
    assert json.loads(response.model_dump_json()) == payload
    assert ActionStatuStr.model_validate({'endpoint-1': 'PENDING'}).root == {'endpoint-1': 'PENDING'}
    assert GetActionStatus.model_validate({'reply': {}}).reply.data is None


def test_request_models_keep_required_fields_and_exclude_unknowns():
    with pytest.raises(ValidationError):
        IoC(indicator='192.0.2.1', type='IP')
    indicator = IoC.model_validate({'indicator': '192.0.2.1', 'type': 'IP', 'severity': 'HIGH',
                                    'class': 'Malware', 'unexpected_request_field': 'ignored'})
    assert indicator.model_dump(mode='json', by_alias=True, exclude_none=True) == {
        'indicator': '192.0.2.1', 'type': 'IP', 'severity': 'HIGH', 'class': 'Malware'}
