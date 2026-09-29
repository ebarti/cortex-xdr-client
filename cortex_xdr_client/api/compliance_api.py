from typing import Any, List, Tuple, Union

from cortex_xdr_client.api.operation import UNSET, UnsetType

from cortex_xdr_client.api.authentication import Authentication
from cortex_xdr_client.api.base_api import BaseAPI
from cortex_xdr_client.api.version import APIVersion


class ComplianceAPI(BaseAPI):
    def __init__(self, auth: Authentication, fqdn: str, timeout: Tuple[int, int],
                 api_version: APIVersion = APIVersion.V3) -> None:
        super(ComplianceAPI, self).__init__(auth, fqdn, 'compliance', timeout, api_version)

    def get_asset_compliance(self, *,
                             asset_id: Union[str, None, UnsetType] = UNSET,
                             last_evaluation_time: Union[int, None, UnsetType] = UNSET,
                             filters: Union[List[dict], None, UnsetType] = UNSET,
                             sort: Union[dict, None, UnsetType] = UNSET,
                             search_from: Union[int, None, UnsetType] = UNSET,
                             search_to: Union[int, None, UnsetType] = UNSET) -> Any:
        """Get asset compliance results

        POST /public_api/v1/compliance/get_asset
        Available in Cortex XDR 5.x.
        Returns the complete JSON response, bytes for downloads, or None for an empty response.
        Omit optional fields with UNSET; explicit None is sent as JSON null.
        :param asset_id: body field asset_id.
        :param last_evaluation_time: body field last_evaluation_time.
        :param filters: body field filters.
        :param sort: body field sort.
        :param search_from: body field search_from.
        :param search_to: body field search_to.
        """
        self._require_versions((5,))
        body = self._values({'asset_id': asset_id, 'last_evaluation_time': last_evaluation_time, 'filters': filters, 'sort': sort, 'search_from': search_from, 'search_to': search_to})
        body = self._values({'request_data': body, **{}})
        return self._operation(
            '/public_api/v1/compliance/get_asset', method='post',
            body=body,
        )
