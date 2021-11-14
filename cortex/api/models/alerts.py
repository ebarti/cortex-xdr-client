from typing import List
from enum import Enum


class AlertSeverity(Enum):
    """
    Severity of an alert.
    """
    LOW = "low"
    MEDIUM = "medium"
    HIGH = "high"
    UNKNOWN = "unknown"


class Event:
    agent_install_type: str
    agent_host_boot_time: None
    event_sub_type: None
    module_id: str
    association_strength: None
    dst_association_strength: None
    story_id: None
    event_id: None
    event_type: str
    event_timestamp: int
    actor_process_instance_id: str
    actor_process_image_path: str
    actor_process_image_name: str
    actor_process_command_line: str
    actor_process_signature_status: str
    actor_process_signature_vendor: None
    actor_process_image_sha256: str
    actor_process_image_md5: None
    actor_process_causality_id: None
    actor_causality_id: None
    actor_process_os_pid: str
    actor_thread_thread_id: None
    causality_actor_process_image_name: None
    causality_actor_process_command_line: None
    causality_actor_process_image_path: None
    causality_actor_process_signature_vendor: None
    causality_actor_process_signature_status: str
    causality_actor_causality_id: None
    causality_actor_process_execution_time: None
    causality_actor_process_image_md5: None
    causality_actor_process_image_sha256: None
    action_file_path: None
    action_file_name: None
    action_file_md5: None
    action_file_sha256: None
    action_file_macro_sha256: None
    action_registry_data: None
    action_registry_key_name: None
    action_registry_value_name: None
    action_registry_full_key: None
    action_local_ip: None
    action_local_port: None
    action_remote_ip: None
    action_remote_port: None
    action_external_hostname: None
    action_country: str
    action_process_instance_id: None
    action_process_causality_id: None
    action_process_image_name: None
    action_process_image_sha256: None
    action_process_image_command_line: None
    action_process_signature_status: str
    action_process_signature_vendor: None
    os_actor_effective_username: None
    os_actor_process_instance_id: None
    os_actor_process_image_path: None
    os_actor_process_image_name: None
    os_actor_process_command_line: None
    os_actor_process_signature_status: str
    os_actor_process_signature_vendor: None
    os_actor_process_image_sha256: None
    os_actor_process_causality_id: None
    os_actor_causality_id: None
    os_actor_process_os_pid: None
    os_actor_thread_thread_id: None
    fw_app_id: None
    fw_interface_from: None
    fw_interface_to: None
    fw_rule: None
    fw_rule_id: None
    fw_device_name: None
    fw_serial_number: None
    fw_url_domain: None
    fw_email_subject: None
    fw_email_sender: None
    fw_email_recipient: None
    fw_app_subcategory: None
    fw_app_category: None
    fw_app_technology: None
    fw_vsys: None
    fw_xff: None
    fw_misc: None
    fw_is_phishing: str
    dst_agent_id: None
    dst_causality_actor_process_execution_time: None
    dns_query_name: None
    dst_action_external_hostname: None
    dst_action_country: None
    dst_action_external_port: None
    user_name: None

    def __init__(self, agent_install_type: str, agent_host_boot_time: None, event_sub_type: None, module_id: str, association_strength: None, dst_association_strength: None, story_id: None, event_id: None, event_type: str, event_timestamp: int, actor_process_instance_id: str, actor_process_image_path: str, actor_process_image_name: str, actor_process_command_line: str, actor_process_signature_status: str, actor_process_signature_vendor: None, actor_process_image_sha256: str, actor_process_image_md5: None, actor_process_causality_id: None, actor_causality_id: None, actor_process_os_pid: str, actor_thread_thread_id: None, causality_actor_process_image_name: None, causality_actor_process_command_line: None, causality_actor_process_image_path: None, causality_actor_process_signature_vendor: None, causality_actor_process_signature_status: str, causality_actor_causality_id: None, causality_actor_process_execution_time: None, causality_actor_process_image_md5: None, causality_actor_process_image_sha256: None, action_file_path: None, action_file_name: None, action_file_md5: None, action_file_sha256: None, action_file_macro_sha256: None, action_registry_data: None, action_registry_key_name: None, action_registry_value_name: None, action_registry_full_key: None, action_local_ip: None, action_local_port: None, action_remote_ip: None, action_remote_port: None, action_external_hostname: None, action_country: str, action_process_instance_id: None, action_process_causality_id: None, action_process_image_name: None, action_process_image_sha256: None, action_process_image_command_line: None, action_process_signature_status: str, action_process_signature_vendor: None, os_actor_effective_username: None, os_actor_process_instance_id: None, os_actor_process_image_path: None, os_actor_process_image_name: None, os_actor_process_command_line: None, os_actor_process_signature_status: str, os_actor_process_signature_vendor: None, os_actor_process_image_sha256: None, os_actor_process_causality_id: None, os_actor_causality_id: None, os_actor_process_os_pid: None, os_actor_thread_thread_id: None, fw_app_id: None, fw_interface_from: None, fw_interface_to: None, fw_rule: None, fw_rule_id: None, fw_device_name: None, fw_serial_number: None, fw_url_domain: None, fw_email_subject: None, fw_email_sender: None, fw_email_recipient: None, fw_app_subcategory: None, fw_app_category: None, fw_app_technology: None, fw_vsys: None, fw_xff: None, fw_misc: None, fw_is_phishing: str, dst_agent_id: None, dst_causality_actor_process_execution_time: None, dns_query_name: None, dst_action_external_hostname: None, dst_action_country: None, dst_action_external_port: None, user_name: None) -> None:
        self.agent_install_type = agent_install_type
        self.agent_host_boot_time = agent_host_boot_time
        self.event_sub_type = event_sub_type
        self.module_id = module_id
        self.association_strength = association_strength
        self.dst_association_strength = dst_association_strength
        self.story_id = story_id
        self.event_id = event_id
        self.event_type = event_type
        self.event_timestamp = event_timestamp
        self.actor_process_instance_id = actor_process_instance_id
        self.actor_process_image_path = actor_process_image_path
        self.actor_process_image_name = actor_process_image_name
        self.actor_process_command_line = actor_process_command_line
        self.actor_process_signature_status = actor_process_signature_status
        self.actor_process_signature_vendor = actor_process_signature_vendor
        self.actor_process_image_sha256 = actor_process_image_sha256
        self.actor_process_image_md5 = actor_process_image_md5
        self.actor_process_causality_id = actor_process_causality_id
        self.actor_causality_id = actor_causality_id
        self.actor_process_os_pid = actor_process_os_pid
        self.actor_thread_thread_id = actor_thread_thread_id
        self.causality_actor_process_image_name = causality_actor_process_image_name
        self.causality_actor_process_command_line = causality_actor_process_command_line
        self.causality_actor_process_image_path = causality_actor_process_image_path
        self.causality_actor_process_signature_vendor = causality_actor_process_signature_vendor
        self.causality_actor_process_signature_status = causality_actor_process_signature_status
        self.causality_actor_causality_id = causality_actor_causality_id
        self.causality_actor_process_execution_time = causality_actor_process_execution_time
        self.causality_actor_process_image_md5 = causality_actor_process_image_md5
        self.causality_actor_process_image_sha256 = causality_actor_process_image_sha256
        self.action_file_path = action_file_path
        self.action_file_name = action_file_name
        self.action_file_md5 = action_file_md5
        self.action_file_sha256 = action_file_sha256
        self.action_file_macro_sha256 = action_file_macro_sha256
        self.action_registry_data = action_registry_data
        self.action_registry_key_name = action_registry_key_name
        self.action_registry_value_name = action_registry_value_name
        self.action_registry_full_key = action_registry_full_key
        self.action_local_ip = action_local_ip
        self.action_local_port = action_local_port
        self.action_remote_ip = action_remote_ip
        self.action_remote_port = action_remote_port
        self.action_external_hostname = action_external_hostname
        self.action_country = action_country
        self.action_process_instance_id = action_process_instance_id
        self.action_process_causality_id = action_process_causality_id
        self.action_process_image_name = action_process_image_name
        self.action_process_image_sha256 = action_process_image_sha256
        self.action_process_image_command_line = action_process_image_command_line
        self.action_process_signature_status = action_process_signature_status
        self.action_process_signature_vendor = action_process_signature_vendor
        self.os_actor_effective_username = os_actor_effective_username
        self.os_actor_process_instance_id = os_actor_process_instance_id
        self.os_actor_process_image_path = os_actor_process_image_path
        self.os_actor_process_image_name = os_actor_process_image_name
        self.os_actor_process_command_line = os_actor_process_command_line
        self.os_actor_process_signature_status = os_actor_process_signature_status
        self.os_actor_process_signature_vendor = os_actor_process_signature_vendor
        self.os_actor_process_image_sha256 = os_actor_process_image_sha256
        self.os_actor_process_causality_id = os_actor_process_causality_id
        self.os_actor_causality_id = os_actor_causality_id
        self.os_actor_process_os_pid = os_actor_process_os_pid
        self.os_actor_thread_thread_id = os_actor_thread_thread_id
        self.fw_app_id = fw_app_id
        self.fw_interface_from = fw_interface_from
        self.fw_interface_to = fw_interface_to
        self.fw_rule = fw_rule
        self.fw_rule_id = fw_rule_id
        self.fw_device_name = fw_device_name
        self.fw_serial_number = fw_serial_number
        self.fw_url_domain = fw_url_domain
        self.fw_email_subject = fw_email_subject
        self.fw_email_sender = fw_email_sender
        self.fw_email_recipient = fw_email_recipient
        self.fw_app_subcategory = fw_app_subcategory
        self.fw_app_category = fw_app_category
        self.fw_app_technology = fw_app_technology
        self.fw_vsys = fw_vsys
        self.fw_xff = fw_xff
        self.fw_misc = fw_misc
        self.fw_is_phishing = fw_is_phishing
        self.dst_agent_id = dst_agent_id
        self.dst_causality_actor_process_execution_time = dst_causality_actor_process_execution_time
        self.dns_query_name = dns_query_name
        self.dst_action_external_hostname = dst_action_external_hostname
        self.dst_action_country = dst_action_country
        self.dst_action_external_port = dst_action_external_port
        self.user_name = user_name

    @classmethod
    def from_json(cls, data: dict) -> "Event":
        return cls(**data)


