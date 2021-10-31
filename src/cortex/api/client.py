from datetime import datetime, timezone
import secrets
import string
import hashlib
import requests
import json
from cortex.api.models.requests import RequestData, Sort, Filter
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

    def _execute_call(self, api_name, call_name, request_data: RequestData = None):
        url = self._get_url(api_name=api_name, call_name=call_name)
        headers = self._get_headers()
        json_data = {"request_data": {}}
        if request_data is not None:
            json_data = json.dumps(request_data, default=lambda o: o.__dict__, indent=4)

        return requests.post(url, headers=headers, json=json, timeout=self._requests_timeout)

    def _get_url(self, api_name, call_name):
        return f"https://api-{self._fqdn}/public_api/v1/{api_name}/{call_name}"
        return Constants.API_URL % (self._fqdn, api_name, call_name)

    def test_advanced_authentication(self, api_key_id, api_key):
        # Generate a 64 bytes random string
        nonce = "".join([secrets.choice(string.ascii_letters + string.digits) for _ in range(64)])
        # Get the current timestamp as milliseconds.
        timestamp = int(datetime.now(timezone.utc).timestamp()) * 1000
        # Generate the auth key:
        auth_key = "%s%s%s" % (api_key, nonce, timestamp)
        # Convert to bytes object
        auth_key = auth_key.encode("utf-8")
        # Calculate sha256:
        api_key_hash = hashlib.sha256(auth_key).hexdigest()
        # Generate HTTP call headers
        headers = {
            "x-xdr-timestamp": str(timestamp),
            "x-xdr-nonce": nonce,
            "x-xdr-auth-id": str(api_key_id),
            "Authorization": api_key_hash
        }
        parameters = {}
        res = requests.post(url="https://api-{fqdn}/public_api/v1/{name of api}/{name of call}",
                            headers=headers,
                            json=parameters)
        return res
