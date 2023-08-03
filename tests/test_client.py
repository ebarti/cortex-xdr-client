from cortex_xdr_client.api.models.action_status import GetActionStatus
from cortex_xdr_client.api.models.alerts import GetAlertsResponse
from cortex_xdr_client.api.models.endpoints import GetAllEndpointsResponse, GetEndpointResponse, ResponseActionResponse
from cortex_xdr_client.api.models.incidents import GetExtraIncidentDataResponse, GetIncidentsResponse
from cortex_xdr_client.api.models.ioc import IoC
from cortex_xdr_client.api.models.scripts import (GetScriptExecutionResults,
                                                  GetScriptMetadataResponse,
                                                  GetScriptsExecutionStatus,
                                                  GetScriptsResponse,
                                                  )


def test_get_alerts(requests_mock, cortex_client, get_alerts_response):
    requests_mock.post(cortex_client.alerts_api._get_url("get_alerts_multi_events"),
                       json=get_alerts_response)

    assert GetAlertsResponse.parse_obj(get_alerts_response) == cortex_client.alerts_api.get_alerts()


def test_get_incidents(requests_mock, cortex_client, get_incidents_response):
    requests_mock.post(cortex_client.incidents_api._get_url("get_incidents"),
                       json=get_incidents_response)
    assert GetIncidentsResponse.parse_obj(get_incidents_response) == cortex_client.incidents_api.get_incidents()


def test_get_incident_extra_data(requests_mock, cortex_client, get_incident_extra_data_response):
    requests_mock.post(cortex_client.incidents_api._get_url("get_incident_extra_data"),
                       json=get_incident_extra_data_response)
    assert GetExtraIncidentDataResponse.parse_obj(
        get_incident_extra_data_response) == cortex_client.incidents_api.get_incident_extra_data("", 10)


def test_get_all_endpoints(requests_mock, cortex_client, get_all_endpoints_response):
    requests_mock.post(cortex_client.endpoints_api._get_url("get_endpoints"),
                       json=get_all_endpoints_response)
    assert GetAllEndpointsResponse.parse_obj(
        get_all_endpoints_response) == cortex_client.endpoints_api.get_all_endpoints()


def test_get_endpoint(requests_mock, cortex_client, get_endpoint_response):
    requests_mock.post(cortex_client.endpoints_api._get_url("get_endpoint"),
                       json=get_endpoint_response)
    assert GetEndpointResponse.parse_obj(get_endpoint_response) == cortex_client.endpoints_api.get_endpoint()


def test_isolate_endpoints(requests_mock, cortex_client, get_isolate_endpoints_response):
    requests_mock.post(cortex_client.endpoints_api._get_url("isolate"),
                       json=get_isolate_endpoints_response)
    assert ResponseActionResponse.parse_obj(
        get_isolate_endpoints_response) == cortex_client.endpoints_api.isolate_endpoints()


def test_scan_endpoints(requests_mock, cortex_client, get_scan_endpoints_response):
    requests_mock.post(cortex_client.endpoints_api._get_url("scan"),
                       json=get_scan_endpoints_response)
    assert ResponseActionResponse.parse_obj(get_scan_endpoints_response) == cortex_client.endpoints_api.scan_endpoints()


def test_get_scripts(requests_mock, cortex_client, get_scripts_response):
    requests_mock.post(cortex_client.scripts_api._get_url("get_scripts"),
                       json=get_scripts_response)
    assert GetScriptsResponse.parse_obj(get_scripts_response['reply']) == cortex_client.scripts_api.get_scripts()


def test_get_script_metadata(requests_mock, cortex_client, get_script_metadata_response):
    requests_mock.post(cortex_client.scripts_api._get_url("get_script_metadata"),
                       json=get_script_metadata_response)
    assert GetScriptMetadataResponse.parse_obj(
        get_script_metadata_response['reply']) == cortex_client.scripts_api.get_script_metadata("")


