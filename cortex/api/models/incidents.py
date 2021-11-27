from enum import Enum
from typing import List


class IncidentStatus(Enum):
    """
    Incident Status Enum
    Represents the status of the incident.
    """
    NEW = "new"
    UNDER_INVESTIGATION = "under_investigation"
    RESOLVED_THREAD_HANDLED = "resolved_threat_handled"
    RESOLVED_KNOWN_ISSUE = "resolved_known_issue"
    RESOLVED_DUPLICATE_INCIDENT = "resolved_duplicate_incident"
    RESOLVED_FALSE_POSITIVE = "resolved_false_positive"
    RESOLVED_AUTO_RESOLVE = "resolved_auto_resolve"


class Incident:
    alert_categories: List[str]
    alert_count: int
    alerts_grouping_status: str
    assigned_user_mail: str
    assigned_user_pretty_name: str
    creation_time: int
    description: str
    detection_time: int
    high_severity_alert_count: int
    host_count: int
    hosts: List[str]
    incident_id: str
    incident_name: str
    incident_sources: List[str]
    low_severity_alert_count: int
    manual_description: str
    manual_score: int
    manual_severity: str
    med_severity_alert_count: int
    mitre_tactics_ids_and_names: List[str]
    mitre_techniques_ids_and_names: List[str]
    modification_time: int
    notes: str
    resolve_comment: str
    rule_based_score: int
    severity: str
    starred: bool
    status: str
    user_count: int
    users: List[str]
    wildfire_hits: int
    xdr_url: str

    def __init__(self,
                 alert_categories: List[str],
                 alert_count: int,
                 creation_time: int,
                 detection_time: int,
                 high_severity_alert_count: int,
                 host_count: int,
                 hosts: List[str],
                 incident_sources: List[str],
                 low_severity_alert_count: int,
                 med_severity_alert_count: int,
                 mitre_tactics_ids_and_names: List[str],
                 mitre_techniques_ids_and_names: List[str],
                 modification_time: int,
                 rule_based_score: int,
                 starred: bool,
                 user_count: int,
                 users: List[str],
                 wildfire_hits: int,
                 alerts_grouping_status: str = None,
                 assigned_user_mail: str = None,
                 assigned_user_pretty_name: str = None,
                 description: str = None,
                 incident_id: str = None,
                 incident_name: str = None,
                 manual_description: str = None,
                 manual_score: str = None,
                 manual_severity: str = None,
                 notes: str = None,
                 resolve_comment: str = None,
                 severity: str = None,
                 status: str = None,
                 xdr_url: str = None,
                 ) -> None:
        self.alert_categories = alert_categories
        self.alert_count = alert_count
        self.alerts_grouping_status = alerts_grouping_status
        self.assigned_user_mail = assigned_user_mail
        self.assigned_user_pretty_name = assigned_user_pretty_name
        self.creation_time = creation_time
        self.description = description
        self.detection_time = detection_time
        self.high_severity_alert_count = high_severity_alert_count
        self.host_count = host_count
        self.hosts = hosts
        self.incident_id = incident_id
        self.incident_name = incident_name
        self.incident_sources = incident_sources
        self.low_severity_alert_count = low_severity_alert_count
        self.manual_description = manual_description
        self.manual_score = manual_score
        self.manual_severity = manual_severity
        self.med_severity_alert_count = med_severity_alert_count
        self.mitre_tactics_ids_and_names = mitre_tactics_ids_and_names
        self.mitre_techniques_ids_and_names = mitre_techniques_ids_and_names
        self.modification_time = modification_time
        self.notes = notes
        self.resolve_comment = resolve_comment
        self.rule_based_score = rule_based_score
        self.severity = severity
        self.starred = starred
        self.status = status
        self.user_count = user_count
        self.users = users
        self.wildfire_hits = wildfire_hits
        self.xdr_url = xdr_url

    @classmethod
    def from_json(cls, data: dict) -> "Incident":
        return cls(**data)


class GetIncidentsResponseItem:
    total_count: int
    result_count: int
    incidents: List[Incident]

    def __init__(self,
                 incidents: List[Incident],
                 result_count: int,
                 total_count: int,
                 ) -> None:
        self.total_count = total_count
        self.result_count = result_count
        self.incidents = incidents

    @classmethod
    def from_json(cls, data: dict) -> "GetIncidentsResponseItem":
        total_count = data["total_count"]
        result_count = data["result_count"]
        incidents = list(map(Incident.from_json, data["incidents"]))
        return cls(total_count=total_count, result_count=result_count, incidents=incidents)


