import json

import pytest

from cortex.client import CortexXDRClient


@pytest.fixture
def cortex_client():
    return CortexXDRClient("a_key_id", "a_key", "a_fqdn")


@pytest.fixture
def get_alerts_response():
    response = r"""
{
   "reply":{
      "total_count":45,
      "result_count":1,
      "alerts":[
         {
            "external_id":"<external ID>",
            "severity":"high",
            "matching_status":"FAILED",
            "end_match_attempt_ts":1603552062824,
            "local_insert_ts":1603279967500,
            "bioc_indicator":null,
            "matching_service_rule_id":null,
            "attempt_counter":55,
            "bioc_category_enum_key":null,
            "is_whitelisted":false,
            "starred":false,
            "deduplicate_tokens":null,
            "filter_rule_id":null,
            "mitre_technique_id_and_name":[
               ""
            ],
            "mitre_tactic_id_and_name":[
               ""
            ],
            "agent_version":"<agent version>",
            "agent_device_domain":null,
            "agent_fqdn":"test",
            "agent_os_type":"Windows",
            "agent_os_sub_type":"<os subtype>",
            "agent_data_collection_status":true,
            "mac":null,
            "mac_address": [
               "<mac address>"
            ],
            "agent_is_vdi": null,
            "contains_featured_host": true,
            "contains_featured_user": true,
            "contains_featured_ip": true,
            "events":[
               {
                  "agent_install_type":"NA",
                  "agent_host_boot_time":null,
                  "event_sub_type":null,
                  "module_id":"Privilege Escalation Protection",
                  "association_strength":null,
                  "dst_association_strength":null,
                  "story_id":null,
                  "event_id":null,
                  "event_type":"Process Execution",
                  "event_timestamp":1603279888980,
                  "actor_process_instance_id":"<instance ID>",
                  "actor_process_image_path":"c:\\<file path>\\virus.exe",
                  "actor_process_image_name":"virus.exe",
                  "actor_process_command_line":"c:\\<file path>\\virus.exe",
                  "actor_process_signature_status":"N/A",
                  "actor_process_signature_vendor":null,
                  "actor_process_image_sha256":"<SHA256 value>",
                  "actor_process_image_md5":null,
                  "actor_process_causality_id":null,
                  "actor_causality_id":null,
                  "actor_process_os_pid":"<PID>",
                  "actor_thread_thread_id":null,
                  "causality_actor_process_image_name":null,
                  "causality_actor_process_command_line":null,
                  "causality_actor_process_image_path":null,
                  "causality_actor_process_signature_vendor":null,
                  "causality_actor_process_signature_status":"N/A",
                  "causality_actor_causality_id":null,
                  "causality_actor_process_execution_time":null,
                  "causality_actor_process_image_md5":null,
                  "causality_actor_process_image_sha256":null,
                  "action_file_path":null,
                  "action_file_name":null,
                  "action_file_md5":null,
                  "action_file_sha256":null,
                  "action_file_macro_sha256":null,
                  "action_registry_data":null,
                  "action_registry_key_name":null,
                  "action_registry_value_name":null,
                  "action_registry_full_key":null,
                  "action_local_ip":null,
                  "action_local_port":null,
                  "action_remote_ip":null,
                  "action_remote_port":null,
                  "action_external_hostname":null,
                  "action_country":"UNKNOWN",
                  "action_process_instance_id":null,
                  "action_process_causality_id":null,
                  "action_process_image_name":null,
                  "action_process_image_sha256":null,
                  "action_process_image_command_line":null,
                  "action_process_signature_status":"N/A",
                  "action_process_signature_vendor":null,
                  "os_actor_effective_username":null,
                  "os_actor_process_instance_id":null,
                  "os_actor_process_image_path":null,
                  "os_actor_process_image_name":null,
                  "os_actor_process_command_line":null,
                  "os_actor_process_signature_status":"N/A",
                  "os_actor_process_signature_vendor":null,
                  "os_actor_process_image_sha256":null,
                  "os_actor_process_causality_id":null,
                  "os_actor_causality_id":null,
                  "os_actor_process_os_pid":null,
                  "os_actor_thread_thread_id":null,
                  "fw_app_id":null,
                  "fw_interface_from":null,
                  "fw_interface_to":null,
                  "fw_rule":null,
                  "fw_rule_id":null,
                  "fw_device_name":null,
                  "fw_serial_number":null,
                  "fw_url_domain":null,
                  "fw_email_subject":null,
                  "fw_email_sender":null,
                  "fw_email_recipient":null,
                  "fw_app_subcategory":null,
                  "fw_app_category":null,
                  "fw_app_technology":null,
                  "fw_vsys":null,
                  "fw_xff":null,
                  "fw_misc":null,
                  "fw_is_phishing":"N/A",
                  "dst_agent_id":null,
                  "dst_causality_actor_process_execution_time":null,
                  "dns_query_name":null,
                  "dst_action_external_hostname":null,
                  "dst_action_country":null,
                  "dst_action_external_port":null,
                  "user_name":null
               }
            ],
            "alert_id":"<alert ID>",
            "detection_timestamp":1603279888980,
            "name":"Kernel Privilege Escalation",
            "category":"Exploit",
            "endpoint_id":"<endpoint ID>",
            "description":"Local privilege escalation prevented",
            "host_ip":[
               "<IP address>"
            ],
            "host_name":"Test",
            "source":"XDR Agent",
            "action":"BLOCKED",
            "action_pretty":"Prevented (Blocked)"
         }
      ]
   }
}
    """
    return json.loads(response)
