from datetime import datetime, timezone
import secrets
import string
import hashlib
import requests


class CortexXDRClient(object):

    def __init__(self, api_key_id, api_key, fqdn, default_timeout=(10, 60)):
        self._api_key_id = api_key_id
        self._api_key = api_key
        self._fqdn = fqdn
        self._requests_timeout = default_timeout

    def _get_headers_(self):
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

    def _execute_call_(self, method, url, headers=None, params=None, json=None):
        if method == 'get':
            response = requests.get(url, headers=headers, params=params, timeout=self._requests_timeout)
        elif method == 'post':
            response = requests.post(url, headers=headers, json=json, timeout=self._requests_timeout)
        elif method == 'put':
            response = requests.put(url, headers=headers, json=json, timeout=self._requests_timeout)
        elif method == 'delete':
            response = requests.delete(url, headers=headers, timeout=self._requests_timeout)

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
