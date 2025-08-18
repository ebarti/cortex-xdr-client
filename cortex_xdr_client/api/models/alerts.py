from enum import Enum
from typing import Any

from cortex_xdr_client.api.models.base import CustomBaseModel


class AlertSeverity(str, Enum):
    """
    Severity of an alert.
    """

    LOW = "low"
    MEDIUM = "medium"
    HIGH = "high"
    UNKNOWN = "unknown"


class QuerySortType(str, Enum):
    """
    XDR query sort type.
    """

    SEVERITY = "severity"
    CREATION_TIME = "creation_time"
    LAST_MODIFIED_TS = "last_modified_ts"


class QuerySortOrder(str, Enum):
    """
    XDR query sort order.
    """

    DESC = "desc"
    ASC = "asc"


class Event(CustomBaseModel):
    action_country: str | None = None
    action_external_hostname: str | None = None
    action_file_macro_sha256: str | None = None
    action_file_md5: str | None = None
    action_file_name: str | None = None
    action_file_path: str | None = None
    action_file_sha256: str | None = None
    action_local_ip: str | None = None
    action_local_port: str | None = None
    action_process_causality_id: str | None = None
    action_process_image_command_line: str | None = None
    action_process_image_name: str | None = None
    action_process_image_sha256: str | None = None
    action_process_instance_id: str | None = None
    action_process_signature_status: str | None = None
    action_process_signature_vendor: str | None = None
    action_registry_data: str | None = None
    action_registry_full_key: str | None = None
    action_registry_key_name: str | None = None
    action_registry_value_name: str | None = None
    action_remote_ip: str | None = None
    action_remote_port: str | None = None
    actor_causality_id: str | None = None
    actor_process_causality_id: str | None = None
    actor_process_command_line: str | None = None
    actor_process_image_md5: str | None = None
    actor_process_image_name: str | None = None
    actor_process_image_path: str | None = None
    actor_process_image_sha256: str | None = None
    actor_process_instance_id: str | None = None
    actor_process_os_pid: str | None = None
    actor_process_signature_status: str | None = None
    actor_process_signature_vendor: str | None = None
    actor_thread_thread_id: str | None = None
    agent_host_boot_time: str | None = None
    agent_install_type: str | None = None
    association_strength: str | None = None
    causality_actor_causality_id: str | None = None
    causality_actor_process_command_line: str | None = None
    causality_actor_process_execution_time: str | None = None
    causality_actor_process_image_md5: str | None = None
    causality_actor_process_image_name: str | None = None
    causality_actor_process_image_path: str | None = None
    causality_actor_process_image_sha256: str | None = None
    causality_actor_process_signature_status: str | None = None
    causality_actor_process_signature_vendor: str | None = None
    dns_query_name: str | None = None
    dst_action_country: str | None = None
    dst_action_external_hostname: str | None = None
    dst_action_external_port: str | None = None
    dst_agent_id: str | None = None
    dst_association_strength: str | None = None
    dst_causality_actor_process_execution_time: str | None = None
    event_id: str | None = None
    event_sub_type: str | None = None
    event_timestamp: int | None = None
    event_type: str | None = None
    fw_app_category: str | None = None
    fw_app_id: str | None = None
    fw_app_subcategory: str | None = None
    fw_app_technology: str | None = None
    fw_device_name: str | None = None
    fw_email_recipient: str | None = None
    fw_email_sender: str | None = None
    fw_email_subject: str | None = None
    fw_interface_from: str | None = None
    fw_interface_to: str | None = None
    fw_is_phishing: str | None = None
    fw_misc: str | None = None
    fw_rule: str | None = None
    fw_rule_id: str | None = None
    fw_serial_number: str | None = None
    fw_url_domain: str | None = None
    fw_vsys: str | None = None
    fw_xff: str | None = None
    module_id: str | None = None
    os_actor_causality_id: str | None = None
    os_actor_effective_username: str | None = None
    os_actor_process_causality_id: str | None = None
    os_actor_process_command_line: str | None = None
    os_actor_process_image_name: str | None = None
    os_actor_process_image_path: str | None = None
    os_actor_process_image_sha256: str | None = None
    os_actor_process_instance_id: str | None = None
    os_actor_process_os_pid: str | None = None
    os_actor_process_signature_status: str | None = None
    os_actor_process_signature_vendor: str | None = None
    os_actor_thread_thread_id: str | None = None
    story_id: str | None = None
    user_name: str | None = None


class AlertDescriptionItem(CustomBaseModel):
    pretty_name: str
    data_type: Any | None = None
    render_type: str
    entity_map: Any | None = None
    dml_ui: bool | None = None
    dml_type: str | None = None


