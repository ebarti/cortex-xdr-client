"""Explicit operations from the pinned Cortex XDR documentation snapshot."""
from typing import Any, Tuple, Union

from cortex_xdr_client.api.operation import UNSET, UnsetType
from cortex_xdr_client.api.authentication import Authentication
from cortex_xdr_client.api.base_api import BaseAPI
from cortex_xdr_client.api.version import APIVersion


class NetscanAPI(BaseAPI):
    def __init__(self, auth: Authentication, fqdn: str, timeout: Tuple[int, int],
                 api_version: APIVersion = APIVersion.V3) -> None:
        super(NetscanAPI, self).__init__(auth, fqdn, 'netscan', timeout, api_version)

    def public_scan_definition_run_status(self, *, id: int, fields: list, user_agent: str) -> Any:
        """Get scan run status

        GET /public_api/netscan/v1/scan/run
        Available in Cortex XDR 5.x.
        Returns the complete JSON response, text, bytes, or None for an empty response.
        Optional fields use UNSET for omission; None is explicit null.
        The source snapshot records this operation and its parameter schema.
        :param id: query field id.
        :param fields: query field fields.
        :param user_agent: header field User-Agent.
        """
        self._require_versions((5,))
        body = UNSET
        return self._operation(
            '/public_api/netscan/v1/scan/run', method='get',
            query=[('id', id, True), ('fields', fields, True)],
            headers={'User-Agent': user_agent},
            body=body,
        )

    def public_launch_scan_run(self, *,
            user_agent: str,
            definition_id: int,
            target: Union[str, None, UnsetType] = UNSET) -> Any:
        """Launch a scan run

        POST /public_api/netscan/v1/scan/run
        Available in Cortex XDR 5.x.
        Returns the complete JSON response, text, bytes, or None for an empty response.
        Optional fields use UNSET for omission; None is explicit null.
        The source snapshot records this operation and its parameter schema.
        :param user_agent: header field User-Agent.
        :param definition_id: body field definition_id.
        :param target: body field target.
        """
        self._require_versions((5,))
        body = self._values({'definition_id': definition_id, 'target': target})
        body = {'request_data': body}
        return self._operation(
            '/public_api/netscan/v1/scan/run', method='post',
            headers={'User-Agent': user_agent},
            body=body,
        )

    def public_get_scan_definition_run_status(self, *,
            id: int,
            fields: list,
            user_agent: str) -> Any:
        """Get scan run status by ID

        GET /public_api/netscan/v1/scan/run/{id}
        Available in Cortex XDR 5.x.
        Returns the complete JSON response, text, bytes, or None for an empty response.
        Optional fields use UNSET for omission; None is explicit null.
        The source snapshot records this operation and its parameter schema.
        :param id: path field id.
        :param fields: query field fields.
        :param user_agent: header field User-Agent.
        """
        self._require_versions((5,))
        body = UNSET
        return self._operation(
            '/public_api/netscan/v1/scan/run/{id}', method='get',
            path_params={'id': id},
            query=[('fields', fields, True)],
            headers={'User-Agent': user_agent},
            body=body,
        )

    def public_launch_scan_run_by_id(self, *,
            id: int,
            user_agent: str,
            definition_id: int,
            target: Union[str, None, UnsetType] = UNSET) -> Any:
        """Launch a scan run by definition ID

        POST /public_api/netscan/v1/scan/run/{id}
        Available in Cortex XDR 5.x.
        Returns the complete JSON response, text, bytes, or None for an empty response.
        Optional fields use UNSET for omission; None is explicit null.
        The source snapshot records this operation and its parameter schema.
        :param id: path field id.
        :param user_agent: header field User-Agent.
        :param definition_id: body field definition_id.
        :param target: body field target.
        """
        self._require_versions((5,))
        body = self._values({'definition_id': definition_id, 'target': target})
        body = {'request_data': body}
        return self._operation(
            '/public_api/netscan/v1/scan/run/{id}', method='post',
            path_params={'id': id},
            headers={'User-Agent': user_agent},
            body=body,
        )

    def configure_new_scan(self, *,
            user_agent: str,
            port_list_id: int,
            scan_ports: list,
            credential_ids: list,
            description: str,
            enable_report: bool,
            excluded_targets: list,
            name: str,
            network: int,
            network_scanner_ids: list,
            override_target_exclusions: bool,
            schedule_cadence: str,
            schedule_dates: list,
            schedule_days: int,
            schedule_quiet_hours: list,
            schedule_start_date: int,
            schedule_time: dict,
            schedule_timezone: str,
            target_ids: list,
            targets: list,
            vt_config_id: int,
            alive_test_methods: Union[list, None, UnsetType] = UNSET,
            alive_test_ports: Union[str, None, UnsetType] = UNSET,
            auth_port_ssh: Union[int, None, UnsetType] = UNSET,
            checks_read_timeout: Union[int, None, UnsetType] = UNSET,
            disable_cgi_cache: Union[str, None, UnsetType] = UNSET,
            disable_win_cmd_exec: Union[str, None, UnsetType] = UNSET,
            disable_wmi_search: Union[str, None, UnsetType] = UNSET,
            exclude_fragile_devices: Union[str, None, UnsetType] = UNSET,
            exclude_printers: Union[str, None, UnsetType] = UNSET,
            expand_vhosts: Union[str, None, UnsetType] = UNSET,
            max_checks: Union[int, None, UnsetType] = UNSET,
            max_hosts: Union[int, None, UnsetType] = UNSET,
            non_simult_ports: Union[str, None, UnsetType] = UNSET,
            open_sock_max_attempts: Union[int, None, UnsetType] = UNSET,
            optimize_test: Union[str, None, UnsetType] = UNSET,
            plugins_timeout: Union[int, None, UnsetType] = UNSET,
            safe_checks: Union[str, None, UnsetType] = UNSET,
            scanner_plugins_timeout: Union[int, None, UnsetType] = UNSET,
            strict_unauthenticated: Union[str, None, UnsetType] = UNSET,
            timeout_retry: Union[int, None, UnsetType] = UNSET,
            asset_groups: Union[list, None, UnsetType] = UNSET,
            definition_id: Union[int, None, UnsetType] = UNSET) -> Any:
        """Create a scan definition

        POST /public_api/netscan/v1/scan/definition
        Available in Cortex XDR 5.x.
        Returns the complete JSON response, text, bytes, or None for an empty response.
        Optional fields use UNSET for omission; None is explicit null.
        The source snapshot records this operation and its parameter schema.
        :param user_agent: header field User-Agent.
        :param port_list_id: body field port_list_id.
        :param scan_ports: body field scan_ports.
        :param credential_ids: body field credential_ids.
        :param description: body field description.
        :param enable_report: body field enable_report.
        :param excluded_targets: body field excluded_targets.
        :param name: body field name.
        :param network: body field network.
        :param network_scanner_ids: body field network_scanner_ids.
        :param override_target_exclusions: body field override_target_exclusions.
        :param schedule_cadence: body field schedule_cadence.
        :param schedule_dates: body field schedule_dates.
        :param schedule_days: body field schedule_days.
        :param schedule_quiet_hours: body field schedule_quiet_hours.
        :param schedule_start_date: body field schedule_start_date.
        :param schedule_time: body field schedule_time.
        :param schedule_timezone: body field schedule_timezone.
        :param target_ids: body field target_ids.
        :param targets: body field targets.
        :param vt_config_id: body field vt_config_id.
        :param alive_test_methods: body field alive_test_methods.
        :param alive_test_ports: body field alive_test_ports.
        :param auth_port_ssh: body field auth_port_ssh.
        :param checks_read_timeout: body field checks_read_timeout.
        :param disable_cgi_cache: body field disable_cgi_cache.
        :param disable_win_cmd_exec: body field disable_win_cmd_exec.
        :param disable_wmi_search: body field disable_wmi_search.
        :param exclude_fragile_devices: body field exclude_fragile_devices.
        :param exclude_printers: body field exclude_printers.
        :param expand_vhosts: body field expand_vhosts.
        :param max_checks: body field max_checks.
        :param max_hosts: body field max_hosts.
        :param non_simult_ports: body field non_simult_ports.
        :param open_sock_max_attempts: body field open_sock_max_attempts.
        :param optimize_test: body field optimize_test.
        :param plugins_timeout: body field plugins_timeout.
        :param safe_checks: body field safe_checks.
        :param scanner_plugins_timeout: body field scanner_plugins_timeout.
        :param strict_unauthenticated: body field strict_unauthenticated.
        :param timeout_retry: body field timeout_retry.
        :param asset_groups: body field asset_groups.
        :param definition_id: body field definition_id.
        """
        self._require_versions((5,))
        body = self._values({
            'port_list_id': port_list_id,
            'scan_ports': scan_ports,
            'credential_ids': credential_ids,
            'description': description,
            'enable_report': enable_report,
            'excluded_targets': excluded_targets,
            'name': name,
            'network': network,
            'network_scanner_ids': network_scanner_ids,
            'override_target_exclusions': override_target_exclusions,
            'schedule_cadence': schedule_cadence,
            'schedule_dates': schedule_dates,
            'schedule_days': schedule_days,
            'schedule_quiet_hours': schedule_quiet_hours,
            'schedule_start_date': schedule_start_date,
            'schedule_time': schedule_time,
            'schedule_timezone': schedule_timezone,
            'target_ids': target_ids,
            'targets': targets,
            'vt_config_id': vt_config_id,
            'alive_test_methods': alive_test_methods,
            'alive_test_ports': alive_test_ports,
            'auth_port_ssh': auth_port_ssh,
            'checks_read_timeout': checks_read_timeout,
            'disable_cgi_cache': disable_cgi_cache,
            'disable_win_cmd_exec': disable_win_cmd_exec,
            'disable_wmi_search': disable_wmi_search,
            'exclude_fragile_devices': exclude_fragile_devices,
            'exclude_printers': exclude_printers,
            'expand_vhosts': expand_vhosts,
            'max_checks': max_checks,
            'max_hosts': max_hosts,
            'non_simult_ports': non_simult_ports,
            'open_sock_max_attempts': open_sock_max_attempts,
            'optimize_test': optimize_test,
            'plugins_timeout': plugins_timeout,
            'safe_checks': safe_checks,
            'scanner_plugins_timeout': scanner_plugins_timeout,
            'strict_unauthenticated': strict_unauthenticated,
            'timeout_retry': timeout_retry,
            'asset_groups': asset_groups,
            'definition_id': definition_id,
        })
        return self._operation(
            '/public_api/netscan/v1/scan/definition', method='post',
            headers={'User-Agent': user_agent},
            body=body,
        )

    def public_scan_definition_run_action(self, *, id: int, user_agent: str, type: str) -> Any:
        """Send a command to a running scan

        POST /public_api/netscan/v1/scan/run/{id}/command
        Available in Cortex XDR 5.x.
        Returns the complete JSON response, text, bytes, or None for an empty response.
        Optional fields use UNSET for omission; None is explicit null.
        The source snapshot records this operation and its parameter schema.
        :param id: path field id.
        :param user_agent: header field User-Agent.
        :param type: body field type.
        """
        self._require_versions((5,))
        body = self._values({'type': type})
        body = {'request_data': body}
        return self._operation(
            '/public_api/netscan/v1/scan/run/{id}/command', method='post',
            path_params={'id': id},
            headers={'User-Agent': user_agent},
            body=body,
        )
