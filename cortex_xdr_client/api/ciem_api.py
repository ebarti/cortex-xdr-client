"""Explicit operations from the pinned Cortex XDR documentation snapshot."""
from typing import Any, Tuple, Union

from cortex_xdr_client.api.operation import UNSET, UnsetType
from cortex_xdr_client.api.authentication import Authentication
from cortex_xdr_client.api.base_api import BaseAPI
from cortex_xdr_client.api.version import APIVersion


class CiemAPI(BaseAPI):
    def __init__(self, auth: Authentication, fqdn: str, timeout: Tuple[int, int],
                 api_version: APIVersion = APIVersion.V3) -> None:
        super(CiemAPI, self).__init__(auth, fqdn, 'ciem', timeout, api_version)

    def least_privilege_access_suggestion_for_an_asset(self, *,
            asset_id: str,
            output_format: str,
            lookback_duration_days: int,
            cloud_type: str) -> Any:
        """Least Privilege Access suggestion for an asset

        GET /public_api/ciem/v1/assets/{assetId}/least-privileged-access
        Available in Cortex XDR 5.x.
        Returns the complete JSON response, text, bytes, or None for an empty response.
        Optional fields use UNSET for omission; None is explicit null.
        The source snapshot records this operation and its parameter schema.
        :param asset_id: path field assetId.
        :param output_format: query field output_format.
        :param lookback_duration_days: query field lookback_duration_days.
        :param cloud_type: query field cloud_type.
        """
        self._require_versions((5,))
        body = UNSET
        return self._operation(
            '/public_api/ciem/v1/assets/{assetId}/least-privileged-access', method='get',
            path_params={'assetId': asset_id},
            query=[('output_format', output_format, True), ('lookback_duration_days', lookback_duration_days, True), ('cloud_type', cloud_type, True)],
            body=body,
        )

    def ciem_access_get_by_source(self, *,
            source_uai: str,
            next_page_token: Union[str, None, UnsetType] = UNSET,
            filter: Union[dict, None, UnsetType] = UNSET,
            sort: Union[list, None, UnsetType] = UNSET) -> Any:
        """Retrieve the resources a source identity can access

        GET /public_api/ciem/v1/access/source/{source_uai}
        Available in Cortex XDR 5.x.
        Returns the complete JSON response, text, bytes, or None for an empty response.
        Optional fields use UNSET for omission; None is explicit null.
        The source snapshot records this operation and its parameter schema.
        :param source_uai: path field source_uai.
        :param next_page_token: query field next_page_token.
        :param filter: body field filter.
        :param sort: body field sort.
        """
        self._require_versions((5,))
        body = self._values({'filter': filter, 'sort': sort})
        return self._operation(
            '/public_api/ciem/v1/access/source/{source_uai}', method='get',
            path_params={'source_uai': source_uai},
            query=[('next_page_token', next_page_token, True)],
            body=body,
        )

    def ciem_access_get_by_granter(self, *,
            granter_uai: str,
            next_page_token: Union[str, None, UnsetType] = UNSET,
            filter: Union[dict, None, UnsetType] = UNSET,
            sort: Union[list, None, UnsetType] = UNSET) -> Any:
        """Retrieve the access conferred by a permission-granting entity

        GET /public_api/ciem/v1/access/granter/{granter_uai}
        Available in Cortex XDR 5.x.
        Returns the complete JSON response, text, bytes, or None for an empty response.
        Optional fields use UNSET for omission; None is explicit null.
        The source snapshot records this operation and its parameter schema.
        :param granter_uai: path field granter_uai.
        :param next_page_token: query field next_page_token.
        :param filter: body field filter.
        :param sort: body field sort.
        """
        self._require_versions((5,))
        body = self._values({'filter': filter, 'sort': sort})
        return self._operation(
            '/public_api/ciem/v1/access/granter/{granter_uai}', method='get',
            path_params={'granter_uai': granter_uai},
            query=[('next_page_token', next_page_token, True)],
            body=body,
        )

    def ciem_access_get_by_destination(self, *,
            destination_uai: str,
            next_page_token: Union[str, None, UnsetType] = UNSET,
            filter: Union[dict, None, UnsetType] = UNSET,
            sort: Union[list, None, UnsetType] = UNSET) -> Any:
        """Retrieve the identities that can access a destination resource

        GET /public_api/ciem/v1/access/destination/{destination_uai}
        Available in Cortex XDR 5.x.
        Returns the complete JSON response, text, bytes, or None for an empty response.
        Optional fields use UNSET for omission; None is explicit null.
        The source snapshot records this operation and its parameter schema.
        :param destination_uai: path field destination_uai.
        :param next_page_token: query field next_page_token.
        :param filter: body field filter.
        :param sort: body field sort.
        """
        self._require_versions((5,))
        body = self._values({'filter': filter, 'sort': sort})
        return self._operation(
            '/public_api/ciem/v1/access/destination/{destination_uai}', method='get',
            path_params={'destination_uai': destination_uai},
            query=[('next_page_token', next_page_token, True)],
            body=body,
        )
