from typing import Optional

from cortex.api.base_api import BaseAPI


class GetIncidentExtraDataItem:
    incident_id: str
    alerts_limit: int

    def __init__(self, incident_id: str, alerts_limit: int) -> None:
        self.incident_id = incident_id
        self.alerts_limit = alerts_limit


class GetIncidentExtraDataRequestData:
    request_data: GetIncidentExtraDataItem

    def __init__(self, request_data: GetIncidentExtraDataItem = None) -> None:
        if request_data is None:
            self.request_data = {}
        else:
            self.request_data = request_data


class IncidentsAPI(BaseAPI):
    def __init__(self, api_key_id: str, api_key: str, fqdn: str, timeout: tuple[int, int]):
        super().__init__(api_key_id, api_key, fqdn, "incidents", timeout)

    # https://docs.paloaltonetworks.com/cortex/cortex-xdr/cortex-xdr-api/cortex-xdr-apis/incident-management/get-incidents.html
    def get_incidents(self) -> Optional[dict]:
        response = self._call(call_name="get_incidents")
        if response.ok:
            return response.json()
        return None

    # https://docs.paloaltonetworks.com/cortex/cortex-xdr/cortex-xdr-api/cortex-xdr-apis/incident-management/get-extra-incident-data.html
    def get_incident_extra_data(self, incident_id: str, alerts_limit: int) -> Optional[dict]:

        request_data = GetIncidentExtraDataRequestData(GetIncidentExtraDataItem(incident_id, alerts_limit))
        response = self._call(api_name="incidents",
                              call_name="get_incident_extra_data",
                              request_data=request_data)
        if response.ok:
            return response.json()
        return None
