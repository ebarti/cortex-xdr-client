import pytest


def test_get_alerts(requests_mock, cortex_client, get_alerts_response):

    requests_mock.post(cortex_client.alerts_api._get_url("get_alerts_multi_events"), json=get_alerts_response)
    output = cortex_client.alerts_api.get_alerts()
    ds = ""
