"""Explicit operations from the pinned Cortex XDR documentation snapshot."""
from typing import Any, Tuple, Union

from cortex_xdr_client.api.operation import UNSET, UnsetType
from cortex_xdr_client.api.authentication import Authentication
from cortex_xdr_client.api.base_api import BaseAPI
from cortex_xdr_client.api.version import APIVersion


class CloudOnboardingAPI(BaseAPI):
    def __init__(self, auth: Authentication, fqdn: str, timeout: Tuple[int, int],
                 api_version: APIVersion = APIVersion.V3) -> None:
        super(CloudOnboardingAPI, self).__init__(auth, fqdn, 'cloud_onboarding', timeout, api_version)

    def post_get_accounts(self, *,
            instance_id: str,
            filter_data: Union[dict, None, UnsetType] = UNSET) -> Any:
        """Get accounts in the specified cloud instances

        POST /public_api/v1/cloud_onboarding/get_accounts
        Available in Cortex XDR 5.x.
        Returns the complete JSON response, text, bytes, or None for an empty response.
        Optional fields use UNSET for omission; None is explicit null.
        The source snapshot records this operation and its parameter schema.
        :param instance_id: body field instance_id.
        :param filter_data: body field filter_data.
        """
        self._require_versions((5,))
        body = self._values({'instance_id': instance_id, 'filter_data': filter_data})
        body = {'request_data': body}
        return self._operation(
            '/public_api/v1/cloud_onboarding/get_accounts', method='post',
            body=body,
        )

    def post_enable_disable_account(self, *, enable: bool, ids: list, instance_id: str) -> Any:
        """Enable or disable cloud accounts

        POST /public_api/v1/cloud_onboarding/enable_disable_account
        Available in Cortex XDR 5.x.
        Returns the complete JSON response, text, bytes, or None for an empty response.
        Optional fields use UNSET for omission; None is explicit null.
        The source snapshot records this operation and its parameter schema.
        :param enable: body field enable.
        :param ids: body field ids.
        :param instance_id: body field instance_id.
        """
        self._require_versions((5,))
        body = self._values({'enable': enable, 'ids': ids, 'instance_id': instance_id})
        body = {'request_data': body}
        return self._operation(
            '/public_api/v1/cloud_onboarding/enable_disable_account', method='post',
            body=body,
        )

    def post_create_instance_template(self, *,
            additional_capabilities: dict,
            cloud_provider: str,
            collection_configuration: dict,
            custom_resources_tags: list,
            scan_mode: str,
            scope: str,
            scope_modifications: dict,
            account_details: Union[dict, None, UnsetType] = UNSET,
            cloud_partition: Union[Any, None, UnsetType] = UNSET,
            gcp_workspace: Union[dict, None, UnsetType] = UNSET,
            instance_name: Union[str, None, UnsetType] = UNSET,
            scan_env_id: Union[str, None, UnsetType] = UNSET) -> Any:
        """Create a cloud onboarding integration template

        POST /public_api/v1/cloud_onboarding/create_instance_template
        Available in Cortex XDR 5.x.
        Returns the complete JSON response, text, bytes, or None for an empty response.
        Optional fields use UNSET for omission; None is explicit null.
        The source snapshot records this operation and its parameter schema.
        :param additional_capabilities: body field additional_capabilities.
        :param cloud_provider: body field cloud_provider.
        :param collection_configuration: body field collection_configuration.
        :param custom_resources_tags: body field custom_resources_tags.
        :param scan_mode: body field scan_mode.
        :param scope: body field scope.
        :param scope_modifications: body field scope_modifications.
        :param account_details: body field account_details.
        :param cloud_partition: body field cloud_partition.
        :param gcp_workspace: body field gcp_workspace.
        :param instance_name: body field instance_name.
        :param scan_env_id: body field scan_env_id.
        """
        self._require_versions((5,))
        body = self._values({
            'additional_capabilities': additional_capabilities,
            'cloud_provider': cloud_provider,
            'collection_configuration': collection_configuration,
            'custom_resources_tags': custom_resources_tags,
            'scan_mode': scan_mode,
            'scope': scope,
            'scope_modifications': scope_modifications,
            'account_details': account_details,
            'cloud_partition': cloud_partition,
            'gcp_workspace': gcp_workspace,
            'instance_name': instance_name,
            'scan_env_id': scan_env_id,
        })
        body = {'request_data': body}
        return self._operation(
            '/public_api/v1/cloud_onboarding/create_instance_template', method='post',
            body=body,
        )

    def post_get_instance_details(self, *, id: str) -> Any:
        """Get cloud instance details

        POST /public_api/v1/cloud_onboarding/get_instance_details
        Available in Cortex XDR 5.x.
        Returns the complete JSON response, text, bytes, or None for an empty response.
        Optional fields use UNSET for omission; None is explicit null.
        The source snapshot records this operation and its parameter schema.
        :param id: body field id.
        """
        self._require_versions((5,))
        body = self._values({'id': id})
        body = {'request_data': body}
        return self._operation(
            '/public_api/v1/cloud_onboarding/get_instance_details', method='post',
            body=body,
        )

    def post_get_instances(self, *, filter_data: Union[dict, None, UnsetType] = UNSET) -> Any:
        """Get all or filtered cloud instances

        POST /public_api/v1/cloud_onboarding/get_instances
        Available in Cortex XDR 5.x.
        Returns the complete JSON response, text, bytes, or None for an empty response.
        Optional fields use UNSET for omission; None is explicit null.
        The source snapshot records this operation and its parameter schema.
        :param filter_data: body field filter_data.
        """
        self._require_versions((5,))
        body = self._values({'filter_data': filter_data})
        body = {'request_data': body}
        return self._operation(
            '/public_api/v1/cloud_onboarding/get_instances', method='post',
            body=body,
        )

    def post_edit_instance(self, *,
            cloud_provider: str,
            custom_resources_tags: list,
            id: str,
            instance_name: str,
            scan_env_id: str,
            scope_modifications: dict,
            additional_capabilities: Union[dict, None, UnsetType] = UNSET,
            collection_configuration: Union[dict, None, UnsetType] = UNSET,
            gcp_workspace: Union[dict, None, UnsetType] = UNSET) -> Any:
        """Edit a cloud instance

        POST /public_api/v1/cloud_onboarding/edit_instance
        Available in Cortex XDR 5.x.
        Returns the complete JSON response, text, bytes, or None for an empty response.
        Optional fields use UNSET for omission; None is explicit null.
        The source snapshot records this operation and its parameter schema.
        :param cloud_provider: body field cloud_provider.
        :param custom_resources_tags: body field custom_resources_tags.
        :param id: body field id.
        :param instance_name: body field instance_name.
        :param scan_env_id: body field scan_env_id.
        :param scope_modifications: body field scope_modifications.
        :param additional_capabilities: body field additional_capabilities.
        :param collection_configuration: body field collection_configuration.
        :param gcp_workspace: body field gcp_workspace.
        """
        self._require_versions((5,))
        body = self._values({
            'cloud_provider': cloud_provider,
            'custom_resources_tags': custom_resources_tags,
            'id': id,
            'instance_name': instance_name,
            'scan_env_id': scan_env_id,
            'scope_modifications': scope_modifications,
            'additional_capabilities': additional_capabilities,
            'collection_configuration': collection_configuration,
            'gcp_workspace': gcp_workspace,
        })
        body = {'request_data': body}
        return self._operation(
            '/public_api/v1/cloud_onboarding/edit_instance', method='post',
            body=body,
        )

    def post_enable_disable_instance(self, *, enable: bool, ids: list) -> Any:
        """Enable or disable cloud instances

        POST /public_api/v1/cloud_onboarding/enable_disable_instance
        Available in Cortex XDR 5.x.
        Returns the complete JSON response, text, bytes, or None for an empty response.
        Optional fields use UNSET for omission; None is explicit null.
        The source snapshot records this operation and its parameter schema.
        :param enable: body field enable.
        :param ids: body field ids.
        """
        self._require_versions((5,))
        body = self._values({'enable': enable, 'ids': ids})
        body = {'request_data': body}
        return self._operation(
            '/public_api/v1/cloud_onboarding/enable_disable_instance', method='post',
            body=body,
        )

    def post_delete_instance(self, *, ids: list) -> Any:
        """Delete the specified cloud instances

        POST /public_api/v1/cloud_onboarding/delete_instance
        Available in Cortex XDR 5.x.
        Returns the complete JSON response, text, bytes, or None for an empty response.
        Optional fields use UNSET for omission; None is explicit null.
        The source snapshot records this operation and its parameter schema.
        :param ids: body field ids.
        """
        self._require_versions((5,))
        body = self._values({'ids': ids})
        body = {'request_data': body}
        return self._operation(
            '/public_api/v1/cloud_onboarding/delete_instance', method='post',
            body=body,
        )

    def get_identifier_roles_for_cloud_instance(self, *,
            cloud_provider: str,
            instance_id: str) -> Any:
        """Get identifier roles for cloud instance

        POST /public_api/v1/cloud_onboarding/get_identifiers
        Available in Cortex XDR 5.x.
        Returns the complete JSON response, text, bytes, or None for an empty response.
        Optional fields use UNSET for omission; None is explicit null.
        The source snapshot records this operation and its parameter schema.
        :param cloud_provider: body field cloud_provider.
        :param instance_id: body field instance_id.
        """
        self._require_versions((5,))
        body = self._values({'cloud_provider': cloud_provider, 'instance_id': instance_id})
        return self._operation(
            '/public_api/v1/cloud_onboarding/get_identifiers', method='post',
            body=body,
        )

    def post_list_regions(self, *,
            cloud_partition: Union[Any, None, UnsetType] = UNSET,
            cloud_provider: Union[str, None, UnsetType] = UNSET) -> Any:
        """Get available regions for a CSP

        POST /public_api/v1/cloud_onboarding/list_regions
        Available in Cortex XDR 5.x.
        Returns the complete JSON response, text, bytes, or None for an empty response.
        Optional fields use UNSET for omission; None is explicit null.
        The source snapshot records this operation and its parameter schema.
        :param cloud_partition: body field cloud_partition.
        :param cloud_provider: body field cloud_provider.
        """
        self._require_versions((5,))
        body = self._values({'cloud_partition': cloud_partition, 'cloud_provider': cloud_provider})
        body = {'request_data': body}
        return self._operation(
            '/public_api/v1/cloud_onboarding/list_regions', method='post',
            body=body,
        )

    def post_get_azure_approved_tenants(self, *,
            cloud_partition: Union[Any, None, UnsetType] = UNSET) -> Any:
        """Get approved Azure tenants

        POST /public_api/v1/cloud_onboarding/get_azure_approved_tenants
        Available in Cortex XDR 5.x.
        Returns the complete JSON response, text, bytes, or None for an empty response.
        Optional fields use UNSET for omission; None is explicit null.
        The source snapshot records this operation and its parameter schema.
        :param cloud_partition: body field cloud_partition.
        """
        self._require_versions((5,))
        body = self._values({'cloud_partition': cloud_partition})
        body = {'request_data': body}
        return self._operation(
            '/public_api/v1/cloud_onboarding/get_azure_approved_tenants', method='post',
            body=body,
        )

    def post_create_outpost_template(self, *,
            cloud_provider: str,
            custom_resources_tags: list,
            app_registration_mode: Union[str, None, UnsetType] = UNSET,
            cloud_partition: Union[str, None, UnsetType] = UNSET,
            customer_app_client_id: Union[str, None, UnsetType] = UNSET,
            customer_sp_object_id: Union[str, None, UnsetType] = UNSET,
            customer_uami_agentless_id: Union[str, None, UnsetType] = UNSET,
            customer_uami_dspm_id: Union[str, None, UnsetType] = UNSET,
            customer_uami_proxy_id: Union[str, None, UnsetType] = UNSET,
            customer_uami_registry_id: Union[str, None, UnsetType] = UNSET,
            customer_uami_serverless_id: Union[str, None, UnsetType] = UNSET,
            instance_name: Union[str, None, UnsetType] = UNSET,
            uami_mode: Union[str, None, UnsetType] = UNSET) -> Any:
        """Create an outpost template

        POST /public_api/v1/cloud_onboarding/create_outpost_template
        Available in Cortex XDR 5.x.
        Returns the complete JSON response, text, bytes, or None for an empty response.
        Optional fields use UNSET for omission; None is explicit null.
        The source snapshot records this operation and its parameter schema.
        :param cloud_provider: body field cloud_provider.
        :param custom_resources_tags: body field custom_resources_tags.
        :param app_registration_mode: body field app_registration_mode.
        :param cloud_partition: body field cloud_partition.
        :param customer_app_client_id: body field customer_app_client_id.
        :param customer_sp_object_id: body field customer_sp_object_id.
        :param customer_uami_agentless_id: body field customer_uami_agentless_id.
        :param customer_uami_dspm_id: body field customer_uami_dspm_id.
        :param customer_uami_proxy_id: body field customer_uami_proxy_id.
        :param customer_uami_registry_id: body field customer_uami_registry_id.
        :param customer_uami_serverless_id: body field customer_uami_serverless_id.
        :param instance_name: body field instance_name.
        :param uami_mode: body field uami_mode.
        """
        self._require_versions((5,))
        body = self._values({
            'cloud_provider': cloud_provider,
            'custom_resources_tags': custom_resources_tags,
            'app_registration_mode': app_registration_mode,
            'cloud_partition': cloud_partition,
            'customer_app_client_id': customer_app_client_id,
            'customer_sp_object_id': customer_sp_object_id,
            'customer_uami_agentless_id': customer_uami_agentless_id,
            'customer_uami_dspm_id': customer_uami_dspm_id,
            'customer_uami_proxy_id': customer_uami_proxy_id,
            'customer_uami_registry_id': customer_uami_registry_id,
            'customer_uami_serverless_id': customer_uami_serverless_id,
            'instance_name': instance_name,
            'uami_mode': uami_mode,
        })
        body = {'request_data': body}
        return self._operation(
            '/public_api/v1/cloud_onboarding/create_outpost_template', method='post',
            body=body,
        )

    def post_edit_outpost(self, *,
            custom_resources_tags: Union[list, None, UnsetType] = UNSET,
            id: Union[str, None, UnsetType] = UNSET) -> Any:
        """Edit an outpost

        POST /public_api/v1/cloud_onboarding/edit_outpost
        Available in Cortex XDR 5.x.
        Returns the complete JSON response, text, bytes, or None for an empty response.
        Optional fields use UNSET for omission; None is explicit null.
        The source snapshot records this operation and its parameter schema.
        :param custom_resources_tags: body field custom_resources_tags.
        :param id: body field id.
        """
        self._require_versions((5,))
        body = self._values({'custom_resources_tags': custom_resources_tags, 'id': id})
        body = {'request_data': body}
        return self._operation(
            '/public_api/v1/cloud_onboarding/edit_outpost', method='post',
            body=body,
        )

    def post_get_outposts(self, *, filter_data: Union[dict, None, UnsetType] = UNSET) -> Any:
        """Get all or filtered outposts

        POST /public_api/v1/cloud_onboarding/get_outposts
        Available in Cortex XDR 5.x.
        Returns the complete JSON response, text, bytes, or None for an empty response.
        Optional fields use UNSET for omission; None is explicit null.
        The source snapshot records this operation and its parameter schema.
        :param filter_data: body field filter_data.
        """
        self._require_versions((5,))
        body = self._values({'filter_data': filter_data})
        body = {'request_data': body}
        return self._operation(
            '/public_api/v1/cloud_onboarding/get_outposts', method='post',
            body=body,
        )
