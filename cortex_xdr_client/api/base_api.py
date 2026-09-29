import collections
from typing import Tuple
from urllib.parse import urlsplit

import requests

from cortex_xdr_client.api.authentication import Authentication
from cortex_xdr_client.api.version import APIVersion


class BaseAPI:
    def __init__(self, auth: Authentication, fqdn: str, api_name: str, timeout: Tuple[int, int],
                 api_version: APIVersion = APIVersion.V3) -> None:
        self._auth = auth
        self._fqdn = fqdn
        self._requests_timeout = timeout
        self._api_name = api_name
        self._api_version = APIVersion(api_version)
        host = fqdn.rstrip('/')
        if '://' in host:
            parsed = urlsplit(host)
            if parsed.scheme != 'https' or parsed.path or parsed.query or parsed.fragment or parsed.username:
                raise ValueError("fqdn must be a tenant hostname or an HTTPS origin without a path")
            host = parsed.netloc
        if not host or any(character in host for character in '/?#@\\'):
            raise ValueError("fqdn must be a tenant hostname")
        if not host.startswith('api-'):
            host = 'api-' + host
        self._base_url = 'https://' + host

    def _require_version(self, api_version: APIVersion, replacement: str = None) -> None:
        if self._api_version != api_version:
            message = f"{self._api_name} requires Cortex XDR {api_version.value}.x."
            if replacement:
                message += f" Use {replacement} instead."
            raise NotImplementedError(message)

    def _get_url(self, call_name: str) -> str:
        if self._api_name == 'incidents':
            self._require_version(APIVersion.V3, 'cases_api')
        elif self._api_name == 'alerts':
            self._require_version(APIVersion.V3, 'issues_api')
        elif self._api_name in ('case', 'issue'):
            self._require_version(APIVersion.V5)
        return f"{self._base_url}/public_api/v1/{self._api_name}/{call_name}"

    def request(self, path: str, method: str = "post", params: dict = None,
                json_value: object = None, header_params: dict = None,
                data=None, files=None) -> requests.Response:
        """
        Call an API using its exact documented path and return the HTTP response.

        :param path: Absolute tenant-relative path, including the API prefix/version.
        :param json_value: Complete JSON body; no request_data envelope is added.
        :param data: Form fields or raw body for non-JSON operations.
        :param files: Multipart files in requests format.
        """
        parsed = urlsplit(path)
        if not path.startswith('/') or path.startswith('//') or parsed.scheme or parsed.netloc or parsed.query or parsed.fragment:
            raise ValueError("path must be a tenant-relative API path; use params for query parameters")
        if '\\' in path or any(part in ('.', '..') for part in path.split('/')):
            raise ValueError("path must not contain relative segments or backslashes")
        return self._execute_call(url=self._base_url + path,
                                  method=method,
                                  params=params,
                                  headers=self.extend(self._auth.get_headers(), header_params or {}),
                                  json_value=json_value,
                                  data=data,
                                  files=files)

    def _call(self,
              call_name: str,
              method: str = "post",
              params: dict = None,
              json_value: object = None,
              header_params=None) -> requests.Response:
        if header_params is None:
            header_params = {}
        url = self._get_url(call_name)
        headers = self.extend(self._auth.get_headers(), header_params)

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
                      json_value: object = None,
                      data=None,
                      files=None) -> requests.Response:
        method = method.lower()
        if method not in ('get', 'post', 'put', 'patch', 'delete', 'head', 'options'):
            raise ValueError(f"Unsupported HTTP method: {method}")
        if json_value is not None and (data is not None or files is not None):
            raise ValueError("Use either json_value or data/files for the request body")
        response = requests.request(method, url, headers=headers, params=params, json=json_value,
                                    data=data, files=files, timeout=self._requests_timeout,
                                    allow_redirects=False)
        response.raise_for_status()
        if response.is_redirect:
            raise requests.HTTPError("Authenticated API requests must not redirect", response=response)
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