class GetIncidentsResponse:
    reply: GetIncidentsResponseItem

    def __init__(self, reply: GetIncidentsResponseItem) -> None:
        self.reply = reply

    @classmethod
    def from_json(cls, data: dict) -> "GetIncidentsResponse":
        return cls(**data)


class AlertsDatum:
    action: str
    action_country: str
    action_external_hostname: str
    action_file_macro_sha256: str
    action_file_md5: str
    action_file_name: str
    action_file_path: str
    action_file_sha256: str
    action_local_ip: str
    action_local_port: int
    action_pretty: str
    action_process_causality_id: str
    action_process_image_command_line: str
    action_process_image_name: str
    action_process_image_sha256: str
    action_process_instance_id: str
    action_process_signature_status: str
    action_process_signature_vendor: str
    action_registry_data: str
    action_registry_full_key: str
    action_registry_key_name: str
    action_registry_value_name: str
    action_remote_ip: str
    action_remote_port: int
    actor_causality_id: str
    actor_process_causality_id: str
    actor_process_command_line: str
    actor_process_image_md5: str
    actor_process_image_name: str
    actor_process_image_path: str
    actor_process_image_sha256: str
    actor_process_instance_id: str
    actor_process_os_pid: str
    actor_process_signature_status: str
    actor_process_signature_vendor: str
    actor_thread_thread_id: str
    agent_data_collection_status: str
    agent_device_domain: str
    agent_fqdn: str
    agent_host_boot_time: str
    agent_install_type: str
    agent_is_vdi: str
    agent_os_sub_type: str
    agent_os_type: str
    agent_version: str
    alert_id: int
    association_strength: str
    attempt_counter: str
    bioc_category_enum_key: str
    bioc_indicator: str
    case_id: int
    category: str
    causality_actor_causality_id: str
    causality_actor_process_command_line: str
    causality_actor_process_execution_time: str
    causality_actor_process_image_md5: str
    causality_actor_process_image_name: str
    causality_actor_process_image_path: str
    causality_actor_process_image_sha256: str
    causality_actor_process_signature_status: str
    causality_actor_process_signature_vendor: str
    contains_featured_host: str
    contains_featured_ip_address: str
    contains_featured_user: str
    deduplicate_tokens: str
    description: str
    detection_timestamp: int
    dns_query_name: str
    dst_action_country: str
    dst_action_external_hostname: str
    dst_action_external_port: str
    dst_agent_id: str
    dst_association_strength: str
    dst_causality_actor_process_execution_time: str
    end_match_attempt_ts: str
    endpoint_id: str
    event_id: str
    event_sub_type: str
    event_timestamp: str
    event_type: str
    external_id: str
    filter_rule_id: str
    fw_app_category: str
    fw_app_id: str
    fw_app_subcategory: str
    fw_app_technology: str
    fw_device_name: str
    fw_email_recipient: str
    fw_email_sender: str
    fw_email_subject: str
    fw_interface_from: str
    fw_interface_to: str
    fw_is_phishing: str
    fw_misc: str
    fw_rule: str
    fw_rule_id: str
    fw_serial_number: str
    fw_url_domain: str
    fw_vsys: str
    fw_xff: str
    host_ip: str
    host_name: str
    is_whitelisted: bool
    local_insert_ts: int
    mac: str
    matching_service_rule_id: str
    matching_status: str
    mitre_tactic_id_and_name: str
    mitre_technique_id_and_name: str
    module_id: str
    name: str
    os_actor_causality_id: str
    os_actor_effective_username: str
    os_actor_process_causality_id: str
    os_actor_process_command_line: str
    os_actor_process_image_name: str
    os_actor_process_image_path: str
    os_actor_process_image_sha256: str
    os_actor_process_instance_id: str
    os_actor_process_os_pid: str
    os_actor_process_signature_status: str
    os_actor_process_signature_vendor: str
    os_actor_thread_thread_id: str
    severity: str
    source: str
    starred: bool
    story_id: str
    user_name: str

    def __init__(self,
                 action_local_port: int,
                 action_remote_port: int,
                 alert_id: int,
                 case_id: int,
                 detection_timestamp: int,
                 is_whitelisted: bool,
                 local_insert_ts: int,
                 starred: bool,
                 action: str = None,
                 action_country: str = None,
                 action_external_hostname: str = None,
                 action_file_macro_sha256: str = None,
                 action_file_md5: str = None,
                 action_file_name: str = None,
                 action_file_path: str = None,
                 action_file_sha256: str = None,
                 action_local_ip: str = None,
                 action_pretty: str = None,
                 action_process_causality_id: str = None,
                 action_process_image_command_line: str = None,
                 action_process_image_name: str = None,
                 action_process_image_sha256: str = None,
                 action_process_instance_id: str = None,
                 action_process_signature_status: str = None,
                 action_process_signature_vendor: str = None,
                 action_registry_data: str = None,
                 action_registry_full_key: str = None,
                 action_registry_key_name: str = None,
                 action_registry_value_name: str = None,
                 action_remote_ip: str = None,
                 actor_causality_id: str = None,
                 actor_process_causality_id: str = None,
                 actor_process_command_line: str = None,
                 actor_process_image_md5: str = None,
                 actor_process_image_name: str = None,
                 actor_process_image_path: str = None,
                 actor_process_image_sha256: str = None,
                 actor_process_instance_id: str = None,
                 actor_process_os_pid: str = None,
                 actor_process_signature_status: str = None,
                 actor_process_signature_vendor: str = None,
                 actor_thread_thread_id: str = None,
                 agent_data_collection_status: str = None,
                 agent_device_domain: str = None,
                 agent_fqdn: str = None,
                 agent_host_boot_time: str = None,
                 agent_install_type: str = None,
                 agent_is_vdi: str = None,
                 agent_os_sub_type: str = None,
                 agent_os_type: str = None,
                 agent_version: str = None,
                 association_strength: str = None,
                 attempt_counter: str = None,
                 bioc_category_enum_key: str = None,
                 bioc_indicator: str = None,
                 category: str = None,
                 causality_actor_causality_id: str = None,
                 causality_actor_process_command_line: str = None,
                 causality_actor_process_execution_time: str = None,
                 causality_actor_process_image_md5: str = None,
                 causality_actor_process_image_name: str = None,
                 causality_actor_process_image_path: str = None,
                 causality_actor_process_image_sha256: str = None,
                 causality_actor_process_signature_status: str = None,
                 causality_actor_process_signature_vendor: str = None,
                 contains_featured_host: str = None,
                 contains_featured_ip_address: str = None,
                 contains_featured_user: str = None,
                 deduplicate_tokens: str = None,
                 description: str = None,
                 dns_query_name: str = None,
                 dst_action_country: str = None,
                 dst_action_external_hostname: str = None,
                 dst_action_external_port: str = None,
                 dst_agent_id: str = None,
                 dst_association_strength: str = None,
                 dst_causality_actor_process_execution_time: str = None,
                 end_match_attempt_ts: str = None,
                 endpoint_id: str = None,
                 event_id: str = None,
                 event_sub_type: str = None,
                 event_timestamp: str = None,
                 event_type: str = None,
                 external_id: str = None,
                 filter_rule_id: str = None,
                 fw_app_category: str = None,
                 fw_app_id: str = None,
                 fw_app_subcategory: str = None,
                 fw_app_technology: str = None,
                 fw_device_name: str = None,
                 fw_email_recipient: str = None,
                 fw_email_sender: str = None,
                 fw_email_subject: str = None,
                 fw_interface_from: str = None,
                 fw_interface_to: str = None,
                 fw_is_phishing: str = None,
                 fw_misc: str = None,
                 fw_rule: str = None,
                 fw_rule_id: str = None,
                 fw_serial_number: str = None,
                 fw_url_domain: str = None,
                 fw_vsys: str = None,
                 fw_xff: str = None,
                 host_ip: str = None,
                 host_name: str = None,
                 mac: str = None,
                 matching_service_rule_id: str = None,
                 matching_status: str = None,
                 mitre_tactic_id_and_name: str = None,
                 mitre_technique_id_and_name: str = None,
                 module_id: str = None,
                 name: str = None,
                 os_actor_causality_id: str = None,
                 os_actor_effective_username: str = None,
                 os_actor_process_causality_id: str = None,
                 os_actor_process_command_line: str = None,
                 os_actor_process_image_name: str = None,
                 os_actor_process_image_path: str = None,
                 os_actor_process_image_sha256: str = None,
                 os_actor_process_instance_id: str = None,
                 os_actor_process_os_pid: str = None,
                 os_actor_process_signature_status: str = None,
                 os_actor_process_signature_vendor: str = None,
                 os_actor_thread_thread_id: str = None,
                 severity: str = None,
                 source: str = None,
                 story_id: str = None,
                 user_name: str = None,
                 ) -> None:
        self.action = action
        self.action_country = action_country
        self.action_external_hostname = action_external_hostname
        self.action_file_macro_sha256 = action_file_macro_sha256
        self.action_file_md5 = action_file_md5
        self.action_file_name = action_file_name
        self.action_file_path = action_file_path
        self.action_file_sha256 = action_file_sha256
        self.action_local_ip = action_local_ip
        self.action_local_port = action_local_port
        self.action_pretty = action_pretty
        self.action_process_causality_id = action_process_causality_id
        self.action_process_image_command_line = action_process_image_command_line
        self.action_process_image_name = action_process_image_name
        self.action_process_image_sha256 = action_process_image_sha256
        self.action_process_instance_id = action_process_instance_id
        self.action_process_signature_status = action_process_signature_status
        self.action_process_signature_vendor = action_process_signature_vendor
        self.action_registry_data = action_registry_data
        self.action_registry_full_key = action_registry_full_key
        self.action_registry_key_name = action_registry_key_name
        self.action_registry_value_name = action_registry_value_name
        self.action_remote_ip = action_remote_ip
        self.action_remote_port = action_remote_port
        self.actor_causality_id = actor_causality_id
        self.actor_process_causality_id = actor_process_causality_id
        self.actor_process_command_line = actor_process_command_line
        self.actor_process_image_md5 = actor_process_image_md5
        self.actor_process_image_name = actor_process_image_name
        self.actor_process_image_path = actor_process_image_path
        self.actor_process_image_sha256 = actor_process_image_sha256
        self.actor_process_instance_id = actor_process_instance_id
        self.actor_process_os_pid = actor_process_os_pid
        self.actor_process_signature_status = actor_process_signature_status
        self.actor_process_signature_vendor = actor_process_signature_vendor
        self.actor_thread_thread_id = actor_thread_thread_id
        self.agent_data_collection_status = agent_data_collection_status
        self.agent_device_domain = agent_device_domain
        self.agent_fqdn = agent_fqdn
        self.agent_host_boot_time = agent_host_boot_time
        self.agent_install_type = agent_install_type
        self.agent_is_vdi = agent_is_vdi
        self.agent_os_sub_type = agent_os_sub_type
        self.agent_os_type = agent_os_type
        self.agent_version = agent_version
        self.alert_id = alert_id
        self.association_strength = association_strength
        self.attempt_counter = attempt_counter
        self.bioc_category_enum_key = bioc_category_enum_key
        self.bioc_indicator = bioc_indicator
        self.case_id = case_id
        self.category = category
        self.causality_actor_causality_id = causality_actor_causality_id
        self.causality_actor_process_command_line = causality_actor_process_command_line
        self.causality_actor_process_execution_time = causality_actor_process_execution_time
        self.causality_actor_process_image_md5 = causality_actor_process_image_md5
        self.causality_actor_process_image_name = causality_actor_process_image_name
        self.causality_actor_process_image_path = causality_actor_process_image_path
        self.causality_actor_process_image_sha256 = causality_actor_process_image_sha256
        self.causality_actor_process_signature_status = causality_actor_process_signature_status
        self.causality_actor_process_signature_vendor = causality_actor_process_signature_vendor
        self.contains_featured_host = contains_featured_host
        self.contains_featured_ip_address = contains_featured_ip_address
        self.contains_featured_user = contains_featured_user
        self.deduplicate_tokens = deduplicate_tokens
        self.description = description
        self.detection_timestamp = detection_timestamp
        self.dns_query_name = dns_query_name
        self.dst_action_country = dst_action_country
        self.dst_action_external_hostname = dst_action_external_hostname
        self.dst_action_external_port = dst_action_external_port
        self.dst_agent_id = dst_agent_id
        self.dst_association_strength = dst_association_strength
        self.dst_causality_actor_process_execution_time = dst_causality_actor_process_execution_time
        self.end_match_attempt_ts = end_match_attempt_ts
        self.endpoint_id = endpoint_id
        self.event_id = event_id
        self.event_sub_type = event_sub_type
        self.event_timestamp = event_timestamp
        self.event_type = event_type
        self.external_id = external_id
        self.filter_rule_id = filter_rule_id
        self.fw_app_category = fw_app_category
        self.fw_app_id = fw_app_id
        self.fw_app_subcategory = fw_app_subcategory
        self.fw_app_technology = fw_app_technology
        self.fw_device_name = fw_device_name
        self.fw_email_recipient = fw_email_recipient
        self.fw_email_sender = fw_email_sender
        self.fw_email_subject = fw_email_subject
        self.fw_interface_from = fw_interface_from
        self.fw_interface_to = fw_interface_to
        self.fw_is_phishing = fw_is_phishing
        self.fw_misc = fw_misc
        self.fw_rule = fw_rule
        self.fw_rule_id = fw_rule_id
        self.fw_serial_number = fw_serial_number
        self.fw_url_domain = fw_url_domain
        self.fw_vsys = fw_vsys
        self.fw_xff = fw_xff
        self.host_ip = host_ip
        self.host_name = host_name
        self.is_whitelisted = is_whitelisted
        self.local_insert_ts = local_insert_ts
        self.mac = mac
        self.matching_service_rule_id = matching_service_rule_id
        self.matching_status = matching_status
        self.mitre_tactic_id_and_name = mitre_tactic_id_and_name
        self.mitre_technique_id_and_name = mitre_technique_id_and_name
        self.module_id = module_id
        self.name = name
        self.os_actor_causality_id = os_actor_causality_id
        self.os_actor_effective_username = os_actor_effective_username
        self.os_actor_process_causality_id = os_actor_process_causality_id
        self.os_actor_process_command_line = os_actor_process_command_line
        self.os_actor_process_image_name = os_actor_process_image_name
        self.os_actor_process_image_path = os_actor_process_image_path
        self.os_actor_process_image_sha256 = os_actor_process_image_sha256
        self.os_actor_process_instance_id = os_actor_process_instance_id
        self.os_actor_process_os_pid = os_actor_process_os_pid
        self.os_actor_process_signature_status = os_actor_process_signature_status
        self.os_actor_process_signature_vendor = os_actor_process_signature_vendor
        self.os_actor_thread_thread_id = os_actor_thread_thread_id
        self.severity = severity
        self.source = source
        self.starred = starred
        self.story_id = story_id
        self.user_name = user_name

    @classmethod
    def from_json(cls, data: dict) -> "AlertsDatum":
        return cls(**data)


