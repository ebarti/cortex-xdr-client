from typing import Any, List, Tuple, Union

from cortex_xdr_client.api.operation import UNSET, UnsetType

from cortex_xdr_client.api.authentication import Authentication
from cortex_xdr_client.api.base_api import BaseAPI
from cortex_xdr_client.api.version import APIVersion


class PlaybooksAPI(BaseAPI):
    def __init__(self, auth: Authentication, fqdn: str, timeout: Tuple[int, int],
                 api_version: APIVersion = APIVersion.V3) -> None:
        super(PlaybooksAPI, self).__init__(auth, fqdn, 'playbooks', timeout, api_version)

    def get(self, *,
            filter: Union[dict, None, UnsetType] = UNSET) -> Any:
        """Get a playbook

        POST /public_api/v1/playbooks/get
        Available in Cortex XDR 5.x.
        Returns the complete JSON response, bytes for downloads, or None for an empty response.
        Omit optional fields with UNSET; explicit None is sent as JSON null.
        :param filter: body field filter.
        """
        self._require_versions((5,))
        body = self._values({'filter': filter})
        body = self._values({'request_data': body, **{}})
        return self._operation(
            '/public_api/v1/playbooks/get', method='post',
            body=body,
        )

    def insert(self, *,
               file: Union[Any, None, UnsetType] = UNSET) -> Any:
        """Insert or update playbooks

        POST /public_api/v1/playbooks/insert
        Available in Cortex XDR 5.x.
        Returns the complete JSON response, bytes for downloads, or None for an empty response.
        Omit optional fields with UNSET; explicit None is sent as JSON null.
        :param file: file field file.
        """
        self._require_versions((5,))
        body = self._values({})
        return self._operation(
            '/public_api/v1/playbooks/insert', method='post',
            data=body, files={'file': file},
        )

    def delete(self, *,
               filter: Union[dict, None, UnsetType] = UNSET) -> Any:
        """Delete a playbook

        POST /public_api/v1/playbooks/delete
        Available in Cortex XDR 5.x.
        Returns the complete JSON response, bytes for downloads, or None for an empty response.
        Omit optional fields with UNSET; explicit None is sent as JSON null.
        :param filter: body field filter.
        """
        self._require_versions((5,))
        body = self._values({'filter': filter})
        body = self._values({'request_data': body, **{}})
        return self._operation(
            '/public_api/v1/playbooks/delete', method='post',
            body=body,
        )
