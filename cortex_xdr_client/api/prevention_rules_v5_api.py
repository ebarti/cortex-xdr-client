"""Explicit operations from the pinned Cortex XDR documentation snapshot."""
from typing import Any, Tuple, Union

from cortex_xdr_client.api.operation import UNSET, UnsetType
from cortex_xdr_client.api.authentication import Authentication
from cortex_xdr_client.api.base_api import BaseAPI
from cortex_xdr_client.api.version import APIVersion


class PreventionRulesV5API(BaseAPI):
    def __init__(self, auth: Authentication, fqdn: str, timeout: Tuple[int, int],
                 api_version: APIVersion = APIVersion.V3) -> None:
        super(PreventionRulesV5API, self).__init__(auth, fqdn, 'prevention_rules_v5', timeout, api_version)

    def fetch_disable_injection_prevention_rules(self, *,
            filters: Union[list, None, UnsetType] = UNSET,
            search_from: Union[int, None, UnsetType] = UNSET,
            search_to: Union[int, None, UnsetType] = UNSET,
            sort: Union[dict, None, UnsetType] = UNSET) -> Any:
        """Get Disable Injection and Prevention rules

        POST /public_api/v1/disable_injection_prevention_rules/fetch
        Available in Cortex XDR 5.x.
        Returns the complete JSON response, text, bytes, or None for an empty response.
        Optional fields use UNSET for omission; None is explicit null.
        The source snapshot records this operation and its parameter schema.
        :param filters: body field filters.
        :param search_from: body field search_from.
        :param search_to: body field search_to.
        :param sort: body field sort.
        """
        self._require_versions((5,))
        body = self._values({
            'filters': filters,
            'search_from': search_from,
            'search_to': search_to,
            'sort': sort,
        })
        body = {'request_data': body}
        return self._operation(
            '/public_api/v1/disable_injection_prevention_rules/fetch', method='post',
            body=body,
        )

    def add_disable_injection_prevention_rule(self, *,
            description: str,
            hours_to_expiration: int,
            path: str,
            platform: str,
            process_name: str,
            rule_name: str,
            scope: str,
            profile_ids: Union[list, None, UnsetType] = UNSET) -> Any:
        """Add Disable Injection and Prevention rule

        POST /public_api/v1/disable_injection_prevention_rules/add
        Available in Cortex XDR 5.x.
        Returns the complete JSON response, text, bytes, or None for an empty response.
        Optional fields use UNSET for omission; None is explicit null.
        The source snapshot records this operation and its parameter schema.
        :param description: body field description.
        :param hours_to_expiration: body field hours_to_expiration.
        :param path: body field path.
        :param platform: body field platform.
        :param process_name: body field process_name.
        :param rule_name: body field rule_name.
        :param scope: body field scope.
        :param profile_ids: body field profile_ids.
        """
        self._require_versions((5,))
        body = self._values({
            'description': description,
            'hours_to_expiration': hours_to_expiration,
            'path': path,
            'platform': platform,
            'process_name': process_name,
            'rule_name': rule_name,
            'scope': scope,
            'profile_ids': profile_ids,
        })
        body = {'request_data': body}
        return self._operation(
            '/public_api/v1/disable_injection_prevention_rules/add', method='post',
            body=body,
        )

    def disable_disable_injection_prevention_rules(self, *, rule_ids: list) -> Any:
        """Disable Disable Injection and Prevention Rules

        POST /public_api/v1/disable_injection_prevention_rules/disable
        Available in Cortex XDR 5.x.
        Returns the complete JSON response, text, bytes, or None for an empty response.
        Optional fields use UNSET for omission; None is explicit null.
        The source snapshot records this operation and its parameter schema.
        :param rule_ids: body field rule_ids.
        """
        self._require_versions((5,))
        body = self._values({'rule_ids': rule_ids})
        body = {'request_data': body}
        return self._operation(
            '/public_api/v1/disable_injection_prevention_rules/disable', method='post',
            body=body,
        )

    def fetch_disable_prevention_rules(self, *,
            filters: Union[list, None, UnsetType] = UNSET,
            search_from: Union[int, None, UnsetType] = UNSET,
            search_to: Union[int, None, UnsetType] = UNSET,
            sort: Union[dict, None, UnsetType] = UNSET) -> Any:
        """Get Disable Prevention Rules

        POST /public_api/v1/disable_prevention/fetch
        Available in Cortex XDR 5.x.
        Returns the complete JSON response, text, bytes, or None for an empty response.
        Optional fields use UNSET for omission; None is explicit null.
        The source snapshot records this operation and its parameter schema.
        :param filters: body field filters.
        :param search_from: body field search_from.
        :param search_to: body field search_to.
        :param sort: body field sort.
        """
        self._require_versions((5,))
        body = self._values({
            'filters': filters,
            'search_from': search_from,
            'search_to': search_to,
            'sort': sort,
        })
        body = {'request_data': body}
        return self._operation(
            '/public_api/v1/disable_prevention/fetch', method='post',
            body=body,
        )

    def get_disable_prevention_modules(self, *, platform: str) -> Any:
        """Get Disable Prevention Modules

        POST /public_api/v1/disable_prevention/get_modules
        Available in Cortex XDR 5.x.
        Returns the complete JSON response, text, bytes, or None for an empty response.
        Optional fields use UNSET for omission; None is explicit null.
        The source snapshot records this operation and its parameter schema.
        :param platform: body field platform.
        """
        self._require_versions((5,))
        body = self._values({'platform': platform})
        body = {'request_data': body}
        return self._operation(
            '/public_api/v1/disable_prevention/get_modules', method='post',
            body=body,
        )

    def add_disable_prevention_rule(self, *,
            conditions: dict,
            description: str,
            module_ids: list,
            platform: str,
            rule_name: str,
            scope: str,
            status: str,
            profile_ids: Union[list, None, UnsetType] = UNSET) -> Any:
        """Add Disable Prevention Rule

        POST /public_api/v1/disable_prevention/add
        Available in Cortex XDR 5.x.
        Returns the complete JSON response, text, bytes, or None for an empty response.
        Optional fields use UNSET for omission; None is explicit null.
        The source snapshot records this operation and its parameter schema.
        :param conditions: body field conditions.
        :param description: body field description.
        :param module_ids: body field module_ids.
        :param platform: body field platform.
        :param rule_name: body field rule_name.
        :param scope: body field scope.
        :param status: body field status.
        :param profile_ids: body field profile_ids.
        """
        self._require_versions((5,))
        body = self._values({
            'conditions': conditions,
            'description': description,
            'module_ids': module_ids,
            'platform': platform,
            'rule_name': rule_name,
            'scope': scope,
            'status': status,
            'profile_ids': profile_ids,
        })
        body = {'request_data': body}
        return self._operation(
            '/public_api/v1/disable_prevention/add', method='post',
            body=body,
        )

    def edit_disable_prevention_rule(self, *,
            conditions: dict,
            description: str,
            module_ids: list,
            platform: str,
            rule_name: str,
            scope: str,
            status: str,
            rule_id: str,
            profile_ids: Union[list, None, UnsetType] = UNSET) -> Any:
        """Edit Disable Prevention Rule

        POST /public_api/v1/disable_prevention/edit
        Available in Cortex XDR 5.x.
        Returns the complete JSON response, text, bytes, or None for an empty response.
        Optional fields use UNSET for omission; None is explicit null.
        The source snapshot records this operation and its parameter schema.
        :param conditions: body field conditions.
        :param description: body field description.
        :param module_ids: body field module_ids.
        :param platform: body field platform.
        :param rule_name: body field rule_name.
        :param scope: body field scope.
        :param status: body field status.
        :param rule_id: body field rule_id.
        :param profile_ids: body field profile_ids.
        """
        self._require_versions((5,))
        body = self._values({
            'conditions': conditions,
            'description': description,
            'module_ids': module_ids,
            'platform': platform,
            'rule_name': rule_name,
            'scope': scope,
            'status': status,
            'rule_id': rule_id,
            'profile_ids': profile_ids,
        })
        body = {'request_data': body}
        return self._operation(
            '/public_api/v1/disable_prevention/edit', method='post',
            body=body,
        )

    def delete_disable_prevention_rules(self, *, rule_ids: list) -> Any:
        """Delete Disable Prevention Rules

        POST /public_api/v1/disable_prevention/delete
        Available in Cortex XDR 5.x.
        Returns the complete JSON response, text, bytes, or None for an empty response.
        Optional fields use UNSET for omission; None is explicit null.
        The source snapshot records this operation and its parameter schema.
        :param rule_ids: body field rule_ids.
        """
        self._require_versions((5,))
        body = self._values({'rule_ids': rule_ids})
        body = {'request_data': body}
        return self._operation(
            '/public_api/v1/disable_prevention/delete', method='post',
            body=body,
        )
