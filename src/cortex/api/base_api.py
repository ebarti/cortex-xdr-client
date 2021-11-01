import hashlib
import secrets
import string
from datetime import timezone, datetime

import requests

from cortex.api.utils.utils import dump_json


class BaseAPI:

    def __init__(self, api_key_id: str, api_key: str, fqdn: str, timeout: tuple[int, int]):
        self._api_key_id = api_key_id
        self._api_key = api_key
        self._fqdn = fqdn
        self._requests_timeout = timeout

    def _get_headers(self) -> dict:
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

    def _get_url(self, api_name: str, call_name: str) -> str:
        return f"https://api-{self._fqdn}/public_api/v1/{api_name}/{call_name}"

    def _call(self, api_name: str, call_name: str, method: str = "post", params: dict = None, request_data: object = None) -> requests.Response:
        url = self._get_url(api_name=api_name, call_name=call_name)
        headers = self._get_headers()
        # json = dump_json(request_data)

        return self._execute_call(url=url,
                                  method=method,
                                  timeout=self._requests_timeout,
                                  params=params,
                                  headers=headers,
                                  json=request_data)

    def _execute_call(self, url: str, method: str, params: dict = None, headers: dict = None, json: object = None) -> requests.Response:
        response = None
        if method == 'get':
            response = requests.get(url, headers=headers, params=params, timeout=self.requests_timeout)
        elif method == 'post':
            response = requests.post(url, headers=headers, json=json, timeout=self.requests_timeout)
        elif method == 'put':
            response = requests.put(url, headers=headers, json=json, timeout=self.requests_timeout)
        elif method == 'delete':
            response = requests.delete(url, headers=headers, timeout=self.requests_timeout)
        return response