class Alert:
    external_id: str
    severity: str
    matching_status: str
    end_match_attempt_ts: int
    local_insert_ts: int
    bioc_indicator: None
    matching_service_rule_id: None
    attempt_counter: int
    bioc_category_enum_key: None
    is_whitelisted: bool
    starred: bool
    deduplicate_tokens: None
    filter_rule_id: None
    mitre_technique_id_and_name: List[str]
    mitre_tactic_id_and_name: List[str]
    agent_version: str
    agent_device_domain: None
    agent_fqdn: str
    agent_os_type: str
    agent_os_sub_type: str
    agent_data_collection_status: bool
    mac: None
    mac_address: List[str]
    agent_is_vdi: None
    contains_featured_host: bool
    contains_featured_user: bool
    contains_featured_ip: bool
    events: List[Event]
    alert_id: str
    detection_timestamp: int
    name: str
    category: str
    endpoint_id: str
    description: str
    host_ip: List[str]
    host_name: str
    source: str
    action: str
    action_pretty: str

    def __init__(self, external_id: str, severity: str, matching_status: str, end_match_attempt_ts: int, local_insert_ts: int, bioc_indicator: None, matching_service_rule_id: None, attempt_counter: int, bioc_category_enum_key: None, is_whitelisted: bool, starred: bool, deduplicate_tokens: None, filter_rule_id: None, mitre_technique_id_and_name: List[str], mitre_tactic_id_and_name: List[str], agent_version: str, agent_device_domain: None, agent_fqdn: str, agent_os_type: str, agent_os_sub_type: str, agent_data_collection_status: bool, mac: None, mac_address: List[str], agent_is_vdi: None, contains_featured_host: bool, contains_featured_user: bool, contains_featured_ip: bool, events: List[Event], alert_id: str, detection_timestamp: int, name: str, category: str, endpoint_id: str, description: str, host_ip: List[str], host_name: str, source: str, action: str, action_pretty: str) -> None:
        self.external_id = external_id
        self.severity = severity
        self.matching_status = matching_status
        self.end_match_attempt_ts = end_match_attempt_ts
        self.local_insert_ts = local_insert_ts
        self.bioc_indicator = bioc_indicator
        self.matching_service_rule_id = matching_service_rule_id
        self.attempt_counter = attempt_counter
        self.bioc_category_enum_key = bioc_category_enum_key
        self.is_whitelisted = is_whitelisted
        self.starred = starred
        self.deduplicate_tokens = deduplicate_tokens
        self.filter_rule_id = filter_rule_id
        self.mitre_technique_id_and_name = mitre_technique_id_and_name
        self.mitre_tactic_id_and_name = mitre_tactic_id_and_name
        self.agent_version = agent_version
        self.agent_device_domain = agent_device_domain
        self.agent_fqdn = agent_fqdn
        self.agent_os_type = agent_os_type
        self.agent_os_sub_type = agent_os_sub_type
        self.agent_data_collection_status = agent_data_collection_status
        self.mac = mac
        self.mac_address = mac_address
        self.agent_is_vdi = agent_is_vdi
        self.contains_featured_host = contains_featured_host
        self.contains_featured_user = contains_featured_user
        self.contains_featured_ip = contains_featured_ip
        self.events = events
        self.alert_id = alert_id
        self.detection_timestamp = detection_timestamp
        self.name = name
        self.category = category
        self.endpoint_id = endpoint_id
        self.description = description
        self.host_ip = host_ip
        self.host_name = host_name
        self.source = source
        self.action = action
        self.action_pretty = action_pretty

    @classmethod
    def from_json(cls, data: dict) -> "Alert":
        return cls(**data)


class GetAlertsResponseItem:
    total_count: int
    result_count: int
    alerts: List[Alert]

    def __init__(self, total_count: int, result_count: int, alerts: List[Alert]) -> None:
        self.total_count = total_count
        self.result_count = result_count
        self.alerts = alerts

    @classmethod
    def from_json(cls, data: dict) -> "GetAlertsResponseItem":
        total_count = data["total_count"]
        result_count = data["result_count"]
        alerts = list(map(Alert.from_json, data["alerts"]))
        return cls(total_count=total_count, result_count=result_count, alerts=alerts)


class GetAlertsResponse:
    reply: GetAlertsResponseItem

    def __init__(self, reply: GetAlertsResponseItem) -> None:
        self.reply = reply

    @classmethod
    def from_json(cls, data: dict) -> "GetAlertsResponse":
        return cls(**data)