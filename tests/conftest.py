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
            "agent_fqdn":"tests",
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
               "127.0.0.1"
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

@pytest.fixture
def get_incidents_response():
    response = r"""
    { 
       "reply":{ 
          "total_count":1,
          "result_count":1,
          "incidents":[ 
             { 
                "incident_id":"<incident ID>",
                "incident_name": "tests",
                "creation_time":1577024425126,
                "modification_time":1577024425126,
                "detection_time":null,
                "status":"new",
                "severity":"medium",
                "description":"'Memory Corruption Exploit' generated by XDR Agent",
                "assigned_user_mail":null,
                "assigned_user_pretty_name":null,
                "alert_count":1,
                "low_severity_alert_count":0,
                "med_severity_alert_count":1,
                "high_severity_alert_count":0,
                "user_count":1,
                "host_count":1,
                "notes":null,
                "resolve_comment":null,
                "manual_severity":null,
                "manual_description":null,
                "xdr_url":"https://<link to incident>",
                "starred":false,
                "hosts":[ 
                   "<host ID>"
                ],
                "users":[
                "test_1",
                "test_2" 
                ],
                "incident_sources":[ 
                   "XDR Agent",
                   "XDR BIOC"
                ],
                "rule_based_score":342,
                "manual_score":null,
                "wildfire_hits": 0,
                    "alerts_grouping_status": "Enabled",
                    "mitre_techniques_ids_and_names": [
                        "TA0004 - Privilege Escalation",
                        "TA0005 - Defense Evasion",
                        "TA0006 - Credential Access"
                    ],
                    "mitre_tactics_ids_and_names": [
                        "T1001.001 - Data Obfuscation: Junk Data",
                        "T1001.002 - Data Obfuscation: Steganography",
                        "T1001.003 - Data Obfuscation: Protocol Impersonation"
                    ],
                    "alert_categories": [
                        "Collection",
                        "Credential Access",
                        "File Name"
                    ]
                }
          ]
       }
    }   
    """
    return json.loads(response)


@pytest.fixture
def get_incident_extra_data_response():
    response = r"""
    {
       "reply":{
          "incident":{
             "incident_id":"<incient ID>",
             "incident_name": "tests",
             "creation_time":1603184209710,
             "modification_time":1603184209710,
             "detection_time":null,
             "status":"new",
             "severity":"high",
             "description":"generated by PAN NGFW",
             "assigned_user_mail":null,
             "assigned_user_pretty_name":null,
             "alert_count":1,
             "low_severity_alert_count":0,
             "med_severity_alert_count":0,
             "high_severity_alert_count":1,
             "user_count":0,
             "host_count":0,
             "notes":null,
             "resolve_comment":null,
             "manual_severity":null,
             "manual_description":null,
             "xdr_url":"https://test.xdr.us.paloaltonetworks.com/incident-view/1",
             "starred":false,
             "hosts":null,
             "users":[
                
             ],
             "incident_sources":[
                "PAN NGFW"
             ],
             "rule_based_score":342,
             "manual_score":null, "wildfire_hits": 0,
                    "alerts_grouping_status": "Enabled",
                    "mitre_techniques_ids_and_names": [
                        "TA0004 - Privilege Escalation",
                        "TA0005 - Defense Evasion",
                        "TA0006 - Credential Access"
                    ],
                    "mitre_tactics_ids_and_names": [
                        "T1001.001 - Data Obfuscation: Junk Data",
                        "T1001.002 - Data Obfuscation: Steganography",
                        "T1001.003 - Data Obfuscation: Protocol Impersonation"
                    ],
                    "alert_categories": [
                        "Collection",
                        "Credential Access",
                        "File Name"
                    ]
         },
          "alerts":{
             "total_count":1,
             "data":[
                {
                   "external_id":"<external ID>",
                   "severity":"high",
                   "matching_status":"UNMATCHABLE",
                   "end_match_attempt_ts":null,
                   "local_insert_ts":1603175431,
                   "bioc_indicator":null,
                   "matching_service_rule_id":null,
                   "attempt_counter":null,
                   "bioc_category_enum_key":null,
                   "case_id":1,
                   "is_whitelisted":false,
                   "starred":false,
                   "deduplicate_tokens":"<token value>",
                   "filter_rule_id":null,
                   "mitre_technique_id_and_name":null,
                   "mitre_tactic_id_and_name":null,
                   "agent_version":null,
                   "agent_device_domain":null,
                   "agent_fqdn":null,
                   "agent_os_type":"NO_HOST",
                   "agent_os_sub_type":null,
                   "agent_data_collection_status":null,
                   "mac":null,
                   "agent_is_vdi":null,
                   "agent_install_type":"NA",
                   "agent_host_boot_time":null,
                   "event_sub_type":null,
                   "module_id":null,
                   "association_strength":null,
                   "dst_association_strength":null,
                   "story_id":null,
                   "event_id":null,
                   "event_type":"Network Event",
                   "event_timestamp":null,
                   "actor_process_instance_id":null,
                   "actor_process_image_path":null,
                   "actor_process_image_name":null,
                   "actor_process_command_line":null,
                   "actor_process_signature_status":"N/A",
                   "actor_process_signature_vendor":null,
                   "actor_process_image_sha256":null,
                   "actor_process_image_md5":null,
                   "actor_process_causality_id":null,
                   "actor_causality_id":null,
                   "actor_process_os_pid":null,
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
                   "action_local_ip":"127.0.0.1",
                   "action_local_port":80,
                   "action_remote_ip":"127.0.0.1",
                   "action_remote_port":80,
                   "action_external_hostname":"<hostname>",
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
                   "fw_serial_number":"<serial number>",
                   "fw_url_domain":null,
                   "fw_email_subject":"",
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
                   "alert_id":"1",
                   "detection_timestamp":1603184109000,
                   "name":"sagcalun",
                   "category":"Spyware Detected via Anti-Spyware profile",
                   "endpoint_id":null,
                   "description":"Spyware Phone Home Detection",
                   "host_ip":"127.0.0.1",
                   "host_name":"<hostname>",
                   "source":"PAN NGFW",
                   "action":"DETECTED_4",
                   "action_pretty":"Detected (Raised An Alert)",
                   "user_name":null, 
                   "contains_featured_host": "Yes",
                   "contains_featured_user": "Yes",
                   "contains_featured_ip_address": "Yes"
                }
             ]
          },
          "network_artifacts":{
             "total_count":2,
             "data":[
                {
                   "type":"DOMAIN",
                   "alert_count":1,
                   "is_manual":false,
                   "network_domain":"<domain name>",
                   "network_remote_ip":"127.0.0.1",
                   "network_remote_port":80,
                   "network_country":"UNKNOWN"
                },
                {
                   "type":"IP",
                   "alert_count":1,
                   "is_manual":false,
                   "network_domain":"<domain name>",
                   "network_remote_ip":"127.0.0.1",
                   "network_remote_port":80,
                   "network_country":"UNKNOWN"
                }
             ]
          },
          "file_artifacts":{
             "total_count":0,
             "data":[           
               ]
          }
       }
    }
    """
    return json.loads(response)


