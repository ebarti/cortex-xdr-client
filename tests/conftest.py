import gzip
import json
from unittest.mock import MagicMock, patch

import pytest

from cortex_xdr_client.api.alerts_api import AlertsAPI
from cortex_xdr_client.api.authentication import Authentication
from cortex_xdr_client.api.endpoints_api import EndpointsAPI
from cortex_xdr_client.api.incidents_api import IncidentsAPI
from cortex_xdr_client.api.ioc_api import IocAPI
from cortex_xdr_client.api.scripts_api import ScriptsAPI
from cortex_xdr_client.api.xql_api import XQLAPI
from cortex_xdr_client.client import CortexXDRClient


@pytest.fixture
def auth():
    return Authentication(api_key="a_key", api_key_id="a_key_id")


@pytest.fixture
def get_url():
    mock = MagicMock()
    with patch('cortex_xdr_client.api.base_api.BaseAPI._get_url', mock):
        yield mock


@pytest.fixture
def successful_response():
    mock = MagicMock()
    mock.return_value = {
        "Prefer":       "code=200",
        "Content-Type": "application/json",
        "Accept":       "application/json"
    }
    with patch('cortex_xdr_client.api.authentication.Authentication.get_headers', mock):
        yield mock


@pytest.fixture
def cortex_client(auth):
    return CortexXDRClient(auth, "a_fqdn")


@pytest.fixture
def incidents_api(auth):
    return IncidentsAPI(auth, "a_fqdn")


@pytest.fixture
def alerts_api(auth):
    return AlertsAPI(auth, "a_fqdn")


@pytest.fixture
def endpoints_api(auth):
    return EndpointsAPI(auth, "a_fqdn")


@pytest.fixture
def ioc_api(auth):
    return IocAPI(auth, "a_fqdn")


@pytest.fixture
def scripts_api(auth):
    return ScriptsAPI(auth, "a_fqdn")


