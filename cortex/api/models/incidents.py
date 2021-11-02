from typing import List


class Incident:
    incident_id: str
    incident_name: str
    creation_time: int
    modification_time: int
    detection_time: None
    status: str
    severity: str
    description: str
    assigned_user_mail: None
    assigned_user_pretty_name: None
    alert_count: int
    low_severity_alert_count: int
    med_severity_alert_count: int
    high_severity_alert_count: int
    user_count: int
    host_count: int
    notes: None
    resolve_comment: None
    manual_severity: None
    manual_description: None
    xdr_url: str
    starred: bool
    hosts: List[str]
    users: List[str]
    incident_sources: List[str]
    rule_based_score: int
    manual_score: None
    wildfire_hits: int
    alerts_grouping_status: str
    mitre_techniques_ids_and_names: List[str]
    mitre_tactics_ids_and_names: List[str]
    alert_categories: List[str]

    def __init__(self, incident_id: str, incident_name: str, creation_time: int, modification_time: int, detection_time: None, status: str, severity: str, description: str, assigned_user_mail: None, assigned_user_pretty_name: None, alert_count: int, low_severity_alert_count: int, med_severity_alert_count: int, high_severity_alert_count: int, user_count: int, host_count: int, notes: None, resolve_comment: None, manual_severity: None, manual_description: None, xdr_url: str, starred: bool, hosts: List[str], users: List[str], incident_sources: List[str], rule_based_score: int, manual_score: None, wildfire_hits: int, alerts_grouping_status: str, mitre_techniques_ids_and_names: List[str], mitre_tactics_ids_and_names: List[str], alert_categories: List[str]) -> None:
        self.incident_id = incident_id
        self.incident_name = incident_name
        self.creation_time = creation_time
        self.modification_time = modification_time
        self.detection_time = detection_time
        self.status = status
        self.severity = severity
        self.description = description
        self.assigned_user_mail = assigned_user_mail
        self.assigned_user_pretty_name = assigned_user_pretty_name
        self.alert_count = alert_count
        self.low_severity_alert_count = low_severity_alert_count
        self.med_severity_alert_count = med_severity_alert_count
        self.high_severity_alert_count = high_severity_alert_count
        self.user_count = user_count
        self.host_count = host_count
        self.notes = notes
        self.resolve_comment = resolve_comment
        self.manual_severity = manual_severity
        self.manual_description = manual_description
        self.xdr_url = xdr_url
        self.starred = starred
        self.hosts = hosts
        self.users = users
        self.incident_sources = incident_sources
        self.rule_based_score = rule_based_score
        self.manual_score = manual_score
        self.wildfire_hits = wildfire_hits
        self.alerts_grouping_status = alerts_grouping_status
        self.mitre_techniques_ids_and_names = mitre_techniques_ids_and_names
        self.mitre_tactics_ids_and_names = mitre_tactics_ids_and_names
        self.alert_categories = alert_categories

    @classmethod
    def from_json(cls, data: dict) -> "Incident":
        return cls(**data)