class NetworkArtifactsDatum:
    alert_count: int
    is_manual: bool
    network_country: str
    network_domain: str
    network_remote_ip: str
    network_remote_port: int
    type: str

    def __init__(self,
                 alert_count: int,
                 is_manual: bool,
                 network_remote_port: int,
                 type: str = None,
                 network_domain: str = None,
                 network_remote_ip: str = None,
                 network_country: str = None,
                 ) -> None:
        self.alert_count = alert_count
        self.is_manual = is_manual
        self.network_country = network_country
        self.network_domain = network_domain
        self.network_remote_ip = network_remote_ip
        self.network_remote_port = network_remote_port
        self.type = type

    @classmethod
    def from_json(cls, data: dict) -> "NetworkArtifactsDatum":
        return cls(**data)


class AlertDatums:
    total_count: int
    data: List[AlertsDatum]

    def __init__(self,
                 data: List[AlertsDatum],
                 total_count: int,
                 ) -> None:
        self.total_count = total_count
        self.data = data

    @classmethod
    def from_json(cls, data: dict) -> "AlertDatums":
        total_count = data["total_count"]
        artifacts = list(map(AlertsDatum.from_json, data["data"]))
        return cls(total_count=total_count, data=artifacts)


class NetworkArtifacts:
    total_count: int
    data: List[NetworkArtifactsDatum]

    def __init__(self,
                 data: List[NetworkArtifactsDatum],
                 total_count: int,
                 ) -> None:
        self.total_count = total_count
        self.data = data

    @classmethod
    def from_json(cls, data: dict) -> "NetworkArtifacts":
        total_count = data["total_count"]
        artifacts = list(map(NetworkArtifactsDatum.from_json, data["data"]))
        return cls(total_count=total_count, data=artifacts)


class GetExtraIncidentDataResponseItem:
    alerts: AlertDatums
    file_artifacts: AlertDatums
    incident: Incident
    network_artifacts: NetworkArtifacts

    def __init__(self,
                 alerts: AlertDatums,
                 file_artifacts: AlertDatums,
                 incident: Incident,
                 network_artifacts: NetworkArtifacts,
                 ) -> None:
        self.alerts = alerts
        self.file_artifacts = file_artifacts
        self.incident = incident
        self.network_artifacts = network_artifacts

    @classmethod
    def from_json(cls, data: dict) -> "GetExtraIncidentDataResponseItem":
        return cls(**data)


class GetExtraIncidentDataResponse:
    reply: GetExtraIncidentDataResponseItem

    def __init__(self, reply: GetExtraIncidentDataResponseItem) -> None:
        self.reply = reply

    @classmethod
    def from_json(cls, data: dict) -> "GetExtraIncidentDataResponse":
        return cls(**data)
