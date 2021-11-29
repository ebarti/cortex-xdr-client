from enum import Enum
from typing import List, Any


class EndpointStatus(Enum):
    """
    Enum for endpoint status
    """
    CONNECTED = "connected"
    DISCONNECTED = "disconnected"


class EndpointPlatform(Enum):
    """
    Enum for endpoint platform
    """
    ANDROID = "android"
    LINUX = "linux"
    WINDOWS = "windows"
    MACOS = "macos"


class IsolateStatus(Enum):
    """
    Enum for isolate status
    """
    ISOLATED = "isolated"
    UNISOLATED = "unisolated"


class ScanStatus(Enum):
    """
    Enum for scan status
    """
    NONE = "none"
    PENDING = "pending"
    IN_PROGRESS = "in_progress"
    CANCELED = "canceled"
    ABORTED = "aborted"
    PENDING_CANCELLATION = "pending_cancellation"
    SUCCESS = "success"
    ERROR = "error"


class LightEndpoint:
    agent_id: str
    agent_status: str
    host_name: str
    agent_type: str
    ip: str

    def __init__(self, agent_id: str, agent_status: str, host_name: str, agent_type: str, ip: str) -> None:
        self.agent_id = agent_id
        self.agent_status = agent_status
        self.host_name = host_name
        self.agent_type = agent_type
        self.ip = ip

    @classmethod
    def from_json(cls, data: dict) -> "LightEndpoint":
        return cls(**data)


class GetAllEndpointsResponse:
    reply: List[LightEndpoint]

    def __init__(self, data: List[LightEndpoint]) -> None:
        self.reply = data

    @classmethod
    def from_json(cls, data: dict) -> "GetAllEndpointsResponse":
        return cls(**data)


class Endpoint:
    active_directory: str
    alias: str
    content_version: str
    domain: str
    endpoint_id: str
    endpoint_name: str
    endpoint_status: str
    endpoint_type: str
    endpoint_version: str
    first_seen: int
    group_name: List[Any]
    install_date: int
    installation_package: str
    ip: List[str]
    is_isolated: str
    isolated_date: str
    last_seen: int
    operational_status: str
    operational_status_description: str
    os_type: str
    scan_status: str
    users: List[str]

    def __init__(self,
                 alias: str,
                 content_version: str,
                 domain: str,
                 endpoint_id: str,
                 endpoint_name: str,
                 endpoint_status: str,
                 endpoint_type: str,
                 endpoint_version: str,
                 first_seen: int,
                 group_name: List[Any],
                 install_date: int,
                 installation_package: str,
                 ip: List[str],
                 is_isolated: str,
                 last_seen: int,
                 operational_status: str,
                 operational_status_description: str,
                 os_type: str,
                 scan_status: str,
                 users: List[str],
                 active_directory: str = None,
                 isolated_date: str = None,
                 ) -> None:
        self.active_directory = active_directory
        self.alias = alias
        self.content_version = content_version
        self.domain = domain
        self.endpoint_id = endpoint_id
        self.endpoint_name = endpoint_name
        self.endpoint_status = endpoint_status
        self.endpoint_type = endpoint_type
        self.endpoint_version = endpoint_version
        self.first_seen = first_seen
        self.group_name = group_name
        self.install_date = install_date
        self.installation_package = installation_package
        self.ip = ip
        self.is_isolated = is_isolated
        self.isolated_date = isolated_date
        self.last_seen = last_seen
        self.operational_status = operational_status
        self.operational_status_description = operational_status_description
        self.os_type = os_type
        self.scan_status = scan_status
        self.users = users

    @classmethod
    def from_json(cls, data: dict) -> "Endpoint":
        return cls(**data)


class GetEndpointResponseItem:
    total_count: int
    result_count: int
    endpoints: List[Endpoint]

    def __init__(self, total_count: int, result_count: int, endpoints: List[Endpoint]) -> None:
        self.total_count = total_count
        self.result_count = result_count
        self.endpoints = endpoints

    @classmethod
    def from_json(cls, data: dict) -> "GetEndpointResponseItem":
        total_count = data["total_count"]
        result_count = data["result_count"]
        endpoints = list(map(Endpoint.from_json, data["endpoints"]))
        return cls(total_count=total_count, result_count=result_count, endpoints=endpoints)


class GetEndpointResponse:
    reply: GetEndpointResponseItem

    def __init__(self, reply: GetEndpointResponseItem) -> None:
        self.reply = reply

    @classmethod
    def from_json(cls, data: dict) -> "GetEndpointResponse":
        return cls(**data)


class ResponseActionResponseItem:
    action_id: str
    status: int
    endpoints_count: int

    def __init__(self, action_id: str, status: int, endpoints_count: int) -> None:
        self.action_id = action_id
        self.status = status
        self.endpoints_count = endpoints_count

    @classmethod
    def from_json(cls, data: dict) -> "ResponseActionResponseItem":
        total_count = data["total_count"]
        result_count = data["result_count"]
        endpoints = list(map(Endpoint.from_json, data["endpoints"]))
        return cls(total_count=total_count, result_count=result_count, endpoints=endpoints)


class ResponseActionResponse:
    reply: ResponseActionResponseItem

    def __init__(self, reply: ResponseActionResponseItem) -> None:
        self.reply = reply

    @classmethod
    def from_json(cls, data: dict) -> "ResponseActionResponse":
        return cls(**data)
