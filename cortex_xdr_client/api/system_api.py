from typing import Tuple

from cortex_xdr_client.api.authentication import Authentication
from cortex_xdr_client.api.base_api import BaseAPI
from cortex_xdr_client.api.models.system import PaloAltoSystemStatus


class SystemAPI(BaseAPI):
    def __init__(self, auth: Authentication, fqdn: str, timeout: Tuple[int, int]) -> None:
        super(SystemAPI, self).__init__(auth, fqdn, "healthcheck", timeout)

    def is_system_available(self) -> bool:
        response = self._call('', 'get')
        result = response.json()
        return result['status'] == PaloAltoSystemStatus.AVAILABLE
