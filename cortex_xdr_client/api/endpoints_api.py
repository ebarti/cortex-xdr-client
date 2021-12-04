from typing import List, Optional

from cortex_xdr_client.api.base_api import BaseAPI
from cortex_xdr_client.api.models.endpoints import (
    EndpointStatus,
    IsolateStatus,
    ScanStatus,
    EndpointPlatform,
    GetEndpointResponse,
    GetAllEndpointsResponse,
    ResponseActionResponse,
)
from cortex_xdr_client.api.models.filters import (
    new_request_data,
    request_gte_lte_filter,
    request_filter
)


class EndpointsAPI(BaseAPI):
    def __init__(self, api_key_id: int, api_key: str, fqdn: str, timeout: tuple[int, int]) -> None:
        super(EndpointsAPI, self).__init__(api_key_id, api_key, fqdn, "endpoints", timeout)

    @staticmethod
    def _get_common_endpoint_filters(endpoint_id_list: List[str] = None,
                                     dist_name: List[str] = None,
                                     first_seen: int = None,
                                     after_first_seen: bool = False,
                                     last_seen: int = None,
                                     after_last_seen: bool = False,
                                     ip_list: List[str] = None,
                                     group_name: List[str] = None,
                                     platform: List[EndpointPlatform] = None,
                                     alias: List[str] = None,
                                     hostname: List[str] = None,
                                     isolate: List[IsolateStatus] = None,
                                     scan_status: List[ScanStatus] = None,
                                     username: List[str] = None) -> List[dict]:
        filters = []
        if endpoint_id_list is not None:
            filters.append(request_filter("endpoint_id_list", "in", endpoint_id_list))
        if dist_name is not None:
            filters.append(request_filter("dist_name", "in", dist_name))
        if first_seen is not None:
            filters.append(request_gte_lte_filter("first_seen", first_seen, after_first_seen))
        if last_seen is not None:
            filters.append(request_gte_lte_filter("last_seen", last_seen, after_last_seen))
        if ip_list is not None:
            filters.append(request_filter("ip_list", "in", ip_list))
        if group_name is not None:
            filters.append(request_filter("group_name", "in", group_name))
        if platform is not None:
            filters.append(request_filter("platform", "in", platform))
        if alias is not None:
            filters.append(request_filter("alias", "in", alias))
        if hostname is not None:
            filters.append(request_filter("hostname", "in", hostname))
        if isolate is not None:
            filters.append(request_filter("isolate", "in", isolate))
        if scan_status is not None:
            filters.append(request_filter("scan_status", "in", scan_status))
        if username is not None:
            filters.append(request_filter("username", "in", username))
        return filters

    def get_all_endpoints(self) -> Optional[GetAllEndpointsResponse]:
        response = self._call(call_name="get_endpoints")
        if response.ok:
            return GetAllEndpointsResponse.parse_obj(response.json())
        return None

    def get_endpoint(self,
                     endpoint_id_list: List[str] = None,
                     endpoint_status: List[EndpointStatus] = None,
                     dist_name: List[str] = None,
                     first_seen: int = None,
                     after_first_seen: bool = False,
                     last_seen: int = None,
                     after_last_seen: bool = False,
                     ip_list: List[str] = None,
                     group_name: List[str] = None,
                     platform: List[EndpointPlatform] = None,
                     alias: List[str] = None,
                     hostname: List[str] = None,
                     isolate: List[IsolateStatus] = None,
                     scan_status: List[ScanStatus] = None,
                     username: List[str] = None,
                     search_from: int = None,
                     search_to: int = None,
                     ) -> Optional[GetEndpointResponse]:
        filters = self._get_common_endpoint_filters(endpoint_id_list=endpoint_id_list,
                                                    dist_name=dist_name,
                                                    first_seen=first_seen,
                                                    after_first_seen=after_first_seen,
                                                    last_seen=last_seen,
                                                    after_last_seen=after_last_seen,
                                                    ip_list=ip_list,
                                                    group_name=group_name,
                                                    platform=platform,
                                                    alias=alias,
                                                    hostname=hostname,
                                                    isolate=isolate,
                                                    scan_status=scan_status,
                                                    username=username)
        if endpoint_status is not None:
            filters.append(request_filter("endpoint_status", "in", endpoint_status))

        request_data = new_request_data(filters=filters, search_from=search_from, search_to=search_to)

        response = self._call(call_name="get_endpoint",
                              json_value=request_data)
        if response.ok:
            return GetEndpointResponse.parse_obj(response.json())
        return None

    # https://docs.paloaltonetworks.com/cortex/cortex-xdr/cortex-xdr-api/cortex-xdr-apis/response-actions/isolate-endpoints.html
    def isolate_endpoints(self,
                          endpoint_id_list: List[str] = None,
                          ) -> Optional[ResponseActionResponse]:
        request_data = new_request_data(filters=[request_filter("endpoint_id_list", "in", endpoint_id_list)])
        response = self._call(call_name="isolate",
                              json_value=request_data)
        if response.ok:
            return ResponseActionResponse.parse_obj(response.json())
        return None

    # https://docs.paloaltonetworks.com/cortex/cortex-xdr/cortex-xdr-api/cortex-xdr-apis/response-actions/scan-endpoints.html
    def scan_endpoints(self,
                       endpoint_id_list: List[str] = None,
                       dist_name: List[str] = None,
                       first_seen: int = None,
                       after_first_seen: bool = False,
                       last_seen: int = None,
                       after_last_seen: bool = False,
                       ip_list: List[str] = None,
                       group_name: List[str] = None,
                       platform: List[EndpointPlatform] = None,
                       alias: List[str] = None,
                       hostname: List[str] = None,
                       isolate: List[IsolateStatus] = None,
                       scan_status: List[ScanStatus] = None,
                       username: List[str] = None,
                       ) -> Optional[ResponseActionResponse]:
        filters = self._get_common_endpoint_filters(endpoint_id_list=endpoint_id_list,
                                                    dist_name=dist_name,
                                                    first_seen=first_seen,
                                                    after_first_seen=after_first_seen,
                                                    last_seen=last_seen,
                                                    after_last_seen=after_last_seen,
                                                    ip_list=ip_list,
                                                    group_name=group_name,
                                                    platform=platform,
                                                    alias=alias,
                                                    hostname=hostname,
                                                    isolate=isolate,
                                                    scan_status=scan_status,
                                                    username=username)

        request_data = new_request_data(filters=filters)

        response = self._call(call_name="scan",
                              json_value=request_data)
        if response.ok:
            return ResponseActionResponse.parse_obj(response.json())
        return None

    def scan_all_endpoints(self) -> Optional[ResponseActionResponse]:
        request_data = {
            "request_data": {
                "filters": "all"
            }
        }
        response = self._call(call_name="scan",
                              json_value=request_data)
        if response.ok:
            return ResponseActionResponse.parse_obj(response.json())
        return None
