from enum import Enum
from typing import List, Optional

from cortex_xdr_client.api.base_api import BaseAPI
from cortex_xdr_client.api.models.alerts import (
    AlertSeverity,
    GetAlertsResponse,
)
from cortex_xdr_client.api.models.filters import (
    new_request_data,
    request_filter,
    request_gte_lte_filter,
)


class AlertsAPI(BaseAPI):
    def __init__(self, api_key_id: int, api_key: str, fqdn: str, timeout: tuple[int, int]) -> None:
        super(AlertsAPI, self).__init__(api_key_id, api_key, fqdn, "alerts", timeout)

    # https://docs.paloaltonetworks.com/cortex/cortex-xdr/cortex-xdr-api/cortex-xdr-apis/incident-management/get-alerts.html
    # TODO: add sorting capabilities
    def get_alerts(self,
                   alert_id_list: List[int] = None,
                   alert_source_list: List[str] = None,
                   severities: List[AlertSeverity] = None,
                   creation_time: int = None,
                   after_creation: bool = False,
                   search_from: int = None,
                   search_to: int = None,
                   ) -> Optional[GetAlertsResponse]:
        filters = []

        if alert_id_list is not None:
            filters.append(request_filter("alert_id_list", "in", alert_id_list))

        if alert_source_list is not None:
            filters.append(request_filter("alert_source", "in", alert_source_list))

        if severities is not None and len(severities) > 0:
            filters.append(request_filter("severity", "in", get_enum_values(severities)))

        if creation_time is not None:
            filters.append(request_gte_lte_filter("creation_time", creation_time, after_creation))

        request_data = new_request_data(filters=filters, search_from=search_from, search_to=search_to)

        response = self._call(call_name="get_alerts_multi_events",
                              json_value=request_data)
        if response.ok:
            return GetAlertsResponse.parse_obj(response.json())
        return None


def get_enum_values(p: List[Enum]) -> List[str]:
    return [e.name for e in p]
