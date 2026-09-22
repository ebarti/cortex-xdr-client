from typing import Tuple

import requests

from cortex_xdr_client.api.actions_api import ActionsAPI
from cortex_xdr_client.api.alerts_api import AlertsAPI
from cortex_xdr_client.api.authentication import Authentication
from cortex_xdr_client.api.base_api import BaseAPI
from cortex_xdr_client.api.cases_api import CasesAPI
from cortex_xdr_client.api.download_api import DownloadAPI
from cortex_xdr_client.api.endpoints_api import EndpointsAPI
from cortex_xdr_client.api.incidents_api import IncidentsAPI
from cortex_xdr_client.api.ioc_api import IocAPI
from cortex_xdr_client.api.issues_api import IssuesAPI
from cortex_xdr_client.api.scripts_api import ScriptsAPI
from cortex_xdr_client.api.version import APIVersion
from cortex_xdr_client.api.xql_api import XQLAPI


class CortexXDRClient(object):
    incidents_api: IncidentsAPI
    alerts_api: AlertsAPI
    endpoints_api: EndpointsAPI
    scripts_api: ScriptsAPI
    xql_api: XQLAPI
    actions_api: ActionsAPI
    download_api: DownloadAPI
    ioc_api: IocAPI
    cases_api: CasesAPI
    issues_api: IssuesAPI

    def __init__(self, auth: Authentication, fqdn: str, default_timeout: Tuple[int, int] = (10, 60),
                 api_version: APIVersion = APIVersion.V3) -> None:
        """
        Constructor of the CortexXDRClient class. This class is used to interact with the Cortex XDR API.
        :param auth: The Authentication object containing type
        :param fqdn: The fully qualified domain name of the Cortex XDR server.
        :param api_version: Cortex XDR product version, 3 or 5. Defaults to 3 for existing callers.
        :param default_timeout: The default timeout for API calls.
        """
        self.api_version = APIVersion(api_version)
        self._api = BaseAPI(auth, fqdn, "", default_timeout, self.api_version)
        self.cases_api = CasesAPI(auth=auth,
                                  fqdn=fqdn,
                                  timeout=default_timeout,
                                  api_version=self.api_version)
        self.issues_api = IssuesAPI(auth=auth,
                                    fqdn=fqdn,
                                    timeout=default_timeout,
                                    api_version=self.api_version)
        self.incidents_api = IncidentsAPI(auth=auth,
                                          fqdn=fqdn,
                                          timeout=default_timeout,
                                          api_version=self.api_version)
        self.alerts_api = AlertsAPI(auth=auth,
                                    fqdn=fqdn,
                                    timeout=default_timeout,
                                    api_version=self.api_version)
        self.endpoints_api = EndpointsAPI(auth=auth,
                                          fqdn=fqdn,
                                          timeout=default_timeout,
                                          api_version=self.api_version)
        self.scripts_api = ScriptsAPI(auth=auth,
                                      fqdn=fqdn,
                                      timeout=default_timeout,
                                      api_version=self.api_version)
        self.xql_api = XQLAPI(auth=auth,
                              fqdn=fqdn,
                              timeout=default_timeout,
                              api_version=self.api_version)
        self.actions_api = ActionsAPI(auth=auth,
                                      fqdn=fqdn,
                                      timeout=default_timeout,
                                      api_version=self.api_version)
        self.download_api = DownloadAPI(auth=auth,
                                      fqdn=fqdn,
                                      timeout=default_timeout,
                                      api_version=self.api_version)
        self.ioc_api = IocAPI(auth=auth,
                              fqdn=fqdn,
                              timeout=default_timeout,
                              api_version=self.api_version)

    def request(self, path: str, method: str = "post", params: dict = None,
                json_value: object = None, header_params: dict = None,
                data=None, files=None) -> requests.Response:
        """
        Call any documented operation for the selected tenant, including APIs
        without a typed wrapper. Supply the complete path and request body from
        the corresponding product documentation. Returns a requests.Response.
        """
        return self._api.request(path, method, params, json_value, header_params, data, files)
