import hashlib
import secrets
import string
from datetime import timezone, datetime

import requests


class BaseAPI:
    def __init__(self, api_key_id: int, api_key: str, fqdn: str, api_name: str, timeout: tuple[int, int]) -> None:
        self._api_key_id = api_key_id
        self._api_key = api_key
        self._fqdn = fqdn
        self._requests_timeout = timeout
        self._api_name = api_name

    def _get_headers(self) -> dict:
        nonce = "".join([secrets.choice(string.ascii_letters + string.digits) for _ in range(64)])
        timestamp = int(datetime.now(timezone.utc).timestamp()) * 1000
        auth_key = "%s%s%s" % (self._api_key, nonce, timestamp)
        auth_key = auth_key.encode("utf-8")
        api_key_hash = hashlib.sha256(auth_key).hexdigest()
        return {
            "x-xdr-timestamp": str(timestamp),
            "x-xdr-nonce": nonce,
            "x-xdr-auth-id": str(self._api_key_id),
            "Authorization": api_key_hash
        }

    def _get_url(self, call_name: str) -> str:
        return f"https://api-{self._fqdn}/public_api/v1/{self._api_name}/{call_name}"

    def _call(self,
              call_name: str,
              method: str = "post",
              params: dict = None,
              json_value: object = None) -> requests.Response:
        url = self._get_url(call_name)
        headers = self._get_headers()

        return self._execute_call(url=url,
                                  method=method,
                                  params=params,
                                  headers=headers,
                                  json_value=json_value)

    def _execute_call(self,
                      url: str,
                      method: str,
                      params: dict = None,
                      headers: dict = None,
                      json_value: object = None) -> requests.Response:
        response = None
        if method == 'get':
            response = requests.get(url, headers=headers, params=params, timeout=self._requests_timeout)
        elif method == 'post':
            response = requests.post(url, headers=headers, json=json_value, timeout=self._requests_timeout)
        elif method == 'put':
            response = requests.put(url, headers=headers, json=json_value, timeout=self._requests_timeout)
        elif method == 'delete':
            response = requests.delete(url, headers=headers, timeout=self._requests_timeout)
        return response
