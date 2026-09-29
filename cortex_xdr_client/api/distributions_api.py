from typing import Any, List, Tuple, Union

from cortex_xdr_client.api.operation import UNSET, UnsetType

from cortex_xdr_client.api.authentication import Authentication
from cortex_xdr_client.api.base_api import BaseAPI
from cortex_xdr_client.api.version import APIVersion


class DistributionsAPI(BaseAPI):
    def __init__(self, auth: Authentication, fqdn: str, timeout: Tuple[int, int],
                 api_version: APIVersion = APIVersion.V3) -> None:
        super(DistributionsAPI, self).__init__(auth, fqdn, 'distributions', timeout, api_version)

    def get_versions(self, *,
                     accept_encoding: Union[str, None, UnsetType] = UNSET,
                     body: Union[dict, None, UnsetType] = UNSET) -> Any:
        """Get Distribution version

        POST /public_api/v1/distributions/get_versions
        Available in Cortex XDR 3.x, 5.x.
        Returns the complete JSON response, bytes for downloads, or None for an empty response.
        Omit optional fields with UNSET; explicit None is sent as JSON null.
        :param accept_encoding: header field Accept-Encoding.
        :param body: payload field body.
        """
        self._require_versions((3, 5))
        if self._api_version == APIVersion.V3:
            body = body
            return self._operation(
                '/public_api/v1/distributions/get_versions', method='post',
                headers={'Accept-Encoding': accept_encoding},
                body=body,
            )
        elif self._api_version == APIVersion.V5:
            self._reject_fields(accept_encoding=accept_encoding)
            body = body
            return self._operation(
                '/public_api/v1/distributions/get_versions', method='post',
                body=body,
            )

    def create(self, *,
               name: Union[str, None, UnsetType] = UNSET,
               platform: Union[str, None, UnsetType] = UNSET,
               package_type: Union[str, None, UnsetType] = UNSET,
               agent_version: Union[str, None, UnsetType] = UNSET,
               windows_version: Union[str, None, UnsetType] = UNSET,
               linux_version: Union[str, None, UnsetType] = UNSET,
               macos_version: Union[str, None, UnsetType] = UNSET,
               deployment_platform: Union[str, None, UnsetType] = UNSET,
               default_namespace: Union[str, None, UnsetType] = UNSET,
               node_selector: Union[dict, None, UnsetType] = UNSET,
               proxy: Union[List[str], None, UnsetType] = UNSET,
               cluster_name: Union[str, None, UnsetType] = UNSET,
               run_on_master_node: Union[bool, None, UnsetType] = UNSET,
               run_on_all_nodes: Union[bool, None, UnsetType] = UNSET,
               description: Union[str, None, UnsetType] = UNSET,
               endpoint_tags: Union[List[str], None, UnsetType] = UNSET,
               yaml_preferences: Union[dict, None, UnsetType] = UNSET) -> Any:
        """Create distributions

        POST /public_api/v1/distributions/create
        Available in Cortex XDR 3.x, 5.x.
        Returns the complete JSON response, bytes for downloads, or None for an empty response.
        Omit optional fields with UNSET; explicit None is sent as JSON null.
        :param name: body field name.
        :param platform: body field platform.
        :param package_type: body field package_type.
        :param agent_version: body field agent_version.
        :param windows_version: body field windows_version.
        :param linux_version: body field linux_version.
        :param macos_version: body field macos_version.
        :param deployment_platform: body field deployment_platform.
        :param default_namespace: body field default_namespace.
        :param node_selector: body field node_selector.
        :param proxy: body field proxy.
        :param cluster_name: body field cluster_name.
        :param run_on_master_node: body field run_on_master_node.
        :param run_on_all_nodes: body field run_on_all_nodes.
        :param description: body field description.
        :param endpoint_tags: body field endpoint_tags.
        :param yaml_preferences: body field yaml_preferences.
        """
        self._require_versions((3, 5))
        if self._api_version == APIVersion.V3:
            self._reject_fields(description=description, endpoint_tags=endpoint_tags, yaml_preferences=yaml_preferences)
            body = self._values({'name': name, 'platform': platform, 'package_type': package_type, 'agent_version': agent_version, 'windows_version': windows_version, 'linux_version': linux_version, 'macos_version': macos_version, 'deployment_platform': deployment_platform, 'default_namespace': default_namespace, 'node_selector': node_selector, 'proxy': proxy, 'cluster_name': cluster_name, 'run_on_master_node': run_on_master_node, 'run_on_all_nodes': run_on_all_nodes})
            body = self._values({'request_data': body, **{}})
            return self._operation(
                '/public_api/v1/distributions/create', method='post',
                body=body,
            )
        elif self._api_version == APIVersion.V5:
            body = self._values({'name': name, 'platform': platform, 'package_type': package_type, 'agent_version': agent_version, 'windows_version': windows_version, 'linux_version': linux_version, 'macos_version': macos_version, 'deployment_platform': deployment_platform, 'default_namespace': default_namespace, 'node_selector': node_selector, 'proxy': proxy, 'cluster_name': cluster_name, 'run_on_master_node': run_on_master_node, 'run_on_all_nodes': run_on_all_nodes, 'description': description, 'endpoint_tags': endpoint_tags, 'yaml_preferences': yaml_preferences})
            body = self._values({'request_data': body, **{}})
            return self._operation(
                '/public_api/v1/distributions/create', method='post',
                body=body,
            )

    def get_status(self, *,
                   accept_encoding: Union[str, None, UnsetType] = UNSET,
                   distribution_id: Union[str, None, UnsetType] = UNSET) -> Any:
        """Get Distribution status

        POST /public_api/v1/distributions/get_status
        Available in Cortex XDR 3.x, 5.x.
        Returns the complete JSON response, bytes for downloads, or None for an empty response.
        Omit optional fields with UNSET; explicit None is sent as JSON null.
        :param accept_encoding: header field Accept-Encoding.
        :param distribution_id: body field distribution_id.
        """
        self._require_versions((3, 5))
        if self._api_version == APIVersion.V3:
            body = self._values({'distribution_id': distribution_id})
            body = self._values({'request_data': body, **{}})
            return self._operation(
                '/public_api/v1/distributions/get_status', method='post',
                headers={'Accept-Encoding': accept_encoding},
                body=body,
            )
        elif self._api_version == APIVersion.V5:
            self._reject_fields(accept_encoding=accept_encoding)
            body = self._values({'distribution_id': distribution_id})
            body = self._values({'request_data': body, **{}})
            return self._operation(
                '/public_api/v1/distributions/get_status', method='post',
                body=body,
            )

    def get_dist_url(self, *,
                     accept_encoding: Union[str, None, UnsetType] = UNSET,
                     distribution_id: Union[str, None, UnsetType] = UNSET,
                     package_type: Union[str, None, UnsetType] = UNSET) -> Any:
        """Get Distribution URL

        POST /public_api/v1/distributions/get_dist_url
        Available in Cortex XDR 3.x, 5.x.
        Returns the complete JSON response, bytes for downloads, or None for an empty response.
        Omit optional fields with UNSET; explicit None is sent as JSON null.
        :param accept_encoding: header field Accept-Encoding.
        :param distribution_id: body field distribution_id.
        :param package_type: body field package_type.
        """
        self._require_versions((3, 5))
        if self._api_version == APIVersion.V3:
            body = self._values({'distribution_id': distribution_id, 'package_type': package_type})
            body = self._values({'request_data': body, **{}})
            return self._operation(
                '/public_api/v1/distributions/get_dist_url', method='post',
                headers={'Accept-Encoding': accept_encoding},
                body=body,
            )
        elif self._api_version == APIVersion.V5:
            self._reject_fields(accept_encoding=accept_encoding)
            body = self._values({'distribution_id': distribution_id, 'package_type': package_type})
            body = self._values({'request_data': body, **{}})
            return self._operation(
                '/public_api/v1/distributions/get_dist_url', method='post',
                body=body,
            )

    def get_distributions(self, *,
                          search_from: Union[int, None, UnsetType] = UNSET,
                          search_to: Union[int, None, UnsetType] = UNSET,
                          sort: Union[dict, None, UnsetType] = UNSET,
                          filters: Union[List[dict], None, UnsetType] = UNSET) -> Any:
        """Get Distributions

        POST /public_api/v1/distributions/get_distributions
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
                '/public_api/v1/distributions/get_distributions', method='post',
                body=body,
            )
        elif self._api_version == APIVersion.V5:
            body = self._values({'search_from': search_from, 'search_to': search_to, 'sort': sort, 'filters': filters})
            body = self._values({'request_data': body, **{}})
            return self._operation(
                '/public_api/v1/distributions/get_distributions', method='post',
                body=body,
            )

    def delete(self, *,
               distribution_id: Union[str, None, UnsetType] = UNSET) -> Any:
        """Delete agent installation packages

        POST /public_api/v1/distributions/delete
        Available in Cortex XDR 3.x, 5.x.
        Returns the complete JSON response, bytes for downloads, or None for an empty response.
        Omit optional fields with UNSET; explicit None is sent as JSON null.
        :param distribution_id: body field distribution_id.
        """
        self._require_versions((3, 5))
        if self._api_version == APIVersion.V3:
            body = self._values({'distribution_id': distribution_id})
            body = self._values({'request_data': body, **{}})
            return self._operation(
                '/public_api/v1/distributions/delete', method='post',
                body=body,
            )
        elif self._api_version == APIVersion.V5:
            body = self._values({'distribution_id': distribution_id})
            body = self._values({'request_data': body, **{}})
            return self._operation(
                '/public_api/v1/distributions/delete', method='post',
                body=body,
            )
