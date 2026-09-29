from cortex_xdr_client.api.models.action_status import GetActionStatus
from cortex_xdr_client.api.models.alerts import GetAlertsResponse
from cortex_xdr_client.api.models.endpoints import (GetAllEndpointsResponse,
                                                    GetEndpointResponse,
                                                    ResponseActionResponse,
                                                    ResponseStatusResponse
                                                    )
from cortex_xdr_client.api.models.incidents import GetExtraIncidentDataResponse, GetIncidentsResponse
from cortex_xdr_client.api.models.scripts import (GetScriptExecutionResults,
                                                  GetScriptMetadataResponse,
                                                  GetScriptsExecutionStatus,
                                                  GetScriptsResponse,
                                                  )


def test_get_alerts(requests_mock, cortex_client, get_alerts_response):
    requests_mock.post("https://api-a_fqdn/public_api/v1/alerts/get_alerts_multi_events",
                       json=get_alerts_response)

    assert GetAlertsResponse.model_validate(get_alerts_response) == cortex_client.alerts_api.get_alerts()


def test_get_incidents(requests_mock, cortex_client, get_incidents_response):
    requests_mock.post("https://api-a_fqdn/public_api/v1/incidents/get_incidents",
                       json=get_incidents_response)
    assert GetIncidentsResponse.model_validate(get_incidents_response) == cortex_client.incidents_api.get_incidents()


def test_get_incident_extra_data(requests_mock, cortex_client, get_incident_extra_data_response):
    requests_mock.post("https://api-a_fqdn/public_api/v1/incidents/get_incident_extra_data",
                       json=get_incident_extra_data_response)
    assert GetExtraIncidentDataResponse.model_validate(
        get_incident_extra_data_response) == cortex_client.incidents_api.get_incident_extra_data("", 10)


def test_get_all_endpoints(requests_mock, cortex_client, get_all_endpoints_response):
    requests_mock.post("https://api-a_fqdn/public_api/v1/endpoints/get_endpoints",
                       json=get_all_endpoints_response)
    assert GetAllEndpointsResponse.model_validate(
        get_all_endpoints_response) == cortex_client.endpoints_api.get_all_endpoints()


def test_get_endpoint(requests_mock, cortex_client, get_endpoint_response):
    requests_mock.post("https://api-a_fqdn/public_api/v1/endpoints/get_endpoint",
                       json=get_endpoint_response)
    assert GetEndpointResponse.model_validate(get_endpoint_response) == cortex_client.endpoints_api.get_endpoint()


def test_isolate_endpoints(requests_mock, cortex_client, get_isolate_endpoints_response):
    requests_mock.post("https://api-a_fqdn/public_api/v1/endpoints/isolate",
                       json=get_isolate_endpoints_response)
    assert ResponseActionResponse.model_validate(
        get_isolate_endpoints_response) == cortex_client.endpoints_api.isolate_endpoints()


def test_scan_endpoints(requests_mock, cortex_client, get_scan_endpoints_response):
    requests_mock.post("https://api-a_fqdn/public_api/v1/endpoints/scan",
                       json=get_scan_endpoints_response)
    assert ResponseActionResponse.model_validate(get_scan_endpoints_response) == cortex_client.endpoints_api.scan_endpoints()


def test_set_endpoint_alias(requests_mock, cortex_client, get_set_endpoint_alias_response):
    requests_mock.post("https://api-a_fqdn/public_api/v1/endpoints/update_agent_name",
                       json=get_set_endpoint_alias_response)
    assert ResponseStatusResponse.model_validate(
        get_set_endpoint_alias_response) == cortex_client.endpoints_api.set_endpoint_alias('new_alias')


def test_get_scripts(requests_mock, cortex_client, get_scripts_response):
    requests_mock.post("https://api-a_fqdn/public_api/v1/scripts/get_scripts",
                       json=get_scripts_response)
    assert GetScriptsResponse.model_validate(get_scripts_response['reply']) == cortex_client.scripts_api.get_scripts()


def test_get_script_metadata(requests_mock, cortex_client, get_script_metadata_response):
    requests_mock.post("https://api-a_fqdn/public_api/v1/scripts/get_script_metadata",
                       json=get_script_metadata_response)
    assert GetScriptMetadataResponse.model_validate(
        get_script_metadata_response['reply']) == cortex_client.scripts_api.get_script_metadata("")


def test_get_script_execution_status(requests_mock, cortex_client, get_script_execution_status_response):
    requests_mock.post("https://api-a_fqdn/public_api/v1/scripts/get_script_execution_status",
                       json=get_script_execution_status_response)
    assert GetScriptsExecutionStatus.model_validate(
        get_script_execution_status_response['reply']) == cortex_client.scripts_api.get_script_execution_status("")


