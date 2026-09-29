from typing import Any, List, Tuple, Union

from cortex_xdr_client.api.operation import UNSET, UnsetType

from cortex_xdr_client.api.authentication import Authentication
from cortex_xdr_client.api.base_api import BaseAPI
from cortex_xdr_client.api.version import APIVersion


class QuarantineAPI(BaseAPI):
    def __init__(self, auth: Authentication, fqdn: str, timeout: Tuple[int, int],
                 api_version: APIVersion = APIVersion.V3) -> None:
        super(QuarantineAPI, self).__init__(auth, fqdn, 'quarantine', timeout, api_version)

    def status(self, *,
               accept_encoding: Union[str, None, UnsetType] = UNSET,
               files: Union[List[dict], None, UnsetType] = UNSET) -> Any:
        """Get Quarantine Status

        POST /public_api/v1/quarantine/status
        Available in Cortex XDR 3.x, 5.x.
        Returns the complete JSON response, bytes for downloads, or None for an empty response.
        Omit optional fields with UNSET; explicit None is sent as JSON null.
        :param accept_encoding: header field Accept-Encoding.
        :param files: body field files.
        """
        self._require_versions((3, 5))
        if self._api_version == APIVersion.V3:
            body = self._values({'files': files})
            body = self._values({'request_data': body, **{}})
            return self._operation(
                '/public_api/v1/quarantine/status', method='post',
                headers={'Accept-Encoding': accept_encoding},
                body=body,
            )
        elif self._api_version == APIVersion.V5:
            self._reject_fields(accept_encoding=accept_encoding)
            body = self._values({'files': files})
            body = self._values({'request_data': body, **{}})
            return self._operation(
                '/public_api/v1/quarantine/status', method='post',
                body=body,
            )
