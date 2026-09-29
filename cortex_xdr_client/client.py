from typing import Tuple

import requests

from cortex_xdr_client.api.brokers_api import BrokersAPI
from cortex_xdr_client.api.featured_fields_api import FeaturedFieldsAPI
from cortex_xdr_client.api.legacy_exceptions_api import LegacyExceptionsAPI
from cortex_xdr_client.api.disable_injection_prevention_rules_api import DisableInjectionPreventionRulesAPI
from cortex_xdr_client.api.disable_prevention_api import DisablePreventionAPI
from cortex_xdr_client.api.distributions_api import DistributionsAPI
from cortex_xdr_client.api.device_control_api import DeviceControlAPI
from cortex_xdr_client.api.tags_api import TagsAPI
from cortex_xdr_client.api.hash_exceptions_api import HashExceptionsAPI
from cortex_xdr_client.api.quarantine_api import QuarantineAPI
from cortex_xdr_client.api.audits_api import AuditsAPI
from cortex_xdr_client.api.system_api import SystemAPI
from cortex_xdr_client.api.rbac_api import RbacAPI
from cortex_xdr_client.api.risk_api import RiskAPI
from cortex_xdr_client.api.automations_api import AutomationsAPI
from cortex_xdr_client.api.integrations_api import IntegrationsAPI
from cortex_xdr_client.api.authentication_settings_api import AuthenticationSettingsAPI
from cortex_xdr_client.api.profiles_api import ProfilesAPI
from cortex_xdr_client.api.agent_configurations_api import AgentConfigurationsAPI
from cortex_xdr_client.api.appsec_api import AppsecAPI
from cortex_xdr_client.api.compliance_api import ComplianceAPI
from cortex_xdr_client.api.cli_api import CliAPI
from cortex_xdr_client.api.api_keys_api import ApiKeysAPI
from cortex_xdr_client.api.assets_api import AssetsAPI
from cortex_xdr_client.api.scheduled_queries_api import ScheduledQueriesAPI
from cortex_xdr_client.api.query_library_api import QueryLibraryAPI
from cortex_xdr_client.api.bioc_api import BiocAPI
from cortex_xdr_client.api.correlations_api import CorrelationsAPI
from cortex_xdr_client.api.playbooks_api import PlaybooksAPI
from cortex_xdr_client.api.dashboards_api import DashboardsAPI
from cortex_xdr_client.api.widgets_api import WidgetsAPI
from cortex_xdr_client.api.asset_groups_api import AssetGroupsAPI
from cortex_xdr_client.api.policies_api import PoliciesAPI
from cortex_xdr_client.api.notifications_api import NotificationsAPI
from cortex_xdr_client.api.brokers_v5_api import BrokersV5API
from cortex_xdr_client.api.ciem_api import CiemAPI
from cortex_xdr_client.api.cloud_onboarding_api import CloudOnboardingAPI
from cortex_xdr_client.api.cloud_workload_protection_api import CloudWorkloadProtectionAPI
from cortex_xdr_client.api.compliance_controls_api import ComplianceControlsAPI
from cortex_xdr_client.api.data_security_api import DataSecurityAPI
from cortex_xdr_client.api.detection_rules_api import DetectionRulesAPI
from cortex_xdr_client.api.prevention_rules_v5_api import PreventionRulesV5API
from cortex_xdr_client.api.external_applications_api import ExternalApplicationsAPI
from cortex_xdr_client.api.forensics_api import ForensicsAPI
from cortex_xdr_client.api.iam_api import IamAPI
from cortex_xdr_client.api.clcs_api import ClcsAPI
from cortex_xdr_client.api.managed_services_api import ManagedServicesAPI
from cortex_xdr_client.api.netscan_api import NetscanAPI
from cortex_xdr_client.api.cloud_security_policies_api import CloudSecurityPoliciesAPI
from cortex_xdr_client.api.restore_distributions_api import RestoreDistributionsAPI
from cortex_xdr_client.api.unified_rules_api import UnifiedRulesAPI
from cortex_xdr_client.api.vulnerability_intelligence_api import VulnerabilityIntelligenceAPI
from cortex_xdr_client.api.vulnerability_management_api import VulnerabilityManagementAPI
from cortex_xdr_client.api.actions_api import ActionsAPI
from cortex_xdr_client.api.alerts_api import AlertsAPI
from cortex_xdr_client.api.authentication import Authentication
from cortex_xdr_client.api.base_api import BaseAPI
from cortex_xdr_client.api.cases_api import CasesAPI
from cortex_xdr_client.api.download_api import DownloadAPI
from cortex_xdr_client.api.endpoints_api import EndpointsAPI
from cortex_xdr_client.api.incidents_api import IncidentsAPI
from cortex_xdr_client.api.ioc_api import IocAPI
from cortex_xdr_client.api.issues_api import IssuesAPI
from cortex_xdr_client.api.scripts_api import ScriptsAPI
from cortex_xdr_client.api.version import APIVersion
from cortex_xdr_client.api.xql_api import XQLAPI


