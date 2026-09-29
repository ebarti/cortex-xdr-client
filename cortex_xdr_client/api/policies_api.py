from typing import Any, List, Tuple, Union

from cortex_xdr_client.api.operation import UNSET, UnsetType

from cortex_xdr_client.api.authentication import Authentication
from cortex_xdr_client.api.base_api import BaseAPI
from cortex_xdr_client.api.version import APIVersion


class PoliciesAPI(BaseAPI):
    def __init__(self, auth: Authentication, fqdn: str, timeout: Tuple[int, int],
                 api_version: APIVersion = APIVersion.V3) -> None:
        super(PoliciesAPI, self).__init__(auth, fqdn, 'policies', timeout, api_version)

    def prevention_edit(self, *,
                        edit_requests: Union[List[dict], None, UnsetType] = UNSET) -> Any:
        """Edit prevention policy rules

        POST /public_api/v1/policies/prevention/edit
        Available in Cortex XDR 5.x.
        Returns the complete JSON response, bytes for downloads, or None for an empty response.
        Omit optional fields with UNSET; explicit None is sent as JSON null.
        :param edit_requests: body field edit_requests.
        """
        self._require_versions((5,))
        body = self._values({'edit_requests': edit_requests})
        body = self._values({'request_data': body, **{}})
        return self._operation(
            '/public_api/v1/policies/prevention/edit', method='post',
            body=body,
        )
