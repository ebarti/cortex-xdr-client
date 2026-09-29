"""Explicit operations from the pinned Cortex XDR documentation snapshot."""
from typing import Any, Tuple, Union

from cortex_xdr_client.api.operation import UNSET, UnsetType
from cortex_xdr_client.api.authentication import Authentication
from cortex_xdr_client.api.base_api import BaseAPI
from cortex_xdr_client.api.version import APIVersion


class RestoreDistributionsAPI(BaseAPI):
    def __init__(self, auth: Authentication, fqdn: str, timeout: Tuple[int, int],
                 api_version: APIVersion = APIVersion.V3) -> None:
        super(RestoreDistributionsAPI, self).__init__(auth, fqdn, 'restore_distributions', timeout, api_version)

    def restore_distribution(self, *, distribution_id: str) -> Any:
        """Restore a deleted agent installation package

        POST /public_api/v1/distributions/restore
        Available in Cortex XDR 5.x.
        Returns the complete JSON response, text, bytes, or None for an empty response.
        Optional fields use UNSET for omission; None is explicit null.
        The source snapshot records this operation and its parameter schema.
        :param distribution_id: body field distribution_id.
        """
        self._require_versions((5,))
        body = self._values({'distribution_id': distribution_id})
        body = {'request_data': body}
        return self._operation(
            '/public_api/v1/distributions/restore', method='post',
            body=body,
        )
