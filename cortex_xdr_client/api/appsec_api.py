from typing import Any, List, Tuple, Union

from cortex_xdr_client.api.operation import UNSET, UnsetType

from cortex_xdr_client.api.authentication import Authentication
from cortex_xdr_client.api.base_api import BaseAPI
from cortex_xdr_client.api.version import APIVersion


class AppsecAPI(BaseAPI):
    def __init__(self, auth: Authentication, fqdn: str, timeout: Tuple[int, int],
                 api_version: APIVersion = APIVersion.V3) -> None:
        super(AppsecAPI, self).__init__(auth, fqdn, 'appsec', timeout, api_version)

    def get_contributors(self) -> Any:
        """Get Billing Contributors

        GET /public_api/appsec/v1/billing/contributors
        Available in Cortex XDR 5.x.
        Returns the complete JSON response, bytes for downloads, or None for an empty response.
        Omit optional fields with UNSET; explicit None is sent as JSON null.
        """
        self._require_versions((5,))
        body = UNSET
        return self._operation(
            '/public_api/appsec/v1/billing/contributors', method='get',
            body=body,
        )

    def get_application_settings_configuration(self) -> Any:
        """Get an application configuration

        GET /public_api/appsec/v1/application/configuration
        Available in Cortex XDR 5.x.
        Returns the complete JSON response, bytes for downloads, or None for an empty response.
        Omit optional fields with UNSET; explicit None is sent as JSON null.
        """
        self._require_versions((5,))
        body = UNSET
        return self._operation(
            '/public_api/appsec/v1/application/configuration', method='get',
            body=body,
        )

    def create_application(self, *,
                           name: Union[str, None, UnsetType] = UNSET,
                           business_criticality: Union[str, None, UnsetType] = UNSET,
                           business_unit: Union[str, None, UnsetType] = UNSET,
                           creation_type: Union[str, None, UnsetType] = UNSET,
                           description: Union[str, None, UnsetType] = UNSET,
                           compliance: Union[str, None, UnsetType] = UNSET,
                           business_owner: Union[List[str], None, UnsetType] = UNSET,
                           dev_owner: Union[List[str], None, UnsetType] = UNSET,
                           dev_ops_owner: Union[List[str], None, UnsetType] = UNSET,
                           product_manager: Union[List[str], None, UnsetType] = UNSET,
                           asset_selection: Union[dict, None, UnsetType] = UNSET) -> Any:
        """Create an application

        POST /public_api/appsec/v1/application
        Available in Cortex XDR 5.x.
        Returns the complete JSON response, bytes for downloads, or None for an empty response.
        Omit optional fields with UNSET; explicit None is sent as JSON null.
        :param name: body field name.
        :param business_criticality: body field businessCriticality.
        :param business_unit: body field businessUnit.
        :param creation_type: body field creationType.
        :param description: body field description.
        :param compliance: body field compliance.
        :param business_owner: body field businessOwner.
        :param dev_owner: body field devOwner.
        :param dev_ops_owner: body field devOpsOwner.
        :param product_manager: body field productManager.
        :param asset_selection: body field assetSelection.
        """
        self._require_versions((5,))
        body = self._values({'name': name, 'businessCriticality': business_criticality, 'businessUnit': business_unit, 'creationType': creation_type, 'description': description, 'compliance': compliance, 'businessOwner': business_owner, 'devOwner': dev_owner, 'devOpsOwner': dev_ops_owner, 'productManager': product_manager, 'assetSelection': asset_selection})
        return self._operation(
            '/public_api/appsec/v1/application', method='post',
            body=body,
        )

    def get_applications(self, *,
                         page: Union[float, None, UnsetType] = UNSET,
                         page_size: Union[float, None, UnsetType] = UNSET) -> Any:
        """Get applications

        GET /public_api/appsec/v1/application
        Available in Cortex XDR 5.x.
        Returns the complete JSON response, bytes for downloads, or None for an empty response.
        Omit optional fields with UNSET; explicit None is sent as JSON null.
        :param page: query field page.
        :param page_size: query field pageSize.
        """
        self._require_versions((5,))
        body = UNSET
        return self._operation(
            '/public_api/appsec/v1/application', method='get',
            query=[('page', page, True), ('pageSize', page_size, True)],
            body=body,
        )

    def get_application(self, *,
                        application_id: str) -> Any:
        """Get an application

        GET /public_api/appsec/v1/application/{applicationId}
        Available in Cortex XDR 5.x.
        Returns the complete JSON response, bytes for downloads, or None for an empty response.
        Omit optional fields with UNSET; explicit None is sent as JSON null.
        :param application_id: path field applicationId.
        """
        self._require_versions((5,))
        body = UNSET
        return self._operation(
            '/public_api/appsec/v1/application/{applicationId}', method='get',
            path_params={'applicationId': application_id},
            body=body,
        )

    def update_application(self, *,
                           application_id: str,
                           x_cas_trace_id: Union[str, None, UnsetType] = UNSET,
                           business_criticality: Union[str, None, UnsetType] = UNSET,
                           creation_type: Union[str, None, UnsetType] = UNSET,
                           business_unit: Union[str, None, UnsetType] = UNSET,
                           description: Union[str, None, UnsetType] = UNSET,
                           compliance: Union[str, None, UnsetType] = UNSET,
                           business_owner: Union[List[str], None, UnsetType] = UNSET,
                           dev_owner: Union[List[str], None, UnsetType] = UNSET,
                           dev_ops_owner: Union[List[str], None, UnsetType] = UNSET,
                           product_manager: Union[List[str], None, UnsetType] = UNSET) -> Any:
        """Update an application

        PUT /public_api/appsec/v1/application/{applicationId}
        Available in Cortex XDR 5.x.
        Returns the complete JSON response, bytes for downloads, or None for an empty response.
        Omit optional fields with UNSET; explicit None is sent as JSON null.
        :param application_id: path field applicationId.
        :param x_cas_trace_id: header field x-cas-trace-id.
        :param business_criticality: body field businessCriticality.
        :param creation_type: body field creationType.
        :param business_unit: body field businessUnit.
        :param description: body field description.
        :param compliance: body field compliance.
        :param business_owner: body field businessOwner.
        :param dev_owner: body field devOwner.
        :param dev_ops_owner: body field devOpsOwner.
        :param product_manager: body field productManager.
        """
        self._require_versions((5,))
        body = self._values({'businessCriticality': business_criticality, 'creationType': creation_type, 'businessUnit': business_unit, 'description': description, 'compliance': compliance, 'businessOwner': business_owner, 'devOwner': dev_owner, 'devOpsOwner': dev_ops_owner, 'productManager': product_manager})
        return self._operation(
            '/public_api/appsec/v1/application/{applicationId}', method='put',
            path_params={'applicationId': application_id},
            headers={'x-cas-trace-id': x_cas_trace_id},
            body=body,
        )

    def delete_application_by_id(self, *,
                                 application_id: str) -> Any:
        """Delete an application

        DELETE /public_api/appsec/v1/application/{applicationId}
        Available in Cortex XDR 5.x.
        Returns the complete JSON response, bytes for downloads, or None for an empty response.
        Omit optional fields with UNSET; explicit None is sent as JSON null.
        :param application_id: path field applicationId.
        """
        self._require_versions((5,))
        body = UNSET
        return self._operation(
            '/public_api/appsec/v1/application/{applicationId}', method='delete',
            path_params={'applicationId': application_id},
            body=body,
        )

    def get_addable_assets(self, *,
                           application_id: str,
                           page: Union[float, None, UnsetType] = UNSET,
                           page_size: Union[float, None, UnsetType] = UNSET,
                           filter: Union[str, None, UnsetType] = UNSET) -> Any:
        """List addable assets

        GET /public_api/appsec/v1/application/{applicationId}/assets/addable
        Available in Cortex XDR 5.x.
        Returns the complete JSON response, bytes for downloads, or None for an empty response.
        Omit optional fields with UNSET; explicit None is sent as JSON null.
        :param application_id: path field applicationId.
        :param page: query field page.
        :param page_size: query field pageSize.
        :param filter: query field filter.
        """
        self._require_versions((5,))
        body = UNSET
        return self._operation(
            '/public_api/appsec/v1/application/{applicationId}/assets/addable', method='get',
            path_params={'applicationId': application_id},
            query=[('page', page, True), ('pageSize', page_size, True), ('filter', filter, True)],
            body=body,
        )

    def get_removable_assets(self, *,
                             application_id: str,
                             page: Union[float, None, UnsetType] = UNSET,
                             page_size: Union[float, None, UnsetType] = UNSET) -> Any:
        """List removable assets

        GET /public_api/appsec/v1/application/{applicationId}/assets/removable
        Available in Cortex XDR 5.x.
        Returns the complete JSON response, bytes for downloads, or None for an empty response.
        Omit optional fields with UNSET; explicit None is sent as JSON null.
        :param application_id: path field applicationId.
        :param page: query field page.
        :param page_size: query field pageSize.
        """
        self._require_versions((5,))
        body = UNSET
        return self._operation(
            '/public_api/appsec/v1/application/{applicationId}/assets/removable', method='get',
            path_params={'applicationId': application_id},
            query=[('page', page, True), ('pageSize', page_size, True)],
            body=body,
        )

    def override_assets(self, *,
                        application_id: str,
                        asset_ids: Union[List[str], None, UnsetType] = UNSET,
                        operation: Union[str, None, UnsetType] = UNSET,
                        filter: Union[str, None, UnsetType] = UNSET) -> Any:
        """Add or remove assets

        POST /public_api/appsec/v1/application/{applicationId}/assets/override
        Available in Cortex XDR 5.x.
        Returns the complete JSON response, bytes for downloads, or None for an empty response.
        Omit optional fields with UNSET; explicit None is sent as JSON null.
        :param application_id: path field applicationId.
        :param asset_ids: body field assetIds.
        :param operation: body field operation.
        :param filter: body field filter.
        """
        self._require_versions((5,))
        body = self._values({'assetIds': asset_ids, 'operation': operation, 'filter': filter})
        return self._operation(
            '/public_api/appsec/v1/application/{applicationId}/assets/override', method='post',
            path_params={'applicationId': application_id},
            body=body,
        )

    def get_overrides(self, *,
                      application_id: str,
                      page: Union[float, None, UnsetType] = UNSET,
                      page_size: Union[float, None, UnsetType] = UNSET) -> Any:
        """List override actions

        GET /public_api/appsec/v1/application/{applicationId}/assets/overrides
        Available in Cortex XDR 5.x.
        Returns the complete JSON response, bytes for downloads, or None for an empty response.
        Omit optional fields with UNSET; explicit None is sent as JSON null.
        :param application_id: path field applicationId.
        :param page: query field page.
        :param page_size: query field pageSize.
        """
        self._require_versions((5,))
        body = UNSET
        return self._operation(
            '/public_api/appsec/v1/application/{applicationId}/assets/overrides', method='get',
            path_params={'applicationId': application_id},
            query=[('page', page, True), ('pageSize', page_size, True)],
            body=body,
        )

    def revert_overrides(self, *,
                         application_id: str,
                         action_id: str) -> Any:
        """Revert asset override action

        DELETE /public_api/appsec/v1/application/{applicationId}/assets/overrides/{actionId}
        Available in Cortex XDR 5.x.
        Returns the complete JSON response, bytes for downloads, or None for an empty response.
        Omit optional fields with UNSET; explicit None is sent as JSON null.
        :param application_id: path field applicationId.
        :param action_id: path field actionId.
        """
        self._require_versions((5,))
        body = UNSET
        return self._operation(
            '/public_api/appsec/v1/application/{applicationId}/assets/overrides/{actionId}', method='delete',
            path_params={'applicationId': application_id, 'actionId': action_id},
            body=body,
        )

    def create_policy(self, *,
                      conditions: Union[dict, None, UnsetType] = UNSET,
                      description: Union[str, None, UnsetType] = UNSET,
                      name: Union[str, None, UnsetType] = UNSET,
                      scope: Union[dict, None, UnsetType] = UNSET,
                      triggers: Union[dict, None, UnsetType] = UNSET,
                      enabled: Union[bool, None, UnsetType] = UNSET,
                      asset_group_ids: Union[List[float], None, UnsetType] = UNSET,
                      suggestion_id: Union[str, None, UnsetType] = UNSET,
                      user_sbac: Union[List[float], None, UnsetType] = UNSET) -> Any:
        """Create an AppSec policy

        POST /public_api/appsec/v1/policies
        Available in Cortex XDR 5.x.
        Returns the complete JSON response, bytes for downloads, or None for an empty response.
        Omit optional fields with UNSET; explicit None is sent as JSON null.
        :param conditions: body field conditions.
        :param description: body field description.
        :param name: body field name.
        :param scope: body field scope.
        :param triggers: body field triggers.
        :param enabled: body field enabled.
        :param asset_group_ids: body field assetGroupIds.
        :param suggestion_id: body field suggestionId.
        :param user_sbac: body field userSbac.
        """
        self._require_versions((5,))
        body = self._values({'conditions': conditions, 'description': description, 'name': name, 'scope': scope, 'triggers': triggers, 'enabled': enabled, 'assetGroupIds': asset_group_ids, 'suggestionId': suggestion_id, 'userSbac': user_sbac})
        return self._operation(
            '/public_api/appsec/v1/policies', method='post',
            body=body,
        )

    def get_policies(self, *,
                     finding_types: Union[List[str], None, UnsetType] = UNSET,
                     actions: Union[List[str], None, UnsetType] = UNSET,
                     status: Union[str, None, UnsetType] = UNSET,
                     triggers: Union[List[str], None, UnsetType] = UNSET,
                     is_custom: Union[bool, None, UnsetType] = UNSET) -> Any:
        """List AppSec policies

        GET /public_api/appsec/v1/policies
        Available in Cortex XDR 5.x.
        Returns the complete JSON response, bytes for downloads, or None for an empty response.
        Omit optional fields with UNSET; explicit None is sent as JSON null.
        :param finding_types: query field findingTypes.
        :param actions: query field actions.
        :param status: query field status.
        :param triggers: query field triggers.
        :param is_custom: query field isCustom.
        """
        self._require_versions((5,))
        body = UNSET
        return self._operation(
            '/public_api/appsec/v1/policies', method='get',
            query=[('findingTypes', finding_types, True), ('actions', actions, True), ('status', status, True), ('triggers', triggers, True), ('isCustom', is_custom, True)],
            body=body,
        )

    def get_rules(self, *,
                  get_scanner_rule_id: Union[bool, None, UnsetType] = UNSET,
                  enabled: Union[bool, None, UnsetType] = UNSET,
                  is_custom: Union[bool, None, UnsetType] = UNSET,
                  categories: Union[List[str], None, UnsetType] = UNSET,
                  sub_categories: Union[List[str], None, UnsetType] = UNSET,
                  cloud_providers: Union[List[str], None, UnsetType] = UNSET,
                  scanners: Union[List[str], None, UnsetType] = UNSET,
                  severities: Union[List[str], None, UnsetType] = UNSET,
                  frameworks: Union[List[str], None, UnsetType] = UNSET,
                  labels: Union[List[str], None, UnsetType] = UNSET,
                  offset: Union[float, None, UnsetType] = UNSET,
                  limit: Union[float, None, UnsetType] = UNSET,
                  sort_by: Union[str, None, UnsetType] = UNSET,
                  sort_order: Union[int, None, UnsetType] = UNSET) -> Any:
        """Get AppSec rules

        GET /public_api/appsec/v1/rules
        Available in Cortex XDR 5.x.
        Returns the complete JSON response, bytes for downloads, or None for an empty response.
        Omit optional fields with UNSET; explicit None is sent as JSON null.
        :param get_scanner_rule_id: header field get-scanner-rule-id.
        :param enabled: query field enabled.
        :param is_custom: query field isCustom.
        :param categories: query field categories.
        :param sub_categories: query field subCategories.
        :param cloud_providers: query field cloudProviders.
        :param scanners: query field scanners.
        :param severities: query field severities.
        :param frameworks: query field frameworks.
        :param labels: query field labels.
        :param offset: query field offset.
        :param limit: query field limit.
        :param sort_by: query field sortBy.
        :param sort_order: query field sortOrder.
        """
        self._require_versions((5,))
        body = UNSET
        return self._operation(
            '/public_api/appsec/v1/rules', method='get',
            query=[('enabled', enabled, True), ('isCustom', is_custom, True), ('categories', categories, False), ('subCategories', sub_categories, True), ('cloudProviders', cloud_providers, True), ('scanners', scanners, True), ('severities', severities, True), ('frameworks', frameworks, True), ('labels', labels, True), ('offset', offset, True), ('limit', limit, True), ('sortBy', sort_by, True), ('sortOrder', sort_order, True)],
            headers={'get-scanner-rule-id': get_scanner_rule_id},
            body=body,
        )

    def create_custom_rule(self, *,
                           name: Union[str, None, UnsetType] = UNSET,
                           description: Union[str, None, UnsetType] = UNSET,
                           severity: Union[str, None, UnsetType] = UNSET,
                           labels: Union[List[str], None, UnsetType] = UNSET,
                           scanner: Union[str, None, UnsetType] = UNSET,
                           frameworks: Union[dict, None, UnsetType] = UNSET,
                           category: Union[Any, None, UnsetType] = UNSET,
                           sub_category: Union[str, None, UnsetType] = UNSET,
                           cspm_rule_id: Union[str, None, UnsetType] = UNSET,
                           cloned_from_rule_id: Union[str, None, UnsetType] = UNSET) -> Any:
        """Create an AppSec rule

        POST /public_api/appsec/v1/rules
        Available in Cortex XDR 5.x.
        Returns the complete JSON response, bytes for downloads, or None for an empty response.
        Omit optional fields with UNSET; explicit None is sent as JSON null.
        :param name: body field name.
        :param description: body field description.
        :param severity: body field severity.
        :param labels: body field labels.
        :param scanner: body field scanner.
        :param frameworks: body field frameworks.
        :param category: body field category.
        :param sub_category: body field subCategory.
        :param cspm_rule_id: body field cspmRuleId.
        :param cloned_from_rule_id: body field clonedFromRuleId.
        """
        self._require_versions((5,))
        body = self._values({'name': name, 'description': description, 'severity': severity, 'labels': labels, 'scanner': scanner, 'frameworks': frameworks, 'category': category, 'subCategory': sub_category, 'cspmRuleId': cspm_rule_id, 'clonedFromRuleId': cloned_from_rule_id})
        return self._operation(
            '/public_api/appsec/v1/rules', method='post',
            body=body,
        )

    def get_rule_by_id(self, *,
                       rule_id: str) -> Any:
        """Get an AppSec rule

        GET /public_api/appsec/v1/rules/{ruleId}
        Available in Cortex XDR 5.x.
        Returns the complete JSON response, bytes for downloads, or None for an empty response.
        Omit optional fields with UNSET; explicit None is sent as JSON null.
        :param rule_id: path field ruleId.
        """
        self._require_versions((5,))
        body = UNSET
        return self._operation(
            '/public_api/appsec/v1/rules/{ruleId}', method='get',
            path_params={'ruleId': rule_id},
            body=body,
        )

    def modify_rule(self, *,
                    rule_id: str,
                    body: Union[Any, None, UnsetType] = UNSET) -> Any:
        """Update an AppSec rule

        PATCH /public_api/appsec/v1/rules/{ruleId}
        Available in Cortex XDR 5.x.
        Returns the complete JSON response, bytes for downloads, or None for an empty response.
        Omit optional fields with UNSET; explicit None is sent as JSON null.
        :param rule_id: path field ruleId.
        :param body: payload field body.
        """
        self._require_versions((5,))
        body = body
        return self._operation(
            '/public_api/appsec/v1/rules/{ruleId}', method='patch',
            path_params={'ruleId': rule_id},
            body=body,
        )

    def delete_rule_by_id(self, *,
                          rule_id: str) -> Any:
        """Delete an AppSec rule

        DELETE /public_api/appsec/v1/rules/{ruleId}
        Available in Cortex XDR 5.x.
        Returns the complete JSON response, bytes for downloads, or None for an empty response.
        Omit optional fields with UNSET; explicit None is sent as JSON null.
        :param rule_id: path field ruleId.
        """
        self._require_versions((5,))
        body = UNSET
        return self._operation(
            '/public_api/appsec/v1/rules/{ruleId}', method='delete',
            path_params={'ruleId': rule_id},
            body=body,
        )

    def get_labels(self) -> Any:
        """Get AppSec rule labels

        GET /public_api/appsec/v1/rules/rule-labels
        Available in Cortex XDR 5.x.
        Returns the complete JSON response, bytes for downloads, or None for an empty response.
        Omit optional fields with UNSET; explicit None is sent as JSON null.
        """
        self._require_versions((5,))
        body = UNSET
        return self._operation(
            '/public_api/appsec/v1/rules/rule-labels', method='get',
            body=body,
        )

    def validate_custom_rule(self, *,
                             body: Union[List[dict], None, UnsetType] = UNSET) -> Any:
        """Create an AppSec rule validation

        POST /public_api/appsec/v1/rules/validate
        Available in Cortex XDR 5.x.
        Returns the complete JSON response, bytes for downloads, or None for an empty response.
        Omit optional fields with UNSET; explicit None is sent as JSON null.
        :param body: payload field body.
        """
        self._require_versions((5,))
        body = body
        return self._operation(
            '/public_api/appsec/v1/rules/validate', method='post',
            body=body,
        )

    def get_repository_assets(self, *,
                              source: Union[List[str], None, UnsetType] = UNSET,
                              search: Union[str, None, UnsetType] = UNSET,
                              offset: Union[float, None, UnsetType] = UNSET,
                              limit: Union[float, None, UnsetType] = UNSET) -> Any:
        """Get repositories

        GET /public_api/appsec/v1/repositories
        Available in Cortex XDR 5.x.
        Returns the complete JSON response, bytes for downloads, or None for an empty response.
        Omit optional fields with UNSET; explicit None is sent as JSON null.
        :param source: query field source.
        :param search: query field search.
        :param offset: query field offset.
        :param limit: query field limit.
        """
        self._require_versions((5,))
        body = UNSET
        return self._operation(
            '/public_api/appsec/v1/repositories', method='get',
            query=[('source', source, True), ('search', search, True), ('offset', offset, True), ('limit', limit, True)],
            body=body,
        )

    def get_repository_asset_by_asset_id(self, *,
                                         asset_id: str) -> Any:
        """Get a repository

        GET /public_api/appsec/v1/repositories/{assetId}
        Available in Cortex XDR 5.x.
        Returns the complete JSON response, bytes for downloads, or None for an empty response.
        Omit optional fields with UNSET; explicit None is sent as JSON null.
        :param asset_id: path field assetId.
        """
        self._require_versions((5,))
        body = UNSET
        return self._operation(
            '/public_api/appsec/v1/repositories/{assetId}', method='get',
            path_params={'assetId': asset_id},
            body=body,
        )

    def get_asset_scan_configuration(self, *,
                                     asset_id: str) -> Any:
        """Get a repository scan configuration

        GET /public_api/appsec/v1/repositories/{assetId}/scan-configuration
        Available in Cortex XDR 5.x.
        Returns the complete JSON response, bytes for downloads, or None for an empty response.
        Omit optional fields with UNSET; explicit None is sent as JSON null.
        :param asset_id: path field assetId.
        """
        self._require_versions((5,))
        body = UNSET
        return self._operation(
            '/public_api/appsec/v1/repositories/{assetId}/scan-configuration', method='get',
            path_params={'assetId': asset_id},
            body=body,
        )

    def update_asset_scan_configuration(self, *,
                                        asset_id: str,
                                        excluded_paths: Union[List[str], None, UnsetType] = UNSET,
                                        pr_scanning: Union[dict, None, UnsetType] = UNSET,
                                        tagging_bot: Union[dict, None, UnsetType] = UNSET,
                                        scanners: Union[dict, None, UnsetType] = UNSET) -> Any:
        """Update a repository scan configuration

        PUT /public_api/appsec/v1/repositories/{assetId}/scan-configuration
        Available in Cortex XDR 5.x.
        Returns the complete JSON response, bytes for downloads, or None for an empty response.
        Omit optional fields with UNSET; explicit None is sent as JSON null.
        :param asset_id: path field assetId.
        :param excluded_paths: body field excludedPaths.
        :param pr_scanning: body field prScanning.
        :param tagging_bot: body field taggingBot.
        :param scanners: body field scanners.
        """
        self._require_versions((5,))
        body = self._values({'excludedPaths': excluded_paths, 'prScanning': pr_scanning, 'taggingBot': tagging_bot, 'scanners': scanners})
        return self._operation(
            '/public_api/appsec/v1/repositories/{assetId}/scan-configuration', method='put',
            path_params={'assetId': asset_id},
            body=body,
        )

    def get_scanned_branches(self, *,
                             asset_id: str) -> Any:
        """Get AppSec repository branches

        GET /public_api/appsec/v1/repositories/{assetId}/branches
        Available in Cortex XDR 5.x.
        Returns the complete JSON response, bytes for downloads, or None for an empty response.
        Omit optional fields with UNSET; explicit None is sent as JSON null.
        :param asset_id: path field assetId.
        """
        self._require_versions((5,))
        body = UNSET
        return self._operation(
            '/public_api/appsec/v1/repositories/{assetId}/branches', method='get',
            path_params={'assetId': asset_id},
            body=body,
        )

    def set_persist_branches(self, *,
                             asset_id: str,
                             selected_branches: Union[List[str], None, UnsetType] = UNSET,
                             primary_branch: Union[str, None, UnsetType] = UNSET) -> Any:
        """Update an AppSec repository branch

        PUT /public_api/appsec/v1/repositories/{assetId}/branches
        Available in Cortex XDR 5.x.
        Returns the complete JSON response, bytes for downloads, or None for an empty response.
        Omit optional fields with UNSET; explicit None is sent as JSON null.
        :param asset_id: path field assetId.
        :param selected_branches: body field selectedBranches.
        :param primary_branch: body field primaryBranch.
        """
        self._require_versions((5,))
        body = self._values({'selectedBranches': selected_branches, 'primaryBranch': primary_branch})
        return self._operation(
            '/public_api/appsec/v1/repositories/{assetId}/branches', method='put',
            path_params={'assetId': asset_id},
            body=body,
        )

    def get_unscanned_repos(self, *,
                            days: Union[float, None, UnsetType] = UNSET) -> Any:
        """Get unscanned AppSec scan management repositories

        GET /public_api/appsec/v1/scans/unscanned-repositories
        Available in Cortex XDR 5.x.
        Returns the complete JSON response, bytes for downloads, or None for an empty response.
        Omit optional fields with UNSET; explicit None is sent as JSON null.
        :param days: query field days.
        """
        self._require_versions((5,))
        body = UNSET
        return self._operation(
            '/public_api/appsec/v1/scans/unscanned-repositories', method='get',
            query=[('days', days, True)],
            body=body,
        )

    def get_sbom_report(self, *,
                        repo_id: str,
                        branch_name: Union[str, None, UnsetType] = UNSET,
                        file_type: Union[str, None, UnsetType] = UNSET,
                        version: Union[str, None, UnsetType] = UNSET,
                        format: Union[str, None, UnsetType] = UNSET) -> Any:
        """Get an SBOM for the specified repository

        GET /public_api/appsec/v1/sbom/repository
        Available in Cortex XDR 5.x.
        Returns the complete JSON response, bytes for downloads, or None for an empty response.
        Omit optional fields with UNSET; explicit None is sent as JSON null.
        :param repo_id: query field repoId.
        :param branch_name: query field branchName.
        :param file_type: query field fileType.
        :param version: query field version.
        :param format: query field format.
        """
        self._require_versions((5,))
        body = UNSET
        return self._operation(
            '/public_api/appsec/v1/sbom/repository', method='get',
            query=[('repoId', repo_id, True), ('branchName', branch_name, True), ('fileType', file_type, True), ('version', version, True), ('format', format, True)],
            body=body,
        )

    def get_org_sbom_report(self, *,
                            org_name: str,
                            file_type: Union[str, None, UnsetType] = UNSET,
                            version: Union[str, None, UnsetType] = UNSET,
                            format: Union[str, None, UnsetType] = UNSET) -> Any:
        """Get all SBOMs for the specified organization

        GET /public_api/appsec/v1/sbom/organization
        Available in Cortex XDR 5.x.
        Returns the complete JSON response, bytes for downloads, or None for an empty response.
        Omit optional fields with UNSET; explicit None is sent as JSON null.
        :param org_name: query field orgName.
        :param file_type: query field fileType.
        :param version: query field version.
        :param format: query field format.
        """
        self._require_versions((5,))
        body = UNSET
        return self._operation(
            '/public_api/appsec/v1/sbom/organization', method='get',
            query=[('orgName', org_name, True), ('fileType', file_type, True), ('version', version, True), ('format', format, True)],
            body=body,
        )

    def get_periodic_scans(self, *,
                           organization_name: Union[str, None, UnsetType] = UNSET,
                           repositories: Union[List[str], None, UnsetType] = UNSET,
                           branch_name: Union[str, None, UnsetType] = UNSET,
                           scan_health: Union[str, None, UnsetType] = UNSET,
                           days: Union[float, None, UnsetType] = UNSET,
                           offset: Union[float, None, UnsetType] = UNSET,
                           limit: Union[float, None, UnsetType] = UNSET) -> Any:
        """Get AppSec branch periodic scans

        GET /public_api/appsec/v1/scans/periodic
        Available in Cortex XDR 5.x.
        Returns the complete JSON response, bytes for downloads, or None for an empty response.
        Omit optional fields with UNSET; explicit None is sent as JSON null.
        :param organization_name: query field organizationName.
        :param repositories: query field repositories.
        :param branch_name: query field branchName.
        :param scan_health: query field scanHealth.
        :param days: query field days.
        :param offset: query field offset.
        :param limit: query field limit.
        """
        self._require_versions((5,))
        body = UNSET
        return self._operation(
            '/public_api/appsec/v1/scans/periodic', method='get',
            query=[('organizationName', organization_name, True), ('repositories', repositories, True), ('branchName', branch_name, True), ('scanHealth', scan_health, True), ('days', days, True), ('offset', offset, True), ('limit', limit, True)],
            body=body,
        )

    def get_pr_scans(self, *,
                     organization_name: Union[str, None, UnsetType] = UNSET,
                     repositories: Union[List[str], None, UnsetType] = UNSET,
                     branch_name: Union[str, None, UnsetType] = UNSET,
                     pr_id: Union[str, None, UnsetType] = UNSET,
                     pr_title: Union[str, None, UnsetType] = UNSET,
                     pr_status: Union[str, None, UnsetType] = UNSET,
                     scan_health: Union[str, None, UnsetType] = UNSET,
                     days: Union[float, None, UnsetType] = UNSET,
                     offset: Union[float, None, UnsetType] = UNSET,
                     limit: Union[float, None, UnsetType] = UNSET) -> Any:
        """Get AppSec Pull Request scans

        GET /public_api/appsec/v1/scans/pr
        Available in Cortex XDR 5.x.
        Returns the complete JSON response, bytes for downloads, or None for an empty response.
        Omit optional fields with UNSET; explicit None is sent as JSON null.
        :param organization_name: query field organizationName.
        :param repositories: query field repositories.
        :param branch_name: query field branchName.
        :param pr_id: query field prId.
        :param pr_title: query field prTitle.
        :param pr_status: query field prStatus.
        :param scan_health: query field scanHealth.
        :param days: query field days.
        :param offset: query field offset.
        :param limit: query field limit.
        """
        self._require_versions((5,))
        body = UNSET
        return self._operation(
            '/public_api/appsec/v1/scans/pr', method='get',
            query=[('organizationName', organization_name, True), ('repositories', repositories, True), ('branchName', branch_name, True), ('prId', pr_id, True), ('prTitle', pr_title, True), ('prStatus', pr_status, True), ('scanHealth', scan_health, True), ('days', days, True), ('offset', offset, True), ('limit', limit, True)],
            body=body,
        )

    def get_ci_scans(self, *,
                     organization_name: Union[str, None, UnsetType] = UNSET,
                     repositories: Union[List[str], None, UnsetType] = UNSET,
                     ci_status: Union[str, None, UnsetType] = UNSET,
                     scan_health: Union[str, None, UnsetType] = UNSET,
                     days: Union[float, None, UnsetType] = UNSET,
                     offset: Union[float, None, UnsetType] = UNSET,
                     limit: Union[float, None, UnsetType] = UNSET) -> Any:
        """Get AppSec CI scans

        GET /public_api/appsec/v1/scans/ci
        Available in Cortex XDR 5.x.
        Returns the complete JSON response, bytes for downloads, or None for an empty response.
        Omit optional fields with UNSET; explicit None is sent as JSON null.
        :param organization_name: query field organizationName.
        :param repositories: query field repositories.
        :param ci_status: query field ciStatus.
        :param scan_health: query field scanHealth.
        :param days: query field days.
        :param offset: query field offset.
        :param limit: query field limit.
        """
        self._require_versions((5,))
        body = UNSET
        return self._operation(
            '/public_api/appsec/v1/scans/ci', method='get',
            query=[('organizationName', organization_name, True), ('repositories', repositories, True), ('ciStatus', ci_status, True), ('scanHealth', scan_health, True), ('days', days, True), ('offset', offset, True), ('limit', limit, True)],
            body=body,
        )

    def get_scan_issues(self, *,
                        scan_id: str,
                        severity: Union[str, None, UnsetType] = UNSET,
                        offset: Union[float, None, UnsetType] = UNSET,
                        limit: Union[float, None, UnsetType] = UNSET) -> Any:
        """List AppSec scan issues

        GET /public_api/appsec/v1/scans/{scanId}/issues
        Available in Cortex XDR 5.x.
        Returns the complete JSON response, bytes for downloads, or None for an empty response.
        Omit optional fields with UNSET; explicit None is sent as JSON null.
        :param scan_id: path field scanId.
        :param severity: query field severity.
        :param offset: query field offset.
        :param limit: query field limit.
        """
        self._require_versions((5,))
        body = UNSET
        return self._operation(
            '/public_api/appsec/v1/scans/{scanId}/issues', method='get',
            path_params={'scanId': scan_id},
            query=[('severity', severity, True), ('offset', offset, True), ('limit', limit, True)],
            body=body,
        )

    def get_scan_findings(self, *,
                          scan_id: str,
                          severity: Union[str, None, UnsetType] = UNSET,
                          offset: Union[float, None, UnsetType] = UNSET,
                          limit: Union[float, None, UnsetType] = UNSET) -> Any:
        """List AppSec scan findings

        GET /public_api/appsec/v1/scans/{scanId}/findings
        Available in Cortex XDR 5.x.
        Returns the complete JSON response, bytes for downloads, or None for an empty response.
        Omit optional fields with UNSET; explicit None is sent as JSON null.
        :param scan_id: path field scanId.
        :param severity: query field severity.
        :param offset: query field offset.
        :param limit: query field limit.
        """
        self._require_versions((5,))
        body = UNSET
        return self._operation(
            '/public_api/appsec/v1/scans/{scanId}/findings', method='get',
            path_params={'scanId': scan_id},
            query=[('severity', severity, True), ('offset', offset, True), ('limit', limit, True)],
            body=body,
        )

    def scan_repository(self, *,
                        repository_id: str,
                        scan_full_git_history: Union[bool, None, UnsetType] = UNSET,
                        branch_name: Union[str, None, UnsetType] = UNSET) -> Any:
        """Rerun a repository scan

        POST /public_api/appsec/v1/scan/repository/{repositoryId}
        Available in Cortex XDR 5.x.
        Returns the complete JSON response, bytes for downloads, or None for an empty response.
        Omit optional fields with UNSET; explicit None is sent as JSON null.
        :param repository_id: path field repositoryId.
        :param scan_full_git_history: query field scanFullGitHistory.
        :param branch_name: body field branchName.
        """
        self._require_versions((5,))
        body = self._values({'branchName': branch_name})
        return self._operation(
            '/public_api/appsec/v1/scan/repository/{repositoryId}', method='post',
            path_params={'repositoryId': repository_id},
            query=[('scanFullGitHistory', scan_full_git_history, True)],
            body=body,
        )

    def get_policy(self, *,
                   policy_id: str) -> Any:
        """Get an AppSec policy

        GET /public_api/appsec/v1/policies/{policyId}
        Available in Cortex XDR 5.x.
        Returns the complete JSON response, bytes for downloads, or None for an empty response.
        Omit optional fields with UNSET; explicit None is sent as JSON null.
        :param policy_id: path field policyId.
        """
        self._require_versions((5,))
        body = UNSET
        return self._operation(
            '/public_api/appsec/v1/policies/{policyId}', method='get',
            path_params={'policyId': policy_id},
            body=body,
        )

    def update_policy(self, *,
                      policy_id: str,
                      name: Union[str, None, UnsetType] = UNSET,
                      description: Union[str, None, UnsetType] = UNSET,
                      conditions: Union[dict, None, UnsetType] = UNSET,
                      scope: Union[dict, None, UnsetType] = UNSET,
                      triggers: Union[dict, None, UnsetType] = UNSET,
                      related_detection_rules: Union[List[str], None, UnsetType] = UNSET,
                      enabled: Union[bool, None, UnsetType] = UNSET,
                      suggestion_id: Union[str, None, UnsetType] = UNSET,
                      asset_group_ids: Union[List[float], None, UnsetType] = UNSET,
                      user_sbac: Union[List[float], None, UnsetType] = UNSET) -> Any:
        """Update an AppSec policy

        PUT /public_api/appsec/v1/policies/{policyId}
        Available in Cortex XDR 5.x.
        Returns the complete JSON response, bytes for downloads, or None for an empty response.
        Omit optional fields with UNSET; explicit None is sent as JSON null.
        :param policy_id: path field policyId.
        :param name: body field name.
        :param description: body field description.
        :param conditions: body field conditions.
        :param scope: body field scope.
        :param triggers: body field triggers.
        :param related_detection_rules: body field relatedDetectionRules.
        :param enabled: body field enabled.
        :param suggestion_id: body field suggestionId.
        :param asset_group_ids: body field assetGroupIds.
        :param user_sbac: body field userSbac.
        """
        self._require_versions((5,))
        body = self._values({'name': name, 'description': description, 'conditions': conditions, 'scope': scope, 'triggers': triggers, 'relatedDetectionRules': related_detection_rules, 'enabled': enabled, 'suggestionId': suggestion_id, 'assetGroupIds': asset_group_ids, 'userSbac': user_sbac})
        return self._operation(
            '/public_api/appsec/v1/policies/{policyId}', method='put',
            path_params={'policyId': policy_id},
            body=body,
        )

    def delete_policy(self, *,
                      policy_id: str) -> Any:
        """Delete an AppSec policy

        DELETE /public_api/appsec/v1/policies/{policyId}
        Available in Cortex XDR 5.x.
        Returns the complete JSON response, bytes for downloads, or None for an empty response.
        Omit optional fields with UNSET; explicit None is sent as JSON null.
        :param policy_id: path field policyId.
        """
        self._require_versions((5,))
        body = UNSET
        return self._operation(
            '/public_api/appsec/v1/policies/{policyId}', method='delete',
            path_params={'policyId': policy_id},
            body=body,
        )

    def get_package_operational_risk_v2(self, *,
                                        package_manager_name: str,
                                        package_name: str) -> Any:
        """Get open source package operational risk

        GET /public_api/appsec/v1/operational-risk
        Available in Cortex XDR 5.x.
        Returns the complete JSON response, bytes for downloads, or None for an empty response.
        Omit optional fields with UNSET; explicit None is sent as JSON null.
        :param package_manager_name: query field packageManagerName.
        :param package_name: query field packageName.
        """
        self._require_versions((5,))
        body = UNSET
        return self._operation(
            '/public_api/appsec/v1/operational-risk', method='get',
            query=[('packageManagerName', package_manager_name, True), ('packageName', package_name, True)],
            body=body,
        )

    def get_all_criteria(self, *,
                         page: Union[float, None, UnsetType] = UNSET,
                         page_size: Union[float, None, UnsetType] = UNSET) -> Any:
        """Get all criteria

        GET /public_api/appsec/v1/application/criteria/all
        Available in Cortex XDR 5.x.
        Returns the complete JSON response, bytes for downloads, or None for an empty response.
        Omit optional fields with UNSET; explicit None is sent as JSON null.
        :param page: query field page.
        :param page_size: query field pageSize.
        """
        self._require_versions((5,))
        body = UNSET
        return self._operation(
            '/public_api/appsec/v1/application/criteria/all', method='get',
            query=[('page', page, True), ('pageSize', page_size, True)],
            body=body,
        )

    def get_criteria(self, *,
                     criteria_id: str) -> Any:
        """Get a Criteria by ID

        GET /public_api/appsec/v1/application/criteria/{criteriaId}
        Available in Cortex XDR 5.x.
        Returns the complete JSON response, bytes for downloads, or None for an empty response.
        Omit optional fields with UNSET; explicit None is sent as JSON null.
        :param criteria_id: path field criteriaId.
        """
        self._require_versions((5,))
        body = UNSET
        return self._operation(
            '/public_api/appsec/v1/application/criteria/{criteriaId}', method='get',
            path_params={'criteriaId': criteria_id},
            body=body,
        )

    def delete_criteria(self, *,
                        criteria_id: str) -> Any:
        """Delete a Criteria

        DELETE /public_api/appsec/v1/application/criteria/{criteriaId}
        Available in Cortex XDR 5.x.
        Returns the complete JSON response, bytes for downloads, or None for an empty response.
        Omit optional fields with UNSET; explicit None is sent as JSON null.
        :param criteria_id: path field criteriaId.
        """
        self._require_versions((5,))
        body = UNSET
        return self._operation(
            '/public_api/appsec/v1/application/criteria/{criteriaId}', method='delete',
            path_params={'criteriaId': criteria_id},
            body=body,
        )

    def create_criteria(self, *,
                        name: Union[str, None, UnsetType] = UNSET,
                        description: Union[str, None, UnsetType] = UNSET,
                        type: Union[str, None, UnsetType] = UNSET,
                        config: Union[Any, None, UnsetType] = UNSET) -> Any:
        """Create a Criteria

        POST /public_api/appsec/v1/application/criteria
        Available in Cortex XDR 5.x.
        Returns the complete JSON response, bytes for downloads, or None for an empty response.
        Omit optional fields with UNSET; explicit None is sent as JSON null.
        :param name: body field name.
        :param description: body field description.
        :param type: body field type.
        :param config: body field config.
        """
        self._require_versions((5,))
        body = self._values({'name': name, 'description': description, 'type': type, 'config': config})
        return self._operation(
            '/public_api/appsec/v1/application/criteria', method='post',
            body=body,
        )

    def get_fix_suggestion(self, *,
                           issue_id: str,
                           show_code_block: Union[bool, None, UnsetType] = UNSET,
                           show_remediation_instruction: Union[bool, None, UnsetType] = UNSET,
                           show_suggested_code_block: Union[bool, None, UnsetType] = UNSET) -> Any:
        """Get Fix Suggestion

        GET /public_api/appsec/v1/issues/fix/{issueId}/fix_suggestion
        Available in Cortex XDR 5.x.
        Returns the complete JSON response, bytes for downloads, or None for an empty response.
        Omit optional fields with UNSET; explicit None is sent as JSON null.
        :param issue_id: path field issueId.
        :param show_code_block: query field showCodeBlock.
        :param show_remediation_instruction: query field showRemediationInstruction.
        :param show_suggested_code_block: query field showSuggestedCodeBlock.
        """
        self._require_versions((5,))
        body = UNSET
        return self._operation(
            '/public_api/appsec/v1/issues/fix/{issueId}/fix_suggestion', method='get',
            path_params={'issueId': issue_id},
            query=[('showCodeBlock', show_code_block, True), ('showRemediationInstruction', show_remediation_instruction, True), ('showSuggestedCodeBlock', show_suggested_code_block, True)],
            body=body,
        )

    def trigger_fix_pr(self, *,
                       fix_branch_name: Union[str, None, UnsetType] = UNSET,
                       title: Union[str, None, UnsetType] = UNSET,
                       issue_ids: Union[List[str], None, UnsetType] = UNSET) -> Any:
        """Trigger Fix Pull Request

        POST /public_api/appsec/v1/issues/fix/trigger_fix_pull_request
        Available in Cortex XDR 5.x.
        Returns the complete JSON response, bytes for downloads, or None for an empty response.
        Omit optional fields with UNSET; explicit None is sent as JSON null.
        :param fix_branch_name: body field fixBranchName.
        :param title: body field title.
        :param issue_ids: body field issueIds.
        """
        self._require_versions((5,))
        body = self._values({'fixBranchName': fix_branch_name, 'title': title, 'issueIds': issue_ids})
        return self._operation(
            '/public_api/appsec/v1/issues/fix/trigger_fix_pull_request', method='post',
            body=body,
        )

    def get_fix_status(self, *,
                       remediation_id: str) -> Any:
        """Get Fix Status

        GET /public_api/appsec/v1/issues/fix/{remediationId}
        Available in Cortex XDR 5.x.
        Returns the complete JSON response, bytes for downloads, or None for an empty response.
        Omit optional fields with UNSET; explicit None is sent as JSON null.
        :param remediation_id: path field remediationId.
        """
        self._require_versions((5,))
        body = UNSET
        return self._operation(
            '/public_api/appsec/v1/issues/fix/{remediationId}', method='get',
            path_params={'remediationId': remediation_id},
            body=body,
        )

    def get_data_source_instances(self, *,
                                  type: Union[str, None, UnsetType] = UNSET,
                                  type_category: Union[str, None, UnsetType] = UNSET) -> Any:
        """Get all Data Sources

        GET /public_api/appsec/v1/data_source_instances
        Available in Cortex XDR 5.x.
        Returns the complete JSON response, bytes for downloads, or None for an empty response.
        Omit optional fields with UNSET; explicit None is sent as JSON null.
        :param type: query field type.
        :param type_category: query field type_category.
        """
        self._require_versions((5,))
        body = UNSET
        return self._operation(
            '/public_api/appsec/v1/data_source_instances', method='get',
            query=[('type', type, True), ('type_category', type_category, True)],
            body=body,
        )

    def create_data_source_instance(self, *,
                                    type: Union[str, None, UnsetType] = UNSET,
                                    domain: Union[dict, None, UnsetType] = UNSET,
                                    credentials: Union[dict, None, UnsetType] = UNSET,
                                    unique_properties: Union[dict, None, UnsetType] = UNSET,
                                    transporter: Union[dict, None, UnsetType] = UNSET,
                                    self_signed_certificate: Union[str, None, UnsetType] = UNSET) -> Any:
        """Create AppSec Data Sources

        POST /public_api/appsec/v1/data_source_instances
        Available in Cortex XDR 5.x.
        Returns the complete JSON response, bytes for downloads, or None for an empty response.
        Omit optional fields with UNSET; explicit None is sent as JSON null.
        :param type: body field type.
        :param domain: body field domain.
        :param credentials: body field credentials.
        :param unique_properties: body field uniqueProperties.
        :param transporter: body field transporter.
        :param self_signed_certificate: body field selfSignedCertificate.
        """
        self._require_versions((5,))
        body = self._values({'type': type, 'domain': domain, 'credentials': credentials, 'uniqueProperties': unique_properties, 'transporter': transporter, 'selfSignedCertificate': self_signed_certificate})
        return self._operation(
            '/public_api/appsec/v1/data_source_instances', method='post',
            body=body,
        )

    def get_data_source_instance(self, *,
                                 id: str) -> Any:
        """Get an AppSec Data Source

        GET /public_api/appsec/v1/data_source_instances/{id}
        Available in Cortex XDR 5.x.
        Returns the complete JSON response, bytes for downloads, or None for an empty response.
        Omit optional fields with UNSET; explicit None is sent as JSON null.
        :param id: path field id.
        """
        self._require_versions((5,))
        body = UNSET
        return self._operation(
            '/public_api/appsec/v1/data_source_instances/{id}', method='get',
            path_params={'id': id},
            body=body,
        )

    def update_data_source_instance(self, *,
                                    id: str,
                                    selection_type: Union[str, None, UnsetType] = UNSET,
                                    state: Union[List[str], None, UnsetType] = UNSET,
                                    external_projects: Union[List[dict], None, UnsetType] = UNSET,
                                    unique_properties: Union[dict, None, UnsetType] = UNSET) -> Any:
        """Update an AppSec Data Source

        PUT /public_api/appsec/v1/data_source_instances/{id}
        Available in Cortex XDR 5.x.
        Returns the complete JSON response, bytes for downloads, or None for an empty response.
        Omit optional fields with UNSET; explicit None is sent as JSON null.
        :param id: path field id.
        :param selection_type: body field selectionType.
        :param state: body field state.
        :param external_projects: body field externalProjects.
        :param unique_properties: body field uniqueProperties.
        """
        self._require_versions((5,))
        body = self._values({'selectionType': selection_type, 'state': state, 'externalProjects': external_projects, 'uniqueProperties': unique_properties})
        return self._operation(
            '/public_api/appsec/v1/data_source_instances/{id}', method='put',
            path_params={'id': id},
            body=body,
        )

    def delete_data_source_instance(self, *,
                                    id: str) -> Any:
        """Delete an AppSec Data Source

        DELETE /public_api/appsec/v1/data_source_instances/{id}
        Available in Cortex XDR 5.x.
        Returns the complete JSON response, bytes for downloads, or None for an empty response.
        Omit optional fields with UNSET; explicit None is sent as JSON null.
        :param id: path field id.
        """
        self._require_versions((5,))
        body = UNSET
        return self._operation(
            '/public_api/appsec/v1/data_source_instances/{id}', method='delete',
            path_params={'id': id},
            body=body,
        )

    def upload_sarif_findings(self, *,
                              collector_id: str,
                              repository_id: str,
                              repository_url: str,
                              branch: Union[str, None, UnsetType] = UNSET,
                              body: Union[dict, None, UnsetType] = UNSET) -> Any:
        """3rd Party AppSec Collector

        POST /public_api/appsec/v1/collectors/{collectorId}
        Available in Cortex XDR 5.x.
        Returns the complete JSON response, bytes for downloads, or None for an empty response.
        Omit optional fields with UNSET; explicit None is sent as JSON null.
        :param collector_id: path field collectorId.
        :param repository_id: query field repository_id.
        :param repository_url: query field repository_url.
        :param branch: query field branch.
        :param body: payload field body.
        """
        self._require_versions((5,))
        body = body
        return self._operation(
            '/public_api/appsec/v1/collectors/{collectorId}', method='post',
            path_params={'collectorId': collector_id},
            query=[('repository_id', repository_id, True), ('repository_url', repository_url, True), ('branch', branch, True)],
            body=body,
        )

    def get_packages(self, *,
                     name: str,
                     version: str,
                     manager: Union[str, None, UnsetType] = UNSET) -> Any:
        """Get Package Version Details

        GET /public_api/appsec/v1/package_explorer/packages/{name}/versions/{version}
        Available in Cortex XDR 5.x.
        Returns the complete JSON response, bytes for downloads, or None for an empty response.
        Omit optional fields with UNSET; explicit None is sent as JSON null.
        The vendor path has a stray "/get " prefix; this method removes that prefix.
        This route correction still needs confirmation against a live tenant.
        :param name: path field name.
        :param version: path field version.
        :param manager: query field manager.
        """
        self._require_versions((5,))
        body = UNSET
        return self._operation(
            '/public_api/appsec/v1/package_explorer/packages/{name}/versions/{version}', method='get',
            path_params={'name': name, 'version': version},
            query=[('manager', manager, True)],
            body=body,
        )

    def get_coverage(self, *,
                     direction: str,
                     type: str,
                     only_onboarded: Union[bool, None, UnsetType] = UNSET,
                     application: Union[str, None, UnsetType] = UNSET,
                     provider: Union[str, None, UnsetType] = UNSET) -> Any:
        """Get Code-to-Cloud Coverage Ratio

        GET /public_api/appsec/v1/code-to-cloud/coverage
        Available in Cortex XDR 5.x.
        Returns the complete JSON response, bytes for downloads, or None for an empty response.
        Omit optional fields with UNSET; explicit None is sent as JSON null.
        :param direction: query field direction.
        :param type: query field type.
        :param only_onboarded: query field only_onboarded.
        :param application: query field application.
        :param provider: query field provider.
        """
        self._require_versions((5,))
        body = UNSET
        return self._operation(
            '/public_api/appsec/v1/code-to-cloud/coverage', method='get',
            query=[('direction', direction, True), ('type', type, True), ('only_onboarded', only_onboarded, True), ('application', application, True), ('provider', provider, True)],
            body=body,
        )
