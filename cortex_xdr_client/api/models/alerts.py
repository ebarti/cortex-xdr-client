from enum import Enum
from typing import Any, List, Optional, Union

from pydantic import BaseModel


class AlertSeverity(str, Enum):
    """
    Severity of an alert.
    """
    LOW = "low"
    MEDIUM = "medium"
    HIGH = "high"
    UNKNOWN = "unknown"


class Event(BaseModel):
    action_country: Optional[str]
    action_external_hostname: Optional[str]
    action_file_macro_sha256: Optional[str]
    action_file_md5: Optional[str]
    action_file_name: Optional[str]
    action_file_path: Optional[str]
    action_file_sha256: Optional[str]
    action_local_ip: Optional[str]
    action_local_port: Optional[str]
    action_process_causality_id: Optional[str]
    action_process_image_command_line: Optional[str]
    action_process_image_name: Optional[str]
    action_process_image_sha256: Optional[str]
    action_process_instance_id: Optional[str]
    action_process_signature_status: Optional[str]
    action_process_signature_vendor: Optional[str]
    action_registry_data: Optional[str]
    action_registry_full_key: Optional[str]
    action_registry_key_name: Optional[str]
    action_registry_value_name: Optional[str]
    action_remote_ip: Optional[str]
    action_remote_port: Optional[str]
    actor_causality_id: Optional[str]
    actor_process_causality_id: Optional[str]
    actor_process_command_line: Optional[str]
    actor_process_image_md5: Optional[str]
    actor_process_image_name: Optional[str]
    actor_process_image_path: Optional[str]
    actor_process_image_sha256: Optional[str]
    actor_process_instance_id: Optional[str]
    actor_process_os_pid: Optional[str]
    actor_process_signature_status: Optional[str]
    actor_process_signature_vendor: Optional[str]
    actor_thread_thread_id: Optional[str]
    agent_host_boot_time: Optional[str]
    agent_install_type: Optional[str]
    association_strength: Optional[str]
    causality_actor_causality_id: Optional[str]
    causality_actor_process_command_line: Optional[str]
    causality_actor_process_execution_time: Optional[str]
    causality_actor_process_image_md5: Optional[str]
    causality_actor_process_image_name: Optional[str]
    causality_actor_process_image_path: Optional[str]
    causality_actor_process_image_sha256: Optional[str]
    causality_actor_process_signature_status: Optional[str]
    causality_actor_process_signature_vendor: Optional[str]
    dns_query_name: Optional[str]
    dst_action_country: Optional[str]
    dst_action_external_hostname: Optional[str]
    dst_action_external_port: Optional[str]
    dst_agent_id: Optional[str]
    dst_association_strength: Optional[str]
    dst_causality_actor_process_execution_time: Optional[str]
    event_id: Optional[str]
    event_sub_type: Optional[str]
    event_timestamp: Optional[int]
    event_type: Optional[str]
    fw_app_category: Optional[str]
    fw_app_id: Optional[str]
    fw_app_subcategory: Optional[str]
    fw_app_technology: Optional[str]
    fw_device_name: Optional[str]
    fw_email_recipient: Optional[str]
    fw_email_sender: Optional[str]
    fw_email_subject: Optional[str]
    fw_interface_from: Optional[str]
    fw_interface_to: Optional[str]
    fw_is_phishing: Optional[str]
    fw_misc: Optional[str]
    fw_rule: Optional[str]
    fw_rule_id: Optional[str]
    fw_serial_number: Optional[str]
    fw_url_domain: Optional[str]
    fw_vsys: Optional[str]
    fw_xff: Optional[str]
    module_id: Optional[str]
    os_actor_causality_id: Optional[str]
    os_actor_effective_username: Optional[str]
    os_actor_process_causality_id: Optional[str]
    os_actor_process_command_line: Optional[str]
    os_actor_process_image_name: Optional[str]
    os_actor_process_image_path: Optional[str]
    os_actor_process_image_sha256: Optional[str]
    os_actor_process_instance_id: Optional[str]
    os_actor_process_os_pid: Optional[str]
    os_actor_process_signature_status: Optional[str]
    os_actor_process_signature_vendor: Optional[str]
    os_actor_thread_thread_id: Optional[str]
    story_id: Optional[str]
    user_name: Optional[str]


class AlertDescriptionItem(BaseModel):
    pretty_name: str
    data_type: Optional[Any]
    render_type: str
    entity_map: Optional[Any]
    dml_ui: Optional[bool]
    dml_type: Optional[Any]


class Alert(BaseModel):
    action: Optional[str]
    action_pretty: Optional[str]
    agent_data_collection_status: Optional[bool]
    agent_device_domain: Optional[str]
    agent_fqdn: Optional[str]
    agent_is_vdi: Optional[str]
    agent_os_sub_type: Optional[str]
    agent_os_type: Optional[str]
    agent_version: Optional[str]
    alert_id: Optional[str]
    attempt_counter: Optional[int]
    bioc_category_enum_key: Optional[str]
    bioc_indicator: Optional[str]
    category: Optional[str]
    contains_featured_host: Optional[bool]
    contains_featured_ip: Optional[bool]
    contains_featured_user: Optional[bool]
    deduplicate_tokens: Optional[str]
    description: Union[str, List[AlertDescriptionItem]]
    detection_timestamp: Optional[int]
    end_match_attempt_ts: Optional[int]
    endpoint_id: Optional[str]
    events: List[Event]
    external_id: Optional[str]
    filter_rule_id: Optional[str]
    host_ip: Optional[List[str]]
    host_name: Optional[str]
    is_whitelisted: Optional[bool]
    local_insert_ts: Optional[int]
    mac: Optional[str]
    mac_address: Optional[List[str]]
    matching_service_rule_id: Optional[str]
    matching_status: Optional[str]
    mitre_tactic_id_and_name: Optional[List[str]]
    mitre_technique_id_and_name: Optional[List[str]]
    name: Optional[str]
    severity: Optional[AlertSeverity]
    source: Optional[str]
    starred: Optional[bool]

    class Config:
        use_enum_values = True


class GetAlertsResponseItem(BaseModel):
    total_count: Optional[int]
    result_count: Optional[int]
    alerts: List[Alert]


class GetAlertsResponse(BaseModel):
    reply: GetAlertsResponseItem