class Alert(CustomBaseModel):
    action: str | None = None
    action_pretty: str | None = None
    agent_data_collection_status: bool | None = None
    agent_device_domain: str | None = None
    agent_fqdn: str | None = None
    agent_is_vdi: str | None = None
    agent_os_sub_type: str | None = None
    agent_os_type: str | None = None
    agent_version: str | None = None
    alert_id: str | None = None
    attempt_counter: int | None = None
    bioc_category_enum_key: str | None = None
    bioc_indicator: str | None = None
    category: str | None = None
    contains_featured_host: bool | None = None
    contains_featured_ip: bool | None = None
    contains_featured_user: bool | None = None
    deduplicate_tokens: str | None = None
    description: str | list[AlertDescriptionItem]
    detection_timestamp: int | None = None
    end_match_attempt_ts: int | None = None
    endpoint_id: str | None = None
    events: list[Event]
    external_id: str | None = None
    filter_rule_id: str | None = None
    host_ip: list[str] | None
    host_name: str | None = None
    is_whitelisted: bool | None = None
    local_insert_ts: int | None = None
    mac: str | None = None
    mac_address: list[str] | None = None
    matching_service_rule_id: str | None = None
    matching_status: str | None = None
    mitre_tactic_id_and_name: list[str] | None = None
    mitre_technique_id_and_name: list[str] | None = None
    name: str | None = None
    severity: AlertSeverity | None = None
    source: str | None = None
    starred: bool | None = None
    case_id: str | None = None
    agent_ip_addresses_v6: list[str] | None = None
    alert_type: str | None = None
    resolution_status: str | None = None
    tags: list[str] | None = None
    original_tags: list[str] | None = None
    malicious_urls: list[str] | None = None


class GetAlertsResponseItem(CustomBaseModel):
    total_count: int | None = None
    result_count: int | None = None
    alerts: list[Alert]


class GetAlertsResponse(CustomBaseModel):
    reply: GetAlertsResponseItem


