from enum import Enum
from typing import List
from typing import Optional
from typing import Tuple

from cortex_xdr_client.api.authentication import Authentication
from cortex_xdr_client.api.base_api import BaseAPI
from cortex_xdr_client.api.models.alerts import AlertSeverity
from cortex_xdr_client.api.models.alerts import GetAlertsResponse
from cortex_xdr_client.api.models.alerts import GetAlertsResponseV2
from cortex_xdr_client.api.models.alerts import QuerySortOrder
from cortex_xdr_client.api.models.alerts import QuerySortType
from cortex_xdr_client.api.models.filters import new_request_data
from cortex_xdr_client.api.models.filters import request_filter
from cortex_xdr_client.api.models.filters import request_gte_lte_filter


class AlertsAPI(BaseAPI):
    def __init__(self, auth: Authentication, fqdn: str, timeout: Tuple[int, int]) -> None:
        super(AlertsAPI, self).__init__(auth, fqdn, "alerts", timeout)

    # https://docs.paloaltonetworks.com/cortex/cortex-xdr/cortex-xdr-api/cortex-xdr-apis/incident-management/get-alerts.html
    def get_alerts(self,
                   alert_id_list: List[int] = None,
                   alert_source_list: List[str] = None,
                   severities: List[AlertSeverity] = None,
                   creation_time: int = None,
                   after_creation: bool = False,
                   server_creation_time: int = None,
                   after_server_creation: bool = False,
                   search_from: int = None,
                   search_to: int = None,
                   sort_type: QuerySortType = None,
                   sort_order: QuerySortOrder = QuerySortOrder.ASC
                   ) -> Optional[GetAlertsResponse]:
        """
        Get a list of alerts with multiple events.

        :param alert_id_list: List of integers of the Alert ID
        :param alert_source_list: List of strings of the Alert source
        :param severities: List of strings of the Alert severity
        :param creation_time: Timestamp of the Creation time. Also known as detection_timestamp.
        :param after_creation: If the creation date will be the upper or lower bound limit.
        :param server_creation_time: Timestamp of the Server creation time. Also known as local_insert_ts.
        :param after_server_creation: If the server creation date will be the upper or lower bound limit.
        :param search_to: Integer representing the end offset within the result set after which you do not want incidents returned.
        :param search_from: Integer representing the starting offset within the query result set from which you want incidents returned.
        :param sort_type: The field to sort by the requested alerts.
        :param sort_order: The order of the sorting.
        :return: Returns a GetAlertsResponse object if successful.
        """
        filters = []
        sort = {'field': sort_type, 'keyword': sort_order} if sort_type else None

        if alert_id_list is not None:
            filters.append(request_filter("alert_id_list", "in", alert_id_list))

        if alert_source_list is not None:
            filters.append(request_filter("alert_source", "in", alert_source_list))

        if severities is not None and len(severities) > 0:
            filters.append(request_filter("severity", "in", get_enum_values(severities)))

        if creation_time is not None:
            filters.append(request_gte_lte_filter("creation_time", creation_time, after_creation))

        if server_creation_time is not None:
            filters.append(request_gte_lte_filter("server_creation_time", server_creation_time, after_server_creation))

        request_data = new_request_data(filters=filters, search_from=search_from, search_to=search_to, sort=sort)

        response = self._call(call_name="get_alerts_multi_events",
                              json_value=request_data)
        return GetAlertsResponse.parse_obj(response.json())

    def get_alerts_v2(self,
                      alert_id_list: List[int] = None,
                      alert_source_list: List[str] = None,
                      severities: List[AlertSeverity] = None,
                      creation_time: int = None,
                      after_creation: bool = False,
                      server_creation_time: int = None,
                      after_server_creation: bool = False,
                      search_from: int = None,
                      search_to: int = None,
                      sort_type: QuerySortType = None,
                      sort_order: QuerySortOrder = QuerySortOrder.ASC
                      ) -> Optional[GetAlertsResponseV2]:
        """
        Get a list of alerts with multiple events.

        :param alert_id_list: List of integers of the Alert ID
        :param alert_source_list: List of strings of the Alert source
        :param severities: List of strings of the Alert severity
        :param creation_time: Timestamp of the Creation time. Also known as detection_timestamp.
        :param after_creation: If the creation date will be the upper or lower bound limit.
        :param server_creation_time: Timestamp of the Server creation time. Also known as local_insert_ts.
        :param after_server_creation: If the server creation date will be the upper or lower bound limit.
        :param search_to: Integer representing the end offset within the result set after which you do not want incidents returned.
        :param search_from: Integer representing the starting offset within the query result set from which you want incidents returned.
        :param sort_type: The field to sort by the requested alerts.
        :param sort_order: The order of the sorting.
        :return: Returns a GetAlertsResponse object if successful.
        """
        filters = []
        sort = {'field': sort_type, 'keyword': sort_order} if sort_type else None

        if alert_id_list is not None:
            filters.append(request_filter("alert_id_list", "in", alert_id_list))

        if alert_source_list is not None:
            filters.append(request_filter("alert_source", "in", alert_source_list))

        if severities is not None and len(severities) > 0:
            filters.append(request_filter("severity", "in", get_enum_values(severities)))

        if creation_time is not None:
            filters.append(request_gte_lte_filter("creation_time", creation_time, after_creation))

        if server_creation_time is not None:
            filters.append(request_gte_lte_filter("server_creation_time", server_creation_time, after_server_creation))

        request_data = new_request_data(filters=filters, search_from=search_from, search_to=search_to,
                                        sort=sort)

        response = self._call(call_name="get_alerts_multi_events",
                              json_value=request_data, api_version="v2")
        return GetAlertsResponseV2.parse_obj(response.json())


def get_enum_values(p: List[Enum]) -> List[str]:
    return [e.name for e in p]
