from datetime import datetime, timezone
from typing import List
import secrets
import string
import hashlib
import requests
from cortex.api.models.requests import (
    FilterRequestData,
    FilterRequestDataItem,
    Filter,
    Sort,
    GetIncidentExtraDataRequestData,
    GetIncidentExtraDataItem,
)
from cortex.api.models.alerts import GetAlertsResponse
from cortex.api.models.incidents import (
    GetIncidentsResponse,
    GetExtraIncidentDataResponse,
)
from cortex.api.models.endpoints import (
    GetEndpointResponse,
    GetAllEndpointsResponse,
    ResponseActionResponse,
)
from cortex.api.utils.utils import dump_json


class CortexXDRClient(object):

    def __init__(self, api_key_id, api_key, fqdn, default_timeout=(10, 60)):
        self._api_key_id = api_key_id
        self._api_key = api_key
        self._fqdn = fqdn
        self._requests_timeout = default_timeout

    def _get_headers(self):
        # Generate a 64 bytes random string
        nonce = "".join([secrets.choice(string.ascii_letters + string.digits) for _ in range(64)])
        # Get the current timestamp as milliseconds.
        timestamp = int(datetime.now(timezone.utc).timestamp()) * 1000
        # Generate the auth key:
        auth_key = "%s%s%s" % (self._api_key, nonce, timestamp)
        # Convert to bytes object
        auth_key = auth_key.encode("utf-8")
        # Calculate sha256:
        api_key_hash = hashlib.sha256(auth_key).hexdigest()
        # Generate HTTP call headers
        return {
            "x-xdr-timestamp": str(timestamp),
            "x-xdr-nonce": nonce,
            "x-xdr-auth-id": str(self._api_key_id),
            "Authorization": api_key_hash
        }

    def _call(self, api_name, call_name, method="post", params=None, request_data: object = None) -> requests.Response:
        url = self._get_url(api_name=api_name, call_name=call_name)
        headers = self._get_headers()
        json = dump_json(request_data)

        return self._execute_call(url=url,
                                  method=method,
                                  timeout=self._requests_timeout,
                                  params=params,
                                  headers=headers,
                                  json=json)

    @staticmethod
    def _execute_call(url, method, timeout, params=None, headers=None, json=None) -> requests.Response:
        response = None
        if method == 'get':
            response = requests.get(url, headers=headers, params=params, timeout=timeout)
        elif method == 'post':
            response = requests.post(url, headers=headers, json=json, timeout=timeout)
        elif method == 'put':
            response = requests.put(url, headers=headers, json=json, timeout=timeout)
        elif method == 'delete':
            response = requests.delete(url, headers=headers, timeout=timeout)
        return response

    def _get_url(self, api_name, call_name):
        return f"https://api-{self._fqdn}/public_api/v1/{api_name}/{call_name}"

    # https://docs.paloaltonetworks.com/cortex/cortex-xdr/cortex-xdr-api/cortex-xdr-apis/incident-management/get-incidents.html
    def get_incidents(self) -> GetIncidentsResponse:
        response = self._call(api_name="incidents",
                              call_name="get_incidents")
        if response.ok:
            return GetIncidentsResponse.from_json(response.json())
        return None

    # https://docs.paloaltonetworks.com/cortex/cortex-xdr/cortex-xdr-api/cortex-xdr-apis/incident-management/get-extra-incident-data.html
    def get_incident_extra_data(self, incident_id: str, alerts_limit: int) -> GetExtraIncidentDataResponse:
        request_data = GetIncidentExtraDataRequestData(GetIncidentExtraDataItem(incident_id, alerts_limit))
        response = self._call(api_name="incidents",
                              call_name="get_incident_extra_data",
                              request_data=request_data)
        if response.ok:
            return GetExtraIncidentDataResponse.from_json(response.json())
        return None

    # https://docs.paloaltonetworks.com/cortex/cortex-xdr/cortex-xdr-api/cortex-xdr-apis/incident-management/get-alerts.html
    def get_alerts(self, request_data: FilterRequestData = None) -> GetAlertsResponse:
        filters = []

        response = self._call(api_name="alerts",
                              call_name="get_alerts_multi_events",
                              request_data=request_data)
        if response.ok:
            return GetAlertsResponse.from_json(response.json())
        return None

    # https://docs.paloaltonetworks.com/cortex/cortex-xdr/cortex-xdr-api/cortex-xdr-apis/endpoint-management/get-endpoints.html
    def get_all_endpoints(self) -> GetAllEndpointsResponse:
        response = self._call(api_name="endpoints",
                              call_name="get_endpoints")
        if response.ok:
            return GetAllEndpointsResponse.from_json(response.json())
        return None

    def get_endpoint(self, request_data: FilterRequestData) -> GetEndpointResponse:
        response = self._call(api_name="endpoints",
                              call_name="get_endpoint",
                              request_data=request_data)
        if response.ok:
            return GetEndpointResponse.from_json(response.json())
        return None

    # https://docs.paloaltonetworks.com/cortex/cortex-xdr/cortex-xdr-api/cortex-xdr-apis/response-actions/isolate-endpoints.html
    def isolate_endpoints(self, endpoint_id_list: List[str] = None) -> ResponseActionResponse:
        filters = [Filter(field="endpoint_id_list", operator="in", value=endpoint_id_list)]
        request_data = FilterRequestData(FilterRequestDataItem(filters=filters))

        response = self._call(api_name="endpoints",
                              call_name="isolate",
                              request_data=request_data)
        if response.ok:
            return GetEndpointResponse.from_json(response.json())
        return None

    # https://docs.paloaltonetworks.com/cortex/cortex-xdr/cortex-xdr-api/cortex-xdr-apis/response-actions/scan-endpoints.html
    def scan_endpoints(self, request_data: FilterRequestData) -> ResponseActionResponse:
        response = self._call(api_name="endpoints",
                              call_name="scan",
                              request_data=request_data)
        if response.ok:
            return GetEndpointResponse.from_json(response.json())
        return None

    def scan_endpoint(self, request_data: FilterRequestData) -> ResponseActionResponse:
        response = self._call(api_name="endpoints",
                              call_name="get_endpoint",
                              request_data=request_data)
        if response.ok:
            return GetEndpointResponse.from_json(response.json())
        return None