class AlertV2(CustomBaseModel):
    external_id: str | None = None
    severity: str | None = None
    matching_status: str | None = None
    end_match_attempt_ts: int | None = None
    local_insert_ts: int | None = None
    last_modified_ts: int | None = None
    bioc_indicator: str | None = None
    matching_service_rule_id: str | None = None
    attempt_counter: int | None = None
    bioc_category_enum_key: str | None = None
    case_id: str | None = None
    is_whitelisted: bool | None = None
    starred: bool | None = None
    deduplicate_tokens: str | None = None
    filter_rule_id: list[str] | None = None
    mitre_technique_id_and_name: list[str] | None = None
    mitre_tactic_id_and_name: list[str] | None = None
    agent_version: str | None = None
    agent_ip_addresses_v6: list[str] | None = None
    agent_device_domain: str | None = None
    agent_fqdn: str | None = None
    agent_os_type: str | None = None
    agent_os_sub_type: str | None = None
    agent_data_collection_status: str | None = None
    agent_is_vdi: bool | None = None
    agent_install_type: str | None = None
    agent_host_boot_time: list[int] | None = None
    event_sub_type: list[int] | None = None
    module_id: list[str] | None = None
    association_strength: list[int] | None = None
    dst_association_strength: list[int] | None = None
    story_id: list[str] | None = None
    event_id: list[str] | None = None
    event_type: list[str] | None = None
    event_timestamp: list[int] | None = None
    actor_process_instance_id: list[str] | None = None
    actor_process_image_path: list[str] | None = None
    actor_process_image_name: list[str] | None = None
    actor_process_command_line: list[str] | None = None
    actor_process_signature_status: list[str] | None = None
    actor_process_signature_vendor: list[str] | None = None
    actor_process_image_sha256: list[str] | None = None
    actor_process_image_md5: list[str] | None = None
    actor_process_causality_id: list[str] | None = None
    actor_causality_id: list[str] | None = None
    actor_process_os_pid: list[int] | None = None
    actor_thread_thread_id: list[int] | None = None
    causality_actor_process_image_name: list[str] | None = None
    causality_actor_process_command_line: list[str] | None = None
    causality_actor_process_image_path: list[str] | None = None
    causality_actor_process_signature_vendor: list[str] | None = None
    causality_actor_process_signature_status: list[str] | None = None
    causality_actor_causality_id: list[str] | None = None
    causality_actor_process_execution_time: list[int] | None = None
    causality_actor_process_image_md5: list[str] | None = None
    causality_actor_process_image_sha256: list[str] | None = None
    action_file_path: list[str] | None = None
    action_file_name: list[str] | None = None
    action_file_md5: list[str] | None = None
    action_file_sha256: list[str] | None = None
    action_file_macro_sha256: list[str] | None = None
    action_registry_data: list[str] | None = None
    action_registry_key_name: list[str] | None = None
    action_registry_value_name: list[str] | None = None
    action_registry_full_key: list[str] | None = None
    action_local_ip: list[str] | None = None
    action_local_ip_v6: list[str] | None = None
    action_local_port: list[int] | None = None
    action_remote_ip: list[str] | None = None
    action_remote_ip_v6: list[str] | None = None
    action_remote_port: list[int] | None = None
    action_external_hostname: list[str] | None = None
    action_country: list[str] | None = None
    action_process_instance_id: list[str] | None = None
    action_process_causality_id: list[str] | None = None
    action_process_image_name: list[str] | None = None
    action_process_image_sha256: list[str] | None = None
    action_process_image_command_line: list[str] | None = None
    action_process_signature_status: list[str] | None = None
    action_process_signature_vendor: list[str] | None = None
    os_actor_effective_username: list[str] | None = None
    os_actor_process_instance_id: list[str] | None = None
    os_actor_process_image_path: list[str] | None = None
    os_actor_process_image_name: list[str] | None = None
    os_actor_process_command_line: list[str] | None = None
    os_actor_process_signature_status: list[str] | None = None
    os_actor_process_signature_vendor: list[str] | None = None
    os_actor_process_image_sha256: list[str] | None = None
    os_actor_process_causality_id: list[str] | None = None
    os_actor_causality_id: list[str] | None = None
    os_actor_process_os_pid: list[int] | None = None
    os_actor_thread_thread_id: list[int] | None = None
    fw_app_id: list[str] | None = None
    fw_interface_from: list[str] | None = None
    fw_interface_to: list[str] | None = None
    fw_rule: list[str] | None = None
    fw_rule_id: list[str] | None = None
    fw_device_name: list[str] | None = None
    fw_serial_number: list[str] | None = None
    fw_url_domain: list[str] | None = None
    fw_email_subject: list[str] | None = None
    fw_email_sender: list[str] | None = None
    fw_email_recipient: list[str] | None = None
    fw_app_subcategory: list[str] | None = None
    fw_app_category: list[str] | None = None
    fw_app_technology: list[str] | None = None
    fw_vsys: list[str] | None = None
    fw_xff: list[str] | None = None
    fw_misc: list[str] | None = None
    fw_is_phishing: list[str] | None = None
    dst_agent_id: list[str] | None = None
    dst_causality_actor_process_execution_time: list[int] | None = None
    dns_query_name: list[str] | None = None
    dst_action_external_hostname: list[str] | None = None
    dst_action_country: list[str] | None = None
    dst_action_external_port: list[int] | None = None
    is_pcap: bool | None = None
    contains_featured_host: list[str] | None = None
    contains_featured_user: list[str] | None = None
    contains_featured_ip: list[str] | None = None
    image_name: list[str] | None = None
    image_id: list[str] | None = None
    container_id: list[str] | None = None
    container_name: list[str] | None = None
    namespace: list[str] | None = None
    cluster_name: list[str] | None = None
    referenced_resource: list[str] | None = None
    operation_name: list[str] | None = None
    identity_sub_type: list[str] | None = None
    identity_type: list[str] | None = None
    project: list[str] | None = None
    cloud_provider: list[str] | None = None
    resource_type: list[str] | None = None
    resource_sub_type: list[str] | None = None
    user_agent: list[str] | None = None
    alert_type: str | None = None
    resolution_status: str | None = None
    resolution_comment: str | None = None
    dynamic_fields: dict | None = None
    tags: list[str] | None = None
    malicious_urls: list[str] | None = None
    alert_id: str | None = None
    detection_timestamp: int | None = None
    name: str | None = None
    category: str | None = None
    endpoint_id: str | None = None
    description: str | None = None
    host_ip: list[str] | None = None
    host_name: str | None = None
    action: str | None = None
    source: str | None = None
    original_tags: list[str] | None = None
    user_name: list[str] | None = None
    mac_addresses: str | None = None
    action_pretty: str | None = None


class GetAlertsResponseV2Item(CustomBaseModel):
    total_count: int | None = None
    result_count: int | None = None
    alerts: list[AlertV2]


class GetAlertsResponseV2(CustomBaseModel):
    reply: GetAlertsResponseV2Item
