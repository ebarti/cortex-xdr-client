from enum import Enum
from typing import List, Optional, Union

from cortex_xdr_client.api.models.base import CortexResponseModel


class EndpointStatus(Enum):
    """
    Enum for endpoint status
    """
    connected = "CONNECTED"
    disconnected = "DISCONNECTED"
    lost = "LOST"
    uninstalled = "UNINSTALLED"


class EndpointPlatform(Enum):
    """
    Enum for endpoint platform
    """
    android = "AGENT_OS_ANDROID"
    linux = "AGENT_OS_LINUX"
    windows = "AGENT_OS_WINDOWS"
    macos = "AGENT_OS_MACOS"
    mac = "AGENT_OS_MAC"


class IsolateStatus(Enum):
    """
    Enum for isolate status
    """
    isolated = "AGENT_ISOLATED"
    unisolated = "AGENT_UNISOLATED"
    pending_isolation = "AGENT_PENDING_ISOLATION"


class ScanStatus(Enum):
    """
    Enum for scan status
    """
    none = "SCAN_STATUS_NONE"
    pending = "SCAN_STATUS_PENDING"
    in_progress = "SCAN_STATUS_IN_PROGRESS"
    canceled = "SCAN_STATUS_CANCELED"
    cancel = "SCAN_STATUS_CANCEL"
    aborted = "SCAN_STATUS_ABORTED"
    pending_cancellation = "SCAN_STATUS_PENDING_CANCELLATION"
    success = "SCAN_STATUS_SUCCESS"
    error = "SCAN_STATUS_ERROR"


class LightEndpoint(CortexResponseModel):
    agent_id: Optional[str] = None
    agent_status: Optional[str] = None
    host_name: Optional[str] = None
    agent_type: Optional[str] = None
    ip: Optional[List[str]] = None


class GetAllEndpointsResponse(CortexResponseModel):
    reply: List[LightEndpoint]


class Endpoint(CortexResponseModel):
    active_directory: Union[List[str], Optional[str]] = None
    alias: Optional[str] = None
    content_version: Optional[str] = None
    domain: Optional[str] = None
    endpoint_id: Optional[str] = None
    endpoint_name: Optional[str] = None
    endpoint_status: EndpointStatus
    endpoint_type: Optional[str] = None
    endpoint_version: Optional[str] = None
    first_seen: Optional[int] = None
    group_name: Optional[List[str]] = None
    install_date: Optional[int] = None
    installation_package: Optional[str] = None
    ip: Optional[List[str]] = None
    is_isolated: IsolateStatus
    isolated_date: Optional[str] = None
    last_seen: Optional[int] = None
    last_content_update_time: Optional[int] = None
    operational_status: Optional[str] = None
    operational_status_description: Optional[str] = None
    os_type: Optional[EndpointPlatform] = None
    scan_status: Optional[ScanStatus] = None
    users: Union[Optional[List[str]], Optional[str]] = None
    mac_address: Optional[List[str]] = None

    os_version: Optional[str] = None
    public_ip: Optional[str] = None
    ipv6: Optional[List[str]] = None
    operational_status_details: Optional[List[dict]] = None
    content_release_timestamp: Optional[int] = None
    content_status: Optional[str] = None
    operating_system: Optional[str] = None
    assigned_prevention_policy: Optional[str] = None
    assigned_extensions_policy: Optional[str] = None
    cloud_provider: Optional[str] = None
    cloud_region: Optional[str] = None
    cloud_provider_account_id: Optional[str] = None
    cloud_instance_id: Optional[str] = None
    cloud_id: Optional[str] = None


class GetEndpointResponseItem(CortexResponseModel):
    total_count: Optional[int] = None
    result_count: Optional[int] = None
    endpoints: List[Endpoint]


class GetEndpointResponse(CortexResponseModel):
    reply: GetEndpointResponseItem


class ResponseActionResponseItem(CortexResponseModel):
    action_id: Optional[str] = None
    status: Optional[int] = None
    endpoints_count: Optional[int] = None


class ResponseActionResponse(CortexResponseModel):
    reply: ResponseActionResponseItem


class ResponseStatusResponse(CortexResponseModel):
    reply: bool
