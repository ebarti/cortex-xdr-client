from enum import Enum
from typing import Any
from typing import List
from typing import Optional
from typing import Union

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


class QuerySortOrder(str, Enum):
    """
    XDR query sort order.
    """
    DESC = "desc"
    ASC = "asc"


class Event(CustomBaseModel):
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


class AlertDescriptionItem(CustomBaseModel):
    pretty_name: str
    data_type: Optional[Any]
    render_type: str
    entity_map: Optional[Any]
    dml_ui: Optional[bool]
    dml_type: Optional[Any]


class Alert(CustomBaseModel):
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
    case_id: Optional[str]
    agent_ip_addresses_v6: Optional[list[str]]
    alert_type: Optional[str]
    resolution_status: Optional[str]
    tags: Optional[list[str]]
    original_tags: Optional[list[str]]
    malicious_urls: Optional[list[str]]


class GetAlertsResponseItem(CustomBaseModel):
    total_count: Optional[int]
    result_count: Optional[int]
    alerts: List[Alert]


class GetAlertsResponse(CustomBaseModel):
    reply: GetAlertsResponseItem


class AlertV2(CustomBaseModel):
    external_id: Optional[str] = None
    severity: Optional[str] = None
    matching_status: Optional[str] = None
    end_match_attempt_ts: Optional[int] = None
    local_insert_ts: Optional[int] = None
    last_modified_ts: Optional[int] = None
    bioc_indicator: Optional[str] = None
    matching_service_rule_id: Optional[str] = None
    attempt_counter: Optional[int] = None
    bioc_category_enum_key: Optional[str] = None
    case_id: Optional[str] = None
    is_whitelisted: Optional[bool] = None
    starred: Optional[bool] = None
    deduplicate_tokens: Optional[str] = None
    filter_rule_id: Optional[list[str]] = None
    mitre_technique_id_and_name: Optional[list[str]] = None
    mitre_tactic_id_and_name: Optional[list[str]] = None
    agent_version: Optional[str] = None
    agent_ip_addresses_v6: Optional[list[str]] = None
    agent_device_domain: Optional[str] = None
    agent_fqdn: Optional[str] = None
    agent_os_type: Optional[str] = None
    agent_os_sub_type: Optional[str] = None
    agent_data_collection_status: Optional[str] = None
    agent_is_vdi: Optional[bool] = None
    agent_install_type: Optional[str] = None
    agent_host_boot_time: Optional[list[int]] = None
    event_sub_type: Optional[list[int]] = None
    module_id: Optional[list[str]] = None
    association_strength: Optional[list[int]] = None
    dst_association_strength: Optional[list[int]] = None
    story_id: Optional[list[str]] = None
    event_id: Optional[list[str]] = None
    event_type: Optional[list[str]] = None
    event_timestamp: Optional[list[int]] = None
    actor_process_instance_id: Optional[list[str]] = None
    actor_process_image_path: Optional[list[str]] = None
    actor_process_image_name: Optional[list[str]] = None
    actor_process_command_line: Optional[list[str]] = None
    actor_process_signature_status: Optional[list[str]] = None
    actor_process_signature_vendor: Optional[list[str]] = None
    actor_process_image_sha256: Optional[list[str]] = None
    actor_process_image_md5: Optional[list[str]] = None
    actor_process_causality_id: Optional[list[str]] = None
    actor_causality_id: Optional[list[str]] = None
    actor_process_os_pid: Optional[list[int]] = None
    actor_thread_thread_id: Optional[list[int]] = None
    causality_actor_process_image_name: Optional[list[str]] = None
    causality_actor_process_command_line: Optional[list[str]] = None
    causality_actor_process_image_path: Optional[list[str]] = None
    causality_actor_process_signature_vendor: Optional[list[str]] = None
    causality_actor_process_signature_status: Optional[list[str]] = None
    causality_actor_causality_id: Optional[list[str]] = None
    causality_actor_process_execution_time: Optional[list[int]] = None
    causality_actor_process_image_md5: Optional[list[str]] = None
    causality_actor_process_image_sha256: Optional[list[str]] = None
    action_file_path: Optional[list[str]] = None
    action_file_name: Optional[list[str]] = None
    action_file_md5: Optional[list[str]] = None
    action_file_sha256: Optional[list[str]] = None
    action_file_macro_sha256: Optional[list[str]] = None
    action_registry_data: Optional[list[str]] = None
    action_registry_key_name: Optional[list[str]] = None
    action_registry_value_name: Optional[list[str]] = None
    action_registry_full_key: Optional[list[str]] = None
    action_local_ip: Optional[list[str]] = None
    action_local_ip_v6: Optional[list[str]] = None
    action_local_port: Optional[list[int]] = None
    action_remote_ip: Optional[list[str]] = None
    action_remote_ip_v6: Optional[list[str]] = None
    action_remote_port: Optional[list[int]] = None
    action_external_hostname: Optional[list[str]] = None
    action_country: Optional[list[str]] = None
    action_process_instance_id: Optional[list[str]] = None
    action_process_causality_id: Optional[list[str]] = None
    action_process_image_name: Optional[list[str]] = None
    action_process_image_sha256: Optional[list[str]] = None
    action_process_image_command_line: Optional[list[str]] = None
    action_process_signature_status: Optional[list[str]] = None
    action_process_signature_vendor: Optional[list[str]] = None
    os_actor_effective_username: Optional[list[str]] = None
    os_actor_process_instance_id: Optional[list[str]] = None
    os_actor_process_image_path: Optional[list[str]] = None
    os_actor_process_image_name: Optional[list[str]] = None
    os_actor_process_command_line: Optional[list[str]] = None
    os_actor_process_signature_status: Optional[list[str]] = None
    os_actor_process_signature_vendor: Optional[list[str]] = None
    os_actor_process_image_sha256: Optional[list[str]] = None
    os_actor_process_causality_id: Optional[list[str]] = None
    os_actor_causality_id: Optional[list[str]] = None
    os_actor_process_os_pid: Optional[list[int]] = None
    os_actor_thread_thread_id: Optional[list[int]] = None
    fw_app_id: Optional[list[str]] = None
    fw_interface_from: Optional[list[str]] = None
    fw_interface_to: Optional[list[str]] = None
    fw_rule: Optional[list[str]] = None
    fw_rule_id: Optional[list[str]] = None
    fw_device_name: Optional[list[str]] = None
    fw_serial_number: Optional[list[str]] = None
    fw_url_domain: Optional[list[str]] = None
    fw_email_subject: Optional[list[str]] = None
    fw_email_sender: Optional[list[str]] = None
    fw_email_recipient: Optional[list[str]] = None
    fw_app_subcategory: Optional[list[str]] = None
    fw_app_category: Optional[list[str]] = None
    fw_app_technology: Optional[list[str]] = None
    fw_vsys: Optional[list[str]] = None
    fw_xff: Optional[list[str]] = None
    fw_misc: Optional[list[str]] = None
    fw_is_phishing: Optional[list[str]] = None
    dst_agent_id: Optional[list[str]] = None
    dst_causality_actor_process_execution_time: Optional[list[int]] = None
    dns_query_name: Optional[list[str]] = None
    dst_action_external_hostname: Optional[list[str]] = None
    dst_action_country: Optional[list[str]] = None
    dst_action_external_port: Optional[list[int]] = None
    is_pcap: Optional[bool] = None
    contains_featured_host: Optional[list[str]] = None
    contains_featured_user: Optional[list[str]] = None
    contains_featured_ip: Optional[list[str]] = None
    image_name: Optional[list[str]] = None
    image_id: Optional[list[str]] = None
    container_id: Optional[list[str]] = None
    container_name: Optional[list[str]] = None
    namespace: Optional[list[str]] = None
    cluster_name: Optional[list[str]] = None
    referenced_resource: Optional[list[str]] = None
    operation_name: Optional[list[str]] = None
    identity_sub_type: Optional[list[str]] = None
    identity_type: Optional[list[str]] = None
    project: Optional[list[str]] = None
    cloud_provider: Optional[list[str]] = None
    resource_type: Optional[list[str]] = None
    resource_sub_type: Optional[list[str]] = None
    user_agent: Optional[list[str]] = None
    alert_type: Optional[str] = None
    resolution_status: Optional[str] = None
    resolution_comment: Optional[str] = None
    dynamic_fields: Optional[dict] = None
    tags: Optional[list[str]] = None
    malicious_urls: Optional[list[str]] = None
    alert_id: Optional[str] = None
    detection_timestamp: Optional[int] = None
    name: Optional[str] = None
    category: Optional[str] = None
    endpoint_id: Optional[str] = None
    description: Optional[str] = None
    host_ip: Optional[list[str]] = None
    host_name: Optional[str] = None
    action: Optional[str] = None
    source: Optional[str] = None
    original_tags: Optional[list[str]] = None
    user_name: Optional[list[str]] = None
    mac_addresses: Optional[str] = None
    action_pretty: Optional[str] = None


class GetAlertsResponseV2Item(CustomBaseModel):
    total_count: Optional[int]
    result_count: Optional[int]
    alerts: list[AlertV2]


class GetAlertsResponseV2(CustomBaseModel):
    reply: GetAlertsResponseV2Item
