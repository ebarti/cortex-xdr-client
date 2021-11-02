from cortex.api.base_api import BaseAPI
from typing import List, Optional
from cortex.api.models.filters import (
    Filter,
    new_filter_request_data,
)
from cortex.api.utils.constants import Constants


class AlertsAPI(BaseAPI):
    def __init__(self, api_key_id: str, api_key: str, fqdn: str, timeout: tuple[int, int]) -> None:
        super(AlertsAPI, self).__init__(api_key_id, api_key, fqdn, "alerts", timeout)

    @staticmethod
    def _alert_id_filter(value: List[str]) -> Filter:
        return Filter("alert_id_filter", "in", value)

    @staticmethod
    def _alert_source_filter(value: List[int]) -> Filter:
        return Filter("alert_source", "in", value)

    @staticmethod
    def _severities_filter(value: List[str]) -> Filter:
        return Filter("severity", "in", value)

    @staticmethod
    def _creation_time_filter(creation_time: int, after: bool) -> Filter:
        if after:
            return Filter("creation_time", "gte", creation_time)
        return Filter("creation_time", "lte", creation_time)

    @staticmethod
    def _are_severities_valid(value: List[str]) -> bool:
        return all(x in Constants.SEVERITIES for x in value)

    # https://docs.paloaltonetworks.com/cortex/cortex-xdr/cortex-xdr-api/cortex-xdr-apis/incident-management/get-alerts.html
    # TODO: add sorting capabilities
    def get_alerts(self,
                   alert_id_list: List[int] = None,
                   alert_source: List[str] = None,
                   severities: List[str] = None,
                   creation_time: int = None,
                   after_creation: bool = False,
                   ) -> Optional[dict]:
        filters = []

        if alert_id_list is not None:
            filters.append(self._alert_id_filter(alert_id_list))

        if alert_source is not None:
            filters.append(self._alert_source_filter(alert_source))

        if severities is not None and self._are_severities_valid(severities):
            filters.append(self._severities_filter(severities))

        if creation_time is not None:
            filters.append(self._creation_time_filter(creation_time, after_creation))

        request_data = new_filter_request_data(filters=filters)

        response = self._call(call_name="get_alerts_multi_events",
                              request_data=request_data)
        if response.ok:
            return response.json()
        return None
