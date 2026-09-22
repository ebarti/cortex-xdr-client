from enum import Enum
from typing import Any, List, Optional, Union

from pydantic import ConfigDict

from cortex_xdr_client.api.models.base import CortexResponseModel


class AlertSeverity(str, Enum):
    """
    Severity of an alert.
    """
    LOW = "low"
    MEDIUM = "medium"
    HIGH = "high"
    CRITICAL = "critical"
    UNKNOWN = "unknown"


class Event(CortexResponseModel):
    action_country: Optional[str] = None
    action_external_hostname: Optional[str] = None
    action_file_macro_sha256: Optional[str] = None
    action_file_md5: Optional[str] = None
    action_file_name: Optional[str] = None
    action_file_path: Optional[str] = None
    action_file_sha256: Optional[str] = None
    action_local_ip: Optional[str] = None
    action_local_port: Optional[str] = None
    action_process_causality_id: Optional[str] = None
    action_process_image_command_line: Optional[str] = None
    action_process_image_name: Optional[str] = None
    action_process_image_sha256: Optional[str] = None
    action_process_instance_id: Optional[str] = None
    action_process_signature_status: Optional[str] = None
    action_process_signature_vendor: Optional[str] = None
    action_registry_data: Optional[str] = None
    action_registry_full_key: Optional[str] = None
    action_registry_key_name: Optional[str] = None
    action_registry_value_name: Optional[str] = None
    action_remote_ip: Optional[str] = None
    action_remote_port: Optional[str] = None
    actor_causality_id: Optional[str] = None
    actor_process_causality_id: Optional[str] = None
    actor_process_command_line: Optional[str] = None
    actor_process_image_md5: Optional[str] = None
    actor_process_image_name: Optional[str] = None
    actor_process_image_path: Optional[str] = None
    actor_process_image_sha256: Optional[str] = None
    actor_process_instance_id: Optional[str] = None
    actor_process_os_pid: Optional[str] = None
    actor_process_signature_status: Optional[str] = None
    actor_process_signature_vendor: Optional[str] = None
    actor_thread_thread_id: Optional[str] = None
    agent_host_boot_time: Optional[str] = None
    agent_install_type: Optional[str] = None
    association_strength: Optional[str] = None
    causality_actor_causality_id: Optional[str] = None
    causality_actor_process_command_line: Optional[str] = None
    causality_actor_process_execution_time: Optional[str] = None
    causality_actor_process_image_md5: Optional[str] = None
    causality_actor_process_image_name: Optional[str] = None
    causality_actor_process_image_path: Optional[str] = None
    causality_actor_process_image_sha256: Optional[str] = None
    causality_actor_process_signature_status: Optional[str] = None
    causality_actor_process_signature_vendor: Optional[str] = None
    dns_query_name: Optional[str] = None
    dst_action_country: Optional[str] = None
    dst_action_external_hostname: Optional[str] = None
    dst_action_external_port: Optional[str] = None
    dst_agent_id: Optional[str] = None
    dst_association_strength: Optional[str] = None
    dst_causality_actor_process_execution_time: Optional[str] = None
    event_id: Optional[str] = None
    event_sub_type: Optional[str] = None
    event_timestamp: Optional[int] = None
    event_type: Optional[str] = None
    fw_app_category: Optional[str] = None
    fw_app_id: Optional[str] = None
    fw_app_subcategory: Optional[str] = None
    fw_app_technology: Optional[str] = None
    fw_device_name: Optional[str] = None
    fw_email_recipient: Optional[str] = None
    fw_email_sender: Optional[str] = None
    fw_email_subject: Optional[str] = None
    fw_interface_from: Optional[str] = None
    fw_interface_to: Optional[str] = None
    fw_is_phishing: Optional[str] = None
    fw_misc: Optional[str] = None
    fw_rule: Optional[str] = None
    fw_rule_id: Optional[str] = None
    fw_serial_number: Optional[str] = None
    fw_url_domain: Optional[str] = None
    fw_vsys: Optional[str] = None
    fw_xff: Optional[str] = None
    module_id: Optional[str] = None
    os_actor_causality_id: Optional[str] = None
    os_actor_effective_username: Optional[str] = None
    os_actor_process_causality_id: Optional[str] = None
    os_actor_process_command_line: Optional[str] = None
    os_actor_process_image_name: Optional[str] = None
    os_actor_process_image_path: Optional[str] = None
    os_actor_process_image_sha256: Optional[str] = None
    os_actor_process_instance_id: Optional[str] = None
    os_actor_process_os_pid: Optional[str] = None
    os_actor_process_signature_status: Optional[str] = None
    os_actor_process_signature_vendor: Optional[str] = None
    os_actor_thread_thread_id: Optional[str] = None
    story_id: Optional[str] = None
    user_name: Optional[str] = None


class AlertDescriptionItem(CortexResponseModel):
    pretty_name: str
    data_type: Optional[Any] = None
    render_type: str
    entity_map: Optional[Any] = None
    dml_ui: Optional[bool] = None
    dml_type: Optional[Any] = None


class Alert(CortexResponseModel):
    action: Optional[str] = None
    action_pretty: Optional[str] = None
    agent_data_collection_status: Optional[bool] = None
    agent_device_domain: Optional[str] = None
    agent_fqdn: Optional[str] = None
    agent_is_vdi: Optional[str] = None
    agent_os_sub_type: Optional[str] = None
    agent_os_type: Optional[str] = None
    agent_version: Optional[str] = None
    alert_id: Optional[str] = None
    attempt_counter: Optional[int] = None
    bioc_category_enum_key: Optional[str] = None
    bioc_indicator: Optional[str] = None
    category: Optional[str] = None
    contains_featured_host: Optional[bool] = None
    contains_featured_ip: Optional[bool] = None
    contains_featured_user: Optional[bool] = None
    deduplicate_tokens: Optional[str] = None
    description: Union[str, List[AlertDescriptionItem]]
    detection_timestamp: Optional[int] = None
    end_match_attempt_ts: Optional[int] = None
    endpoint_id: Optional[str] = None
    events: List[Event]
    external_id: Optional[str] = None
    filter_rule_id: Optional[str] = None
    host_ip: Optional[List[str]] = None
    host_name: Optional[str] = None
    is_whitelisted: Optional[bool] = None
    local_insert_ts: Optional[int] = None
    mac: Optional[str] = None
    mac_address: Optional[List[str]] = None
    matching_service_rule_id: Optional[str] = None
    matching_status: Optional[str] = None
    mitre_tactic_id_and_name: Optional[List[str]] = None
    mitre_technique_id_and_name: Optional[List[str]] = None
    name: Optional[str] = None
    severity: Optional[AlertSeverity] = None
    source: Optional[str] = None
    starred: Optional[bool] = None

    model_config = ConfigDict(use_enum_values=True)


class GetAlertsResponseItem(CortexResponseModel):
    total_count: Optional[int] = None
    result_count: Optional[int] = None
    alerts: List[Alert]


class GetAlertsResponse(CortexResponseModel):
    reply: GetAlertsResponseItem
