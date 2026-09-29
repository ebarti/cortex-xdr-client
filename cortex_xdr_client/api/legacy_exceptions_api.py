from typing import Any, List, Tuple, Union

from cortex_xdr_client.api.operation import UNSET, UnsetType

from cortex_xdr_client.api.authentication import Authentication
from cortex_xdr_client.api.base_api import BaseAPI
from cortex_xdr_client.api.version import APIVersion


class LegacyExceptionsAPI(BaseAPI):
    def __init__(self, auth: Authentication, fqdn: str, timeout: Tuple[int, int],
                 api_version: APIVersion = APIVersion.V3) -> None:
        super(LegacyExceptionsAPI, self).__init__(auth, fqdn, 'legacy_exceptions', timeout, api_version)

    def get_modules(self) -> Any:
        """Get Legacy Exceptions Modules

        POST /public_api/v1/legacy_exceptions/get_modules
        Available in Cortex XDR 3.x, 5.x.
        Returns the complete JSON response, bytes for downloads, or None for an empty response.
        Omit optional fields with UNSET; explicit None is sent as JSON null.
        """
        self._require_versions((3, 5))
        if self._api_version == APIVersion.V3:
            body = UNSET
            return self._operation(
                '/public_api/v1/legacy_exceptions/get_modules', method='post',
                body=body,
            )
        elif self._api_version == APIVersion.V5:
            body = self._values({})
            return self._operation(
                '/public_api/v1/legacy_exceptions/get_modules', method='post',
                body=body,
            )

    def fetch(self, *,
              search_from: Union[int, None, UnsetType] = UNSET,
              search_to: Union[int, None, UnsetType] = UNSET,
              sort: Union[dict, None, UnsetType] = UNSET,
              filters: Union[List[dict], None, UnsetType] = UNSET) -> Any:
        """Fetch Legacy Exception Rules

        POST /public_api/v1/legacy_exceptions/fetch
        Available in Cortex XDR 3.x, 5.x.
        Returns the complete JSON response, bytes for downloads, or None for an empty response.
        Omit optional fields with UNSET; explicit None is sent as JSON null.
        :param search_from: body field search_from.
        :param search_to: body field search_to.
        :param sort: body field sort.
        :param filters: body field filters.
        """
        self._require_versions((3, 5))
        if self._api_version == APIVersion.V3:
            body = self._values({'search_from': search_from, 'search_to': search_to, 'sort': sort, 'filters': filters})
            body = self._values({'request_data': body, **{}})
            return self._operation(
                '/public_api/v1/legacy_exceptions/fetch', method='post',
                body=body,
            )
        elif self._api_version == APIVersion.V5:
            body = self._values({'search_from': search_from, 'search_to': search_to, 'sort': sort, 'filters': filters})
            body = self._values({'request_data': body, **{}})
            return self._operation(
                '/public_api/v1/legacy_exceptions/fetch', method='post',
                body=body,
            )

    def add(self, *,
            name: Union[str, None, UnsetType] = UNSET,
            platform: Union[str, None, UnsetType] = UNSET,
            module: Union[int, None, UnsetType] = UNSET,
            profile_ids: Union[List[int], None, UnsetType] = UNSET,
            status: Union[str, None, UnsetType] = UNSET,
            scope: Union[str, None, UnsetType] = UNSET,
            description: Union[str, None, UnsetType] = UNSET,
            conditions: Union[dict, None, UnsetType] = UNSET) -> Any:
        """Add Legacy Exception Rule

        POST /public_api/v1/legacy_exceptions/add
        Available in Cortex XDR 3.x, 5.x.
        Returns the complete JSON response, bytes for downloads, or None for an empty response.
        Omit optional fields with UNSET; explicit None is sent as JSON null.
        :param name: body field name.
        :param platform: body field platform.
        :param module: body field module.
        :param profile_ids: body field profile_ids.
        :param status: body field status.
        :param scope: body field scope.
        :param description: body field description.
        :param conditions: body field conditions.
        """
        self._require_versions((3, 5))
        if self._api_version == APIVersion.V3:
            body = self._values({'name': name, 'platform': platform, 'module': module, 'profile_ids': profile_ids, 'status': status, 'scope': scope, 'description': description, 'conditions': conditions})
            body = self._values({'request_data': body, **{}})
            return self._operation(
                '/public_api/v1/legacy_exceptions/add', method='post',
                body=body,
            )
        elif self._api_version == APIVersion.V5:
            body = self._values({'name': name, 'platform': platform, 'module': module, 'profile_ids': profile_ids, 'status': status, 'scope': scope, 'description': description, 'conditions': conditions})
            body = self._values({'request_data': body, **{}})
            return self._operation(
                '/public_api/v1/legacy_exceptions/add', method='post',
                body=body,
            )

    def edit(self, *,
             exception_id: Union[str, None, UnsetType] = UNSET,
             update_data: Union[dict, None, UnsetType] = UNSET) -> Any:
        """Edit Legacy Exception Rule

        POST /public_api/v1/legacy_exceptions/edit
        Available in Cortex XDR 3.x, 5.x.
        Returns the complete JSON response, bytes for downloads, or None for an empty response.
        Omit optional fields with UNSET; explicit None is sent as JSON null.
        :param exception_id: body field exception_id.
        :param update_data: body field update_data.
        """
        self._require_versions((3, 5))
        if self._api_version == APIVersion.V3:
            body = self._values({'exception_id': exception_id, 'update_data': update_data})
            body = self._values({'request_data': body, **{}})
            return self._operation(
                '/public_api/v1/legacy_exceptions/edit', method='post',
                body=body,
            )
        elif self._api_version == APIVersion.V5:
            body = self._values({'exception_id': exception_id, 'update_data': update_data})
            body = self._values({'request_data': body, **{}})
            return self._operation(
                '/public_api/v1/legacy_exceptions/edit', method='post',
                body=body,
            )

    def delete(self, *,
               exception_ids: Union[List[str], None, UnsetType] = UNSET) -> Any:
        """Delete Legacy Exception Rules

        POST /public_api/v1/legacy_exceptions/delete
        Available in Cortex XDR 3.x, 5.x.
        Returns the complete JSON response, bytes for downloads, or None for an empty response.
        Omit optional fields with UNSET; explicit None is sent as JSON null.
        :param exception_ids: body field exception_ids.
        """
        self._require_versions((3, 5))
        if self._api_version == APIVersion.V3:
            body = self._values({'exception_ids': exception_ids})
            body = self._values({'request_data': body, **{}})
            return self._operation(
                '/public_api/v1/legacy_exceptions/delete', method='post',
                body=body,
            )
        elif self._api_version == APIVersion.V5:
            body = self._values({'exception_ids': exception_ids})
            body = self._values({'request_data': body, **{}})
            return self._operation(
                '/public_api/v1/legacy_exceptions/delete', method='post',
                body=body,
            )
