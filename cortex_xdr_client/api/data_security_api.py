"""Explicit operations from the pinned Cortex XDR documentation snapshot."""
from typing import Any, Tuple, Union

from cortex_xdr_client.api.operation import UNSET, UnsetType
from cortex_xdr_client.api.authentication import Authentication
from cortex_xdr_client.api.base_api import BaseAPI
from cortex_xdr_client.api.version import APIVersion


class DataSecurityAPI(BaseAPI):
    def __init__(self, auth: Authentication, fqdn: str, timeout: Tuple[int, int],
                 api_version: APIVersion = APIVersion.V3) -> None:
        super(DataSecurityAPI, self).__init__(auth, fqdn, 'data_security', timeout, api_version)

    def post_get_data_pattern_inventory(self, *,
            filter: Union[dict, None, UnsetType] = UNSET,
            next_page_token: Union[str, None, UnsetType] = UNSET,
            sort: Union[list, None, UnsetType] = UNSET) -> Any:
        """Get data pattern inventory

        POST /public_api/v1/data-security/data-patterns
        Available in Cortex XDR 5.x.
        Returns the complete JSON response, text, bytes, or None for an empty response.
        Optional fields use UNSET for omission; None is explicit null.
        The source snapshot records this operation and its parameter schema.
        :param filter: body field filter.
        :param next_page_token: body field next_page_token.
        :param sort: body field sort.
        """
        self._require_versions((5,))
        body = self._values({'filter': filter, 'next_page_token': next_page_token, 'sort': sort})
        return self._operation(
            '/public_api/v1/data-security/data-patterns', method='post',
            body=body,
        )

    def post_get_field_inventory_details(self, *,
            filter: Union[dict, None, UnsetType] = UNSET,
            next_page_token: Union[str, None, UnsetType] = UNSET,
            sort: Union[list, None, UnsetType] = UNSET) -> Any:
        """Get field inventory details

        POST /public_api/v1/data-security/objects/fields
        Available in Cortex XDR 5.x.
        Returns the complete JSON response, text, bytes, or None for an empty response.
        Optional fields use UNSET for omission; None is explicit null.
        The source snapshot records this operation and its parameter schema.
        :param filter: body field filter.
        :param next_page_token: body field next_page_token.
        :param sort: body field sort.
        """
        self._require_versions((5,))
        body = self._values({'filter': filter, 'next_page_token': next_page_token, 'sort': sort})
        return self._operation(
            '/public_api/v1/data-security/objects/fields', method='post',
            body=body,
        )

    def post_get_file_inventory_details(self, *,
            filter: Union[dict, None, UnsetType] = UNSET,
            next_page_token: Union[str, None, UnsetType] = UNSET,
            sort: Union[list, None, UnsetType] = UNSET) -> Any:
        """Get file inventory details

        POST /public_api/v1/data-security/objects/files
        Available in Cortex XDR 5.x.
        Returns the complete JSON response, text, bytes, or None for an empty response.
        Optional fields use UNSET for omission; None is explicit null.
        The source snapshot records this operation and its parameter schema.
        :param filter: body field filter.
        :param next_page_token: body field next_page_token.
        :param sort: body field sort.
        """
        self._require_versions((5,))
        body = self._values({'filter': filter, 'next_page_token': next_page_token, 'sort': sort})
        return self._operation(
            '/public_api/v1/data-security/objects/files', method='post',
            body=body,
        )
