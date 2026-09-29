from typing import Any, List, Tuple, Union

from cortex_xdr_client.api.operation import UNSET, UnsetType

from cortex_xdr_client.api.authentication import Authentication
from cortex_xdr_client.api.base_api import BaseAPI
from cortex_xdr_client.api.version import APIVersion


class ScheduledQueriesAPI(BaseAPI):
    def __init__(self, auth: Authentication, fqdn: str, timeout: Tuple[int, int],
                 api_version: APIVersion = APIVersion.V3) -> None:
        super(ScheduledQueriesAPI, self).__init__(auth, fqdn, 'scheduled_queries', timeout, api_version)

    def list(self, *,
             filters: Union[List[dict], None, UnsetType] = UNSET,
             extended_view: Union[bool, None, UnsetType] = UNSET,
             list_ids: Union[List[str], None, UnsetType] = UNSET) -> Any:
        """Get scheduled queries

        POST /public_api/v1/scheduled_queries/list
        Available in Cortex XDR 5.x.
        Returns the complete JSON response, bytes for downloads, or None for an empty response.
        Omit optional fields with UNSET; explicit None is sent as JSON null.
        :param filters: body field filters.
        :param extended_view: body field extended_view.
        :param list_ids: body field list_ids.
        """
        self._require_versions((5,))
        body = self._values({'filters': filters, 'extended_view': extended_view, 'list_ids': list_ids})
        body = self._values({'request_data': body, **{}})
        return self._operation(
            '/public_api/v1/scheduled_queries/list', method='post',
            body=body,
        )

    def insert(self, *,
               request_data: Union[List[dict], None, UnsetType] = UNSET) -> Any:
        """Insert or update scheduled queries

        POST /public_api/v1/scheduled_queries/insert
        Available in Cortex XDR 5.x.
        Returns the complete JSON response, bytes for downloads, or None for an empty response.
        Omit optional fields with UNSET; explicit None is sent as JSON null.
        :param request_data: payload field request_data.
        """
        self._require_versions((5,))
        body = request_data
        body = self._values({'request_data': body, **{}})
        return self._operation(
            '/public_api/v1/scheduled_queries/insert', method='post',
            body=body,
        )

    def delete(self, *,
               request_data: Union[List[str], None, UnsetType] = UNSET) -> Any:
        """Delete a scheduled query

        POST /public_api/v1/scheduled_queries/delete
        Available in Cortex XDR 5.x.
        Returns the complete JSON response, bytes for downloads, or None for an empty response.
        Omit optional fields with UNSET; explicit None is sent as JSON null.
        :param request_data: payload field request_data.
        """
        self._require_versions((5,))
        body = request_data
        body = self._values({'request_data': body, **{}})
        return self._operation(
            '/public_api/v1/scheduled_queries/delete', method='post',
            body=body,
        )
