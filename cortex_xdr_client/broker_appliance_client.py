"""Direct Broker VM appliance API, separate from the tenant API-key client."""

from typing import Optional, Tuple
from urllib.parse import urlsplit

import requests

from cortex_xdr_client.api.broker_appliance_operations import BrokerApplianceOperations
from cortex_xdr_client.api.version import APIVersion


class BrokerApplianceClient(BrokerApplianceOperations):
    """Opt-in client for Broker VM 32+ on-appliance HTTPS operations.

    A broker origin is the appliance itself (for example,
    ``https://broker.example.local``). No tenant API key is accepted, and no
    network call occurs during construction. The bootstrap operations require
    the local admin password. Call ``set_token`` with the ``reply.api_key``
    returned by ``generate_token`` before other operations.
    """

    _BOOTSTRAP = frozenset(('/public_api/v1/auth/reset-initial-password',
                            '/public_api/v1/auth/token'))

    def __init__(self, broker_origin: str, token: Optional[str] = None,
                 timeout: Tuple[int, int] = (10, 60)) -> None:
        parsed = urlsplit(broker_origin)
        if (parsed.scheme != 'https' or not parsed.hostname or parsed.username or parsed.password
                or parsed.path not in ('', '/') or parsed.query or parsed.fragment
                or '\\' in broker_origin):
            raise ValueError('broker_origin must be an HTTPS origin without credentials or a path')
        self._base_url = broker_origin.rstrip('/')
        self._requests_timeout = timeout
        self._api_version = APIVersion.V5
        self._token = None
        if token is not None:
            self.set_token(token)

    def set_token(self, token: str) -> None:
        """Install the short-lived Bearer token returned by ``generate_token``."""
        if not isinstance(token, str) or not token or any(c in token for c in '\r\n'):
            raise ValueError('token must be a nonempty single-line string')
        self._token = token

    def clear_token(self) -> None:
        self._token = None

    def request(self, path: str, method: str = 'post', params=None, json_value=None,
                header_params=None, data=None, files=None) -> requests.Response:
        parsed = urlsplit(path)
        if (not path.startswith('/') or path.startswith('//') or parsed.scheme or parsed.netloc
                or parsed.query or parsed.fragment or '\\' in path
                or any(part in ('.', '..') for part in path.split('/'))):
            raise ValueError('path must be an appliance-relative API path without query or relative segments')
        method = method.lower()
        if method not in ('get', 'post', 'put', 'patch', 'delete', 'head', 'options'):
            raise ValueError('unsupported HTTP method')
        if json_value is not None and (data is not None or files is not None):
            raise ValueError('use either JSON or data/files for the request body')
        headers = dict(header_params or {})
        if any(key.lower() in ('authorization', 'x-xdr-auth-id', 'x-xdr-timestamp', 'x-xdr-nonce')
               for key in headers):
            raise ValueError('authentication headers are controlled by this client')
        if path not in self._BOOTSTRAP:
            if self._token is None:
                raise ValueError('a Broker VM Bearer token is required for this operation')
            headers['Authorization'] = 'Bearer ' + self._token
        response = requests.request(method, self._base_url + path, params=params,
                                    json=json_value, data=data, files=files, headers=headers,
                                    timeout=self._requests_timeout, allow_redirects=False)
        response.raise_for_status()
        if response.is_redirect:
            raise requests.HTTPError('Broker appliance API requests must not redirect', response=response)
        return response
