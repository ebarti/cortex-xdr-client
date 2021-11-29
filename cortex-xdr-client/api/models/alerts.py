from enum import Enum
from typing import List


class AlertSeverity(Enum):
    """
    Severity of an alert.
    """
    LOW = "low"
    MEDIUM = "medium"
    HIGH = "high"
    UNKNOWN = "unknown"


class Event:
    action_country: str
    action_external_hostname: str
    action_file_macro_sha256: str
    action_file_md5: str
    action_file_name: str
    action_file_path: str
    action_file_sha256: str
    action_local_ip: str
    action_local_port: str
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
    action_remote_port: str
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
    agent_host_boot_time: str
    agent_install_type: str
    association_strength: str
    causality_actor_causality_id: str
    causality_actor_process_command_line: str
    causality_actor_process_execution_time: str
    causality_actor_process_image_md5: str
    causality_actor_process_image_name: str
    causality_actor_process_image_path: str
    causality_actor_process_image_sha256: str
    causality_actor_process_signature_status: str
    causality_actor_process_signature_vendor: str
    dns_query_name: str
    dst_action_country: str
    dst_action_external_hostname: str
    dst_action_external_port: str
    dst_agent_id: str
    dst_association_strength: str
    dst_causality_actor_process_execution_time: str
    event_id: str
    event_sub_type: str
    event_timestamp: int
    event_type: str
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
    module_id: str
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
    story_id: str
    user_name: str

    def __init__(self,
                 event_timestamp: int,
                 action_country: str = None,
                 action_external_hostname: str = None,
                 action_file_macro_sha256: str = None,
                 action_file_md5: str = None,
                 action_file_name: str = None,
                 action_file_path: str = None,
                 action_file_sha256: str = None,
                 action_local_ip: str = None,
                 action_local_port: str = None,
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
                 action_remote_port: str = None,
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
                 agent_host_boot_time: str = None,
                 agent_install_type: str = None,
                 association_strength: str = None,
                 causality_actor_causality_id: str = None,
                 causality_actor_process_command_line: str = None,
                 causality_actor_process_execution_time: str = None,
                 causality_actor_process_image_md5: str = None,
                 causality_actor_process_image_name: str = None,
                 causality_actor_process_image_path: str = None,
                 causality_actor_process_image_sha256: str = None,
                 causality_actor_process_signature_status: str = None,
                 causality_actor_process_signature_vendor: str = None,
                 dns_query_name: str = None,
                 dst_action_country: str = None,
                 dst_action_external_hostname: str = None,
                 dst_action_external_port: str = None,
                 dst_agent_id: str = None,
                 dst_association_strength: str = None,
                 dst_causality_actor_process_execution_time: str = None,
                 event_id: str = None,
                 event_sub_type: str = None,
                 event_type: str = None,
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
                 module_id: str = None,
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
                 story_id: str = None,
                 user_name: str = None,
                 ) -> None:
        self.action_country = action_country
        self.action_external_hostname = action_external_hostname
        self.action_file_macro_sha256 = action_file_macro_sha256
        self.action_file_md5 = action_file_md5
        self.action_file_name = action_file_name
        self.action_file_path = action_file_path
        self.action_file_sha256 = action_file_sha256
        self.action_local_ip = action_local_ip
        self.action_local_port = action_local_port
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
        self.agent_host_boot_time = agent_host_boot_time
        self.agent_install_type = agent_install_type
        self.association_strength = association_strength
        self.causality_actor_causality_id = causality_actor_causality_id
        self.causality_actor_process_command_line = causality_actor_process_command_line
        self.causality_actor_process_execution_time = causality_actor_process_execution_time
        self.causality_actor_process_image_md5 = causality_actor_process_image_md5
        self.causality_actor_process_image_name = causality_actor_process_image_name
        self.causality_actor_process_image_path = causality_actor_process_image_path
        self.causality_actor_process_image_sha256 = causality_actor_process_image_sha256
        self.causality_actor_process_signature_status = causality_actor_process_signature_status
        self.causality_actor_process_signature_vendor = causality_actor_process_signature_vendor
        self.dns_query_name = dns_query_name
        self.dst_action_country = dst_action_country
        self.dst_action_external_hostname = dst_action_external_hostname
        self.dst_action_external_port = dst_action_external_port
        self.dst_agent_id = dst_agent_id
        self.dst_association_strength = dst_association_strength
        self.dst_causality_actor_process_execution_time = dst_causality_actor_process_execution_time
        self.event_id = event_id
        self.event_sub_type = event_sub_type
        self.event_timestamp = event_timestamp
        self.event_type = event_type
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
        self.module_id = module_id
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
        self.story_id = story_id
        self.user_name = user_name

    @classmethod
    def from_json(cls, data: dict) -> "Event":
        return cls(**data)


