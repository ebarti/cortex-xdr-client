"""Explicit operations from the pinned Cortex XDR documentation snapshot."""
from typing import Any, Tuple, Union

from cortex_xdr_client.api.operation import UNSET, UnsetType
from cortex_xdr_client.api.authentication import Authentication
from cortex_xdr_client.api.base_api import BaseAPI
from cortex_xdr_client.api.version import APIVersion


class ClcsAPI(BaseAPI):
    def __init__(self, auth: Authentication, fqdn: str, timeout: Tuple[int, int],
                 api_version: APIVersion = APIVersion.V3) -> None:
        super(ClcsAPI, self).__init__(auth, fqdn, 'clcs', timeout, api_version)

    def get_clcs_connected_devices(self) -> Any:
        """List connected NGFW devices

        GET /public_api/v1/clcs/get_connected_devices
        Available in Cortex XDR 5.x.
        Returns the complete JSON response, text, bytes, or None for an empty response.
        Optional fields use UNSET for omission; None is explicit null.
        The source snapshot records this operation and its parameter schema.
        """
        self._require_versions((5,))
        body = UNSET
        return self._operation(
            '/public_api/v1/clcs/get_connected_devices', method='get',
            body=body,
        )

    def post_clcs_disconnect_devices(self, *,
            csp_account_id: int,
            device_ids: list,
            region: str) -> Any:
        """Disconnect NGFW devices from CLCS

        POST /public_api/v1/clcs/disconnect_devices
        Available in Cortex XDR 5.x.
        Returns the complete JSON response, text, bytes, or None for an empty response.
        Optional fields use UNSET for omission; None is explicit null.
        The source snapshot records this operation and its parameter schema.
        :param csp_account_id: body field csp_account_id.
        :param device_ids: body field device_ids.
        :param region: body field region.
        """
        self._require_versions((5,))
        body = self._values({
            'csp_account_id': csp_account_id,
            'device_ids': device_ids,
            'region': region,
        })
        body = {'request_data': body}
        return self._operation(
            '/public_api/v1/clcs/disconnect_devices', method='post',
            body=body,
        )
