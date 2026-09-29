from typing import Any, List, Tuple, Union

from cortex_xdr_client.api.operation import UNSET, UnsetType

from cortex_xdr_client.api.authentication import Authentication
from cortex_xdr_client.api.base_api import BaseAPI
from cortex_xdr_client.api.version import APIVersion


class ApiKeysAPI(BaseAPI):
    def __init__(self, auth: Authentication, fqdn: str, timeout: Tuple[int, int],
                 api_version: APIVersion = APIVersion.V3) -> None:
        super(ApiKeysAPI, self).__init__(auth, fqdn, 'api_keys', timeout, api_version)

    def get_api_keys(self, *,
                     x_child_tenant_id: Union[str, None, UnsetType] = UNSET,
                     filters: Union[List[dict], None, UnsetType] = UNSET,
                     sort: Union[dict, None, UnsetType] = UNSET,
                     search_from: Union[int, None, UnsetType] = UNSET,
                     search_to: Union[int, None, UnsetType] = UNSET) -> Any:
        """Get existing API Keys

        POST /public_api/v1/api_keys/get_api_keys
        Available in Cortex XDR 5.x.
        Returns the complete JSON response, bytes for downloads, or None for an empty response.
        Omit optional fields with UNSET; explicit None is sent as JSON null.
        :param x_child_tenant_id: header field x-child-tenant-id.
        :param filters: body field filters.
        :param sort: body field sort.
        :param search_from: body field search_from.
        :param search_to: body field search_to.
        """
        self._require_versions((5,))
        body = self._values({'filters': filters, 'sort': sort, 'search_from': search_from, 'search_to': search_to})
        body = self._values({'request_data': body, **{}})
        return self._operation(
            '/public_api/v1/api_keys/get_api_keys', method='post',
            headers={'x-child-tenant-id': x_child_tenant_id},
            body=body,
        )

    def generate(self, *,
                 x_child_tenant_id: Union[str, None, UnsetType] = UNSET,
                 roles: Union[List[str], None, UnsetType] = UNSET,
                 security_level: Union[Any, None, UnsetType] = UNSET,
                 expiration: Union[int, None, UnsetType] = UNSET,
                 comment: Union[str, None, UnsetType] = UNSET) -> Any:
        """Generate an API Key

        POST /public_api/v1/api_keys/generate
        Available in Cortex XDR 5.x.
        Returns the complete JSON response, bytes for downloads, or None for an empty response.
        Omit optional fields with UNSET; explicit None is sent as JSON null.
        :param x_child_tenant_id: header field x-child-tenant-id.
        :param roles: body field roles.
        :param security_level: body field security_level.
        :param expiration: body field expiration.
        :param comment: body field comment.
        """
        self._require_versions((5,))
        body = self._values({'roles': roles, 'security_level': security_level, 'expiration': expiration, 'comment': comment})
        body = self._values({'request_data': body, **{}})
        return self._operation(
            '/public_api/v1/api_keys/generate', method='post',
            headers={'x-child-tenant-id': x_child_tenant_id},
            body=body,
        )

    def delete(self, *,
               x_child_tenant_id: Union[str, None, UnsetType] = UNSET,
               filters: Union[List[dict], None, UnsetType] = UNSET) -> Any:
        """Delete API Keys

        POST /public_api/v1/api_keys/delete
        Available in Cortex XDR 5.x.
        Returns the complete JSON response, bytes for downloads, or None for an empty response.
        Omit optional fields with UNSET; explicit None is sent as JSON null.
        :param x_child_tenant_id: header field x-child-tenant-id.
        :param filters: body field filters.
        """
        self._require_versions((5,))
        body = self._values({'filters': filters})
        body = self._values({'request_data': body, **{}})
        return self._operation(
            '/public_api/v1/api_keys/delete', method='post',
            headers={'x-child-tenant-id': x_child_tenant_id},
            body=body,
        )
