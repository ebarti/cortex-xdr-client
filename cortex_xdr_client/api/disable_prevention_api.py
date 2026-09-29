from typing import Any, List, Tuple, Union

from cortex_xdr_client.api.operation import UNSET, UnsetType

from cortex_xdr_client.api.authentication import Authentication
from cortex_xdr_client.api.base_api import BaseAPI
from cortex_xdr_client.api.version import APIVersion


class DisablePreventionAPI(BaseAPI):
    def __init__(self, auth: Authentication, fqdn: str, timeout: Tuple[int, int],
                 api_version: APIVersion = APIVersion.V3) -> None:
        super(DisablePreventionAPI, self).__init__(auth, fqdn, 'disable_prevention', timeout, api_version)

    def fetch(self, *,
              search_from: Union[int, None, UnsetType] = UNSET,
              search_to: Union[int, None, UnsetType] = UNSET,
              sort: Union[dict, None, UnsetType] = UNSET,
              filters: Union[List[dict], None, UnsetType] = UNSET) -> Any:
        """Get Disable Prevention Rules

        POST /public_api/v1/disable_prevention/fetch
        Available in Cortex XDR 3.x.
        Returns the complete JSON response, bytes for downloads, or None for an empty response.
        Omit optional fields with UNSET; explicit None is sent as JSON null.
        :param search_from: body field search_from.
        :param search_to: body field search_to.
        :param sort: body field sort.
        :param filters: body field filters.
        """
        self._require_versions((3,))
        body = self._values({'search_from': search_from, 'search_to': search_to, 'sort': sort, 'filters': filters})
        body = self._values({'request_data': body, **{}})
        return self._operation(
            '/public_api/v1/disable_prevention/fetch', method='post',
            body=body,
        )

    def get_modules(self, *,
                    platform: Union[str, None, UnsetType] = UNSET) -> Any:
        """Get Disable Prevention Modules

        POST /public_api/v1/disable_prevention/get_modules
        Available in Cortex XDR 3.x.
        Returns the complete JSON response, bytes for downloads, or None for an empty response.
        Omit optional fields with UNSET; explicit None is sent as JSON null.
        :param platform: body field platform.
        """
        self._require_versions((3,))
        body = self._values({'platform': platform})
        body = self._values({'request_data': body, **{}})
        return self._operation(
            '/public_api/v1/disable_prevention/get_modules', method='post',
            body=body,
        )

    def add(self, *,
            rule_name: Union[str, None, UnsetType] = UNSET,
            description: Union[str, None, UnsetType] = UNSET,
            platform: Union[str, None, UnsetType] = UNSET,
            module_ids: Union[List[int], None, UnsetType] = UNSET,
            conditions: Union[dict, None, UnsetType] = UNSET,
            profile_ids: Union[List[int], None, UnsetType] = UNSET,
            status: Union[str, None, UnsetType] = UNSET,
            scope: Union[str, None, UnsetType] = UNSET) -> Any:
        """Add Disable Prevention Rule

        POST /public_api/v1/disable_prevention/add
        Available in Cortex XDR 3.x.
        Returns the complete JSON response, bytes for downloads, or None for an empty response.
        Omit optional fields with UNSET; explicit None is sent as JSON null.
        :param rule_name: body field rule_name.
        :param description: body field description.
        :param platform: body field platform.
        :param module_ids: body field module_ids.
        :param conditions: body field conditions.
        :param profile_ids: body field profile_ids.
        :param status: body field status.
        :param scope: body field scope.
        """
        self._require_versions((3,))
        body = self._values({'rule_name': rule_name, 'description': description, 'platform': platform, 'module_ids': module_ids, 'conditions': conditions, 'profile_ids': profile_ids, 'status': status, 'scope': scope})
        body = self._values({'request_data': body, **{}})
        return self._operation(
            '/public_api/v1/disable_prevention/add', method='post',
            body=body,
        )

    def edit(self, *,
             rule_name: Union[str, None, UnsetType] = UNSET,
             description: Union[str, None, UnsetType] = UNSET,
             platform: Union[str, None, UnsetType] = UNSET,
             module_ids: Union[List[int], None, UnsetType] = UNSET,
             conditions: Union[dict, None, UnsetType] = UNSET,
             profile_ids: Union[List[int], None, UnsetType] = UNSET,
             status: Union[str, None, UnsetType] = UNSET,
             scope: Union[str, None, UnsetType] = UNSET,
             rule_id: Union[str, None, UnsetType] = UNSET) -> Any:
        """Edit Disable Prevention Rule

        POST /public_api/v1/disable_prevention/edit
        Available in Cortex XDR 3.x.
        Returns the complete JSON response, bytes for downloads, or None for an empty response.
        Omit optional fields with UNSET; explicit None is sent as JSON null.
        :param rule_name: body field rule_name.
        :param description: body field description.
        :param platform: body field platform.
        :param module_ids: body field module_ids.
        :param conditions: body field conditions.
        :param profile_ids: body field profile_ids.
        :param status: body field status.
        :param scope: body field scope.
        :param rule_id: body field rule_id.
        """
        self._require_versions((3,))
        body = self._values({'rule_name': rule_name, 'description': description, 'platform': platform, 'module_ids': module_ids, 'conditions': conditions, 'profile_ids': profile_ids, 'status': status, 'scope': scope, 'rule_id': rule_id})
        body = self._values({'request_data': body, **{}})
        return self._operation(
            '/public_api/v1/disable_prevention/edit', method='post',
            body=body,
        )

    def delete(self, *,
               rule_ids: Union[List[str], None, UnsetType] = UNSET) -> Any:
        """Delete Disable Prevention Rules

        POST /public_api/v1/disable_prevention/delete
        Available in Cortex XDR 3.x.
        Returns the complete JSON response, bytes for downloads, or None for an empty response.
        Omit optional fields with UNSET; explicit None is sent as JSON null.
        :param rule_ids: body field rule_ids.
        """
        self._require_versions((3,))
        body = self._values({'rule_ids': rule_ids})
        body = self._values({'request_data': body, **{}})
        return self._operation(
            '/public_api/v1/disable_prevention/delete', method='post',
            body=body,
        )