class GetIncidentsResponseItem:
    total_count: int
    result_count: int
    incidents: List[Incident]

    def __init__(self, total_count: int, result_count: int, incidents: List[Incident]) -> None:
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
    external_id: str
    severity: str
    matching_status: str
    end_match_attempt_ts: None
    local_insert_ts: int
    bioc_indicator: None
    matching_service_rule_id: None
    attempt_counter: None
    bioc_category_enum_key: None
    case_id: int
    is_whitelisted: bool
    starred: bool
    deduplicate_tokens: str
    filter_rule_id: None
    mitre_technique_id_and_name: None
    mitre_tactic_id_and_name: None
    agent_version: None
    agent_device_domain: None
    agent_fqdn: None
    agent_os_type: str
    agent_os_sub_type: None
    agent_data_collection_status: None
    mac: None
    agent_is_vdi: None
    agent_install_type: str
    agent_host_boot_time: None
    event_sub_type: None
    module_id: None
    association_strength: None
    dst_association_strength: None
    story_id: None
    event_id: None
    event_type: str
    event_timestamp: None
    actor_process_instance_id: None
    actor_process_image_path: None
    actor_process_image_name: None
    actor_process_command_line: None
    actor_process_signature_status: str
    actor_process_signature_vendor: None
    actor_process_image_sha256: None
    actor_process_image_md5: None
    actor_process_causality_id: None
    actor_causality_id: None
    actor_process_os_pid: None
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
    action_local_ip: str
    action_local_port: int
    action_remote_ip: str
    action_remote_port: int
    action_external_hostname: str
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
    fw_serial_number: str
    fw_url_domain: None
    fw_email_subject: str
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
    alert_id: int
    detection_timestamp: int
    name: str
    category: str
    endpoint_id: None
    description: str
    host_ip: str
    host_name: str
    source: str
    action: str
    action_pretty: str
    user_name: None
    contains_featured_host: str
    contains_featured_user: str
    contains_featured_ip_address: str

    def __init__(self, external_id: str, severity: str, matching_status: str, end_match_attempt_ts: None, local_insert_ts: int, bioc_indicator: None, matching_service_rule_id: None, attempt_counter: None, bioc_category_enum_key: None, case_id: int, is_whitelisted: bool, starred: bool, deduplicate_tokens: str, filter_rule_id: None, mitre_technique_id_and_name: None, mitre_tactic_id_and_name: None, agent_version: None, agent_device_domain: None, agent_fqdn: None, agent_os_type: str, agent_os_sub_type: None, agent_data_collection_status: None, mac: None, agent_is_vdi: None, agent_install_type: str, agent_host_boot_time: None, event_sub_type: None, module_id: None, association_strength: None, dst_association_strength: None, story_id: None, event_id: None, event_type: str, event_timestamp: None, actor_process_instance_id: None, actor_process_image_path: None, actor_process_image_name: None, actor_process_command_line: None, actor_process_signature_status: str, actor_process_signature_vendor: None, actor_process_image_sha256: None, actor_process_image_md5: None, actor_process_causality_id: None, actor_causality_id: None, actor_process_os_pid: None, actor_thread_thread_id: None, causality_actor_process_image_name: None, causality_actor_process_command_line: None, causality_actor_process_image_path: None, causality_actor_process_signature_vendor: None, causality_actor_process_signature_status: str, causality_actor_causality_id: None, causality_actor_process_execution_time: None, causality_actor_process_image_md5: None, causality_actor_process_image_sha256: None, action_file_path: None, action_file_name: None, action_file_md5: None, action_file_sha256: None, action_file_macro_sha256: None, action_registry_data: None, action_registry_key_name: None, action_registry_value_name: None, action_registry_full_key: None, action_local_ip: str, action_local_port: int, action_remote_ip: str, action_remote_port: int, action_external_hostname: str, action_country: str, action_process_instance_id: None, action_process_causality_id: None, action_process_image_name: None, action_process_image_sha256: None, action_process_image_command_line: None, action_process_signature_status: str, action_process_signature_vendor: None, os_actor_effective_username: None, os_actor_process_instance_id: None, os_actor_process_image_path: None, os_actor_process_image_name: None, os_actor_process_command_line: None, os_actor_process_signature_status: str, os_actor_process_signature_vendor: None, os_actor_process_image_sha256: None, os_actor_process_causality_id: None, os_actor_causality_id: None, os_actor_process_os_pid: None, os_actor_thread_thread_id: None, fw_app_id: None, fw_interface_from: None, fw_interface_to: None, fw_rule: None, fw_rule_id: None, fw_device_name: None, fw_serial_number: str, fw_url_domain: None, fw_email_subject: str, fw_email_sender: None, fw_email_recipient: None, fw_app_subcategory: None, fw_app_category: None, fw_app_technology: None, fw_vsys: None, fw_xff: None, fw_misc: None, fw_is_phishing: str, dst_agent_id: None, dst_causality_actor_process_execution_time: None, dns_query_name: None, dst_action_external_hostname: None, dst_action_country: None, dst_action_external_port: None, alert_id: int, detection_timestamp: int, name: str, category: str, endpoint_id: None, description: str, host_ip: str, host_name: str, source: str, action: str, action_pretty: str, user_name: None, contains_featured_host: str, contains_featured_user: str, contains_featured_ip_address: str) -> None:
        self.external_id = external_id
        self.severity = severity
        self.matching_status = matching_status
        self.end_match_attempt_ts = end_match_attempt_ts
        self.local_insert_ts = local_insert_ts
        self.bioc_indicator = bioc_indicator
        self.matching_service_rule_id = matching_service_rule_id
        self.attempt_counter = attempt_counter
        self.bioc_category_enum_key = bioc_category_enum_key
        self.case_id = case_id
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
        self.agent_is_vdi = agent_is_vdi
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
        self.user_name = user_name
        self.contains_featured_host = contains_featured_host
        self.contains_featured_user = contains_featured_user
        self.contains_featured_ip_address = contains_featured_ip_address

    @classmethod
    def from_json(cls, data: dict) -> "AlertsDatum":
        return cls(**data)


class NetworkArtifactsDatum:
    type: str
    alert_count: int
    is_manual: bool
    network_domain: str
    network_remote_ip: str
    network_remote_port: int
    network_country: str

    def __init__(self, type: str, alert_count: int, is_manual: bool, network_domain: str, network_remote_ip: str, network_remote_port: int, network_country: str) -> None:
        self.type = type
        self.alert_count = alert_count
        self.is_manual = is_manual
        self.network_domain = network_domain
        self.network_remote_ip = network_remote_ip
        self.network_remote_port = network_remote_port
        self.network_country = network_country

    @classmethod
    def from_json(cls, data: dict) -> "NetworkArtifactsDatum":
        return cls(**data)


class AlertDatums:
    total_count: int
    data: List[AlertsDatum]

    def __init__(self, total_count: int, data: List[AlertsDatum]) -> None:
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

    def __init__(self, total_count: int, data: List[NetworkArtifactsDatum]) -> None:
        self.total_count = total_count
        self.data = data

    @classmethod
    def from_json(cls, data: dict) -> "NetworkArtifacts":
        total_count = data["total_count"]
        artifacts = list(map(NetworkArtifactsDatum.from_json, data["data"]))
        return cls(total_count=total_count, data=artifacts)


class GetExtraIncidentDataResponseItem:
    incident: Incident
    alerts: AlertDatums
    network_artifacts: NetworkArtifacts
    file_artifacts: AlertDatums

    def __init__(self, incident: Incident, alerts: AlertDatums, network_artifacts: NetworkArtifacts, file_artifacts: AlertDatums) -> None:
        self.incident = incident
        self.alerts = alerts
        self.network_artifacts = network_artifacts
        self.file_artifacts = file_artifacts

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