from typing import Any, List, Tuple, Union

from cortex_xdr_client.api.operation import UNSET, UnsetType

from cortex_xdr_client.api.authentication import Authentication
from cortex_xdr_client.api.base_api import BaseAPI
from cortex_xdr_client.api.version import APIVersion


class QueryLibraryAPI(BaseAPI):
    def __init__(self, auth: Authentication, fqdn: str, timeout: Tuple[int, int],
                 api_version: APIVersion = APIVersion.V3) -> None:
        super(QueryLibraryAPI, self).__init__(auth, fqdn, 'query_library', timeout, api_version)

    def get_queries(self, *,
                    extended_view: Union[bool, None, UnsetType] = UNSET,
                    xql_query_names: Union[List[str], None, UnsetType] = UNSET,
                    xql_query_tags: Union[List[str], None, UnsetType] = UNSET) -> Any:
        """Get XQL Queries

        POST /public_api/xql_library/get
        Available in Cortex XDR 5.x.
        Returns the complete JSON response, bytes for downloads, or None for an empty response.
        Omit optional fields with UNSET; explicit None is sent as JSON null.
        :param extended_view: body field extended_view.
        :param xql_query_names: body field xql_query_names.
        :param xql_query_tags: body field xql_query_tags.
        """
        self._require_versions((5,))
        body = self._values({'extended_view': extended_view, 'xql_query_names': xql_query_names, 'xql_query_tags': xql_query_tags})
        body = self._values({'request_data': body, **{}})
        return self._operation(
            '/public_api/xql_library/get', method='post',
            body=body,
        )

    def insert_queries(self, *,
                       xql_queries_override: Union[bool, None, UnsetType] = UNSET,
                       xql_queries: Union[List[dict], None, UnsetType] = UNSET,
                       xql_query_tags: Union[List[str], None, UnsetType] = UNSET) -> Any:
        """Insert or update XQL queries

        POST /public_api/xql_library/insert
        Available in Cortex XDR 5.x.
        Returns the complete JSON response, bytes for downloads, or None for an empty response.
        Omit optional fields with UNSET; explicit None is sent as JSON null.
        :param xql_queries_override: body field xql_queries_override.
        :param xql_queries: body field xql_queries.
        :param xql_query_tags: body field xql_query_tags.
        """
        self._require_versions((5,))
        body = self._values({'xql_queries_override': xql_queries_override, 'xql_queries': xql_queries, 'xql_query_tags': xql_query_tags})
        body = self._values({'request_data': body, **{}})
        return self._operation(
            '/public_api/xql_library/insert', method='post',
            body=body,
        )

    def delete_queries(self, *,
                       xql_query_names: Union[List[str], None, UnsetType] = UNSET,
                       xql_query_tags: Union[List[str], None, UnsetType] = UNSET) -> Any:
        """Delete XQL Queries

        POST /public_api/xql_library/delete
        Available in Cortex XDR 5.x.
        Returns the complete JSON response, bytes for downloads, or None for an empty response.
        Omit optional fields with UNSET; explicit None is sent as JSON null.
        :param xql_query_names: body field xql_query_names.
        :param xql_query_tags: body field xql_query_tags.
        """
        self._require_versions((5,))
        body = self._values({'xql_query_names': xql_query_names, 'xql_query_tags': xql_query_tags})
        body = self._values({'request_data': body, **{}})
        return self._operation(
            '/public_api/xql_library/delete', method='post',
            body=body,
        )
