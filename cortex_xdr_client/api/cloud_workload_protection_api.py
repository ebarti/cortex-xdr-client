"""Explicit operations from the pinned Cortex XDR documentation snapshot."""
from typing import Any, Tuple, Union

from cortex_xdr_client.api.operation import UNSET, UnsetType
from cortex_xdr_client.api.authentication import Authentication
from cortex_xdr_client.api.base_api import BaseAPI
from cortex_xdr_client.api.version import APIVersion


class CloudWorkloadProtectionAPI(BaseAPI):
    def __init__(self, auth: Authentication, fqdn: str, timeout: Tuple[int, int],
                 api_version: APIVersion = APIVersion.V3) -> None:
        super(CloudWorkloadProtectionAPI, self).__init__(auth, fqdn, 'cloud_workload_protection', timeout, api_version)

    def get_v2_cwp_policies(self, *,
            types: Union[list, None, UnsetType] = UNSET,
            disable_verbose: Union[bool, None, UnsetType] = UNSET) -> Any:
        """Get CWP Policies (v2)

        GET /public_api/v2/cwp/policies
        Available in Cortex XDR 5.x.
        Returns the complete JSON response, text, bytes, or None for an empty response.
        Optional fields use UNSET for omission; None is explicit null.
        The source snapshot records this operation and its parameter schema.
        :param types: query field types.
        :param disable_verbose: query field disableVerbose.
        """
        self._require_versions((5,))
        body = UNSET
        return self._operation(
            '/public_api/v2/cwp/policies', method='get',
            query=[('types', types, True), ('disableVerbose', disable_verbose, True)],
            body=body,
        )

    def addv2_cwp_policies(self, *,
            action: str,
            asset_groups: list,
            asset_groups_ids: list,
            asset_scope: str,
            condition: str,
            created_by: str,
            description: str,
            disabled: bool,
            evaluation_modes: list,
            evaluation_stage: str,
            exception: str,
            grace_period: str,
            name: str,
            policy_rules: list,
            remediation_guidance: str,
            severity: str,
            type: str,
            using_system_asset_groups: bool,
            missing_information_action: Union[str, None, UnsetType] = UNSET,
            unified_policy_id: Union[str, None, UnsetType] = UNSET) -> Any:
        """Add CWP Policies (v2)

        POST /public_api/v2/cwp/policies
        Available in Cortex XDR 5.x.
        Returns the complete JSON response, text, bytes, or None for an empty response.
        Optional fields use UNSET for omission; None is explicit null.
        The source snapshot records this operation and its parameter schema.
        :param action: body field action.
        :param asset_groups: body field assetGroups.
        :param asset_groups_ids: body field assetGroupsIDs.
        :param asset_scope: body field assetScope.
        :param condition: body field condition.
        :param created_by: body field createdBy.
        :param description: body field description.
        :param disabled: body field disabled.
        :param evaluation_modes: body field evaluationModes.
        :param evaluation_stage: body field evaluationStage.
        :param exception: body field exception.
        :param grace_period: body field gracePeriod.
        :param name: body field name.
        :param policy_rules: body field policyRules.
        :param remediation_guidance: body field remediationGuidance.
        :param severity: body field severity.
        :param type: body field type.
        :param using_system_asset_groups: body field usingSystemAssetGroups.
        :param missing_information_action: body field missingInformationAction.
        :param unified_policy_id: body field unifiedPolicyId.
        """
        self._require_versions((5,))
        body = self._values({
            'action': action,
            'assetGroups': asset_groups,
            'assetGroupsIDs': asset_groups_ids,
            'assetScope': asset_scope,
            'condition': condition,
            'createdBy': created_by,
            'description': description,
            'disabled': disabled,
            'evaluationModes': evaluation_modes,
            'evaluationStage': evaluation_stage,
            'exception': exception,
            'gracePeriod': grace_period,
            'name': name,
            'policyRules': policy_rules,
            'remediationGuidance': remediation_guidance,
            'severity': severity,
            'type': type,
            'usingSystemAssetGroups': using_system_asset_groups,
            'missingInformationAction': missing_information_action,
            'unifiedPolicyId': unified_policy_id,
        })
        return self._operation(
            '/public_api/v2/cwp/policies', method='post',
            body=body,
        )

    def get_v2_cwp_policiesby_id(self, *,
            id: str,
            disable_verbose: Union[bool, None, UnsetType] = UNSET) -> Any:
        """Get a CWP Policy by ID (v2)

        GET /public_api/v2/cwp/policies/{id}
        Available in Cortex XDR 5.x.
        Returns the complete JSON response, text, bytes, or None for an empty response.
        Optional fields use UNSET for omission; None is explicit null.
        The source snapshot records this operation and its parameter schema.
        :param id: path field id.
        :param disable_verbose: query field disableVerbose.
        """
        self._require_versions((5,))
        body = UNSET
        return self._operation(
            '/public_api/v2/cwp/policies/{id}', method='get',
            path_params={'id': id},
            query=[('disableVerbose', disable_verbose, True)],
            body=body,
        )

    def updatev2_cwp_policies(self, *,
            id: str,
            action: str,
            asset_groups: list,
            asset_groups_ids: list,
            asset_scope: str,
            condition: str,
            description: str,
            disabled: bool,
            evaluation_modes: list,
            evaluation_stage: str,
            exception: str,
            grace_period: str,
            id_field: str,
            name: str,
            policy_rules: list,
            remediation_guidance: str,
            severity: str,
            type: str,
            using_system_asset_groups: bool,
            created_by: Union[str, None, UnsetType] = UNSET,
            missing_information_action: Union[str, None, UnsetType] = UNSET,
            unified_policy_id: Union[str, None, UnsetType] = UNSET) -> Any:
        """Update a CWP Policy by ID (v2)

        PUT /public_api/v2/cwp/policies/{id}
        Available in Cortex XDR 5.x.
        Returns the complete JSON response, text, bytes, or None for an empty response.
        Optional fields use UNSET for omission; None is explicit null.
        The source snapshot records this operation and its parameter schema.
        :param id: path field id.
        :param action: body field action.
        :param asset_groups: body field assetGroups.
        :param asset_groups_ids: body field assetGroupsIDs.
        :param asset_scope: body field assetScope.
        :param condition: body field condition.
        :param description: body field description.
        :param disabled: body field disabled.
        :param evaluation_modes: body field evaluationModes.
        :param evaluation_stage: body field evaluationStage.
        :param exception: body field exception.
        :param grace_period: body field gracePeriod.
        :param id_field: body field id.
        :param name: body field name.
        :param policy_rules: body field policyRules.
        :param remediation_guidance: body field remediationGuidance.
        :param severity: body field severity.
        :param type: body field type.
        :param using_system_asset_groups: body field usingSystemAssetGroups.
        :param created_by: body field createdBy.
        :param missing_information_action: body field missingInformationAction.
        :param unified_policy_id: body field unifiedPolicyId.
        """
        self._require_versions((5,))
        body = self._values({
            'action': action,
            'assetGroups': asset_groups,
            'assetGroupsIDs': asset_groups_ids,
            'assetScope': asset_scope,
            'condition': condition,
            'description': description,
            'disabled': disabled,
            'evaluationModes': evaluation_modes,
            'evaluationStage': evaluation_stage,
            'exception': exception,
            'gracePeriod': grace_period,
            'id': id_field,
            'name': name,
            'policyRules': policy_rules,
            'remediationGuidance': remediation_guidance,
            'severity': severity,
            'type': type,
            'usingSystemAssetGroups': using_system_asset_groups,
            'createdBy': created_by,
            'missingInformationAction': missing_information_action,
            'unifiedPolicyId': unified_policy_id,
        })
        return self._operation(
            '/public_api/v2/cwp/policies/{id}', method='put',
            path_params={'id': id},
            body=body,
        )

    def get_cwp_policies(self, *, types: Union[list, None, UnsetType] = UNSET) -> Any:
        """Get CWP Policies (v1)

        GET /public_api/v1/cwp/policies
        Available in Cortex XDR 5.x.
        Returns the complete JSON response, text, bytes, or None for an empty response.
        Optional fields use UNSET for omission; None is explicit null.
        The source snapshot records this operation and its parameter schema.
        :param types: query field types.
        """
        self._require_versions((5,))
        body = UNSET
        return self._operation(
            '/public_api/v1/cwp/policies', method='get',
            query=[('types', types, True)],
            body=body,
        )

    def post_cwp_policies(self, *,
            action: str,
            asset_groups_ids: list,
            condition: str,
            description: str,
            evaluation_stage: str,
            missing_information_action: str,
            name: str,
            rules_ids: list,
            severity: str,
            type: str,
            asset_groups: Union[list, None, UnsetType] = UNSET,
            asset_scope: Union[str, None, UnsetType] = UNSET,
            created_at: Union[str, None, UnsetType] = UNSET,
            created_by: Union[str, None, UnsetType] = UNSET,
            disabled: Union[bool, None, UnsetType] = UNSET,
            evaluation_modes: Union[list, None, UnsetType] = UNSET,
            exception: Union[str, None, UnsetType] = UNSET,
            id: Union[str, None, UnsetType] = UNSET,
            modified_at: Union[str, None, UnsetType] = UNSET,
            remediation_guidance: Union[str, None, UnsetType] = UNSET,
            revision: Union[int, None, UnsetType] = UNSET) -> Any:
        """Add CWP Policies (v1)

        POST /public_api/v1/cwp/policies
        Available in Cortex XDR 5.x.
        Returns the complete JSON response, text, bytes, or None for an empty response.
        Optional fields use UNSET for omission; None is explicit null.
        The source snapshot records this operation and its parameter schema.
        :param action: body field action.
        :param asset_groups_ids: body field assetGroupsIDs.
        :param condition: body field condition.
        :param description: body field description.
        :param evaluation_stage: body field evaluationStage.
        :param missing_information_action: body field missingInformationAction.
        :param name: body field name.
        :param rules_ids: body field rulesIds.
        :param severity: body field severity.
        :param type: body field type.
        :param asset_groups: body field assetGroups.
        :param asset_scope: body field assetScope.
        :param created_at: body field createdAt.
        :param created_by: body field createdBy.
        :param disabled: body field disabled.
        :param evaluation_modes: body field evaluationModes.
        :param exception: body field exception.
        :param id: body field id.
        :param modified_at: body field modifiedAt.
        :param remediation_guidance: body field remediationGuidance.
        :param revision: body field revision.
        """
        self._require_versions((5,))
        body = self._values({
            'action': action,
            'assetGroupsIDs': asset_groups_ids,
            'condition': condition,
            'description': description,
            'evaluationStage': evaluation_stage,
            'missingInformationAction': missing_information_action,
            'name': name,
            'rulesIds': rules_ids,
            'severity': severity,
            'type': type,
            'assetGroups': asset_groups,
            'assetScope': asset_scope,
            'createdAt': created_at,
            'createdBy': created_by,
            'disabled': disabled,
            'evaluationModes': evaluation_modes,
            'exception': exception,
            'id': id,
            'modifiedAt': modified_at,
            'remediationGuidance': remediation_guidance,
            'revision': revision,
        })
        return self._operation(
            '/public_api/v1/cwp/policies', method='post',
            body=body,
        )

    def get_cwp_policies_id(self, *, id: str) -> Any:
        """Get a CWP Policy by ID (v1)

        GET /public_api/v1/cwp/policies/{id}
        Available in Cortex XDR 5.x.
        Returns the complete JSON response, text, bytes, or None for an empty response.
        Optional fields use UNSET for omission; None is explicit null.
        The source snapshot records this operation and its parameter schema.
        :param id: path field id.
        """
        self._require_versions((5,))
        body = UNSET
        return self._operation(
            '/public_api/v1/cwp/policies/{id}', method='get',
            path_params={'id': id},
            body=body,
        )

    def put_cwp_policies_id(self, *,
            id: str,
            action: str,
            asset_groups_ids: list,
            condition: str,
            description: str,
            evaluation_stage: str,
            missing_information_action: str,
            name: str,
            rules_ids: list,
            severity: str,
            type: str,
            asset_groups: Union[list, None, UnsetType] = UNSET,
            asset_scope: Union[str, None, UnsetType] = UNSET,
            created_at: Union[str, None, UnsetType] = UNSET,
            created_by: Union[str, None, UnsetType] = UNSET,
            disabled: Union[bool, None, UnsetType] = UNSET,
            evaluation_modes: Union[list, None, UnsetType] = UNSET,
            exception: Union[str, None, UnsetType] = UNSET,
            id_field: Union[str, None, UnsetType] = UNSET,
            modified_at: Union[str, None, UnsetType] = UNSET,
            remediation_guidance: Union[str, None, UnsetType] = UNSET,
            revision: Union[int, None, UnsetType] = UNSET) -> Any:
        """Update a CWP Policy by ID (v1)

        PUT /public_api/v1/cwp/policies/{id}
        Available in Cortex XDR 5.x.
        Returns the complete JSON response, text, bytes, or None for an empty response.
        Optional fields use UNSET for omission; None is explicit null.
        The source snapshot records this operation and its parameter schema.
        :param id: path field id.
        :param action: body field action.
        :param asset_groups_ids: body field assetGroupsIDs.
        :param condition: body field condition.
        :param description: body field description.
        :param evaluation_stage: body field evaluationStage.
        :param missing_information_action: body field missingInformationAction.
        :param name: body field name.
        :param rules_ids: body field rulesIds.
        :param severity: body field severity.
        :param type: body field type.
        :param asset_groups: body field assetGroups.
        :param asset_scope: body field assetScope.
        :param created_at: body field createdAt.
        :param created_by: body field createdBy.
        :param disabled: body field disabled.
        :param evaluation_modes: body field evaluationModes.
        :param exception: body field exception.
        :param id_field: body field id.
        :param modified_at: body field modifiedAt.
        :param remediation_guidance: body field remediationGuidance.
        :param revision: body field revision.
        """
        self._require_versions((5,))
        body = self._values({
            'action': action,
            'assetGroupsIDs': asset_groups_ids,
            'condition': condition,
            'description': description,
            'evaluationStage': evaluation_stage,
            'missingInformationAction': missing_information_action,
            'name': name,
            'rulesIds': rules_ids,
            'severity': severity,
            'type': type,
            'assetGroups': asset_groups,
            'assetScope': asset_scope,
            'createdAt': created_at,
            'createdBy': created_by,
            'disabled': disabled,
            'evaluationModes': evaluation_modes,
            'exception': exception,
            'id': id_field,
            'modifiedAt': modified_at,
            'remediationGuidance': remediation_guidance,
            'revision': revision,
        })
        return self._operation(
            '/public_api/v1/cwp/policies/{id}', method='put',
            path_params={'id': id},
            body=body,
        )

    def delete_cwp_policies_id(self, *,
            id: str,
            close_issues: Union[bool, None, UnsetType] = UNSET) -> Any:
        """Delete a CWP Policy by ID (v1)

        DELETE /public_api/v1/cwp/policies/{id}
        Available in Cortex XDR 5.x.
        Returns the complete JSON response, text, bytes, or None for an empty response.
        Optional fields use UNSET for omission; None is explicit null.
        The source snapshot records this operation and its parameter schema.
        :param id: path field id.
        :param close_issues: query field closeIssues.
        """
        self._require_versions((5,))
        body = UNSET
        return self._operation(
            '/public_api/v1/cwp/policies/{id}', method='delete',
            path_params={'id': id},
            query=[('closeIssues', close_issues, True)],
            body=body,
        )

    def create_unmanaged_registry_connector_public_api(self, *,
            auth_token: str,
            initial_scan_configuration: dict,
            insecure_pull: bool,
            name: str,
            password: str,
            region: str,
            scanning_mode: str,
            url: str,
            username: str,
            vendor: str,
            allow_static_ips: Union[bool, None, UnsetType] = UNSET,
            asset_scope_filters: Union[Any, None, UnsetType] = UNSET,
            broker_id: Union[str, None, UnsetType] = UNSET,
            broker_type: Union[dict, None, UnsetType] = UNSET,
            ca_certificate: Union[str, None, UnsetType] = UNSET,
            cloud_provider: Union[str, None, UnsetType] = UNSET,
            connector_id: Union[str, None, UnsetType] = UNSET,
            enabled: Union[bool, None, UnsetType] = UNSET,
            filter_type: Union[dict, None, UnsetType] = UNSET,
            ip_identifier: Union[str, None, UnsetType] = UNSET,
            outpost_id: Union[str, None, UnsetType] = UNSET,
            registry_type: Union[str, None, UnsetType] = UNSET,
            repository: Union[str, None, UnsetType] = UNSET,
            tenant_id: Union[str, None, UnsetType] = UNSET,
            vendor_specific_configuration: Union[dict, None, UnsetType] = UNSET) -> Any:
        """Create a registry connector

        POST /public_api/v1/cwp/registry_onboarding/instances
        Available in Cortex XDR 5.x.
        Returns the complete JSON response, text, bytes, or None for an empty response.
        Optional fields use UNSET for omission; None is explicit null.
        The source snapshot records this operation and its parameter schema.
        :param auth_token: body field auth_token.
        :param initial_scan_configuration: body field initial_scan_configuration.
        :param insecure_pull: body field insecure_pull.
        :param name: body field name.
        :param password: body field password.
        :param region: body field region.
        :param scanning_mode: body field scanning_mode.
        :param url: body field url.
        :param username: body field username.
        :param vendor: body field vendor.
        :param allow_static_ips: body field allow_static_ips.
        :param asset_scope_filters: body field asset_scope_filters.
        :param broker_id: body field broker_id.
        :param broker_type: body field broker_type.
        :param ca_certificate: body field ca_certificate.
        :param cloud_provider: body field cloud_provider.
        :param connector_id: body field connector_id.
        :param enabled: body field enabled.
        :param filter_type: body field filter_type.
        :param ip_identifier: body field ip_identifier.
        :param outpost_id: body field outpost_id.
        :param registry_type: body field registry_type.
        :param repository: body field repository.
        :param tenant_id: body field tenant_id.
        :param vendor_specific_configuration: body field vendor_specific_configuration.
        """
        self._require_versions((5,))
        body = self._values({
            'auth_token': auth_token,
            'initial_scan_configuration': initial_scan_configuration,
            'insecure_pull': insecure_pull,
            'name': name,
            'password': password,
            'region': region,
            'scanning_mode': scanning_mode,
            'url': url,
            'username': username,
            'vendor': vendor,
            'allow_static_ips': allow_static_ips,
            'asset_scope_filters': asset_scope_filters,
            'broker_id': broker_id,
            'broker_type': broker_type,
            'ca_certificate': ca_certificate,
            'cloud_provider': cloud_provider,
            'connector_id': connector_id,
            'enabled': enabled,
            'filter_type': filter_type,
            'ip_identifier': ip_identifier,
            'outpost_id': outpost_id,
            'registry_type': registry_type,
            'repository': repository,
            'tenant_id': tenant_id,
            'vendor_specific_configuration': vendor_specific_configuration,
        })
        return self._operation(
            '/public_api/v1/cwp/registry_onboarding/instances', method='post',
            body=body,
        )

    def get_unmanaged_registry_connector_public_api(self, *,
            connector_id: str,
            authentication: str) -> Any:
        """Get a registry connector

        GET /public_api/v1/cwp/registry_onboarding/instances/{connectorID}
        Available in Cortex XDR 5.x.
        Returns the complete JSON response, text, bytes, or None for an empty response.
        Optional fields use UNSET for omission; None is explicit null.
        The source snapshot records this operation and its parameter schema.
        :param connector_id: path field connectorID.
        :param authentication: header field Authentication.
        """
        self._require_versions((5,))
        body = UNSET
        return self._operation(
            '/public_api/v1/cwp/registry_onboarding/instances/{connectorID}', method='get',
            path_params={'connectorID': connector_id},
            headers={'Authentication': authentication},
            body=body,
        )

    def modify_unmanaged_registry_connector_public_api(self, *,
            connector_id: str,
            authentication: str,
            auth_token: str,
            initial_scan_configuration: dict,
            insecure_pull: bool,
            name: str,
            password: str,
            region: str,
            scanning_mode: str,
            url: str,
            username: str,
            vendor: str,
            allow_static_ips: Union[bool, None, UnsetType] = UNSET,
            asset_scope_filters: Union[Any, None, UnsetType] = UNSET,
            broker_id: Union[str, None, UnsetType] = UNSET,
            broker_type: Union[dict, None, UnsetType] = UNSET,
            ca_certificate: Union[str, None, UnsetType] = UNSET,
            cloud_provider: Union[str, None, UnsetType] = UNSET,
            connector_id_field: Union[str, None, UnsetType] = UNSET,
            enabled: Union[bool, None, UnsetType] = UNSET,
            filter_type: Union[dict, None, UnsetType] = UNSET,
            ip_identifier: Union[str, None, UnsetType] = UNSET,
            outpost_id: Union[str, None, UnsetType] = UNSET,
            registry_type: Union[str, None, UnsetType] = UNSET,
            repository: Union[str, None, UnsetType] = UNSET,
            tenant_id: Union[str, None, UnsetType] = UNSET,
            vendor_specific_configuration: Union[dict, None, UnsetType] = UNSET) -> Any:
        """Update a registry connector

        PUT /public_api/v1/cwp/registry_onboarding/instances/{connectorID}
        Available in Cortex XDR 5.x.
        Returns the complete JSON response, text, bytes, or None for an empty response.
        Optional fields use UNSET for omission; None is explicit null.
        The source snapshot records this operation and its parameter schema.
        :param connector_id: path field connectorID.
        :param authentication: header field Authentication.
        :param auth_token: body field auth_token.
        :param initial_scan_configuration: body field initial_scan_configuration.
        :param insecure_pull: body field insecure_pull.
        :param name: body field name.
        :param password: body field password.
        :param region: body field region.
        :param scanning_mode: body field scanning_mode.
        :param url: body field url.
        :param username: body field username.
        :param vendor: body field vendor.
        :param allow_static_ips: body field allow_static_ips.
        :param asset_scope_filters: body field asset_scope_filters.
        :param broker_id: body field broker_id.
        :param broker_type: body field broker_type.
        :param ca_certificate: body field ca_certificate.
        :param cloud_provider: body field cloud_provider.
        :param connector_id_field: body field connector_id.
        :param enabled: body field enabled.
        :param filter_type: body field filter_type.
        :param ip_identifier: body field ip_identifier.
        :param outpost_id: body field outpost_id.
        :param registry_type: body field registry_type.
        :param repository: body field repository.
        :param tenant_id: body field tenant_id.
        :param vendor_specific_configuration: body field vendor_specific_configuration.
        """
        self._require_versions((5,))
        body = self._values({
            'auth_token': auth_token,
            'initial_scan_configuration': initial_scan_configuration,
            'insecure_pull': insecure_pull,
            'name': name,
            'password': password,
            'region': region,
            'scanning_mode': scanning_mode,
            'url': url,
            'username': username,
            'vendor': vendor,
            'allow_static_ips': allow_static_ips,
            'asset_scope_filters': asset_scope_filters,
            'broker_id': broker_id,
            'broker_type': broker_type,
            'ca_certificate': ca_certificate,
            'cloud_provider': cloud_provider,
            'connector_id': connector_id_field,
            'enabled': enabled,
            'filter_type': filter_type,
            'ip_identifier': ip_identifier,
            'outpost_id': outpost_id,
            'registry_type': registry_type,
            'repository': repository,
            'tenant_id': tenant_id,
            'vendor_specific_configuration': vendor_specific_configuration,
        })
        return self._operation(
            '/public_api/v1/cwp/registry_onboarding/instances/{connectorID}', method='put',
            path_params={'connectorID': connector_id},
            headers={'Authentication': authentication},
            body=body,
        )

    def delete_unmanaged_registry_connector_public_api(self, *,
            connector_id: str,
            authentication: str) -> Any:
        """Delete a registry connector

        DELETE /public_api/v1/cwp/registry_onboarding/instances/{connectorID}
        Available in Cortex XDR 5.x.
        Returns the complete JSON response, text, bytes, or None for an empty response.
        Optional fields use UNSET for omission; None is explicit null.
        The source snapshot records this operation and its parameter schema.
        :param connector_id: path field connectorID.
        :param authentication: header field Authentication.
        """
        self._require_versions((5,))
        body = UNSET
        return self._operation(
            '/public_api/v1/cwp/registry_onboarding/instances/{connectorID}', method='delete',
            path_params={'connectorID': connector_id},
            headers={'Authentication': authentication},
            body=body,
        )

    def get_the_sbom_of_the_specified_asset(self, *,
            asset_id: str,
            format: Union[str, None, UnsetType] = UNSET,
            output_format: Union[str, None, UnsetType] = UNSET,
            attributes: Union[str, None, UnsetType] = UNSET) -> Any:
        """Get the SBOM of the specified asset

        GET /public_api/v1/assets/{assetID}/sbom
        Available in Cortex XDR 5.x.
        Returns the complete JSON response, text, bytes, or None for an empty response.
        Optional fields use UNSET for omission; None is explicit null.
        The source snapshot records this operation and its parameter schema.
        :param asset_id: path field assetID.
        :param format: query field format.
        :param output_format: query field output_format.
        :param attributes: query field attributes.
        """
        self._require_versions((5,))
        body = UNSET
        return self._operation(
            '/public_api/v1/assets/{assetID}/sbom', method='get',
            path_params={'assetID': asset_id},
            query=[('format', format, True), ('output_format', output_format, True), ('attributes', attributes, True)],
            body=body,
        )
