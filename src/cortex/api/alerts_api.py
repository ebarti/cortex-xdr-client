from cortex.api.base_api import BaseAPI
from typing import List
from cortex.api.models.filters import (
    Filter,
    FilterRequestData,
    FilterRequestDataItem,
)


class AlertIdFilter(Filter):
    def __init__(self, value: List[str]) -> None:
        super().__init__("alert_id_filter", "in", value)


class AlertSourceFilter(Filter):
    def __init__(self, value: List[int]) -> None:
        super().__init__("alert_source", "in", value)


class AlertSeverityFilter(Filter):
    def __init__(self, value: List[str]) -> None:
        super().__init__("severity", "in", value)


class CreationTimeBeforeFilter(Filter):
    def __init__(self, creation_time: int) -> None:
        super().__init__("creation_time", "lte", creation_time)


class CreationTimeAfterFilter(Filter):
    def __init__(self, creation_time: int) -> None:
        super().__init__("creation_time", "gte", creation_time)


class AlertsAPI(BaseAPI):
    def __init__(self, api_key_id: str, api_key: str, fqdn: str, default_timeout: tuple[int, int] = (10, 60)) -> None:
        super(AlertsAPI, self).__init__(api_key_id, api_key, fqdn, default_timeout)

    # https://docs.paloaltonetworks.com/cortex/cortex-xdr/cortex-xdr-api/cortex-xdr-apis/incident-management/get-alerts.html
    def get_alerts(self,
                   alert_id_list: List[int] = None,
                   alert_source: List[str] = None,
                   severity: List[str] = None,
                   creation_time: int = None,
                   after_creation: bool = False,
                   ) -> dict:
        filters = []

        if alert_id_list is not None:
            filters.append(AlertIdFilter(alert_id_list))

        if alert_source is not None:
            filters.append(AlertSourceFilter(alert_source))

        if severity is not None:
            filters.append(AlertSeverityFilter(severity))



        response = self._call(api_name="alerts",
                              call_name="get_alerts_multi_events",
                              request_data=request_data)
        if response.ok:
            return response.json()
        return None
