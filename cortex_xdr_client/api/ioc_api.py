from typing import List, Optional, Tuple

from cortex_xdr_client.api.authentication import Authentication
from cortex_xdr_client.api.base_api import BaseAPI
from cortex_xdr_client.api.models.ioc import IoC, IoCResponse


class IocAPI(BaseAPI):
    def __init__(self, auth: Authentication, fqdn: str, timeout: Tuple[int, int]) -> None:
        super(IocAPI, self).__init__(auth, fqdn, "indicators", timeout)

    def insert_json(self, indicators: List[IoC], validate: Optional[bool] = True) -> IoCResponse:
        """
        Upload IOCs as JSON objects that you retrieved from external threat intelligence sources.
        :param indicators: List of IoC objects
        :param validate: Whether to return an array of errors in the case of an unsuccessful update indicator API request.
        :return: Returns an IoCResponse object if successful.
        """
        request_data = {
            "request_data": [indicator.dict(by_alias=True, exclude_none=True) for indicator in indicators],
            "validate":     validate
        }
        response = self._call(call_name="insert_jsons", json_value=request_data)
        return IoCResponse.parse_obj(response.json())
