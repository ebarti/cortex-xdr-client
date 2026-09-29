from typing import Any, List, Tuple, Union

from cortex_xdr_client.api.operation import UNSET, UnsetType

from cortex_xdr_client.api.authentication import Authentication
from cortex_xdr_client.api.base_api import BaseAPI
from cortex_xdr_client.api.version import APIVersion


class AgentConfigurationsAPI(BaseAPI):
    def __init__(self, auth: Authentication, fqdn: str, timeout: Tuple[int, int],
                 api_version: APIVersion = APIVersion.V3) -> None:
        super(AgentConfigurationsAPI, self).__init__(auth, fqdn, 'agent_configurations', timeout, api_version)

    def get_content_management(self) -> Any:
        """Retrieve content management settings

        POST /public_api/v1/configurations/agent/content_management
        Available in Cortex XDR 5.x.
        Returns the complete JSON response, bytes for downloads, or None for an empty response.
        Omit optional fields with UNSET; explicit None is sent as JSON null.
        """
        self._require_versions((5,))
        body = UNSET
        return self._operation(
            '/public_api/v1/configurations/agent/content_management', method='post',
            body=body,
        )

    def set_content_management(self, *,
                               enable_bandwidth_control: Union[bool, None, UnsetType] = UNSET,
                               bandwidth_in_mbps: Union[int, None, UnsetType] = UNSET,
                               enable_minor_content_version_updates: Union[bool, None, UnsetType] = UNSET) -> Any:
        """Update content management settings

        POST /public_api/v1/configurations/agent/content_management/set
        Available in Cortex XDR 5.x.
        Returns the complete JSON response, bytes for downloads, or None for an empty response.
        Omit optional fields with UNSET; explicit None is sent as JSON null.
        :param enable_bandwidth_control: body field enable_bandwidth_control.
        :param bandwidth_in_mbps: body field bandwidth_in_mbps.
        :param enable_minor_content_version_updates: body field enable_minor_content_version_updates.
        """
        self._require_versions((5,))
        body = self._values({'enable_bandwidth_control': enable_bandwidth_control, 'bandwidth_in_mbps': bandwidth_in_mbps, 'enable_minor_content_version_updates': enable_minor_content_version_updates})
        body = self._values({'request_data': body, **{}})
        return self._operation(
            '/public_api/v1/configurations/agent/content_management/set', method='post',
            body=body,
        )

    def get_agent_status(self) -> Any:
        """Retrieve agent status configurations

        POST /public_api/v1/configurations/agent/agent_status
        Available in Cortex XDR 5.x.
        Returns the complete JSON response, bytes for downloads, or None for an empty response.
        Omit optional fields with UNSET; explicit None is sent as JSON null.
        """
        self._require_versions((5,))
        body = UNSET
        return self._operation(
            '/public_api/v1/configurations/agent/agent_status', method='post',
            body=body,
        )

    def set_agent_status(self, *,
                         license_revocation_after_lost_connection: Union[int, None, UnsetType] = UNSET,
                         agent_deletion_retention: Union[int, None, UnsetType] = UNSET) -> Any:
        """Update the Agent license revocation and deletion period.

        POST /public_api/v1/configurations/agent/agent_status/set
        Available in Cortex XDR 5.x.
        Returns the complete JSON response, bytes for downloads, or None for an empty response.
        Omit optional fields with UNSET; explicit None is sent as JSON null.
        :param license_revocation_after_lost_connection: body field license_revocation_after_lost_connection.
        :param agent_deletion_retention: body field agent_deletion_retention.
        """
        self._require_versions((5,))
        body = self._values({'license_revocation_after_lost_connection': license_revocation_after_lost_connection, 'agent_deletion_retention': agent_deletion_retention})
        body = self._values({'request_data': body, **{}})
        return self._operation(
            '/public_api/v1/configurations/agent/agent_status/set', method='post',
            body=body,
        )

    def get_agent_auto_upgrade(self) -> Any:
        """Retrieve agent auto-upgrade settings

        POST /public_api/v1/configurations/agent/auto_upgrade
        Available in Cortex XDR 5.x.
        Returns the complete JSON response, bytes for downloads, or None for an empty response.
        Omit optional fields with UNSET; explicit None is sent as JSON null.
        """
        self._require_versions((5,))
        body = UNSET
        return self._operation(
            '/public_api/v1/configurations/agent/auto_upgrade', method='post',
            body=body,
        )

    def set_agent_auto_upgrade(self, *,
                               amount_of_parallel_upgrades: Union[int, None, UnsetType] = UNSET) -> Any:
        """Update agent auto-upgrade settings

        POST /public_api/v1/configurations/agent/auto_upgrade/set
        Available in Cortex XDR 5.x.
        Returns the complete JSON response, bytes for downloads, or None for an empty response.
        Omit optional fields with UNSET; explicit None is sent as JSON null.
        :param amount_of_parallel_upgrades: body field amount_of_parallel_upgrades.
        """
        self._require_versions((5,))
        body = self._values({'amount_of_parallel_upgrades': amount_of_parallel_upgrades})
        body = self._values({'request_data': body, **{}})
        return self._operation(
            '/public_api/v1/configurations/agent/auto_upgrade/set', method='post',
            body=body,
        )

    def get_wildfire_analysis(self) -> Any:
        """Retrieve WildFire analysis settings

        POST /public_api/v1/configurations/agent/wildfire_analysis
        Available in Cortex XDR 5.x.
        Returns the complete JSON response, bytes for downloads, or None for an empty response.
        Omit optional fields with UNSET; explicit None is sent as JSON null.
        """
        self._require_versions((5,))
        body = UNSET
        return self._operation(
            '/public_api/v1/configurations/agent/wildfire_analysis', method='post',
            body=body,
        )

    def set_wildfire_analysis(self, *,
                              enable_wildfire_analysis_scoring_for_benign_verdicts: Union[bool, None, UnsetType] = UNSET) -> Any:
        """Update WildFire analysis settings

        POST /public_api/v1/configurations/agent/wildfire_analysis/set
        Available in Cortex XDR 5.x.
        Returns the complete JSON response, bytes for downloads, or None for an empty response.
        Omit optional fields with UNSET; explicit None is sent as JSON null.
        :param enable_wildfire_analysis_scoring_for_benign_verdicts: body field enable_wildfire_analysis_scoring_for_benign_verdicts.
        """
        self._require_versions((5,))
        body = self._values({'enable_wildfire_analysis_scoring_for_benign_verdicts': enable_wildfire_analysis_scoring_for_benign_verdicts})
        body = self._values({'request_data': body, **{}})
        return self._operation(
            '/public_api/v1/configurations/agent/wildfire_analysis/set', method='post',
            body=body,
        )

    def get_informative_btp_issues(self) -> Any:
        """Retrieve informative BTP issues settings

        POST /public_api/v1/configurations/agent/informative_btp_issues
        Available in Cortex XDR 5.x.
        Returns the complete JSON response, bytes for downloads, or None for an empty response.
        Omit optional fields with UNSET; explicit None is sent as JSON null.
        """
        self._require_versions((5,))
        body = UNSET
        return self._operation(
            '/public_api/v1/configurations/agent/informative_btp_issues', method='post',
            body=body,
        )

    def set_informative_btp_issues(self, *,
                                   display_unique_and_informative_btp_rules: Union[bool, None, UnsetType] = UNSET) -> Any:
        """Update informative BTP issues settings

        POST /public_api/v1/configurations/agent/informative_btp_issues/set
        Available in Cortex XDR 5.x.
        Returns the complete JSON response, bytes for downloads, or None for an empty response.
        Omit optional fields with UNSET; explicit None is sent as JSON null.
        :param display_unique_and_informative_btp_rules: body field display_unique_and_informative_btp_rules.
        """
        self._require_versions((5,))
        body = self._values({'display_unique_and_informative_btp_rules': display_unique_and_informative_btp_rules})
        body = self._values({'request_data': body, **{}})
        return self._operation(
            '/public_api/v1/configurations/agent/informative_btp_issues/set', method='post',
            body=body,
        )

    def get_cortex_xdr_log_collection(self) -> Any:
        """Retrieve log collection settings

        POST /public_api/v1/configurations/agent/cortex_xdr_log_collection
        Available in Cortex XDR 5.x.
        Returns the complete JSON response, bytes for downloads, or None for an empty response.
        Omit optional fields with UNSET; explicit None is sent as JSON null.
        """
        self._require_versions((5,))
        body = UNSET
        return self._operation(
            '/public_api/v1/configurations/agent/cortex_xdr_log_collection', method='post',
            body=body,
        )

    def set_cortex_xdr_log_collection(self, *,
                                      allow_logs_collection: Union[bool, None, UnsetType] = UNSET) -> Any:
        """Update log collection settings

        POST /public_api/v1/configurations/agent/cortex_xdr_log_collection/set
        Available in Cortex XDR 5.x.
        Returns the complete JSON response, bytes for downloads, or None for an empty response.
        Omit optional fields with UNSET; explicit None is sent as JSON null.
        :param allow_logs_collection: body field allow_logs_collection.
        """
        self._require_versions((5,))
        body = self._values({'allow_logs_collection': allow_logs_collection})
        body = self._values({'request_data': body, **{}})
        return self._operation(
            '/public_api/v1/configurations/agent/cortex_xdr_log_collection/set', method='post',
            body=body,
        )

    def get_action_center_expiration(self) -> Any:
        """Retrieve action center expiration settings

        POST /public_api/v1/configurations/agent/action_center_expiration
        Available in Cortex XDR 5.x.
        Returns the complete JSON response, bytes for downloads, or None for an empty response.
        Omit optional fields with UNSET; explicit None is sent as JSON null.
        """
        self._require_versions((5,))
        body = UNSET
        return self._operation(
            '/public_api/v1/configurations/agent/action_center_expiration', method='post',
            body=body,
        )

    def set_action_center_expiration(self, *,
                                     request_data: Union[dict, None, UnsetType] = UNSET) -> Any:
        """Update action center expiration settings

        POST /public_api/v1/configurations/agent/action_center_expiration/set
        Available in Cortex XDR 5.x.
        Returns the complete JSON response, bytes for downloads, or None for an empty response.
        Omit optional fields with UNSET; explicit None is sent as JSON null.
        :param request_data: payload field request_data.
        """
        self._require_versions((5,))
        body = request_data
        body = self._values({'request_data': body, **{}})
        return self._operation(
            '/public_api/v1/configurations/agent/action_center_expiration/set', method='post',
            body=body,
        )

    def get_critical_environment_versions(self) -> Any:
        """Retrieve critical environment versions settings

        POST /public_api/v1/configurations/agent/critical_environment_versions
        Available in Cortex XDR 5.x.
        Returns the complete JSON response, bytes for downloads, or None for an empty response.
        Omit optional fields with UNSET; explicit None is sent as JSON null.
        """
        self._require_versions((5,))
        body = UNSET
        return self._operation(
            '/public_api/v1/configurations/agent/critical_environment_versions', method='post',
            body=body,
        )

    def set_critical_environment_versions(self, *,
                                          enabled_critical_environment_versions: Union[bool, None, UnsetType] = UNSET) -> Any:
        """Update critical environment versions settings

        POST /public_api/v1/configurations/agent/critical_environment_versions/set
        Available in Cortex XDR 5.x.
        Returns the complete JSON response, bytes for downloads, or None for an empty response.
        Omit optional fields with UNSET; explicit None is sent as JSON null.
        :param enabled_critical_environment_versions: body field enabled_critical_environment_versions.
        """
        self._require_versions((5,))
        body = self._values({'enabled_critical_environment_versions': enabled_critical_environment_versions})
        body = self._values({'request_data': body, **{}})
        return self._operation(
            '/public_api/v1/configurations/agent/critical_environment_versions/set', method='post',
            body=body,
        )

    def get_advanced_analysis(self) -> Any:
        """Retrieve advanced analysis settings

        POST /public_api/v1/configurations/agent/advanced_analysis
        Available in Cortex XDR 5.x.
        Returns the complete JSON response, bytes for downloads, or None for an empty response.
        Omit optional fields with UNSET; explicit None is sent as JSON null.
        """
        self._require_versions((5,))
        body = UNSET
        return self._operation(
            '/public_api/v1/configurations/agent/advanced_analysis', method='post',
            body=body,
        )

    def set_advanced_analysis(self, *,
                              automatically_upload_defined_issue_data_files: Union[bool, None, UnsetType] = UNSET,
                              automatically_apply_advanced_analysis_exceptions: Union[bool, None, UnsetType] = UNSET) -> Any:
        """Update advanced analysis settings

        POST /public_api/v1/configurations/agent/advanced_analysis/set
        Available in Cortex XDR 5.x.
        Returns the complete JSON response, bytes for downloads, or None for an empty response.
        Omit optional fields with UNSET; explicit None is sent as JSON null.
        :param automatically_upload_defined_issue_data_files: body field automatically_upload_defined_issue_data_files.
        :param automatically_apply_advanced_analysis_exceptions: body field automatically_apply_advanced_analysis_exceptions.
        """
        self._require_versions((5,))
        body = self._values({'automatically_upload_defined_issue_data_files': automatically_upload_defined_issue_data_files, 'automatically_apply_advanced_analysis_exceptions': automatically_apply_advanced_analysis_exceptions})
        body = self._values({'request_data': body, **{}})
        return self._operation(
            '/public_api/v1/configurations/agent/advanced_analysis/set', method='post',
            body=body,
        )

    def get_endpoint_administration_cleanup(self) -> Any:
        """Retrieve endpoint administration cleanup settings

        POST /public_api/v1/configurations/agent/endpoint_administration_cleanup
        Available in Cortex XDR 5.x.
        Returns the complete JSON response, bytes for downloads, or None for an empty response.
        Omit optional fields with UNSET; explicit None is sent as JSON null.
        """
        self._require_versions((5,))
        body = UNSET
        return self._operation(
            '/public_api/v1/configurations/agent/endpoint_administration_cleanup', method='post',
            body=body,
        )

    def set_endpoint_administration_cleanup(self, *,
                                            periodic_duplicate_cleanup: Union[bool, None, UnsetType] = UNSET,
                                            host_name: Union[bool, None, UnsetType] = UNSET,
                                            ip: Union[bool, None, UnsetType] = UNSET,
                                            mac: Union[bool, None, UnsetType] = UNSET,
                                            time_interval_hours: Union[int, None, UnsetType] = UNSET) -> Any:
        """Update endpoint administration cleanup settings

        POST /public_api/v1/configurations/agent/endpoint_administration_cleanup/set
        Available in Cortex XDR 5.x.
        Returns the complete JSON response, bytes for downloads, or None for an empty response.
        Omit optional fields with UNSET; explicit None is sent as JSON null.
        :param periodic_duplicate_cleanup: body field periodic_duplicate_cleanup.
        :param host_name: body field host_name.
        :param ip: body field ip.
        :param mac: body field mac.
        :param time_interval_hours: body field time_interval_hours.
        """
        self._require_versions((5,))
        body = self._values({'periodic_duplicate_cleanup': periodic_duplicate_cleanup, 'host_name': host_name, 'ip': ip, 'mac': mac, 'time_interval_hours': time_interval_hours})
        body = self._values({'request_data': body, **{}})
        return self._operation(
            '/public_api/v1/configurations/agent/endpoint_administration_cleanup/set', method='post',
            body=body,
        )
