from typing import Any, List, Tuple, Union

from cortex_xdr_client.api.operation import UNSET, UnsetType

from cortex_xdr_client.api.authentication import Authentication
from cortex_xdr_client.api.base_api import BaseAPI
from cortex_xdr_client.api.version import APIVersion


class BrokersAPI(BaseAPI):
    def __init__(self, auth: Authentication, fqdn: str, timeout: Tuple[int, int],
                 api_version: APIVersion = APIVersion.V3) -> None:
        super(BrokersAPI, self).__init__(auth, fqdn, 'brokers', timeout, api_version)

    def get_brokers(self, *,
                    id: Union[List[str], None, UnsetType] = UNSET,
                    name: Union[List[str], None, UnsetType] = UNSET) -> Any:
        """List registered Broker VMs

        GET /public_api/v1/brokers/
        Available in Cortex XDR 3.x.
        Returns the complete JSON response, bytes for downloads, or None for an empty response.
        Omit optional fields with UNSET; explicit None is sent as JSON null.
        :param id: body field id.
        :param name: body field name.
        """
        self._require_versions((3,))
        body = self._values({'id': id, 'name': name})
        return self._operation(
            '/public_api/v1/brokers/', method='get',
            body=body,
        )

    def edit_broker(self, *,
                    device_id: str,
                    name: Union[str, None, UnsetType] = UNSET,
                    fqdn: Union[str, None, UnsetType] = UNSET,
                    proxy: Union[dict, None, UnsetType] = UNSET,
                    webui_port: Union[str, None, UnsetType] = UNSET,
                    ntp: Union[List[str], None, UnsetType] = UNSET,
                    internal_network: Union[str, None, UnsetType] = UNSET,
                    auto_upgrade: Union[bool, None, UnsetType] = UNSET,
                    upgrade_window: Union[dict, None, UnsetType] = UNSET,
                    allow_monitoring: Union[bool, None, UnsetType] = UNSET,
                    ssh_enabled: Union[bool, None, UnsetType] = UNSET,
                    ssh_keys: Union[List[str], None, UnsetType] = UNSET,
                    welcome_message: Union[str, None, UnsetType] = UNSET,
                    ssl_crt: Union[str, None, UnsetType] = UNSET,
                    ssl_key: Union[str, None, UnsetType] = UNSET,
                    ssl_crt_file_name: Union[str, None, UnsetType] = UNSET,
                    ssl_key_file_name: Union[str, None, UnsetType] = UNSET,
                    custom_ca: Union[dict, None, UnsetType] = UNSET,
                    broker_ui_password: Union[str, None, UnsetType] = UNSET) -> Any:
        """Edit a Broker VM

        POST /public_api/v1/brokers/{device_id}/
        Available in Cortex XDR 3.x.
        Returns the complete JSON response, bytes for downloads, or None for an empty response.
        Omit optional fields with UNSET; explicit None is sent as JSON null.
        :param device_id: path field device_id.
        :param name: body field name.
        :param fqdn: body field fqdn.
        :param proxy: body field proxy.
        :param webui_port: body field webui_port.
        :param ntp: body field ntp.
        :param internal_network: body field internal_network.
        :param auto_upgrade: body field auto_upgrade.
        :param upgrade_window: body field upgrade_window.
        :param allow_monitoring: body field allow_monitoring.
        :param ssh_enabled: body field ssh_enabled.
        :param ssh_keys: body field ssh_keys.
        :param welcome_message: body field welcome_message.
        :param ssl_crt: body field ssl_crt.
        :param ssl_key: body field ssl_key.
        :param ssl_crt_file_name: body field ssl_crt_file_name.
        :param ssl_key_file_name: body field ssl_key_file_name.
        :param custom_ca: body field custom_ca.
        :param broker_ui_password: body field broker_ui_password.
        """
        self._require_versions((3,))
        body = self._values({'name': name, 'fqdn': fqdn, 'proxy': proxy, 'webui_port': webui_port, 'ntp': ntp, 'internal_network': internal_network, 'auto_upgrade': auto_upgrade, 'upgrade_window': upgrade_window, 'allow_monitoring': allow_monitoring, 'ssh_enabled': ssh_enabled, 'ssh_keys': ssh_keys, 'welcome_message': welcome_message, 'ssl_crt': ssl_crt, 'ssl_key': ssl_key, 'ssl_crt_file_name': ssl_crt_file_name, 'ssl_key_file_name': ssl_key_file_name, 'custom_ca': custom_ca, 'broker_ui_password': broker_ui_password})
        return self._operation(
            '/public_api/v1/brokers/{device_id}/', method='post',
            path_params={'device_id': device_id},
            body=body,
        )

    def remove_broker(self, *,
                      device_id: str) -> Any:
        """Remove a Broker VM from the tenant

        POST /public_api/v1/brokers/{device_id}/delete/
        Available in Cortex XDR 3.x.
        Returns the complete JSON response, bytes for downloads, or None for an empty response.
        Omit optional fields with UNSET; explicit None is sent as JSON null.
        :param device_id: path field device_id.
        """
        self._require_versions((3,))
        body = UNSET
        return self._operation(
            '/public_api/v1/brokers/{device_id}/delete/', method='post',
            path_params={'device_id': device_id},
            body=body,
        )

    def generate_registration_token(self) -> Any:
        """Generate a Broker VM registration token

        POST /public_api/v1/brokers/registration_token/
        Available in Cortex XDR 3.x.
        Returns the complete JSON response, bytes for downloads, or None for an empty response.
        Omit optional fields with UNSET; explicit None is sent as JSON null.
        """
        self._require_versions((3,))
        body = UNSET
        return self._operation(
            '/public_api/v1/brokers/registration_token/', method='post',
            body=body,
        )

    def reboot_broker(self, *,
                      device_id: str) -> Any:
        """Reboot a Broker VM

        POST /public_api/v1/brokers/{device_id}/reboot/
        Available in Cortex XDR 3.x.
        Returns the complete JSON response, bytes for downloads, or None for an empty response.
        Omit optional fields with UNSET; explicit None is sent as JSON null.
        :param device_id: path field device_id.
        """
        self._require_versions((3,))
        body = UNSET
        return self._operation(
            '/public_api/v1/brokers/{device_id}/reboot/', method='post',
            path_params={'device_id': device_id},
            body=body,
        )

    def shutdown_broker(self, *,
                        device_id: str) -> Any:
        """Shut down a Broker VM

        POST /public_api/v1/brokers/{device_id}/shutdown/
        Available in Cortex XDR 3.x.
        Returns the complete JSON response, bytes for downloads, or None for an empty response.
        Omit optional fields with UNSET; explicit None is sent as JSON null.
        :param device_id: path field device_id.
        """
        self._require_versions((3,))
        body = UNSET
        return self._operation(
            '/public_api/v1/brokers/{device_id}/shutdown/', method='post',
            path_params={'device_id': device_id},
            body=body,
        )

    def upgrade_broker(self, *,
                       device_id: str) -> Any:
        """Upgrade a Broker VM to the latest available version

        POST /public_api/v1/brokers/{device_id}/upgrade/
        Available in Cortex XDR 3.x.
        Returns the complete JSON response, bytes for downloads, or None for an empty response.
        Omit optional fields with UNSET; explicit None is sent as JSON null.
        :param device_id: path field device_id.
        """
        self._require_versions((3,))
        body = UNSET
        return self._operation(
            '/public_api/v1/brokers/{device_id}/upgrade/', method='post',
            path_params={'device_id': device_id},
            body=body,
        )

    def get_action_status(self, *,
                          action_id: str) -> Any:
        """Poll the status of an asynchronous broker action

        GET /public_api/v1/brokers/action_status/{action_id}/
        Available in Cortex XDR 3.x.
        Returns the complete JSON response, bytes for downloads, or None for an empty response.
        Omit optional fields with UNSET; explicit None is sent as JSON null.
        :param action_id: path field action_id.
        """
        self._require_versions((3,))
        body = UNSET
        return self._operation(
            '/public_api/v1/brokers/action_status/{action_id}/', method='get',
            path_params={'action_id': action_id},
            body=body,
        )

    def download_install_image(self, *,
                               type: Union[str, None, UnsetType] = UNSET) -> Any:
        """Get a signed URL for a Broker VM install image

        GET /public_api/v1/brokers/images/
        Available in Cortex XDR 3.x.
        Returns the complete JSON response, bytes for downloads, or None for an empty response.
        Omit optional fields with UNSET; explicit None is sent as JSON null.
        :param type: body field type.
        """
        self._require_versions((3,))
        body = self._values({'type': type})
        return self._operation(
            '/public_api/v1/brokers/images/', method='get',
            body=body,
        )

    def generate_log_bundle(self, *,
                            device_id: str) -> Any:
        """Request asynchronous log-bundle collection from a broker

        POST /public_api/v1/brokers/{device_id}/logs/generate/
        Available in Cortex XDR 3.x.
        Returns the complete JSON response, bytes for downloads, or None for an empty response.
        Omit optional fields with UNSET; explicit None is sent as JSON null.
        :param device_id: path field device_id.
        """
        self._require_versions((3,))
        body = UNSET
        return self._operation(
            '/public_api/v1/brokers/{device_id}/logs/generate/', method='post',
            path_params={'device_id': device_id},
            body=body,
        )

    def get_log_bundle_status(self, *,
                              device_id: str) -> Any:
        """Poll the status of a log-bundle request

        GET /public_api/v1/brokers/{device_id}/logs/status/
        Available in Cortex XDR 3.x.
        Returns the complete JSON response, bytes for downloads, or None for an empty response.
        Omit optional fields with UNSET; explicit None is sent as JSON null.
        :param device_id: path field device_id.
        """
        self._require_versions((3,))
        body = UNSET
        return self._operation(
            '/public_api/v1/brokers/{device_id}/logs/status/', method='get',
            path_params={'device_id': device_id},
            body=body,
        )

    def download_log_bundle(self, *,
                            device_id: str) -> Any:
        """Download the most recent log bundle for a broker

        GET /public_api/v1/brokers/{device_id}/logs/download/
        Available in Cortex XDR 3.x.
        Returns the complete JSON response, bytes for downloads, or None for an empty response.
        Omit optional fields with UNSET; explicit None is sent as JSON null.
        :param device_id: path field device_id.
        """
        self._require_versions((3,))
        body = UNSET
        return self._operation(
            '/public_api/v1/brokers/{device_id}/logs/download/', method='get',
            path_params={'device_id': device_id},
            body=body,
        )

    def get_applet(self, *,
                   device_id: str,
                   applet_name: str) -> Any:
        """Get an applet's configuration and status

        GET /public_api/v1/brokers/{device_id}/applets/{applet_name}/
        Available in Cortex XDR 3.x.
        Returns the complete JSON response, bytes for downloads, or None for an empty response.
        Omit optional fields with UNSET; explicit None is sent as JSON null.
        :param device_id: path field device_id.
        :param applet_name: path field applet_name.
        """
        self._require_versions((3,))
        body = UNSET
        return self._operation(
            '/public_api/v1/brokers/{device_id}/applets/{applet_name}/', method='get',
            path_params={'device_id': device_id, 'applet_name': applet_name},
            body=body,
        )

    def edit_applet(self, *,
                    device_id: str,
                    applet_name: str,
                    body: Union[Any, None, UnsetType] = UNSET) -> Any:
        """Edit an applet's configuration

        POST /public_api/v1/brokers/{device_id}/applets/{applet_name}/config/
        Available in Cortex XDR 3.x.
        Returns the complete JSON response, bytes for downloads, or None for an empty response.
        Omit optional fields with UNSET; explicit None is sent as JSON null.
        :param device_id: path field device_id.
        :param applet_name: path field applet_name.
        :param body: payload field body.
        """
        self._require_versions((3,))
        body = body
        return self._operation(
            '/public_api/v1/brokers/{device_id}/applets/{applet_name}/config/', method='post',
            path_params={'device_id': device_id, 'applet_name': applet_name},
            body=body,
        )

    def activate_applet(self, *,
                        device_id: str,
                        applet_name: str,
                        body: Union[Any, None, UnsetType] = UNSET) -> Any:
        """Activate an applet with a configuration

        POST /public_api/v1/brokers/{device_id}/applets/{applet_name}/activate/
        Available in Cortex XDR 3.x.
        Returns the complete JSON response, bytes for downloads, or None for an empty response.
        Omit optional fields with UNSET; explicit None is sent as JSON null.
        :param device_id: path field device_id.
        :param applet_name: path field applet_name.
        :param body: payload field body.
        """
        self._require_versions((3,))
        body = body
        return self._operation(
            '/public_api/v1/brokers/{device_id}/applets/{applet_name}/activate/', method='post',
            path_params={'device_id': device_id, 'applet_name': applet_name},
            body=body,
        )

    def deactivate_applet(self, *,
                          device_id: str,
                          applet_name: str,
                          save_config: Union[bool, None, UnsetType] = UNSET) -> Any:
        """Deactivate an applet

        POST /public_api/v1/brokers/{device_id}/applets/{applet_name}/deactivate/
        Available in Cortex XDR 3.x.
        Returns the complete JSON response, bytes for downloads, or None for an empty response.
        Omit optional fields with UNSET; explicit None is sent as JSON null.
        :param device_id: path field device_id.
        :param applet_name: path field applet_name.
        :param save_config: body field save_config.
        """
        self._require_versions((3,))
        body = self._values({'save_config': save_config})
        return self._operation(
            '/public_api/v1/brokers/{device_id}/applets/{applet_name}/deactivate/', method='post',
            path_params={'device_id': device_id, 'applet_name': applet_name},
            body=body,
        )

    def download_wef_cert(self, *,
                          device_id: str,
                          password: Union[str, None, UnsetType] = UNSET) -> Any:
        """Download the WEC/WEF client certificate as a PFX archive

        POST /public_api/v1/brokers/{device_id}/applets/wec/wef_cert/
        Available in Cortex XDR 3.x.
        Returns the complete JSON response, bytes for downloads, or None for an empty response.
        Omit optional fields with UNSET; explicit None is sent as JSON null.
        :param device_id: path field device_id.
        :param password: body field password.
        """
        self._require_versions((3,))
        body = self._values({'password': password})
        return self._operation(
            '/public_api/v1/brokers/{device_id}/applets/wec/wef_cert/', method='post',
            path_params={'device_id': device_id},
            body=body,
        )

    def network_mapper_scan_now(self, *,
                                device_id: str) -> Any:
        """Trigger an immediate Network Mapper scan

        POST /public_api/v1/brokers/{device_id}/applets/network_mapper/scan_now/
        Available in Cortex XDR 3.x.
        Returns the complete JSON response, bytes for downloads, or None for an empty response.
        Omit optional fields with UNSET; explicit None is sent as JSON null.
        :param device_id: path field device_id.
        """
        self._require_versions((3,))
        body = UNSET
        return self._operation(
            '/public_api/v1/brokers/{device_id}/applets/network_mapper/scan_now/', method='post',
            path_params={'device_id': device_id},
            body=body,
        )
