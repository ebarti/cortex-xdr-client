from typing import Any, List, Tuple, Union

from cortex_xdr_client.api.operation import UNSET, UnsetType

from cortex_xdr_client.api.authentication import Authentication
from cortex_xdr_client.api.base_api import BaseAPI
from cortex_xdr_client.api.version import APIVersion


class HashExceptionsAPI(BaseAPI):
    def __init__(self, auth: Authentication, fqdn: str, timeout: Tuple[int, int],
                 api_version: APIVersion = APIVersion.V3) -> None:
        super(HashExceptionsAPI, self).__init__(auth, fqdn, 'hash_exceptions', timeout, api_version)

    def allowlist(self, *,
                  accept_encoding: Union[str, None, UnsetType] = UNSET,
                  hash_list: Union[List[str], None, UnsetType] = UNSET,
                  comment: Union[str, None, UnsetType] = UNSET,
                  incident_id: Union[int, None, UnsetType] = UNSET) -> Any:
        """Allow List Files

        POST /public_api/v1/hash_exceptions/allowlist
        Available in Cortex XDR 3.x, 5.x.
        Returns the complete JSON response, bytes for downloads, or None for an empty response.
        Omit optional fields with UNSET; explicit None is sent as JSON null.
        :param accept_encoding: header field Accept-Encoding.
        :param hash_list: body field hash_list.
        :param comment: body field comment.
        :param incident_id: body field incident_id.
        """
        self._require_versions((3, 5))
        if self._api_version == APIVersion.V3:
            body = self._values({'hash_list': hash_list, 'comment': comment, 'incident_id': incident_id})
            body = self._values({'request_data': body, **{}})
            return self._operation(
                '/public_api/v1/hash_exceptions/allowlist', method='post',
                headers={'Accept-Encoding': accept_encoding},
                body=body,
            )
        elif self._api_version == APIVersion.V5:
            self._reject_fields(accept_encoding=accept_encoding)
            body = self._values({'hash_list': hash_list, 'comment': comment, 'incident_id': incident_id})
            body = self._values({'request_data': body, **{}})
            return self._operation(
                '/public_api/v1/hash_exceptions/allowlist', method='post',
                body=body,
            )

    def blocklist(self, *,
                  accept_encoding: Union[str, None, UnsetType] = UNSET,
                  hash_list: Union[List[str], None, UnsetType] = UNSET,
                  comment: Union[str, None, UnsetType] = UNSET,
                  incident_id: Union[int, None, UnsetType] = UNSET) -> Any:
        """Block List Files

        POST /public_api/v1/hash_exceptions/blocklist
        Available in Cortex XDR 3.x, 5.x.
        Returns the complete JSON response, bytes for downloads, or None for an empty response.
        Omit optional fields with UNSET; explicit None is sent as JSON null.
        :param accept_encoding: header field Accept-Encoding.
        :param hash_list: body field hash_list.
        :param comment: body field comment.
        :param incident_id: body field incident_id.
        """
        self._require_versions((3, 5))
        if self._api_version == APIVersion.V3:
            body = self._values({'hash_list': hash_list, 'comment': comment, 'incident_id': incident_id})
            body = self._values({'request_data': body, **{}})
            return self._operation(
                '/public_api/v1/hash_exceptions/blocklist', method='post',
                headers={'Accept-Encoding': accept_encoding},
                body=body,
            )
        elif self._api_version == APIVersion.V5:
            self._reject_fields(accept_encoding=accept_encoding)
            body = self._values({'hash_list': hash_list, 'comment': comment, 'incident_id': incident_id})
            body = self._values({'request_data': body, **{}})
            return self._operation(
                '/public_api/v1/hash_exceptions/blocklist', method='post',
                body=body,
            )