@pytest.fixture
def get_all_endpoints_response():
    response = r"""
    { 
       "reply":[ 
          { 
             "agent_id":"<agent ID>",
             "agent_status":"LOST",
             "host_name":"EX2",
             "agent_type":"Server",
             "ip":"127.0.0.1"
          },
          { 
             "agent_id":"<agent ID>",
             "agent_status":"LOST",
             "host_name":"EX1",
             "agent_type":"Server",
             "ip":"127.0.0.1"
          },
          { 
             "agent_id":"<agent ID>",
             "agent_status":"CONNECTED",
             "host_name":"<host name>",
             "agent_type":"Workstation",
             "ip":"127.0.0.1"
          },
          { 
             "agent_id":"<agent ID>",
             "agent_status":"CONNECTED",
             "host_name":"<host name>",
             "agent_type":"Workstation",
             "ip":"127.0.0.1"
          },
          { 
             "agent_id":"<agent ID>",
             "agent_status":"CONNECTED",
             "host_name":"<host Name>",
             "agent_type":"Workstation",
             "ip":"127.0.0.1"
          },
          { 
             "agent_id":"<agent ID>",
             "agent_status":"LOST",
             "host_name":"<host name>",
             "agent_type":"Workstation",
             "ip":"127.0.0.1"
          },
          { 
             "agent_id":"<agent ID>",
             "agent_status":"DISCONNECTED",
             "host_name":"<host name>",
             "agent_type":"Workstation",
             "ip":"127.0.0.1"
          }
       ]
    }
    """
    return json.loads(response)


@pytest.fixture
def get_endpoint_response():
    response = r"""
    {
       "reply":{
          "total_count":1,
          "result_count":1,
          "endpoints":[
             {
                "endpoint_id":"<endpoint ID>",
                "endpoint_name":"<endpoint name>",
                "endpoint_type":"<endpoint type>",
                "endpoint_status":"CONNECTED",
                "os_type":"AGENT_OS_WINDOWS",
                "ip":[
                   "127.0.0.1"
                ],
                "users":[
                   "XDR"
                ],
                "domain":"WORKGROUP",
                "alias":"",
                "first_seen":1606218761377,
                "last_seen":1606218769163,
                "content_version":"",
                "installation_package":"XDR",
                "active_directory":null,
                "install_date":1606218762089,
                "endpoint_version":"<version>",
                "is_isolated":"AGENT_UNISOLATED",
                "isolated_date":null,
                "group_name":[
                   
                ],
                "operational_status":"PARTIALLY_PROTECTED",
                "operational_status_description":"[{\"name\": \"generalStatus\", \"error_code\": 10004}]",
                "scan_status":"SCAN_STATUS_NONE"
             }
          ]
       }
    }
    """
    return json.loads(response)


@pytest.fixture
def get_isolate_endpoints_response():
    response = r"""
    {
        "reply": {
                "action_id":"<action ID>",
                "status": "1",
                "endpoints_count": "673"
            }
    }
    """
    return json.loads(response)


@pytest.fixture
def get_scan_endpoints_response():
    response = r"""
    {
        "reply": {
                "action_id":"<action ID>",
                "status": "1",
                "endpoints_count": "673"
            }
    }
    """
    return json.loads(response)
