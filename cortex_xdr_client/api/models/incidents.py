from enum import Enum
from typing import List, Optional

from cortex_xdr_client.api.models.base import CortexResponseModel


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


class Incident(CortexResponseModel):
    alert_categories: Optional[List[str]] = None
    alert_count: Optional[int] = None
    alerts_grouping_status: Optional[str] = None
    assigned_user_mail: Optional[str] = None
    assigned_user_pretty_name: Optional[str] = None
    creation_time: Optional[int] = None
    description: Optional[str] = None
    detection_time: Optional[int] = None
    high_severity_alert_count: Optional[int] = None
    host_count: Optional[int] = None
    hosts: Optional[List[str]] = None
    incident_id: Optional[str] = None
    incident_name: Optional[str] = None
    incident_sources: Optional[List[str]] = None
    low_severity_alert_count: Optional[int] = None
    manual_description: Optional[str] = None
    manual_score: Optional[int] = None
    manual_severity: Optional[str] = None
    med_severity_alert_count: Optional[int] = None
    mitre_tactics_ids_and_names: Optional[List[str]] = None
    mitre_techniques_ids_and_names: Optional[List[str]] = None
    modification_time: Optional[int] = None
    notes: Optional[str] = None
    resolve_comment: Optional[str] = None
    rule_based_score: Optional[int] = None
    severity: Optional[str] = None
    starred: Optional[bool] = None
    status: IncidentStatus
    user_count: Optional[int] = None
    users: Optional[List[str]] = None
    wildfire_hits: Optional[int] = None
    xdr_url: Optional[str] = None


class GetIncidentsResponseItem(CortexResponseModel):
    total_count: Optional[int] = None
    result_count: Optional[int] = None
    incidents: List[Incident]


class GetIncidentsResponse(CortexResponseModel):
    reply: GetIncidentsResponseItem


class AlertsDatum(CortexResponseModel):
    action: Optional[str] = None
    action_country: Optional[str] = None
    action_external_hostname: Optional[str] = None
    action_file_macro_sha256: Optional[str] = None
    action_file_md5: Optional[str] = None
    action_file_name: Optional[str] = None
    action_file_path: Optional[str] = None
    action_file_sha256: Optional[str] = None
    action_local_ip: Optional[str] = None
    action_local_port: Optional[int] = None
    action_pretty: Optional[str] = None
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
    action_remote_port: Optional[int] = None
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
    agent_data_collection_status: Optional[str] = None
    agent_device_domain: Optional[str] = None
    agent_fqdn: Optional[str] = None
    agent_host_boot_time: Optional[str] = None
    agent_install_type: Optional[str] = None
    agent_is_vdi: Optional[str] = None
    agent_os_sub_type: Optional[str] = None
    agent_os_type: Optional[str] = None
    agent_version: Optional[str] = None
    alert_id: Optional[int] = None
    association_strength: Optional[str] = None
    attempt_counter: Optional[str] = None
    bioc_category_enum_key: Optional[str] = None
    bioc_indicator: Optional[str] = None
    case_id: Optional[int] = None
    category: Optional[str] = None
    causality_actor_causality_id: Optional[str] = None
    causality_actor_process_command_line: Optional[str] = None
    causality_actor_process_execution_time: Optional[str] = None
    causality_actor_process_image_md5: Optional[str] = None
    causality_actor_process_image_name: Optional[str] = None
    causality_actor_process_image_path: Optional[str] = None
    causality_actor_process_image_sha256: Optional[str] = None
    causality_actor_process_signature_status: Optional[str] = None
    causality_actor_process_signature_vendor: Optional[str] = None
    contains_featured_host: Optional[str] = None
    contains_featured_ip_address: Optional[str] = None
    contains_featured_user: Optional[str] = None
    deduplicate_tokens: Optional[str] = None
    description: Optional[str] = None
    detection_timestamp: Optional[int] = None
    dns_query_name: Optional[str] = None
    dst_action_country: Optional[str] = None
    dst_action_external_hostname: Optional[str] = None
    dst_action_external_port: Optional[str] = None
    dst_agent_id: Optional[str] = None
    dst_association_strength: Optional[str] = None
    dst_causality_actor_process_execution_time: Optional[str] = None
    end_match_attempt_ts: Optional[str] = None
    endpoint_id: Optional[str] = None
    event_id: Optional[str] = None
    event_sub_type: Optional[str] = None
    event_timestamp: Optional[str] = None
    event_type: Optional[str] = None
    external_id: Optional[str] = None
    filter_rule_id: Optional[str] = None
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
    host_ip: Optional[str] = None
    host_name: Optional[str] = None
    is_whitelisted: Optional[bool] = None
    local_insert_ts: Optional[int] = None
    mac: Optional[str] = None
    matching_service_rule_id: Optional[str] = None
    matching_status: Optional[str] = None
    mitre_tactic_id_and_name: Optional[str] = None
    mitre_technique_id_and_name: Optional[str] = None
    module_id: Optional[str] = None
    name: Optional[str] = None
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
    severity: Optional[str] = None
    source: Optional[str] = None
    starred: Optional[bool] = None
    story_id: Optional[str] = None
    user_name: Optional[str] = None


class NetworkArtifactsDatum(CortexResponseModel):
    alert_count: Optional[int] = None
    is_manual: Optional[bool] = None
    network_country: Optional[str] = None
    network_domain: Optional[str] = None
    network_remote_ip: Optional[str] = None
    network_remote_port: Optional[int] = None
    type: Optional[str] = None


class AlertDatums(CortexResponseModel):
    total_count: Optional[int] = None
    data: List[AlertsDatum]


class NetworkArtifacts(CortexResponseModel):
    total_count: Optional[int] = None
    data: List[NetworkArtifactsDatum]


class GetExtraIncidentDataResponseItem(CortexResponseModel):
    alerts: AlertDatums
    file_artifacts: AlertDatums
    incident: Incident
    network_artifacts: NetworkArtifacts


class GetExtraIncidentDataResponse(CortexResponseModel):
    reply: GetExtraIncidentDataResponseItem
