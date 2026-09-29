from typing import Any, List, Tuple, Union

from cortex_xdr_client.api.operation import UNSET, UnsetType

from cortex_xdr_client.api.authentication import Authentication
from cortex_xdr_client.api.base_api import BaseAPI
from cortex_xdr_client.api.version import APIVersion


class RiskAPI(BaseAPI):
    def __init__(self, auth: Authentication, fqdn: str, timeout: Tuple[int, int],
                 api_version: APIVersion = APIVersion.V3) -> None:
        super(RiskAPI, self).__init__(auth, fqdn, 'risk', timeout, api_version)

    def get_risk_score(self, *,
                       accept_encoding: Union[str, None, UnsetType] = UNSET,
                       id: Union[str, None, UnsetType] = UNSET) -> Any:
        """Get Risk Score

        POST /public_api/v1/get_risk_score
        Available in Cortex XDR 3.x.
        Returns the complete JSON response, bytes for downloads, or None for an empty response.
        Omit optional fields with UNSET; explicit None is sent as JSON null.
        :param accept_encoding: header field Accept-Encoding.
        :param id: body field id.
        """
        self._require_versions((3,))
        body = self._values({'id': id})
        body = self._values({'request_data': body, **{}})
        return self._operation(
            '/public_api/v1/get_risk_score', method='post',
            headers={'Accept-Encoding': accept_encoding},
            body=body,
        )

    def get_risky_users(self, *,
                        accept_encoding: Union[str, None, UnsetType] = UNSET,
                        body: Union[dict, None, UnsetType] = UNSET) -> Any:
        """Get Risky Users

        POST /public_api/v1/get_risky_users
        Available in Cortex XDR 3.x.
        Returns the complete JSON response, bytes for downloads, or None for an empty response.
        Omit optional fields with UNSET; explicit None is sent as JSON null.
        :param accept_encoding: header field Accept-Encoding.
        :param body: payload field body.
        """
        self._require_versions((3,))
        body = body
        return self._operation(
            '/public_api/v1/get_risky_users', method='post',
            headers={'Accept-Encoding': accept_encoding},
            body=body,
        )

    def get_risky_hosts(self, *,
                        accept_encoding: Union[str, None, UnsetType] = UNSET,
                        body: Union[dict, None, UnsetType] = UNSET) -> Any:
        """Get Risky Hosts

        POST /public_api/v1/get_risky_hosts
        Available in Cortex XDR 3.x.
        Returns the complete JSON response, bytes for downloads, or None for an empty response.
        Omit optional fields with UNSET; explicit None is sent as JSON null.
        :param accept_encoding: header field Accept-Encoding.
        :param body: payload field body.
        """
        self._require_versions((3,))
        body = body
        return self._operation(
            '/public_api/v1/get_risky_hosts', method='post',
            headers={'Accept-Encoding': accept_encoding},
            body=body,
        )
