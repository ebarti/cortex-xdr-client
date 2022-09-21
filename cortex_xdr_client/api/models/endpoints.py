from enum import Enum
from typing import List, Optional, Union, Any

from pydantic import BaseModel


class EndpointStatus(Enum):
    """
    Enum for endpoint status
    """
    connected = "CONNECTED"
    disconnected = "DISCONNECTED"
    lost = "LOST"


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


class LightEndpoint(BaseModel):
    agent_id: Optional[str]
    agent_status: Optional[str]
    host_name: Optional[str]
    agent_type: Optional[str]
    ip: Optional[List[str]]


class GetAllEndpointsResponse(BaseModel):
    reply: List[LightEndpoint]


class Endpoint(BaseModel):
    active_directory: Union[List[str], Optional[str]]
    alias: Optional[str]
    content_version: Optional[str]
    domain: Optional[str]
    endpoint_id: Optional[str]
    endpoint_name: Optional[str]
    endpoint_status: EndpointStatus
    endpoint_type: Optional[str]
    endpoint_version: Optional[str]
    first_seen: Optional[int]
    group_name: Optional[List[str]]
    install_date: Optional[int]
    installation_package: Optional[str]
    ip: Optional[List[str]]
    is_isolated: IsolateStatus
    isolated_date: Optional[str]
    last_seen: Optional[int]
    last_content_update_time: Optional[int]
    operational_status: Optional[str]
    operational_status_description: Optional[str]
    os_type: Optional[EndpointPlatform]
    scan_status: Optional[ScanStatus]
    users: Union[Optional[List[str]], Optional[str]]
    mac_address: Optional[List[str]]

    class Config:
        use_enum_names = True


class GetEndpointResponseItem(BaseModel):
    total_count: Optional[int]
    result_count: Optional[int]
    endpoints: List[Endpoint]


class GetEndpointResponse(BaseModel):
    reply: GetEndpointResponseItem


class ResponseActionResponseItem(BaseModel):
    action_id: Optional[str]
    status: Optional[int]
    endpoints_count: Optional[int]


class ResponseActionResponse(BaseModel):
    reply: ResponseActionResponseItem
