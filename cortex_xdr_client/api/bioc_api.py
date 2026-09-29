from typing import Any, List, Tuple, Union

from cortex_xdr_client.api.operation import UNSET, UnsetType

from cortex_xdr_client.api.authentication import Authentication
from cortex_xdr_client.api.base_api import BaseAPI
from cortex_xdr_client.api.version import APIVersion


class BiocAPI(BaseAPI):
    def __init__(self, auth: Authentication, fqdn: str, timeout: Tuple[int, int],
                 api_version: APIVersion = APIVersion.V3) -> None:
        super(BiocAPI, self).__init__(auth, fqdn, 'bioc', timeout, api_version)

    def get(self, *,
            extended_view: Union[bool, None, UnsetType] = UNSET,
            filters: Union[List[dict], None, UnsetType] = UNSET,
            search_from: Union[int, None, UnsetType] = UNSET,
            search_to: Union[int, None, UnsetType] = UNSET) -> Any:
        """Get BIOCs

        POST /public_api/v1/bioc/get
        Available in Cortex XDR 5.x.
        Returns the complete JSON response, bytes for downloads, or None for an empty response.
        Omit optional fields with UNSET; explicit None is sent as JSON null.
        :param extended_view: body field extended_view.
        :param filters: body field filters.
        :param search_from: body field search_from.
        :param search_to: body field search_to.
        """
        self._require_versions((5,))
        body = self._values({'extended_view': extended_view, 'filters': filters, 'search_from': search_from, 'search_to': search_to})
        body = self._values({'request_data': body, **{}})
        return self._operation(
            '/public_api/v1/bioc/get', method='post',
            body=body,
        )

    def insert(self, *,
               request_data: Union[List[dict], None, UnsetType] = UNSET) -> Any:
        """Insert or update BIOCs

        POST /public_api/v1/bioc/insert
        Available in Cortex XDR 5.x.
        Returns the complete JSON response, bytes for downloads, or None for an empty response.
        Omit optional fields with UNSET; explicit None is sent as JSON null.
        :param request_data: payload field request_data.
        """
        self._require_versions((5,))
        body = request_data
        body = self._values({'request_data': body, **{}})
        return self._operation(
            '/public_api/v1/bioc/insert', method='post',
            body=body,
        )

    def delete(self, *,
               filters: Union[List[dict], None, UnsetType] = UNSET) -> Any:
        """Delete BIOCs

        POST /public_api/v1/bioc/delete
        Available in Cortex XDR 5.x.
        Returns the complete JSON response, bytes for downloads, or None for an empty response.
        Omit optional fields with UNSET; explicit None is sent as JSON null.
        :param filters: body field filters.
        """
        self._require_versions((5,))
        body = self._values({'filters': filters})
        body = self._values({'request_data': body, **{}})
        return self._operation(
            '/public_api/v1/bioc/delete', method='post',
            body=body,
        )
