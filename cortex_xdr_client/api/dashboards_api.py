from typing import Any, List, Tuple, Union

from cortex_xdr_client.api.operation import UNSET, UnsetType

from cortex_xdr_client.api.authentication import Authentication
from cortex_xdr_client.api.base_api import BaseAPI
from cortex_xdr_client.api.version import APIVersion


class DashboardsAPI(BaseAPI):
    def __init__(self, auth: Authentication, fqdn: str, timeout: Tuple[int, int],
                 api_version: APIVersion = APIVersion.V3) -> None:
        super(DashboardsAPI, self).__init__(auth, fqdn, 'dashboards', timeout, api_version)

    def get(self, *,
            filters: Union[List[dict], None, UnsetType] = UNSET) -> Any:
        """Get dashboards

        POST /public_api/v1/dashboards/get
        Available in Cortex XDR 5.x.
        Returns the complete JSON response, bytes for downloads, or None for an empty response.
        Omit optional fields with UNSET; explicit None is sent as JSON null.
        :param filters: body field filters.
        """
        self._require_versions((5,))
        body = self._values({'filters': filters})
        body = self._values({'request_data': body, **{}})
        return self._operation(
            '/public_api/v1/dashboards/get', method='post',
            body=body,
        )

    def insert(self, *,
               dashboards_data: Union[List[dict], None, UnsetType] = UNSET,
               widgets_data: Union[List[dict], None, UnsetType] = UNSET) -> Any:
        """Insert or update dashboards

        POST /public_api/v1/dashboards/insert
        Available in Cortex XDR 5.x.
        Returns the complete JSON response, bytes for downloads, or None for an empty response.
        Omit optional fields with UNSET; explicit None is sent as JSON null.
        :param dashboards_data: body field dashboards_data.
        :param widgets_data: body field widgets_data.
        """
        self._require_versions((5,))
        body = self._values({'dashboards_data': dashboards_data, 'widgets_data': widgets_data})
        body = self._values({'request_data': body, **{}})
        return self._operation(
            '/public_api/v1/dashboards/insert', method='post',
            body=body,
        )

    def delete(self, *,
               filters: Union[List[dict], None, UnsetType] = UNSET) -> Any:
        """Delete dashboards

        POST /public_api/v1/dashboards/delete
        Available in Cortex XDR 5.x.
        Returns the complete JSON response, bytes for downloads, or None for an empty response.
        Omit optional fields with UNSET; explicit None is sent as JSON null.
        :param filters: body field filters.
        """
        self._require_versions((5,))
        body = self._values({'filters': filters})
        body = self._values({'request_data': body, **{}})
        return self._operation(
            '/public_api/v1/dashboards/delete', method='post',
            body=body,
        )
