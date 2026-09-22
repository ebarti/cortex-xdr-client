from typing import List, Optional, Tuple

from cortex_xdr_client.api.authentication import Authentication
from cortex_xdr_client.api.base_api import BaseAPI
from cortex_xdr_client.api.version import APIVersion
from cortex_xdr_client.api.models.ioc import IoC, IoCResponse


class IocAPI(BaseAPI):
    def __init__(self, auth: Authentication, fqdn: str, timeout: Tuple[int, int],
                 api_version: APIVersion = APIVersion.V3) -> None:
        super(IocAPI, self).__init__(auth, fqdn, "indicators", timeout, api_version)

    def insert_json(self, indicators: List[IoC], validate: Optional[bool] = True) -> IoCResponse:
        """
        Upload IOCs as JSON objects that you retrieved from external threat intelligence sources.
        :param indicators: List of IoC objects
        :param validate: Whether to return an array of errors in the case of an unsuccessful update indicator API request.
        :return: Returns an IoCResponse object if successful.
        """
        values = [indicator.model_dump(by_alias=True, exclude_none=True) for indicator in indicators]
        for value in values:
            if value['severity'] == 'INFORMATIONAL':
                value['severity'] = 'INFO'
            elif value['severity'] == 'UNKNOWN':
                if self._api_version == APIVersion.V5:
                    raise ValueError("XDR 5 indicators require INFO, LOW, MEDIUM, HIGH or CRITICAL severity")
                value['severity'] = 'unknown'
        request_data = {
            "request_data": values,
            "validate":     validate
        }
        response = self._call(call_name="insert_jsons", json_value=request_data)
        return IoCResponse.model_validate(response.json())