class Alert:
    action: str
    action_pretty: str
    agent_data_collection_status: bool
    agent_device_domain: str
    agent_fqdn: str
    agent_is_vdi: str
    agent_os_sub_type: str
    agent_os_type: str
    agent_version: str
    alert_id: str
    attempt_counter: int
    bioc_category_enum_key: str
    bioc_indicator: str
    category: str
    contains_featured_host: bool
    contains_featured_ip: bool
    contains_featured_user: bool
    deduplicate_tokens: str
    description: str
    detection_timestamp: int
    end_match_attempt_ts: int
    endpoint_id: str
    events: List[Event]
    external_id: str
    filter_rule_id: str
    host_ip: List[str]
    host_name: str
    is_whitelisted: bool
    local_insert_ts: int
    mac: str
    mac_address: List[str]
    matching_service_rule_id: str
    matching_status: str
    mitre_tactic_id_and_name: List[str]
    mitre_technique_id_and_name: List[str]
    name: str
    severity: str
    source: str
    starred: bool

    def __init__(self,
                 action_pretty: str,
                 agent_data_collection_status: bool,
                 attempt_counter: int,
                 contains_featured_host: bool,
                 contains_featured_ip: bool,
                 contains_featured_user: bool,
                 detection_timestamp: int,
                 end_match_attempt_ts: int,
                 events: List[Event],
                 host_ip: List[str],
                 is_whitelisted: bool,
                 local_insert_ts: int,
                 mac_address: List[str],
                 mitre_tactic_id_and_name: List[str],
                 mitre_technique_id_and_name: List[str],
                 starred: bool,
                 action: str = None,
                 agent_device_domain: str = None,
                 agent_fqdn: str = None,
                 agent_is_vdi: str = None,
                 agent_os_sub_type: str = None,
                 agent_os_type: str = None,
                 agent_version: str = None,
                 alert_id: str = None,
                 bioc_category_enum_key: str = None,
                 bioc_indicator: str = None,
                 category: str = None,
                 deduplicate_tokens: str = None,
                 description: str = None,
                 endpoint_id: str = None,
                 external_id: str = None,
                 filter_rule_id: str = None,
                 host_name: str = None,
                 mac: str = None,
                 matching_service_rule_id: str = None,
                 matching_status: str = None,
                 name: str = None,
                 severity: str = None,
                 source: str = None,
                 ) -> None:
        self.action = action
        self.action_pretty = action_pretty
        self.agent_data_collection_status = agent_data_collection_status
        self.agent_device_domain = agent_device_domain
        self.agent_fqdn = agent_fqdn
        self.agent_is_vdi = agent_is_vdi
        self.agent_os_sub_type = agent_os_sub_type
        self.agent_os_type = agent_os_type
        self.agent_version = agent_version
        self.alert_id = alert_id
        self.attempt_counter = attempt_counter
        self.bioc_category_enum_key = bioc_category_enum_key
        self.bioc_indicator = bioc_indicator
        self.category = category
        self.contains_featured_host = contains_featured_host
        self.contains_featured_ip = contains_featured_ip
        self.contains_featured_user = contains_featured_user
        self.deduplicate_tokens = deduplicate_tokens
        self.description = description
        self.detection_timestamp = detection_timestamp
        self.end_match_attempt_ts = end_match_attempt_ts
        self.endpoint_id = endpoint_id
        self.events = events
        self.external_id = external_id
        self.filter_rule_id = filter_rule_id
        self.host_ip = host_ip
        self.host_name = host_name
        self.is_whitelisted = is_whitelisted
        self.local_insert_ts = local_insert_ts
        self.mac = mac
        self.mac_address = mac_address
        self.matching_service_rule_id = matching_service_rule_id
        self.matching_status = matching_status
        self.mitre_tactic_id_and_name = mitre_tactic_id_and_name
        self.mitre_technique_id_and_name = mitre_technique_id_and_name
        self.name = name
        self.severity = severity
        self.source = source
        self.starred = starred

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
