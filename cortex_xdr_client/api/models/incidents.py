from enum import Enum
from typing import List, Optional

from pydantic import BaseModel


class IncidentStatus(str, Enum):
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


class Incident(BaseModel):
    alert_categories: Optional[List[str]]
    alert_count: Optional[int]
    alerts_grouping_status: Optional[str]
    assigned_user_mail: Optional[str]
    assigned_user_pretty_name: Optional[str]
    creation_time: Optional[int]
    description: Optional[str]
    detection_time: Optional[int]
    high_severity_alert_count: Optional[int]
    host_count: Optional[int]
    hosts: Optional[List[str]]
    incident_id: Optional[str]
    incident_name: Optional[str]
    incident_sources: Optional[List[str]]
    low_severity_alert_count: Optional[int]
    manual_description: Optional[str]
    manual_score: Optional[int]
    manual_severity: Optional[str]
    med_severity_alert_count: Optional[int]
    mitre_tactics_ids_and_names: Optional[List[str]]
    mitre_techniques_ids_and_names: Optional[List[str]]
    modification_time: Optional[int]
    notes: Optional[str]
    resolve_comment: Optional[str]
    rule_based_score: Optional[int]
    severity: Optional[str]
    starred: Optional[bool]
    status: IncidentStatus
    user_count: Optional[int]
    users: Optional[List[str]]
    wildfire_hits: Optional[int]
    xdr_url: Optional[str]


class GetIncidentsResponseItem(BaseModel):
    total_count: Optional[int]
    result_count: Optional[int]
    incidents: List[Incident]


class GetIncidentsResponse(BaseModel):
    reply: GetIncidentsResponseItem


class AlertsDatum(BaseModel):
    action: Optional[str]
    action_country: Optional[str]
    action_external_hostname: Optional[str]
    action_file_macro_sha256: Optional[str]
    action_file_md5: Optional[str]
    action_file_name: Optional[str]
    action_file_path: Optional[str]
    action_file_sha256: Optional[str]
    action_local_ip: Optional[str]
    action_local_port: Optional[int]
    action_pretty: Optional[str]
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
    action_remote_port: Optional[int]
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
    agent_data_collection_status: Optional[str]
    agent_device_domain: Optional[str]
    agent_fqdn: Optional[str]
    agent_host_boot_time: Optional[str]
    agent_install_type: Optional[str]
    agent_is_vdi: Optional[str]
    agent_os_sub_type: Optional[str]
    agent_os_type: Optional[str]
    agent_version: Optional[str]
    alert_id: Optional[int]
    association_strength: Optional[str]
    attempt_counter: Optional[str]
    bioc_category_enum_key: Optional[str]
    bioc_indicator: Optional[str]
    case_id: Optional[int]
    category: Optional[str]
    causality_actor_causality_id: Optional[str]
    causality_actor_process_command_line: Optional[str]
    causality_actor_process_execution_time: Optional[str]
    causality_actor_process_image_md5: Optional[str]
    causality_actor_process_image_name: Optional[str]
    causality_actor_process_image_path: Optional[str]
    causality_actor_process_image_sha256: Optional[str]
    causality_actor_process_signature_status: Optional[str]
    causality_actor_process_signature_vendor: Optional[str]
    contains_featured_host: Optional[str]
    contains_featured_ip_address: Optional[str]
    contains_featured_user: Optional[str]
    deduplicate_tokens: Optional[str]
    description: Optional[str]
    detection_timestamp: Optional[int]
    dns_query_name: Optional[str]
    dst_action_country: Optional[str]
    dst_action_external_hostname: Optional[str]
    dst_action_external_port: Optional[str]
    dst_agent_id: Optional[str]
    dst_association_strength: Optional[str]
    dst_causality_actor_process_execution_time: Optional[str]
    end_match_attempt_ts: Optional[str]
    endpoint_id: Optional[str]
    event_id: Optional[str]
    event_sub_type: Optional[str]
    event_timestamp: Optional[str]
    event_type: Optional[str]
    external_id: Optional[str]
    filter_rule_id: Optional[str]
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
    host_ip: Optional[str]
    host_name: Optional[str]
    is_whitelisted: Optional[bool]
    local_insert_ts: Optional[int]
    mac: Optional[str]
    matching_service_rule_id: Optional[str]
    matching_status: Optional[str]
    mitre_tactic_id_and_name: Optional[str]
    mitre_technique_id_and_name: Optional[str]
    module_id: Optional[str]
    name: Optional[str]
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
    severity: Optional[str]
    source: Optional[str]
    starred: Optional[bool]
    story_id: Optional[str]
    user_name: Optional[str]


class NetworkArtifactsDatum(BaseModel):
    alert_count: Optional[int]
    is_manual: Optional[bool]
    network_country: Optional[str]
    network_domain: Optional[str]
    network_remote_ip: Optional[str]
    network_remote_port: Optional[int]
    type: Optional[str]


class AlertDatums(BaseModel):
    total_count: Optional[int]
    data: List[AlertsDatum]


class NetworkArtifacts(BaseModel):
    total_count: Optional[int]
    data: List[NetworkArtifactsDatum]


class GetExtraIncidentDataResponseItem(BaseModel):
    alerts: AlertDatums
    file_artifacts: AlertDatums
    incident: Incident
    network_artifacts: NetworkArtifacts


class GetExtraIncidentDataResponse(BaseModel):
    reply: GetExtraIncidentDataResponseItem
