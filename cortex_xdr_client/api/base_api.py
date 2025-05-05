import collections

import requests

from cortex_xdr_client.api.authentication import Authentication


class BaseAPI:
    def __init__(
        self, auth: Authentication, fqdn: str, api_name: str, timeout: tuple[int, int]
    ) -> None:
        self._auth = auth
        self._fqdn = fqdn.replace('api-', '') if fqdn.startswith('api-') else fqdn
        self._requests_timeout = timeout
        self._api_name = api_name

    def _get_url(self, call_name: str, api_version: str | None = None) -> str:
        if api_version is None:
            return (
                f"https://api-{self._fqdn}/public_api/v1/{self._api_name}/{call_name}"
            )
        else:
            return f"https://api-{self._fqdn}/public_api/{api_version}/{self._api_name}/{call_name}"

    def _call(
        self,
        call_name: str,
        method: str = "post",
        params: dict = None,
        json_value: object = None,
        header_params=None,
        api_version: str | None = None,
    ) -> requests.Response:
        if header_params is None:
            header_params = {}
        url = self._get_url(call_name, api_version)
        headers = self.extend(self._auth.get_headers(), header_params)

        return self._execute_call(
            url=url,
            method=method,
            params=params,
            headers=headers,
            json_value=json_value,
        )

    def _execute_call(
        self,
        url: str,
        method: str,
        params: dict = None,
        headers: dict = None,
        json_value: object = None,
    ) -> requests.Response:
        response = None
        if method == "get":
            response = requests.get(
                url, headers=headers, params=params, timeout=self._requests_timeout
            )
        elif method == "post":
            response = requests.post(
                url, headers=headers, json=json_value, timeout=self._requests_timeout
            )
        elif method == "put":
            response = requests.put(
                url, headers=headers, json=json_value, timeout=self._requests_timeout
            )
        elif method == "delete":
            response = requests.delete(
                url, headers=headers, timeout=self._requests_timeout
            )
        response.raise_for_status()
        return response

    @staticmethod
    def extend(*args):
        if args is not None:
            if type(args[0]) is collections.OrderedDict:
                result = collections.OrderedDict()
            else:
                result = {}
            for arg in args:
                result.update(arg)
            return result
        return {}