class CortexXDRClient(object):
    brokers_v5_api: BrokersV5API
    ciem_api: CiemAPI
    cloud_onboarding_api: CloudOnboardingAPI
    cloud_workload_protection_api: CloudWorkloadProtectionAPI
    compliance_controls_api: ComplianceControlsAPI
    data_security_api: DataSecurityAPI
    detection_rules_api: DetectionRulesAPI
    prevention_rules_v5_api: PreventionRulesV5API
    external_applications_api: ExternalApplicationsAPI
    forensics_api: ForensicsAPI
    iam_api: IamAPI
    clcs_api: ClcsAPI
    managed_services_api: ManagedServicesAPI
    netscan_api: NetscanAPI
    cloud_security_policies_api: CloudSecurityPoliciesAPI
    restore_distributions_api: RestoreDistributionsAPI
    unified_rules_api: UnifiedRulesAPI
    vulnerability_intelligence_api: VulnerabilityIntelligenceAPI
    vulnerability_management_api: VulnerabilityManagementAPI
    brokers_api: BrokersAPI
    featured_fields_api: FeaturedFieldsAPI
    legacy_exceptions_api: LegacyExceptionsAPI
    disable_injection_prevention_rules_api: DisableInjectionPreventionRulesAPI
    disable_prevention_api: DisablePreventionAPI
    distributions_api: DistributionsAPI
    device_control_api: DeviceControlAPI
    tags_api: TagsAPI
    hash_exceptions_api: HashExceptionsAPI
    quarantine_api: QuarantineAPI
    audits_api: AuditsAPI
    system_api: SystemAPI
    rbac_api: RbacAPI
    risk_api: RiskAPI
    automations_api: AutomationsAPI
    integrations_api: IntegrationsAPI
    authentication_settings_api: AuthenticationSettingsAPI
    profiles_api: ProfilesAPI
    agent_configurations_api: AgentConfigurationsAPI
    appsec_api: AppsecAPI
    compliance_api: ComplianceAPI
    cli_api: CliAPI
    api_keys_api: ApiKeysAPI
    assets_api: AssetsAPI
    scheduled_queries_api: ScheduledQueriesAPI
    query_library_api: QueryLibraryAPI
    bioc_api: BiocAPI
    correlations_api: CorrelationsAPI
    playbooks_api: PlaybooksAPI
    dashboards_api: DashboardsAPI
    widgets_api: WidgetsAPI
    asset_groups_api: AssetGroupsAPI
    policies_api: PoliciesAPI
    notifications_api: NotificationsAPI
    incidents_api: IncidentsAPI
    alerts_api: AlertsAPI
    endpoints_api: EndpointsAPI
    scripts_api: ScriptsAPI
    xql_api: XQLAPI
    actions_api: ActionsAPI
    download_api: DownloadAPI
    ioc_api: IocAPI
    cases_api: CasesAPI
    issues_api: IssuesAPI

    def __init__(self, auth: Authentication, fqdn: str, default_timeout: Tuple[int, int] = (10, 60),
                 api_version: APIVersion = APIVersion.V3) -> None:
        """
        Constructor of the CortexXDRClient class. This class is used to interact with the Cortex XDR API.
        :param auth: The Authentication object containing type
        :param fqdn: The fully qualified domain name of the Cortex XDR server.
        :param api_version: Cortex XDR product version, 3 or 5. Defaults to 3 for existing callers.
        :param default_timeout: The default timeout for API calls.
        """
        self.api_version = APIVersion(api_version)
        self.brokers_api = BrokersAPI(auth=auth, fqdn=fqdn, timeout=default_timeout,
                                      api_version=self.api_version)
        self.featured_fields_api = FeaturedFieldsAPI(auth=auth, fqdn=fqdn, timeout=default_timeout,
                                                     api_version=self.api_version)
        self.legacy_exceptions_api = LegacyExceptionsAPI(auth=auth, fqdn=fqdn, timeout=default_timeout,
                                                         api_version=self.api_version)
        self.disable_injection_prevention_rules_api = DisableInjectionPreventionRulesAPI(auth=auth, fqdn=fqdn, timeout=default_timeout,
                                                                                         api_version=self.api_version)
        self.disable_prevention_api = DisablePreventionAPI(auth=auth, fqdn=fqdn, timeout=default_timeout,
                                                           api_version=self.api_version)
        self.distributions_api = DistributionsAPI(auth=auth, fqdn=fqdn, timeout=default_timeout,
                                                  api_version=self.api_version)
        self.device_control_api = DeviceControlAPI(auth=auth, fqdn=fqdn, timeout=default_timeout,
                                                   api_version=self.api_version)
        self.tags_api = TagsAPI(auth=auth, fqdn=fqdn, timeout=default_timeout,
                                api_version=self.api_version)
        self.hash_exceptions_api = HashExceptionsAPI(auth=auth, fqdn=fqdn, timeout=default_timeout,
                                                     api_version=self.api_version)
        self.quarantine_api = QuarantineAPI(auth=auth, fqdn=fqdn, timeout=default_timeout,
                                            api_version=self.api_version)
        self.audits_api = AuditsAPI(auth=auth, fqdn=fqdn, timeout=default_timeout,
                                    api_version=self.api_version)
        self.system_api = SystemAPI(auth=auth, fqdn=fqdn, timeout=default_timeout,
                                    api_version=self.api_version)
        self.rbac_api = RbacAPI(auth=auth, fqdn=fqdn, timeout=default_timeout,
                                api_version=self.api_version)
        self.risk_api = RiskAPI(auth=auth, fqdn=fqdn, timeout=default_timeout,
                                api_version=self.api_version)
        self.automations_api = AutomationsAPI(auth=auth, fqdn=fqdn, timeout=default_timeout,
                                              api_version=self.api_version)
        self.integrations_api = IntegrationsAPI(auth=auth, fqdn=fqdn, timeout=default_timeout,
                                                api_version=self.api_version)
        self.authentication_settings_api = AuthenticationSettingsAPI(auth=auth, fqdn=fqdn, timeout=default_timeout,
                                                                     api_version=self.api_version)
        self.profiles_api = ProfilesAPI(auth=auth, fqdn=fqdn, timeout=default_timeout,
                                        api_version=self.api_version)
        self.agent_configurations_api = AgentConfigurationsAPI(auth=auth, fqdn=fqdn, timeout=default_timeout,
                                                               api_version=self.api_version)
        self.appsec_api = AppsecAPI(auth=auth, fqdn=fqdn, timeout=default_timeout,
                                    api_version=self.api_version)
        self.compliance_api = ComplianceAPI(auth=auth, fqdn=fqdn, timeout=default_timeout,
                                            api_version=self.api_version)
        self.cli_api = CliAPI(auth=auth, fqdn=fqdn, timeout=default_timeout,
                              api_version=self.api_version)
        self.api_keys_api = ApiKeysAPI(auth=auth, fqdn=fqdn, timeout=default_timeout,
                                       api_version=self.api_version)
        self.assets_api = AssetsAPI(auth=auth, fqdn=fqdn, timeout=default_timeout,
                                    api_version=self.api_version)
        self.scheduled_queries_api = ScheduledQueriesAPI(auth=auth, fqdn=fqdn, timeout=default_timeout,
                                                         api_version=self.api_version)
        self.query_library_api = QueryLibraryAPI(auth=auth, fqdn=fqdn, timeout=default_timeout,
                                                 api_version=self.api_version)
        self.bioc_api = BiocAPI(auth=auth, fqdn=fqdn, timeout=default_timeout,
                                api_version=self.api_version)
        self.correlations_api = CorrelationsAPI(auth=auth, fqdn=fqdn, timeout=default_timeout,
                                                api_version=self.api_version)
        self.playbooks_api = PlaybooksAPI(auth=auth, fqdn=fqdn, timeout=default_timeout,
                                          api_version=self.api_version)
        self.dashboards_api = DashboardsAPI(auth=auth, fqdn=fqdn, timeout=default_timeout,
                                            api_version=self.api_version)
        self.widgets_api = WidgetsAPI(auth=auth, fqdn=fqdn, timeout=default_timeout,
                                      api_version=self.api_version)
        self.asset_groups_api = AssetGroupsAPI(auth=auth, fqdn=fqdn, timeout=default_timeout,
                                               api_version=self.api_version)
        self.policies_api = PoliciesAPI(auth=auth, fqdn=fqdn, timeout=default_timeout,
                                        api_version=self.api_version)
        self.notifications_api = NotificationsAPI(auth=auth, fqdn=fqdn, timeout=default_timeout,
                                                  api_version=self.api_version)
        self.brokers_v5_api = BrokersV5API(auth=auth, fqdn=fqdn, timeout=default_timeout,
                                           api_version=self.api_version)
        self.ciem_api = CiemAPI(auth=auth, fqdn=fqdn, timeout=default_timeout,
                                 api_version=self.api_version)
        self.cloud_onboarding_api = CloudOnboardingAPI(auth=auth, fqdn=fqdn, timeout=default_timeout,
                                                       api_version=self.api_version)
        self.cloud_workload_protection_api = CloudWorkloadProtectionAPI(auth=auth, fqdn=fqdn, timeout=default_timeout,
                                                                         api_version=self.api_version)
        self.compliance_controls_api = ComplianceControlsAPI(auth=auth, fqdn=fqdn, timeout=default_timeout,
                                                               api_version=self.api_version)
        self.data_security_api = DataSecurityAPI(auth=auth, fqdn=fqdn, timeout=default_timeout,
                                                 api_version=self.api_version)
        self.detection_rules_api = DetectionRulesAPI(auth=auth, fqdn=fqdn, timeout=default_timeout,
                                                     api_version=self.api_version)
        self.prevention_rules_v5_api = PreventionRulesV5API(auth=auth, fqdn=fqdn, timeout=default_timeout,
                                                             api_version=self.api_version)
        self.external_applications_api = ExternalApplicationsAPI(auth=auth, fqdn=fqdn, timeout=default_timeout,
                                                                 api_version=self.api_version)
        self.forensics_api = ForensicsAPI(auth=auth, fqdn=fqdn, timeout=default_timeout,
                                         api_version=self.api_version)
        self.iam_api = IamAPI(auth=auth, fqdn=fqdn, timeout=default_timeout,
                             api_version=self.api_version)
        self.clcs_api = ClcsAPI(auth=auth, fqdn=fqdn, timeout=default_timeout,
                               api_version=self.api_version)
        self.managed_services_api = ManagedServicesAPI(auth=auth, fqdn=fqdn, timeout=default_timeout,
                                                       api_version=self.api_version)
        self.netscan_api = NetscanAPI(auth=auth, fqdn=fqdn, timeout=default_timeout,
                                     api_version=self.api_version)
        self.cloud_security_policies_api = CloudSecurityPoliciesAPI(auth=auth, fqdn=fqdn, timeout=default_timeout,
                                                                     api_version=self.api_version)
        self.restore_distributions_api = RestoreDistributionsAPI(auth=auth, fqdn=fqdn, timeout=default_timeout,
                                                                 api_version=self.api_version)
        self.unified_rules_api = UnifiedRulesAPI(auth=auth, fqdn=fqdn, timeout=default_timeout,
                                                 api_version=self.api_version)
        self.vulnerability_intelligence_api = VulnerabilityIntelligenceAPI(auth=auth, fqdn=fqdn, timeout=default_timeout,
                                                                           api_version=self.api_version)
        self.vulnerability_management_api = VulnerabilityManagementAPI(auth=auth, fqdn=fqdn, timeout=default_timeout,
                                                                       api_version=self.api_version)
        self._api = BaseAPI(auth, fqdn, "", default_timeout, self.api_version)
        self.cases_api = CasesAPI(auth=auth,
                                  fqdn=fqdn,
                                  timeout=default_timeout,
                                  api_version=self.api_version)
        self.issues_api = IssuesAPI(auth=auth,
                                    fqdn=fqdn,
                                    timeout=default_timeout,
                                    api_version=self.api_version)
        self.incidents_api = IncidentsAPI(auth=auth,
                                          fqdn=fqdn,
                                          timeout=default_timeout,
                                          api_version=self.api_version)
        self.alerts_api = AlertsAPI(auth=auth,
                                    fqdn=fqdn,
                                    timeout=default_timeout,
                                    api_version=self.api_version)
        self.endpoints_api = EndpointsAPI(auth=auth,
                                          fqdn=fqdn,
                                          timeout=default_timeout,
                                          api_version=self.api_version)
        self.scripts_api = ScriptsAPI(auth=auth,
                                      fqdn=fqdn,
                                      timeout=default_timeout,
                                      api_version=self.api_version)
        self.xql_api = XQLAPI(auth=auth,
                              fqdn=fqdn,
                              timeout=default_timeout,
                              api_version=self.api_version)
        self.actions_api = ActionsAPI(auth=auth,
                                      fqdn=fqdn,
                                      timeout=default_timeout,
                                      api_version=self.api_version)
        self.download_api = DownloadAPI(auth=auth,
                                      fqdn=fqdn,
                                      timeout=default_timeout,
                                      api_version=self.api_version)
        self.ioc_api = IocAPI(auth=auth,
                              fqdn=fqdn,
                              timeout=default_timeout,
                              api_version=self.api_version)

    def request(self, path: str, method: str = "post", params: dict = None,
                json_value: object = None, header_params: dict = None,
                data=None, files=None) -> requests.Response:
        """
        Call any documented operation for the selected tenant, including APIs
        without a typed wrapper. Supply the complete path and request body from
        the corresponding product documentation. Returns a requests.Response.
        """
        return self._api.request(path, method, params, json_value, header_params, data, files)