def test_get_script_execution_results(requests_mock, cortex_client, get_script_execution_results_response):
    requests_mock.post("https://api-a_fqdn/public_api/v1/scripts/get_script_execution_results",
                       json=get_script_execution_results_response)
    assert GetScriptExecutionResults.model_validate(
        get_script_execution_results_response['reply']) == cortex_client.scripts_api.get_script_execution_results("")


def test_get_script_execution_result_files(requests_mock, cortex_client, get_script_execution_result_files_response):
    requests_mock.post("https://api-a_fqdn/public_api/v1/scripts/get_script_execution_results_files",
                       json=get_script_execution_result_files_response)
    assert get_script_execution_result_files_response['reply'][
               'DATA'] == cortex_client.scripts_api.get_script_execution_result_files("", None)


def test_run_script(requests_mock, cortex_client, run_script_response):
    requests_mock.post("https://api-a_fqdn/public_api/v1/scripts/run_script",
                       json=run_script_response)
    assert run_script_response['reply'] == cortex_client.scripts_api.run_script("", None, None)


def test_run_snippet_code_script(requests_mock, cortex_client, run_snippet_code_script_response):
    requests_mock.post("https://api-a_fqdn/public_api/v1/scripts/run_snippet_code_script",
                       json=run_snippet_code_script_response)
    assert run_snippet_code_script_response['reply'] == cortex_client.scripts_api.run_snippet_code_script("", None)


def test_start_xql(requests_mock, cortex_client, start_xql_response):
    requests_mock.post("https://api-a_fqdn/public_api/v1/xql/start_xql_query",
                       json=start_xql_response)
    assert start_xql_response['reply'] == cortex_client.xql_api.start_xql_query("")


def test_get_action_status(requests_mock, cortex_client, get_action_status):
    requests_mock.post("https://api-a_fqdn/public_api/v1/actions/get_action_status",
                       json=get_action_status)
    assert GetActionStatus.model_validate(get_action_status) == cortex_client.actions_api.get_action_status(0)


def test_get_file_retrieval_details(requests_mock, cortex_client, get_action_status):
    requests_mock.post("https://api-a_fqdn/public_api/v1/actions/file_retrieval_details",
                       json=get_action_status)
    assert GetActionStatus.model_validate(get_action_status) == cortex_client.actions_api.get_file_retrieval_details(0)


def test_get_xql_results(requests_mock, cortex_client, get_xql_results_response):
    requests_mock.post("https://api-a_fqdn/public_api/v1/xql/get_query_results",
                       json=get_xql_results_response)
    assert get_xql_results_response['reply']['results'] == cortex_client.xql_api.get_query_results("")


def test_get_xql_result_stream(requests_mock, cortex_client, get_xql_result_stream_response):
    requests_mock.post("https://api-a_fqdn/public_api/v1/xql/get_query_results_stream",
                       content=get_xql_result_stream_response)
    expected = {
        'data': [
            {
                "event_id":       "eventID", "insert_timestamp": "2021-05-18 14:24:51.681 UTC",
                "_time":          "2021-05-18 09:59:28 UTC", "_vendor": "PANW", "_product": "Fusion",
                "event_type":     "STORY",
                "event_sub_type": "NULL"
            },
            {
                "event_id":       "eventID", "insert_timestamp": "2021-05-18 14:24:34.779 UTC",
                "_time":          "2021-05-18 09:59:28 UTC", "_vendor": "PANW", "_product": "Fusion",
                "event_type":     "STORY",
                "event_sub_type": "NULL"
            },
            {
                "event_id":       "eventID", "insert_timestamp": "2021-05-18 14:24:49.664 UTC",
                "_time":          "2021-05-18 09:59:28 UTC", "_vendor": "PANW", "_product": "Fusion",
                "event_type":     "STORY",
                "event_sub_type": "NULL"
            }
        ]
    }
    got = cortex_client.xql_api.get_query_results_stream("")
    assert expected == got


def test_post_insert_json(cortex_client, requests_mock, post_insert_json_response):
    from cortex_xdr_client.api.models.ioc import IoC, IoCResponse

    requests_mock.post("https://api-a_fqdn/public_api/v1/indicators/insert_jsons",
                       json=post_insert_json_response)
    indicator = IoC(indicator="testtest.com", type="HASH", severity="HIGH", **{"class": "Malware"})
    result = cortex_client.ioc_api.insert_json([indicator])
    assert result == IoCResponse.model_validate(post_insert_json_response)
    assert requests_mock.last_request.json()['request_data'][0]['class'] == 'Malware'
