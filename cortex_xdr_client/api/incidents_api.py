from typing import List, Optional, Tuple

from cortex_xdr_client.api.authentication import Authentication
from cortex_xdr_client.api.base_api import BaseAPI
from cortex_xdr_client.api.models.filters import (new_request_data,
                                                  request_eq_neq_filter,
                                                  request_filter,
                                                  request_gte_lte_filter,
                                                  request_in_contains_filter,
                                                  )
from cortex_xdr_client.api.models.incidents import (GetExtraIncidentDataResponse, GetIncidentsResponse, IncidentStatus)


class IncidentsAPI(BaseAPI):
    def __init__(self, auth: Authentication, fqdn: str, timeout: Tuple[int, int]) -> None:
        super(IncidentsAPI, self).__init__(auth, fqdn, "incidents", timeout)

    @staticmethod
    def _get_incident_extra_data_filter(incident_id: str, alerts_limit: int) -> dict:
        return {
            "incident_id":  incident_id,
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
        """
        Get a list of incidents filtered by a list of incident IDs, modification time, or creation time.

        :param modification_time: Time the incident has been modified.
        :param after_modification: If the modification date will be the upper or lower bound limit.
        :param creation_time: Incident's creation time.
        :param after_creation: If the creation date will be the upper or lower bound limit.
        :param incident_id_list: List of incident IDs.
        :param description: Incident description.
        :param description_contains: If the description will contain the search string.
        :param alert_sources: Source which detected the alert.
        :param status: Represents the status of the incident.
        :param status_equal: If the status will be equal to the given status.
        :param search_from: Integer representing the starting offset within the query result set from which you want incidents returned.
        :param search_to: Integer representing the end offset within the result set after which you do not want incidents returned.
        :return: Returns a GetIncidentsResponse object if successful.
        """
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
        return GetIncidentsResponse.parse_obj(response.json())

    # https://docs.paloaltonetworks.com/cortex/cortex-xdr/cortex-xdr-api/cortex-xdr-apis/incident-management/get-extra-incident-data.html
    def get_incident_extra_data(self,
                                incident_id: str,
                                alerts_limit: int = 1000,
                                ) -> Optional[GetExtraIncidentDataResponse]:
        """
        Get extra data fields of a specific incident including alerts and key artifacts.

        :param incident_id: The ID of the incident for which you want to retrieve extra data.
        :param alerts_limit: Maximum number of related alerts in the incident that you want to retrieve (default 1000).
        :return: Returns a GetExtraIncidentDataResponse object if successful.
        """
        request_data = new_request_data(other=self._get_incident_extra_data_filter(incident_id, alerts_limit))
        response = self._call(call_name="get_incident_extra_data",
                              json_value=request_data)
        return GetExtraIncidentDataResponse.parse_obj(response.json())
