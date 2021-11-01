from cortex.api.base_api import BaseAPI


class IncidentsAPI(BaseAPI):
    def __init__(self, api_key_id: str, api_key: str, fqdn: str, timeout: tuple[int, int] = (10, 60)):
        super().__init__(api_key_id, api_key, fqdn, timeout)