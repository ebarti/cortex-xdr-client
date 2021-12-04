from typing import Optional, List

from cortex_xdr_client.api.base_api import BaseAPI
from cortex_xdr_client.api.models.filters import (
    new_request_data,
    request_eq_neq_filter,
    request_gte_lte_filter,
    request_in_contains_filter,
    request_filter
)
from cortex_xdr_client.api.models.incidents import (
    IncidentStatus,
    GetIncidentsResponse,
    GetExtraIncidentDataResponse,
)


class IncidentsAPI(BaseAPI):
    def __init__(self, api_key_id: int, api_key: str, fqdn: str, timeout: tuple[int, int]) -> None:
        super(IncidentsAPI, self).__init__(api_key_id, api_key, fqdn, "incidents", timeout)

    @staticmethod
    def _get_incident_extra_data_filter(incident_id: str, alerts_limit: int) -> dict:
        return {
            "incident_id": incident_id,
            "alerts_limit": alerts_limit
        }

    # https://docs.paloaltonetworks.com/cortex/cortex-xdr/cortex-xdr-api/cortex-xdr-apis/incident-management/get-incidents.html
    def get_incidents(self,
                      modification_time: int = None,
                      after_modification: bool = False,
                      creation_time: int = None,
                      after_creation: bool = False,
                      incident_id_list: List[str] = None,
                      description: str = None,
                      description_contains: bool = False,
                      alert_sources: List[str] = None,
                      status: IncidentStatus = None,
                      status_equal: bool = True,
                      search_from: int = None,
                      search_to: int = None,
                      ) -> Optional[GetIncidentsResponse]:
        filters = []
        if modification_time is not None:
            filters.append(request_gte_lte_filter("modification_time", modification_time, after_modification))

        if creation_time is not None:
            filters.append(request_gte_lte_filter("creation_time", creation_time, after_creation))

        if incident_id_list is not None:
            filters.append(request_filter("incident_id_list", "in", incident_id_list))

        if description is not None:
            filters.append(request_in_contains_filter("description", description, description_contains))

        if alert_sources is not None:
            filters.append(request_filter("alert_sources", "in", alert_sources))

        if status is not None:
            filters.append(request_eq_neq_filter("status", status, status_equal))

        request_data = new_request_data(filters=filters, search_from=search_from, search_to=search_to)
        response = self._call(call_name="get_incidents", json_value=request_data)
        if response.ok:
            return GetIncidentsResponse.parse_obj(response.json())
        return None

    # https://docs.paloaltonetworks.com/cortex/cortex-xdr/cortex-xdr-api/cortex-xdr-apis/incident-management/get-extra-incident-data.html
    def get_incident_extra_data(self,
                                incident_id: str,
                                alerts_limit: int = 1000,
                                ) -> Optional[GetExtraIncidentDataResponse]:
        request_data = new_request_data(other=self._get_incident_extra_data_filter(incident_id, alerts_limit))
        response = self._call(call_name="get_incident_extra_data",
                              json_value=request_data)
        if response.ok:
            return GetExtraIncidentDataResponse.parse_obj(response.json())
        return None
