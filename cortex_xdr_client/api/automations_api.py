from typing import Any, List, Tuple, Union

from cortex_xdr_client.api.operation import UNSET, UnsetType

from cortex_xdr_client.api.authentication import Authentication
from cortex_xdr_client.api.base_api import BaseAPI
from cortex_xdr_client.api.version import APIVersion


class AutomationsAPI(BaseAPI):
    def __init__(self, auth: Authentication, fqdn: str, timeout: Tuple[int, int],
                 api_version: APIVersion = APIVersion.V3) -> None:
        super(AutomationsAPI, self).__init__(auth, fqdn, 'automations', timeout, api_version)

    def get_automation_rules(self, *,
                             accept_encoding: Union[str, None, UnsetType] = UNSET,
                             request: Union[dict, None, UnsetType] = UNSET) -> Any:
        """Get automation rules

        POST /public_api/v1/automations/get_automation_rules
        Available in Cortex XDR 3.x.
        Returns the complete JSON response, bytes for downloads, or None for an empty response.
        Omit optional fields with UNSET; explicit None is sent as JSON null.
        :param accept_encoding: header field Accept-Encoding.
        :param request: payload field request.
        """
        self._require_versions((3,))
        body = request
        body = self._values({'request': body, **{}})
        return self._operation(
            '/public_api/v1/automations/get_automation_rules', method='post',
            headers={'Accept-Encoding': accept_encoding},
            body=body,
        )
