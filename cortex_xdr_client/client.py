from cortex_xdr_client.api.alerts_api import AlertsAPI
from cortex_xdr_client.api.endpoints_api import EndpointsAPI
from cortex_xdr_client.api.incidents_api import IncidentsAPI


class CortexXDRClient(object):
    incidents_api: IncidentsAPI
    alerts_api: AlertsAPI
    endpoints_api: EndpointsAPI

    def __init__(self, api_key_id: int, api_key: str, fqdn: str, default_timeout: tuple[int, int] = (10, 60)) -> None:
        self._api_key_id = api_key_id
        self._api_key = api_key
        self._fqdn = fqdn
        self.incidents_api = IncidentsAPI(api_key_id=api_key_id,
                                          api_key=api_key,
                                          fqdn=fqdn,
                                          timeout=default_timeout)
        self.alerts_api = AlertsAPI(api_key_id=api_key_id,
                                    api_key=api_key,
                                    fqdn=fqdn,
                                    timeout=default_timeout)
        self.endpoints_api = EndpointsAPI(api_key_id=api_key_id,
                                          api_key=api_key,
                                          fqdn=fqdn,
                                          timeout=default_timeout)
