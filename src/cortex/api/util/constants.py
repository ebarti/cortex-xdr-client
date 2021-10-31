

class Constants(object):

    INCIDENTS_API_NAME = "incidents"
    INCIDENTS_API_CALL_NAMES = {
        "get": "get_incidents",
        "get_extra_data": "get_incident_extra_data",
        "update": "update_incident",
    }

    ALERTS_API_NAME = "alerts"
    ALERTS_API_CALL_NAMES = {
        "get": "get_alerts_multi_events",
        "get_extra_data": "get_incident_extra_data",
        "update": "update_incident",
    }

    ENDPOINTS_API_NAME = "endpoints"
    ENDPOINTS_API_CALL_NAMES = {
        "get": "get_endpoints",
        "get_endpoint": "get_endpoint",
        "delete": "delete",
        "quarantine": "quarantine",
        "scan": "scan",
        "isolate": "isolate",
    }

