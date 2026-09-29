from typing import Any, List, Tuple, Union

from cortex_xdr_client.api.operation import UNSET, UnsetType

from cortex_xdr_client.api.authentication import Authentication
from cortex_xdr_client.api.base_api import BaseAPI
from cortex_xdr_client.api.version import APIVersion


class WidgetsAPI(BaseAPI):
    def __init__(self, auth: Authentication, fqdn: str, timeout: Tuple[int, int],
                 api_version: APIVersion = APIVersion.V3) -> None:
        super(WidgetsAPI, self).__init__(auth, fqdn, 'widgets', timeout, api_version)

    def get(self, *,
            filters: Union[List[dict], None, UnsetType] = UNSET) -> Any:
        """Get widgets

        POST /public_api/v1/widgets/get
        Available in Cortex XDR 5.x.
        Returns the complete JSON response, bytes for downloads, or None for an empty response.
        Omit optional fields with UNSET; explicit None is sent as JSON null.
        :param filters: body field filters.
        """
        self._require_versions((5,))
        body = self._values({'filters': filters})
        body = self._values({'request_data': body, **{}})
        return self._operation(
            '/public_api/v1/widgets/get', method='post',
            body=body,
        )

    def insert(self, *,
               request_data: Union[List[dict], None, UnsetType] = UNSET) -> Any:
        """Insert or update widgets

        POST /public_api/v1/widgets/insert
        Available in Cortex XDR 5.x.
        Returns the complete JSON response, bytes for downloads, or None for an empty response.
        Omit optional fields with UNSET; explicit None is sent as JSON null.
        :param request_data: payload field request_data.
        """
        self._require_versions((5,))
        body = request_data
        body = self._values({'request_data': body, **{}})
        return self._operation(
            '/public_api/v1/widgets/insert', method='post',
            body=body,
        )

    def delete(self, *,
               filters: Union[List[dict], None, UnsetType] = UNSET) -> Any:
        """Delete widgets

        POST /public_api/v1/widgets/delete
        Available in Cortex XDR 5.x.
        Returns the complete JSON response, bytes for downloads, or None for an empty response.
        Omit optional fields with UNSET; explicit None is sent as JSON null.
        :param filters: body field filters.
        """
        self._require_versions((5,))
        body = self._values({'filters': filters})
        body = self._values({'request_data': body, **{}})
        return self._operation(
            '/public_api/v1/widgets/delete', method='post',
            body=body,
        )