def test_get_script_execution_status(requests_mock, cortex_client, get_script_execution_status_response):
    requests_mock.post(cortex_client.scripts_api._get_url("get_script_execution_status"),
                       json=get_script_execution_status_response)
    assert GetScriptsExecutionStatus.parse_obj(
        get_script_execution_status_response['reply']) == cortex_client.scripts_api.get_script_execution_status("")


def test_get_script_execution_results(requests_mock, cortex_client, get_script_execution_results_response):
    requests_mock.post(cortex_client.scripts_api._get_url("get_script_execution_results"),
                       json=get_script_execution_results_response)
    assert GetScriptExecutionResults.parse_obj(
        get_script_execution_results_response['reply']) == cortex_client.scripts_api.get_script_execution_results("")


def test_get_script_execution_result_files(requests_mock, cortex_client, get_script_execution_result_files_response):
    requests_mock.post(cortex_client.scripts_api._get_url("get_script_execution_results_files"),
                       json=get_script_execution_result_files_response)
    assert get_script_execution_result_files_response['reply'][
               'DATA'] == cortex_client.scripts_api.get_script_execution_result_files("", None)


def test_run_script(requests_mock, cortex_client, run_script_response):
    requests_mock.post(cortex_client.scripts_api._get_url("run_script"),
                       json=run_script_response)
    assert run_script_response['reply'] == cortex_client.scripts_api.run_script("", None, None)


def test_run_snippet_code_script(requests_mock, cortex_client, run_snippet_code_script_response):
    requests_mock.post(cortex_client.scripts_api._get_url("run_snippet_code_script"),
                       json=run_snippet_code_script_response)
    assert run_snippet_code_script_response['reply'] == cortex_client.scripts_api.run_snippet_code_script("", None)


def test_start_xql(requests_mock, cortex_client, start_xql_response):
    requests_mock.post(cortex_client.xql_api._get_url("start_xql_query"),
                       json=start_xql_response)
    assert start_xql_response['reply'] == cortex_client.xql_api.start_xql_query("")


def test_get_action_status(requests_mock, cortex_client, get_action_status):
    requests_mock.post(cortex_client.actions_api._get_url("get_action_status"),
                       json=get_action_status)
    assert GetActionStatus.parse_obj(get_action_status) == cortex_client.actions_api.get_action_status(0)


def test_get_file_retrieval_details(requests_mock, cortex_client, get_action_status):
    requests_mock.post(cortex_client.actions_api._get_url("file_retrieval_details"),
                       json=get_action_status)
    assert GetActionStatus.parse_obj(get_action_status) == cortex_client.actions_api.get_file_retrieval_details(0)


def test_get_xql_results(requests_mock, cortex_client, get_xql_results_response):
    requests_mock.post(cortex_client.xql_api._get_url("get_query_results"),
                       json=get_xql_results_response)
    assert get_xql_results_response['reply']['results'] == cortex_client.xql_api.get_query_results("")


def test_get_xql_result_stream(requests_mock, cortex_client, get_xql_result_stream_response):
    requests_mock.post(cortex_client.xql_api._get_url("get_query_results_stream"),
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


def test_post_insert_json(cortex_client, get_url, post_insert_json_response, successful_response):
    get_url.return_value = "https://stoplight.io/mocks/cortex-panw/cortex-xdr/183739843/public_api/v1/indicators/insert_jsons"
    indicator = {
        "indicator":   "<fgg>",
        "type":        "HASH",
        "comment":     "test",
        "reputation":  "GOOD",
        "reliability": "D",
        "severity":    "high",
        "vendors":     [
            {
                "vendor_name": "V1",
                "reliability": "A",
                "reputation":  "GOOD"
            },
            {
                "vendor_name": "V2",
                "reliability": "A",
                "reputation":  "SUSPICIOUS"
            }
        ],
        "class":       "Malware"
    }
    assert post_insert_json_response == cortex_client.ioc_api.insert_json([IoC.parse_obj(indicator)])