@pytest.fixture
def xql_api(auth):
    return XQLAPI(auth, "a_fqdn")


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
         },
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
            "description":[
                {
                  "pretty_name": "Process",
                  "data_type": null,
                  "render_type": "entity",
                  "entity_map": null,
                  "dml_ui": false
                },
                {
                  "pretty_name": "action type",
                  "data_type": null,
                  "render_type": "attribute",
                  "entity_map": null,
                  "dml_type": null
                },
                {
                  "pretty_name": "=",
                  "data_type": null,
                  "render_type": "operator",
                  "entity_map": null
                },
                {
                  "pretty_name": "execution",
                  "data_type": null,
                  "render_type": "value",
                  "entity_map": null
                },
                {
                  "pretty_name": "AND",
                  "data_type": null,
                  "render_type": "connector",
                  "entity_map": null
                },
                {
                  "pretty_name": "target process cmd",
                  "data_type": "TEXT",
                  "render_type": "attribute",
                  "entity_map": "attributes",
                  "dml_type": null
                },
                {
                  "pretty_name": "=",
                  "data_type": null,
                  "render_type": "operator",
                  "entity_map": "attributes"
                },
                {
                  "pretty_name": "*vbscript.encode*",
                  "data_type": null,
                  "render_type": "value",
                  "entity_map": "attributes"
                }
            ],
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
             "ip":["127.0.0.1"]
          },
          { 
             "agent_id":"<agent ID>",
             "agent_status":"LOST",
             "host_name":"EX1",
             "agent_type":"Server",
             "ip":["127.0.0.1"]
          },
          { 
             "agent_id":"<agent ID>",
             "agent_status":"CONNECTED",
             "host_name":"<host name>",
             "agent_type":"Workstation",
             "ip":["127.0.0.1"]
          },
          { 
             "agent_id":"<agent ID>",
             "agent_status":"CONNECTED",
             "host_name":"<host name>",
             "agent_type":"Workstation",
             "ip":["127.0.0.1"]
          },
          { 
             "agent_id":"<agent ID>",
             "agent_status":"CONNECTED",
             "host_name":"<host Name>",
             "agent_type":"Workstation",
             "ip":["127.0.0.1"]
          },
          { 
             "agent_id":"<agent ID>",
             "agent_status":"LOST",
             "host_name":"<host name>",
             "agent_type":"Workstation",
             "ip":["127.0.0.1"]
          },
          { 
             "agent_id":"<agent ID>",
             "agent_status":"DISCONNECTED",
             "host_name":"<host name>",
             "agent_type":"Workstation",
             "ip":["127.0.0.1"]
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


@pytest.fixture
def get_scripts_response():
    response = r"""
    {
   "reply":{
      "total_count": 129,
      "result_count":24,
      "scripts":[
         {
            "script_id":1,
            "name":"list_directories",
            "description":"List all directories under path",
            "modification_date":1585074627259,
            "created_by":"Palo Alto Networks",
            "is_high_risk":false,
            "windows_supported":true,
            "linux_supported":true,
            "macos_supported":true,
            "script_uid":"<unique ID>"
         },
         {
            "script_id":4,
            "name":"test 1",
            "description":"test",
            "modification_date":1583052236449,
            "created_by":"User 1",
            "is_high_risk":false,
            "windows_supported":true,
            "linux_supported":false,
            "macos_supported":false,
            "script_uid":"<unique ID>"
         },
         {
            "script_id":8,
            "name":"test 2",
            "description":"test 2",
            "modification_date":1582709343498,
            "created_by":"User 2",
            "is_high_risk":false,
            "windows_supported":true,
            "linux_supported":true,
            "macos_supported":true,
            "script_uid":"<unique ID>"
         }
      ]
   }
}
    """
    return json.loads(response)


@pytest.fixture
def get_script_metadata_response():
    response = r"""
       {
   "reply":{
      "script_id":2,
      "name":"list_directories",
      "description":"List all directories under path",
      "modification_date":1585074627259,
      "created_by":"Palo Alto Networks",
      "is_high_risk":false,
      "windows_supported":true,
      "linux_supported":true,
      "macos_supported":true,
      "script_uid":"<unique ID>",
      "entry_point":"run",
      "script_input":[
         {
            "name":"path",
            "type":"string"
         },
         {
            "friendly_name":"Number of levels",
            "name":"num_levels",
            "type":"number"
         }
      ],
      "script_output_type":   "dictionary",
   	  "script_output_dictionary_definitions":   [
         {
            "friendly_name":"Number Of Processes",
            "name":"output_2",
            "type":"number"
         },
         {
            "friendly_name":"Name",
            "name":"output_1",
            "type":"string"
         }
      ]
   }
}

       """
    return json.loads(response)


@pytest.fixture
def get_script_execution_status_response():
    response = r"""
    {
   "reply":{
      "general_status":"PENDING",
      "endpoints_pending":1,
      "endpoints_canceled":0,
      "endpoints_in_progress":0,
      "endpoints_timeout":0,
      "endpoints_failed":0,
      "endpoints_completed_successfully":0,
      "endpoints_pending_abort":0,
      "endpoints_aborted":0,
      "endpoints_expired":0
   }
}
    """
    return json.loads(response)


@pytest.fixture
def get_script_execution_results_response():
    response = r"""
       {
   "reply":{
      "script_name":"snippet script",
      "script_description":null,
      "script_parameters":[

      ],
      "date_created":"2020-03-29 13:21:59",
      "scope":"win_10and 21 other endpoints",
      "error_message":"",
      "results":[
         {
            "endpoint_name":"<name>",
            "endpoint_ip_address":[
               "<IP address>"
            ],
            "endpoint_status":"LOST",
            "domain":"aaaa",
            "endpoint_id":"<endpoint ID>",
            "execution_status":"PENDING",
            "standard_output":null,
            "retrieved_files":0,
            "failed_files":0,
            "retention_date":null
         },
         {
            "endpoint_name":"<name>",
            "endpoint_ip_address":[
               "<IP address>"
            ],
            "endpoint_status":"LOST",
            "domain":"<domain name>",
            "endpoint_id":"<endpoint ID>",
            "execution_status":"PENDING",
            "standard_output":null,
            "retrieved_files":0,
            "failed_files":0,
            "retention_date":null
         },
         {
            "endpoint_name":"<name>",
            "endpoint_ip_address":[
               "<IP address>"
            ],
            "endpoint_status":"DISCONNECTED",
            "domain":"WORKGROUP",
            "endpoint_id":"<endpoint ID>",
            "execution_status":"PENDING",
            "standard_output":null,
            "retrieved_files":0,
            "failed_files":0,
            "retention_date":null
         }
      ]
   }
}
       """
    return json.loads(response)


@pytest.fixture
def get_script_execution_result_files_response():
    response = r"""
       {
    "reply": {
        "DATA": "https://example-link"
        }
}
       """
    return json.loads(response)


@pytest.fixture
def run_script_response():
    response = r"""
       {
   "reply":{
      "action_id":22519813685366,
      "status":1,
      "endpoints_count":1
   }
}
       """
    return json.loads(response)


@pytest.fixture
def run_snippet_code_script_response():
    response = r"""
       {
   "reply":{
      "action_id":434,
      "endpoints_count":21
   }
}
       """
    return json.loads(response)


@pytest.fixture
def start_xql_response():
    response = r"""
       {
           "reply": "543gdf"
       }
       """
    return json.loads(response)


@pytest.fixture
def get_action_status():
    response = r"""
        {
            "reply": {
                "data": {
                    "<agent ID>": "COMPLETED_SUCCESSFULLY"
                    }
               }
        }
       """
    return json.loads(response)


@pytest.fixture
def get_xql_results_response():
    response = r"""
       {
    "reply": {
        "status": "SUCCESS",
        "number_of_results": 3,
        "query_cost": {"tenant_id_1": 0.001596388888888889},
        "remaining_quota": 4.998403611111111,
        "results": {
            "data": [
                {"event_id": "eventID1", "_vendor": "PANW", "_product": "Fusion", "insert_timestamp": 1621541825324, "_time": 1621541523000, "event_type": "STORY", "event_sub_type": "NULL"},
                {"event_id": "eventID2", "_vendor": "PANW", "_product": "Fusion", "insert_timestamp": 1621541825326, "_time": 1621541528000, "event_type": "STORY", "event_sub_type": "NULL"},
                {"event_id": "eventID3", "_vendor": "PANW", "_product": "Fusion", "insert_timestamp": 1621541825325, "_time": 1621541517000, "event_type": "STORY", "event_sub_type": "NULL"}
            ]
        }
    }
}
       """
    return json.loads(response)


@pytest.fixture
def get_xql_result_stream_response():
    response = r"""
       {"event_id":"eventID","insert_timestamp":"2021-05-18 14:24:51.681 UTC","_time":"2021-05-18 09:59:28 UTC","_vendor":"PANW","_product":"Fusion","event_type":"STORY","event_sub_type":"NULL"}
       {"event_id":"eventID","insert_timestamp":"2021-05-18 14:24:34.779 UTC","_time":"2021-05-18 09:59:28 UTC","_vendor":"PANW","_product":"Fusion","event_type":"STORY","event_sub_type":"NULL"}
       {"event_id":"eventID","insert_timestamp":"2021-05-18 14:24:49.664 UTC","_time":"2021-05-18 09:59:28 UTC","_vendor":"PANW","_product":"Fusion","event_type":"STORY","event_sub_type":"NULL"}
       """
    return gzip.compress(response.encode('utf-8'))


@pytest.fixture
def post_insert_json_response():
    response = r"""
    {"reply":{"success":true,"validation_errors":[{"indicator":"testtest.com","error":"Got type: HASH, Indicator: testtest.com mismatch"}]}}
    """
    return json.loads(response)
