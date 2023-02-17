from typing import Dict, List, Optional, Tuple

from cortex_xdr_client.api.authentication import Authentication
from cortex_xdr_client.api.base_api import BaseAPI
from cortex_xdr_client.api.models.endpoints import (EndpointPlatform,
                                                    EndpointStatus,
                                                    GetAllEndpointsResponse,
                                                    GetEndpointResponse,
                                                    IsolateStatus,
                                                    ResponseActionResponse,
                                                    ScanStatus,
                                                    )
from cortex_xdr_client.api.models.filters import (new_request_data, request_filter, request_gte_lte_filter)


class EndpointsAPI(BaseAPI):
    def __init__(self, auth: Authentication, fqdn: str, timeout: Tuple[int, int]) -> None:
        super(EndpointsAPI, self).__init__(auth, fqdn, "endpoints", timeout)

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
                                     username: List[str] = None,
                                     ) -> List[dict]:
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
        """
        Gets a list of your endpoints.

        :return: A GetAllEndpointsResponse object if successful.
        """
        response = self._call(call_name="get_endpoints")
        return GetAllEndpointsResponse.parse_obj(response.json())

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
        """
        Gets a list of filtered endpoints.

        :param endpoint_id_list: List of endpoint IDs.
        :param endpoint_status: Status of the endpoint ID.
        :param dist_name: Distribution / Installation Package name.
        :param first_seen: When the agent was first seen.
        :param after_first_seen: If the first seen date will be the upper or lower bound limit.
        :param last_seen: When the agent was last seen.
        :param after_last_seen: If the last seen date will be the upper or lower bound limit.
        :param ip_list: List of IP addresses.
        :param group_name: Group name the agent belongs to.
        :param platform: Platform name.
        :param alias: Alias name.
        :param hostname: Hostname.
        :param isolate: If the endpoint was isolated.
        :param scan_status: A list of ScanStatus
        :param username: Username.
        :param search_from: Integer representing the starting offset within the query result set from which you want incidents returned.
        :param search_to: Integer representing the end offset within the result set after which you do not want incidents returned.
        :return: A GetEndpointResponse object if successful.
        """
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
        return GetEndpointResponse.parse_obj(response.json())

    # https://docs.paloaltonetworks.com/cortex/cortex-xdr/cortex-xdr-api/cortex-xdr-apis/response-actions/isolate-endpoints.html
    def isolate_endpoints(self,
                          endpoint_id_list: List[str] = None,
                          ) -> Optional[ResponseActionResponse]:
        """
        Isolate one or more endpoints in a single request. Request is limited to 1000 endpoints.

        :param endpoint_id_list: List of endpoint IDs.
        :return: A ResponseActionResponse object if successful.
        """
        request_data = new_request_data(filters=[request_filter("endpoint_id_list", "in", endpoint_id_list)])
        response = self._call(call_name="isolate",
                              json_value=request_data)
        return ResponseActionResponse.parse_obj(response.json())

    # https://docs.paloaltonetworks.com/cortex/cortex-xdr/cortex-xdr-api/cortex-xdr-apis/response-actions/unisolate-endpoints.html
    def unisolate_endpoints(self,
                            endpoint_id_list: List[str] = None,
                            ) -> Optional[ResponseActionResponse]:
        """
        Unisolate one or more endpoints in a single request. Request is limited to 1000 endpoints.

        :param endpoint_id_list: List of endpoint IDs.
        :return: A ResponseActionResponse object if successful.
        """
        request_data = new_request_data(filters=[request_filter("endpoint_id_list", "in", endpoint_id_list)])
        response = self._call(call_name="unisolate",
                              json_value=request_data)
        return ResponseActionResponse.parse_obj(response.json())

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
        """
        Run a scan on selected endpoints.

        :param endpoint_id_list: List of endpoint IDs.
        :param dist_name: Name of the distribution list.
        :param first_seen: When an endpoint was first seen.
        :param after_first_seen: If the first seen date will be the upper or lower bound limit.
        :param last_seen: When an endpoint was last seen.
        :param after_last_seen: If the last seen date will be the upper or lower bound limit.
        :param ip_list: List of IP addresses.
        :param group_name: Name of the endpoint group.
        :param platform: Platform name.
        :param alias: Endpoint alias name.
        :param hostname: Name of host.
        :param isolate: If the endpoint has been isolated.
        :param scan_status: The scan status.
        :param username: Username.
        :return: A ResponseActionResponse object if successful.
        """
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
        return ResponseActionResponse.parse_obj(response.json())

    # https://docs.paloaltonetworks.com/cortex/cortex-xdr/cortex-xdr-api/cortex-xdr-apis/response-actions/retrieve-file.html
    def retrieve_file(self,
                      endpoint_id_list: List[str] = None,
                      files: Dict[str, List[str]] = None,
                      incident_id: str = None,
                      ) -> Optional[ResponseActionResponse]:
        """
        Retrieve files from selected endpoints. You can retrieve up to 20 files, from no more than 10 endpoints.

        :param endpoint_id_list: List of endpoint IDs.
        :param files: dictionary containing the type of platform and list of file paths you want to retrieve. Valid platform type keywords are: ["windows", "linux", "macos"].
        :param incident_id: When included in the request, the Retrieve File action will appear in the Cortex XDR Incident View Timeline tab.
        :return: A ResponseActionResponse object if successful.
        """

        filters = [request_filter("endpoint_id_list", "in", endpoint_id_list)]

        # Check if the dictionary contains anything other than supported Os.
        acceptable_oses = list(["windows", "linux", "macos"])

        for os in set(acceptable_oses).intersection(files):
            if os not in acceptable_oses:
                return None
        request_data = new_request_data(filters=filters, other=files)
        if incident_id is not None:
            request_data["incident_id"] = incident_id

        response = self._call(call_name="file_retrieval",
                              json_value=request_data)
        return ResponseActionResponse.parse_obj(response.json())

    # https://docs.paloaltonetworks.com/cortex/cortex-xdr/cortex-xdr-api/cortex-xdr-apis/response-actions/quarantine-files.html
    def quarantine_file(self,
                        endpoint_id_list: List[str] = None,
                        file_path: str = None,
                        file_hash: str = None,
                        incident_id: str = None,
                        ) -> Optional[ResponseActionResponse]:
        """
        Quarantine file on selected endpoints. You can select up to 1000 endpoints.

        :param endpoint_id_list: List of endpoint IDs.
        :param file_path: String that represents the path of the file you want to quarantine. You must enter a proper path and not symbolic links.
        :param file_hash: String that represents the file’s hash. Hash must be a valid SHA256.
        :return: A ResponseActionResponse object if successful.
        """

        filters = [request_filter("endpoint_id_list", "in", endpoint_id_list)]

        request_data = new_request_data(filters=filters, other={"file_path": file_path, "file_hash": file_hash})
        if incident_id is not None:
            request_data["incident_id"] = incident_id

        response = self._call(call_name="quarantine",
                              json_value=request_data)
        return ResponseActionResponse.parse_obj(response.json())

    def scan_all_endpoints(self) -> Optional[ResponseActionResponse]:
        """
        Scans all endpoints.

        :return: A ResponseActionResponse object if successful.
        """
        request_data = {
            "request_data": {
                "filters": "all"
            }
        }
        response = self._call(call_name="scan",
                              json_value=request_data)
        return ResponseActionResponse.parse_obj(response.json())
