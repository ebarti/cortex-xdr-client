"""Explicit operations from the pinned Cortex XDR documentation snapshot."""
from typing import Any, Tuple, Union

from cortex_xdr_client.api.operation import UNSET, UnsetType
from cortex_xdr_client.api.authentication import Authentication
from cortex_xdr_client.api.base_api import BaseAPI
from cortex_xdr_client.api.version import APIVersion


class UnifiedRulesAPI(BaseAPI):
    def __init__(self, auth: Authentication, fqdn: str, timeout: Tuple[int, int],
                 api_version: APIVersion = APIVersion.V3) -> None:
        super(UnifiedRulesAPI, self).__init__(auth, fqdn, 'unified_rules', timeout, api_version)

    def list_unified_rules(self, *,
            severities: Union[list, None, UnsetType] = UNSET,
            categories: Union[list, None, UnsetType] = UNSET,
            cloud_providers: Union[list, None, UnsetType] = UNSET,
            offset: Union[float, None, UnsetType] = UNSET,
            limit: Union[float, None, UnsetType] = UNSET) -> Any:
        """List unified rules

        GET /public_api/appsec/v1/unified-rules
        Available in Cortex XDR 5.x.
        Returns the complete JSON response, text, bytes, or None for an empty response.
        Optional fields use UNSET for omission; None is explicit null.
        The source snapshot records this operation and its parameter schema.
        :param severities: query field severities.
        :param categories: query field categories.
        :param cloud_providers: query field cloudProviders.
        :param offset: query field offset.
        :param limit: query field limit.
        """
        self._require_versions((5,))
        body = UNSET
        return self._operation(
            '/public_api/appsec/v1/unified-rules', method='get',
            query=[('severities', severities, True), ('categories', categories, True), ('cloudProviders', cloud_providers, True), ('offset', offset, True), ('limit', limit, True)],
            body=body,
        )

    def create_unified_rule(self, *, appsec: dict, cspm: dict) -> Any:
        """Create a unified rule

        POST /public_api/appsec/v1/unified-rules
        Available in Cortex XDR 5.x.
        Returns the complete JSON response, text, bytes, or None for an empty response.
        Optional fields use UNSET for omission; None is explicit null.
        The source snapshot records this operation and its parameter schema.
        :param appsec: body field appsec.
        :param cspm: body field cspm.
        """
        self._require_versions((5,))
        body = self._values({'appsec': appsec, 'cspm': cspm})
        return self._operation(
            '/public_api/appsec/v1/unified-rules', method='post',
            body=body,
        )

    def get_unified_rule(self, *, rule_id: str) -> Any:
        """Get a unified rule

        GET /public_api/appsec/v1/unified-rules/{ruleId}
        Available in Cortex XDR 5.x.
        Returns the complete JSON response, text, bytes, or None for an empty response.
        Optional fields use UNSET for omission; None is explicit null.
        The source snapshot records this operation and its parameter schema.
        :param rule_id: path field ruleId.
        """
        self._require_versions((5,))
        body = UNSET
        return self._operation(
            '/public_api/appsec/v1/unified-rules/{ruleId}', method='get',
            path_params={'ruleId': rule_id},
            body=body,
        )

    def update_unified_rule(self, *,
            rule_id: str,
            appsec: Union[dict, None, UnsetType] = UNSET,
            cspm: Union[dict, None, UnsetType] = UNSET) -> Any:
        """Update a unified rule

        PUT /public_api/appsec/v1/unified-rules/{ruleId}
        Available in Cortex XDR 5.x.
        Returns the complete JSON response, text, bytes, or None for an empty response.
        Optional fields use UNSET for omission; None is explicit null.
        The source snapshot records this operation and its parameter schema.
        :param rule_id: path field ruleId.
        :param appsec: body field appsec.
        :param cspm: body field cspm.
        """
        self._require_versions((5,))
        body = self._values({'appsec': appsec, 'cspm': cspm})
        return self._operation(
            '/public_api/appsec/v1/unified-rules/{ruleId}', method='put',
            path_params={'ruleId': rule_id},
            body=body,
        )

    def delete_unified_rule(self, *, rule_id: str) -> Any:
        """Delete a unified rule

        DELETE /public_api/appsec/v1/unified-rules/{ruleId}
        Available in Cortex XDR 5.x.
        Returns the complete JSON response, text, bytes, or None for an empty response.
        Optional fields use UNSET for omission; None is explicit null.
        The source snapshot records this operation and its parameter schema.
        :param rule_id: path field ruleId.
        """
        self._require_versions((5,))
        body = UNSET
        return self._operation(
            '/public_api/appsec/v1/unified-rules/{ruleId}', method='delete',
            path_params={'ruleId': rule_id},
            body=body,
        )
