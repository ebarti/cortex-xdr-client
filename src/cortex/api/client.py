from datetime import datetime, timezone
import secrets
import string
import hashlib
import requests
import json
from cortex.api.models.requests import RequestData, RequestDataItem, Sort, Filter
from cortex.api.models.alerts import GetAlertsResponseItem
from cortex.api.models.incidents import GetIncidentsResponseItem, GetExtraIncidentDataResponseItem
from cortex.api.models.endpoints import GetEndpointResponseItem, GetAllEndpointsResponse, ResponseActionResponseItem


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

    def _dump_json(self, data):
        return json.dumps(data, default=lambda o: o.__dict__, indent=4)

    def _execute_call(self, api_name, call_name, request_data: RequestData = None):
        url = self._get_url(api_name=api_name, call_name=call_name)
        headers = self._get_headers()
        json_data = self._dump_json(request_data)

        return requests.post(url, headers=headers, json=json_data, timeout=self._requests_timeout)

    def _get_url(self, api_name, call_name):
        return f"https://api-{self._fqdn}/public_api/v1/{api_name}/{call_name}"
        return Constants.API_URL % (self._fqdn, api_name, call_name)

