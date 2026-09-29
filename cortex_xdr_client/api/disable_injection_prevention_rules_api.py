from typing import Any, List, Tuple, Union

from cortex_xdr_client.api.operation import UNSET, UnsetType

from cortex_xdr_client.api.authentication import Authentication
from cortex_xdr_client.api.base_api import BaseAPI
from cortex_xdr_client.api.version import APIVersion


class DisableInjectionPreventionRulesAPI(BaseAPI):
    def __init__(self, auth: Authentication, fqdn: str, timeout: Tuple[int, int],
                 api_version: APIVersion = APIVersion.V3) -> None:
        super(DisableInjectionPreventionRulesAPI, self).__init__(auth, fqdn, 'disable_injection_prevention_rules', timeout, api_version)

    def fetch(self, *,
              search_from: Union[int, None, UnsetType] = UNSET,
              search_to: Union[int, None, UnsetType] = UNSET,
              sort: Union[dict, None, UnsetType] = UNSET,
              filters: Union[List[dict], None, UnsetType] = UNSET) -> Any:
        """Get Disable Injection and Prevention rules

        POST /public_api/v1/disable_injection_prevention_rules/fetch
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
            '/public_api/v1/disable_injection_prevention_rules/fetch', method='post',
            body=body,
        )

    def add(self, *,
            rule_name: Union[str, None, UnsetType] = UNSET,
            description: Union[str, None, UnsetType] = UNSET,
            platform: Union[str, None, UnsetType] = UNSET,
            process_name: Union[str, None, UnsetType] = UNSET,
            path: Union[str, None, UnsetType] = UNSET,
            hours_to_expiration: Union[int, None, UnsetType] = UNSET,
            profile_ids: Union[List[int], None, UnsetType] = UNSET,
            scope: Union[str, None, UnsetType] = UNSET) -> Any:
        """Add Disable Injection and Prevention rule

        POST /public_api/v1/disable_injection_prevention_rules/add
        Available in Cortex XDR 3.x.
        Returns the complete JSON response, bytes for downloads, or None for an empty response.
        Omit optional fields with UNSET; explicit None is sent as JSON null.
        :param rule_name: body field rule_name.
        :param description: body field description.
        :param platform: body field platform.
        :param process_name: body field process_name.
        :param path: body field path.
        :param hours_to_expiration: body field hours_to_expiration.
        :param profile_ids: body field profile_ids.
        :param scope: body field scope.
        """
        self._require_versions((3,))
        body = self._values({'rule_name': rule_name, 'description': description, 'platform': platform, 'process_name': process_name, 'path': path, 'hours_to_expiration': hours_to_expiration, 'profile_ids': profile_ids, 'scope': scope})
        body = self._values({'request_data': body, **{}})
        return self._operation(
            '/public_api/v1/disable_injection_prevention_rules/add', method='post',
            body=body,
        )

    def disable(self, *,
                rule_ids: Union[List[str], None, UnsetType] = UNSET) -> Any:
        """Disable Disable Injection and Prevention Rules

        POST /public_api/v1/disable_injection_prevention_rules/disable
        Available in Cortex XDR 3.x.
        Returns the complete JSON response, bytes for downloads, or None for an empty response.
        Omit optional fields with UNSET; explicit None is sent as JSON null.
        :param rule_ids: body field rule_ids.
        """
        self._require_versions((3,))
        body = self._values({'rule_ids': rule_ids})
        body = self._values({'request_data': body, **{}})
        return self._operation(
            '/public_api/v1/disable_injection_prevention_rules/disable', method='post',
            body=body,
        )
