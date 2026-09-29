from typing import Any, List, Tuple, Union

from cortex_xdr_client.api.operation import UNSET, UnsetType

from cortex_xdr_client.api.authentication import Authentication
from cortex_xdr_client.api.base_api import BaseAPI
from cortex_xdr_client.api.version import APIVersion


class AssetGroupsAPI(BaseAPI):
    def __init__(self, auth: Authentication, fqdn: str, timeout: Tuple[int, int],
                 api_version: APIVersion = APIVersion.V3) -> None:
        super(AssetGroupsAPI, self).__init__(auth, fqdn, 'asset_groups', timeout, api_version)

    def create(self, *,
               asset_group: Union[dict, None, UnsetType] = UNSET) -> Any:
        """Create an Asset Group

        POST /public_api/v1/asset-groups/create
        Available in Cortex XDR 5.x.
        Returns the complete JSON response, bytes for downloads, or None for an empty response.
        Omit optional fields with UNSET; explicit None is sent as JSON null.
        :param asset_group: body field asset_group.
        """
        self._require_versions((5,))
        body = self._values({'asset_group': asset_group})
        body = self._values({'request_data': body, **{}})
        return self._operation(
            '/public_api/v1/asset-groups/create', method='post',
            body=body,
        )

    def post_public_api_v1_asset_groups_update_by_id(self, *,
                                                     group_id: str,
                                                     asset_group: Union[dict, None, UnsetType] = UNSET) -> Any:
        """Update an Asset Group

        POST /public_api/v1/asset-groups/update/{group_id}
        Available in Cortex XDR 5.x.
        Returns the complete JSON response, bytes for downloads, or None for an empty response.
        Omit optional fields with UNSET; explicit None is sent as JSON null.
        :param group_id: path field group_id.
        :param asset_group: body field asset_group.
        """
        self._require_versions((5,))
        body = self._values({'asset_group': asset_group})
        body = self._values({'request_data': body, **{}})
        return self._operation(
            '/public_api/v1/asset-groups/update/{group_id}', method='post',
            path_params={'group_id': group_id},
            body=body,
        )

    def post_public_api_v1_asset_groups_delete_by_id(self, *,
                                                     group_id: str) -> Any:
        """Delete an Asset Group

        POST /public_api/v1/asset-groups/delete/{group_id}
        Available in Cortex XDR 5.x.
        Returns the complete JSON response, bytes for downloads, or None for an empty response.
        Omit optional fields with UNSET; explicit None is sent as JSON null.
        :param group_id: path field group_id.
        """
        self._require_versions((5,))
        body = UNSET
        return self._operation(
            '/public_api/v1/asset-groups/delete/{group_id}', method='post',
            path_params={'group_id': group_id},
            body=body,
        )
