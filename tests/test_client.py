
def test_get_alerts(requests_mock, cortex_client, get_alerts_response):
    requests_mock.post(cortex_client.alerts_api._get_url("get_alerts_multi_events"), json=get_alerts_response)
    assert get_alerts_response == cortex_client.alerts_api.get_alerts()


def test_get_incidents(requests_mock, cortex_client, get_incidents_response):
    requests_mock.post(cortex_client.incidents_api._get_url("get_incidents"), json=get_incidents_response)
    assert get_incidents_response == cortex_client.incidents_api.get_incidents()


def test_get_incident_extra_data(requests_mock, cortex_client, get_incident_extra_data_response):
    requests_mock.post(cortex_client.incidents_api._get_url("get_incident_extra_data"), json=get_incident_extra_data_response)
    assert get_incident_extra_data_response == cortex_client.incidents_api.get_incident_extra_data("", 10)


def test_get_all_endpoints(requests_mock, cortex_client, get_all_endpoints_response):
    requests_mock.post(cortex_client.endpoints_api._get_url("get_endpoints"), json=get_all_endpoints_response)
    assert get_all_endpoints_response == cortex_client.endpoints_api.get_all_endpoints()


def test_get_endpoint(requests_mock, cortex_client, get_endpoint_response):
    requests_mock.post(cortex_client.endpoints_api._get_url("get_endpoint"), json=get_endpoint_response)
    assert get_endpoint_response == cortex_client.endpoints_api.get_endpoint()


def test_isolate_endpoints(requests_mock, cortex_client, get_isolate_endpoints_response):
    requests_mock.post(cortex_client.endpoints_api._get_url("isolate"), json=get_isolate_endpoints_response)
    assert get_isolate_endpoints_response == cortex_client.endpoints_api.isolate_endpoints()


def test_scan_endpoints(requests_mock, cortex_client, get_scan_endpoints_response):
    requests_mock.post(cortex_client.endpoints_api._get_url("scan"), json=get_scan_endpoints_response)
    assert get_scan_endpoints_response == cortex_client.endpoints_api.scan_endpoints()
