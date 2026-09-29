from typing import Any, List, Tuple, Union

from cortex_xdr_client.api.operation import UNSET, UnsetType

from cortex_xdr_client.api.authentication import Authentication
from cortex_xdr_client.api.base_api import BaseAPI
from cortex_xdr_client.api.version import APIVersion


class TagsAPI(BaseAPI):
    def __init__(self, auth: Authentication, fqdn: str, timeout: Tuple[int, int],
                 api_version: APIVersion = APIVersion.V3) -> None:
        super(TagsAPI, self).__init__(auth, fqdn, 'tags', timeout, api_version)

    def agents_assign(self, *,
                      accept_encoding: Union[str, None, UnsetType] = UNSET,
                      filters: Union[List[dict], None, UnsetType] = UNSET,
                      tag: Union[str, None, UnsetType] = UNSET) -> Any:
        """Assign Tags

        POST /public_api/v1/tags/agents/assign
        Available in Cortex XDR 3.x, 5.x.
        Returns the complete JSON response, bytes for downloads, or None for an empty response.
        Omit optional fields with UNSET; explicit None is sent as JSON null.
        :param accept_encoding: header field Accept-Encoding.
        :param filters: body field filters.
        :param tag: body field tag.
        """
        self._require_versions((3, 5))
        if self._api_version == APIVersion.V3:
            body = self._values({'filters': filters, 'tag': tag})
            body = self._values({'request_data': body, **{}})
            return self._operation(
                '/public_api/v1/tags/agents/assign', method='post',
                headers={'Accept-Encoding': accept_encoding},
                body=body,
            )
        elif self._api_version == APIVersion.V5:
            self._reject_fields(accept_encoding=accept_encoding)
            body = self._values({'filters': filters, 'tag': tag})
            body = self._values({'request_data': body, **{}})
            return self._operation(
                '/public_api/v1/tags/agents/assign', method='post',
                body=body,
            )

    def agents_create(self, *,
                      accept_encoding: Union[str, None, UnsetType] = UNSET,
                      tag: Union[str, None, UnsetType] = UNSET) -> Any:
        """Create Tag

        POST /public_api/v1/tags/agents/create
        Available in Cortex XDR 3.x, 5.x.
        Returns the complete JSON response, bytes for downloads, or None for an empty response.
        Omit optional fields with UNSET; explicit None is sent as JSON null.
        :param accept_encoding: header field Accept-Encoding.
        :param tag: body field tag.
        """
        self._require_versions((3, 5))
        if self._api_version == APIVersion.V3:
            body = self._values({'tag': tag})
            body = self._values({'request_data': body, **{}})
            return self._operation(
                '/public_api/v1/tags/agents/create', method='post',
                headers={'Accept-Encoding': accept_encoding},
                body=body,
            )
        elif self._api_version == APIVersion.V5:
            self._reject_fields(accept_encoding=accept_encoding)
            body = self._values({'tag': tag})
            body = self._values({'request_data': body, **{}})
            return self._operation(
                '/public_api/v1/tags/agents/create', method='post',
                body=body,
            )

    def agents_remove(self, *,
                      accept_encoding: Union[str, None, UnsetType] = UNSET,
                      filters: Union[List[dict], None, UnsetType] = UNSET,
                      tag: Union[str, None, UnsetType] = UNSET) -> Any:
        """Remove Tags

        POST /public_api/v1/tags/agents/remove
        Available in Cortex XDR 3.x, 5.x.
        Returns the complete JSON response, bytes for downloads, or None for an empty response.
        Omit optional fields with UNSET; explicit None is sent as JSON null.
        :param accept_encoding: header field Accept-Encoding.
        :param filters: body field filters.
        :param tag: body field tag.
        """
        self._require_versions((3, 5))
        if self._api_version == APIVersion.V3:
            body = self._values({'filters': filters, 'tag': tag})
            body = self._values({'request_data': body, **{}})
            return self._operation(
                '/public_api/v1/tags/agents/remove', method='post',
                headers={'Accept-Encoding': accept_encoding},
                body=body,
            )
        elif self._api_version == APIVersion.V5:
            self._reject_fields(accept_encoding=accept_encoding)
            body = self._values({'filters': filters, 'tag': tag})
            body = self._values({'request_data': body, **{}})
            return self._operation(
                '/public_api/v1/tags/agents/remove', method='post',
                body=body,
            )

    def agents_delete_permanently(self, *,
                                  tags: Union[List[str], None, UnsetType] = UNSET,
                                  reason: Union[str, None, UnsetType] = UNSET) -> Any:
        """Delete Tags Permanently

        POST /public_api/v1/tags/agents/delete_permanently
        Available in Cortex XDR 3.x, 5.x.
        Returns the complete JSON response, bytes for downloads, or None for an empty response.
        Omit optional fields with UNSET; explicit None is sent as JSON null.
        :param tags: body field tags.
        :param reason: body field reason.
        """
        self._require_versions((3, 5))
        if self._api_version == APIVersion.V3:
            body = self._values({'tags': tags, 'reason': reason})
            body = self._values({'request_data': body, **{}})
            return self._operation(
                '/public_api/v1/tags/agents/delete_permanently', method='post',
                body=body,
            )
        elif self._api_version == APIVersion.V5:
            body = self._values({'tags': tags, 'reason': reason})
            body = self._values({'request_data': body, **{}})
            return self._operation(
                '/public_api/v1/tags/agents/delete_permanently', method='post',
                body=body,
            )
