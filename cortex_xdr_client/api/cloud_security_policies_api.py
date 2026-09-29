"""Explicit operations from the pinned Cortex XDR documentation snapshot."""
from typing import Any, Tuple, Union

from cortex_xdr_client.api.operation import UNSET, UnsetType
from cortex_xdr_client.api.authentication import Authentication
from cortex_xdr_client.api.base_api import BaseAPI
from cortex_xdr_client.api.version import APIVersion


class CloudSecurityPoliciesAPI(BaseAPI):
    def __init__(self, auth: Authentication, fqdn: str, timeout: Tuple[int, int],
                 api_version: APIVersion = APIVersion.V3) -> None:
        super(CloudSecurityPoliciesAPI, self).__init__(auth, fqdn, 'cloud_security_policies', timeout, api_version)

    def create_cloud_security_policy(self, *,
            asset_matching_type: str,
            description: str,
            name: str,
            rule_matching_type: str,
            associated_asset_group_ids: Union[Any, None, UnsetType] = UNSET,
            associated_cloud_account_ids: Union[Any, None, UnsetType] = UNSET,
            associated_rule_filter: Union[Any, None, UnsetType] = UNSET,
            associated_rule_ids: Union[Any, None, UnsetType] = UNSET,
            enabled: Union[bool, None, UnsetType] = UNSET,
            labels: Union[Any, None, UnsetType] = UNSET) -> Any:
        """Create Cloud Security Policy

        POST /public_api/v1/policy
        Available in Cortex XDR 5.x.
        Returns the complete JSON response, text, bytes, or None for an empty response.
        Optional fields use UNSET for omission; None is explicit null.
        The source snapshot records this operation and its parameter schema.
        :param asset_matching_type: body field asset_matching_type.
        :param description: body field description.
        :param name: body field name.
        :param rule_matching_type: body field rule_matching_type.
        :param associated_asset_group_ids: body field associated_asset_group_ids.
        :param associated_cloud_account_ids: body field associated_cloud_account_ids.
        :param associated_rule_filter: body field associated_rule_filter.
        :param associated_rule_ids: body field associated_rule_ids.
        :param enabled: body field enabled.
        :param labels: body field labels.
        """
        self._require_versions((5,))
        body = self._values({
            'asset_matching_type': asset_matching_type,
            'description': description,
            'name': name,
            'rule_matching_type': rule_matching_type,
            'associated_asset_group_ids': associated_asset_group_ids,
            'associated_cloud_account_ids': associated_cloud_account_ids,
            'associated_rule_filter': associated_rule_filter,
            'associated_rule_ids': associated_rule_ids,
            'enabled': enabled,
            'labels': labels,
        })
        return self._operation(
            '/public_api/v1/policy', method='post',
            body=body,
        )

    def list_cloud_security_policies(self, *,
            filter: Union[Any, None, UnsetType] = UNSET,
            search_from: Union[int, None, UnsetType] = UNSET,
            search_to: Union[int, None, UnsetType] = UNSET,
            sort: Union[list, None, UnsetType] = UNSET) -> Any:
        """List Cloud Security Policies

        POST /public_api/v1/policy/search
        Available in Cortex XDR 5.x.
        Returns the complete JSON response, text, bytes, or None for an empty response.
        Optional fields use UNSET for omission; None is explicit null.
        The source snapshot records this operation and its parameter schema.
        :param filter: body field filter.
        :param search_from: body field search_from.
        :param search_to: body field search_to.
        :param sort: body field sort.
        """
        self._require_versions((5,))
        body = self._values({
            'filter': filter,
            'search_from': search_from,
            'search_to': search_to,
            'sort': sort,
        })
        return self._operation(
            '/public_api/v1/policy/search', method='post',
            body=body,
        )

    def get_cloud_security_policy(self, *, policy_id: str) -> Any:
        """Get Cloud Security Policy

        GET /public_api/v1/policy/{policy_id}
        Available in Cortex XDR 5.x.
        Returns the complete JSON response, text, bytes, or None for an empty response.
        Optional fields use UNSET for omission; None is explicit null.
        The source snapshot records this operation and its parameter schema.
        :param policy_id: path field policy_id.
        """
        self._require_versions((5,))
        body = UNSET
        return self._operation(
            '/public_api/v1/policy/{policy_id}', method='get',
            path_params={'policy_id': policy_id},
            body=body,
        )

    def delete_cloud_security_policy(self, *, policy_id: str) -> Any:
        """Delete Cloud Security Policy

        DELETE /public_api/v1/policy/{policy_id}
        Available in Cortex XDR 5.x.
        Returns the complete JSON response, text, bytes, or None for an empty response.
        Optional fields use UNSET for omission; None is explicit null.
        The source snapshot records this operation and its parameter schema.
        :param policy_id: path field policy_id.
        """
        self._require_versions((5,))
        body = UNSET
        return self._operation(
            '/public_api/v1/policy/{policy_id}', method='delete',
            path_params={'policy_id': policy_id},
            body=body,
        )

    def update_cloud_security_policy(self, *,
            policy_id: str,
            asset_matching_type: Union[Any, None, UnsetType] = UNSET,
            associated_asset_group_ids: Union[Any, None, UnsetType] = UNSET,
            associated_cloud_account_ids: Union[Any, None, UnsetType] = UNSET,
            associated_rule_filter: Union[Any, None, UnsetType] = UNSET,
            associated_rule_ids: Union[Any, None, UnsetType] = UNSET,
            description: Union[Any, None, UnsetType] = UNSET,
            enabled: Union[Any, None, UnsetType] = UNSET,
            labels: Union[Any, None, UnsetType] = UNSET,
            name: Union[Any, None, UnsetType] = UNSET,
            rule_matching_type: Union[Any, None, UnsetType] = UNSET) -> Any:
        """Update Cloud Security Policy

        PATCH /public_api/v1/policy/{policy_id}
        Available in Cortex XDR 5.x.
        Returns the complete JSON response, text, bytes, or None for an empty response.
        Optional fields use UNSET for omission; None is explicit null.
        The source snapshot records this operation and its parameter schema.
        :param policy_id: path field policy_id.
        :param asset_matching_type: body field asset_matching_type.
        :param associated_asset_group_ids: body field associated_asset_group_ids.
        :param associated_cloud_account_ids: body field associated_cloud_account_ids.
        :param associated_rule_filter: body field associated_rule_filter.
        :param associated_rule_ids: body field associated_rule_ids.
        :param description: body field description.
        :param enabled: body field enabled.
        :param labels: body field labels.
        :param name: body field name.
        :param rule_matching_type: body field rule_matching_type.
        """
        self._require_versions((5,))
        body = self._values({
            'asset_matching_type': asset_matching_type,
            'associated_asset_group_ids': associated_asset_group_ids,
            'associated_cloud_account_ids': associated_cloud_account_ids,
            'associated_rule_filter': associated_rule_filter,
            'associated_rule_ids': associated_rule_ids,
            'description': description,
            'enabled': enabled,
            'labels': labels,
            'name': name,
            'rule_matching_type': rule_matching_type,
        })
        return self._operation(
            '/public_api/v1/policy/{policy_id}', method='patch',
            path_params={'policy_id': policy_id},
            body=body,
        )
