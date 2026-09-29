from typing import Any, Dict, List, Optional, Tuple, Union

from cortex_xdr_client.api.operation import UNSET, UnsetType

from enum import Enum

from cortex_xdr_client.api.authentication import Authentication
from cortex_xdr_client.api.base_api import BaseAPI
from cortex_xdr_client.api.version import APIVersion
from cortex_xdr_client.api.models.endpoints import (EndpointPlatform,
                                                    EndpointStatus,
                                                    GetAllEndpointsResponse,
                                                    GetEndpointResponse,
                                                    IsolateStatus,
                                                    ResponseActionResponse,
                                                    ResponseStatusResponse,
                                                    ScanStatus,
                                                    )
from cortex_xdr_client.api.models.filters import (new_request_data, request_filter, request_gte_lte_filter)


class EndpointsAPI(BaseAPI):
    def __init__(self, auth: Authentication, fqdn: str, timeout: Tuple[int, int],
                 api_version: APIVersion = APIVersion.V3) -> None:
        super(EndpointsAPI, self).__init__(auth, fqdn, "endpoints", timeout, api_version)

    @staticmethod
    def _get_filter_value(value):
        if isinstance(value, list):
            return [EndpointsAPI._get_filter_value(item) for item in value]
        if isinstance(value, Enum):
            return {"mac": "macos", "cancel": "canceled"}.get(value.name, value.name)
        return value

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
            filters.append(request_filter("platform", "in", EndpointsAPI._get_filter_value(platform)))
        if alias is not None:
            filters.append(request_filter("alias", "in", alias))
        if hostname is not None:
            filters.append(request_filter("hostname", "in", hostname))
        if isolate is not None:
            filters.append(request_filter("isolate", "in", EndpointsAPI._get_filter_value(isolate)))
        if scan_status is not None:
            filters.append(request_filter("scan_status", "in", EndpointsAPI._get_filter_value(scan_status)))
        if username is not None:
            filters.append(request_filter("username", "in", username))
        return filters

    def get_all_endpoints(self) -> Optional[GetAllEndpointsResponse]:
        """
        Gets a list of your endpoints.

        :return: A GetAllEndpointsResponse object if successful.
        """
        response = self._call(call_name="get_endpoints")
        return GetAllEndpointsResponse.model_validate(response.json())

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
                     sort: dict = None,
                     public_ip_list: List[str] = None,
                     cloud_provider: List[str] = None,
                     cloud_region: List[str] = None,
                     cloud_provider_account_id: List[str] = None,
                     cloud_instance_id: List[str] = None,
                     cloud_id: List[str] = None,
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
        :param sort: Sort field and keyword (asc or desc).
        :param public_ip_list: Last origin IP addresses.
        :param cloud_provider: Cloud providers to match (XDR 5.x).
        :param cloud_region: Cloud regions to match (XDR 5.x).
        :param cloud_provider_account_id: Cloud account IDs (XDR 5.x).
        :param cloud_instance_id: Cloud instance IDs (XDR 5.x).
        :param cloud_id: Cloud IDs (XDR 5.x).
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
            filters.append(request_filter("endpoint_status", "in", self._get_filter_value(endpoint_status)))

        if public_ip_list is not None:
            filters.append(request_filter("public_ip_list", "in", public_ip_list))
        cloud_filters = {"cloud_provider": cloud_provider, "cloud_region": cloud_region,
                         "cloud_provider_account_id": cloud_provider_account_id,
                         "cloud_instance_id": cloud_instance_id, "cloud_id": cloud_id}
        for field, value in cloud_filters.items():
            if value is not None:
                self._require_version(APIVersion.V5)
                filters.append(request_filter(field, "in", value))

        request_data = new_request_data(filters=filters, search_from=search_from, search_to=search_to, sort=sort)

        response = self._call(call_name="get_endpoint",
                              json_value=request_data)
        return GetEndpointResponse.model_validate(response.json())

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
        return ResponseActionResponse.model_validate(response.json())

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
        return ResponseActionResponse.model_validate(response.json())

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
        return ResponseActionResponse.model_validate(response.json())

    # https://docs-cortex.paloaltonetworks.com/r/Cortex-XDR-REST-API/Set-an-Endpoint-Alias
    def set_endpoint_alias(self,
                           new_alias: str,
                           endpoint_id_list: List[str] = None,
                           endpoint_status: EndpointStatus = None,
                           dist_name: str = None,
                           ip_list: List[str] = None,
                           group_name: List[str] = None,
                           platform: List[EndpointPlatform] = None,
                           alias: List[str] = None,
                           isolate: List[IsolateStatus] = None,
                           hostname: List[str] = None,
                           ) -> Optional[ResponseStatusResponse]:
        """
        Set or modify an Alias field for your endpoints.

        :param new_alias: The alias name you want to set or modify.
        :param endpoint_id_list: List of endpoint IDs.
        :param endpoint_status: Status of the endpoint ID.
        :param dist_name: Distribution / Installation Package name.
        :param ip_list: List of IP addresses.
        :param group_name: Group name the agent belongs to.
        :param platform: Platform name.
        :param alias: Alias name.
        :param isolate: If the endpoint was isolated.
        :param hostname: Hostname
        :return: A ResponseStatusResponse if successful.
        """
        filters = self._get_common_endpoint_filters(endpoint_id_list=endpoint_id_list,
                                                    dist_name=dist_name,
                                                    ip_list=ip_list,
                                                    group_name=group_name,
                                                    platform=platform,
                                                    alias=alias,
                                                    isolate=isolate,
                                                    hostname=hostname)
        if endpoint_status is not None:
            filters.append(request_filter("endpoint_status", "in", self._get_filter_value(endpoint_status)))

        request_data = new_request_data(filters=filters, other={"alias": new_alias})

        response = self._call(call_name="update_agent_name",
                              json_value=request_data)

        return ResponseStatusResponse.model_validate(response.json())

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

        if not files or any(os not in ("windows", "linux", "macos") for os in files):
            raise ValueError("files must contain paths keyed by windows, linux or macos")
        request_data = new_request_data(filters=filters, other={"files": files})
        if incident_id is not None:
            request_data["request_data"]["incident_id"] = incident_id

        response = self._call(call_name="file_retrieval",
                              json_value=request_data)
        return ResponseActionResponse.model_validate(response.json())

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
        :param incident_id: When included in the request, the Quarantine File action will appear in the Cortex XDR Incident View Timeline tab.
        :return: A ResponseActionResponse object if successful.
        """

        filters = [request_filter("endpoint_id_list", "in", endpoint_id_list)]

        request_data = new_request_data(filters=filters, other={"file_path": file_path, "file_hash": file_hash})
        if incident_id is not None:
            request_data["request_data"]["incident_id"] = incident_id

        response = self._call(call_name="quarantine",
                              json_value=request_data)
        return ResponseActionResponse.model_validate(response.json())

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
        return ResponseActionResponse.model_validate(response.json())


    def get_endpoints(self, *,
                      accept_encoding: Union[str, None, UnsetType] = UNSET,
                      body: Union[dict, None, UnsetType] = UNSET) -> Any:
        """Get all Endpoints

        POST /public_api/v1/endpoints/get_endpoints
        Available in Cortex XDR 3.x, 5.x.
        Returns the complete JSON response, bytes for downloads, or None for an empty response.
        Omit optional fields with UNSET; explicit None is sent as JSON null.
        :param accept_encoding: header field Accept-Encoding.
        :param body: payload field body.
        """
        self._require_versions((3, 5))
        if self._api_version == APIVersion.V3:
            body = body
            return self._operation(
                '/public_api/v1/endpoints/get_endpoints', method='post',
                headers={'Accept-Encoding': accept_encoding},
                body=body,
            )
        elif self._api_version == APIVersion.V5:
            self._reject_fields(accept_encoding=accept_encoding)
            body = body
            return self._operation(
                '/public_api/v1/endpoints/get_endpoints', method='post',
                body=body,
            )

    def get_endpoint_request(self, *,
                             accept_encoding: Union[str, None, UnsetType] = UNSET,
                             filters: Union[List[dict], None, UnsetType] = UNSET,
                             search_from: Union[int, None, UnsetType] = UNSET,
                             search_to: Union[int, None, UnsetType] = UNSET,
                             sort: Union[dict, None, UnsetType] = UNSET) -> Any:
        """Get Endpoint

        POST /public_api/v1/endpoints/get_endpoint
        Available in Cortex XDR 3.x, 5.x.
        Returns the complete JSON response, bytes for downloads, or None for an empty response.
        Omit optional fields with UNSET; explicit None is sent as JSON null.
        :param accept_encoding: header field Accept-Encoding.
        :param filters: body field filters.
        :param search_from: body field search_from.
        :param search_to: body field search_to.
        :param sort: body field sort.
        """
        self._require_versions((3, 5))
        if self._api_version == APIVersion.V3:
            body = self._values({'filters': filters, 'search_from': search_from, 'search_to': search_to, 'sort': sort})
            body = self._values({'request_data': body, **{}})
            return self._operation(
                '/public_api/v1/endpoints/get_endpoint', method='post',
                headers={'Accept-Encoding': accept_encoding},
                body=body,
            )
        elif self._api_version == APIVersion.V5:
            self._reject_fields(accept_encoding=accept_encoding)
            body = self._values({'filters': filters, 'search_from': search_from, 'search_to': search_to, 'sort': sort})
            body = self._values({'request_data': body, **{}})
            return self._operation(
                '/public_api/v1/endpoints/get_endpoint', method='post',
                body=body,
            )

    def update_agent_name(self, *,
                          accept_encoding: Union[str, None, UnsetType] = UNSET,
                          filters: Union[List[dict], None, UnsetType] = UNSET,
                          alias: Union[str, None, UnsetType] = UNSET) -> Any:
        """Set an Endpoint Alias

        POST /public_api/v1/endpoints/update_agent_name
        Available in Cortex XDR 3.x, 5.x.
        Returns the complete JSON response, bytes for downloads, or None for an empty response.
        Omit optional fields with UNSET; explicit None is sent as JSON null.
        :param accept_encoding: header field Accept-Encoding.
        :param filters: body field filters.
        :param alias: body field alias.
        """
        self._require_versions((3, 5))
        if self._api_version == APIVersion.V3:
            body = self._values({'filters': filters, 'alias': alias})
            body = self._values({'request_data': body, **{}})
            return self._operation(
                '/public_api/v1/endpoints/update_agent_name', method='post',
                headers={'Accept-Encoding': accept_encoding},
                body=body,
            )
        elif self._api_version == APIVersion.V5:
            self._reject_fields(accept_encoding=accept_encoding)
            body = self._values({'filters': filters, 'alias': alias})
            body = self._values({'request_data': body, **{}})
            return self._operation(
                '/public_api/v1/endpoints/update_agent_name', method='post',
                body=body,
            )

    def get_policy(self, *,
                   accept_encoding: Union[str, None, UnsetType] = UNSET,
                   endpoint_id: Union[str, None, UnsetType] = UNSET) -> Any:
        """Get Policy

        POST /public_api/v1/endpoints/get_policy
        Available in Cortex XDR 3.x, 5.x.
        Returns the complete JSON response, bytes for downloads, or None for an empty response.
        Omit optional fields with UNSET; explicit None is sent as JSON null.
        :param accept_encoding: header field Accept-Encoding.
        :param endpoint_id: body field endpoint_id.
        """
        self._require_versions((3, 5))
        if self._api_version == APIVersion.V3:
            body = self._values({'endpoint_id': endpoint_id})
            body = self._values({'request_data': body, **{}})
            return self._operation(
                '/public_api/v1/endpoints/get_policy', method='post',
                headers={'Accept-Encoding': accept_encoding},
                body=body,
            )
        elif self._api_version == APIVersion.V5:
            self._reject_fields(accept_encoding=accept_encoding)
            body = self._values({'endpoint_id': endpoint_id})
            body = self._values({'request_data': body, **{}})
            return self._operation(
                '/public_api/v1/endpoints/get_policy', method='post',
                body=body,
            )

    def terminate_process(self, *,
                          accept_encoding: Union[str, None, UnsetType] = UNSET,
                          agent_id: Union[str, None, UnsetType] = UNSET,
                          instance_id: Union[str, None, UnsetType] = UNSET,
                          process_name: Union[str, None, UnsetType] = UNSET,
                          incident_id: Union[str, None, UnsetType] = UNSET) -> Any:
        """Terminate the specified agent process

        POST /public_api/v1/endpoints/terminate_process
        Available in Cortex XDR 3.x.
        Returns the complete JSON response, bytes for downloads, or None for an empty response.
        Omit optional fields with UNSET; explicit None is sent as JSON null.
        :param accept_encoding: header field Accept-Encoding.
        :param agent_id: body field agent_id.
        :param instance_id: body field instance_id.
        :param process_name: body field process_name.
        :param incident_id: body field incident_id.
        """
        self._require_versions((3,))
        body = self._values({'agent_id': agent_id, 'instance_id': instance_id, 'process_name': process_name, 'incident_id': incident_id})
        body = self._values({'request_data': body, **{}})
        return self._operation(
            '/public_api/v1/endpoints/terminate_process', method='post',
            headers={'Accept-Encoding': accept_encoding},
            body=body,
        )

    def terminate_causality(self, *,
                            accept_encoding: Union[str, None, UnsetType] = UNSET,
                            agent_id: Union[str, None, UnsetType] = UNSET,
                            causality_id: Union[str, None, UnsetType] = UNSET,
                            process_name: Union[str, None, UnsetType] = UNSET,
                            incident_id: Union[str, None, UnsetType] = UNSET) -> Any:
        """Terminate a process by causality ID

        POST /public_api/v1/endpoints/terminate_causality
        Available in Cortex XDR 3.x.
        Returns the complete JSON response, bytes for downloads, or None for an empty response.
        Omit optional fields with UNSET; explicit None is sent as JSON null.
        :param accept_encoding: header field Accept-Encoding.
        :param agent_id: body field agent_id.
        :param causality_id: body field causality_id.
        :param process_name: body field process_name.
        :param incident_id: body field incident_id.
        """
        self._require_versions((3,))
        body = self._values({'agent_id': agent_id, 'causality_id': causality_id, 'process_name': process_name, 'incident_id': incident_id})
        body = self._values({'request_data': body, **{}})
        return self._operation(
            '/public_api/v1/endpoints/terminate_causality', method='post',
            headers={'Accept-Encoding': accept_encoding},
            body=body,
        )

    def delete(self, *,
               accept_encoding: Union[str, None, UnsetType] = UNSET,
               filters: Union[List[dict], None, UnsetType] = UNSET) -> Any:
        """Delete Endpoints

        POST /public_api/v1/endpoints/delete
        Available in Cortex XDR 3.x, 5.x.
        Returns the complete JSON response, bytes for downloads, or None for an empty response.
        Omit optional fields with UNSET; explicit None is sent as JSON null.
        :param accept_encoding: header field Accept-Encoding.
        :param filters: body field filters.
        """
        self._require_versions((3, 5))
        if self._api_version == APIVersion.V3:
            body = self._values({'filters': filters})
            body = self._values({'request_data': body, **{}})
            return self._operation(
                '/public_api/v1/endpoints/delete', method='post',
                headers={'Accept-Encoding': accept_encoding},
                body=body,
            )
        elif self._api_version == APIVersion.V5:
            self._reject_fields(accept_encoding=accept_encoding)
            body = self._values({'filters': filters})
            body = self._values({'request_data': body, **{}})
            return self._operation(
                '/public_api/v1/endpoints/delete', method='post',
                body=body,
            )

    def get_profiles(self, *,
                     type: Union[str, None, UnsetType] = UNSET,
                     profile_ids: Union[List[int], None, UnsetType] = UNSET) -> Any:
        """Get endpoint security profiles

        POST /public_api/v1/endpoints/get_profiles
        Available in Cortex XDR 3.x, 5.x.
        Returns the complete JSON response, bytes for downloads, or None for an empty response.
        Omit optional fields with UNSET; explicit None is sent as JSON null.
        :param type: body field type.
        :param profile_ids: body field profile_ids.
        """
        self._require_versions((3, 5))
        if self._api_version == APIVersion.V3:
            body = self._values({'type': type, 'profile_ids': profile_ids})
            body = self._values({'request_data': body, **{}})
            return self._operation(
                '/public_api/v1/endpoints/get_profiles', method='post',
                body=body,
            )
        elif self._api_version == APIVersion.V5:
            body = self._values({'type': type, 'profile_ids': profile_ids})
            body = self._values({'request_data': body, **{}})
            return self._operation(
                '/public_api/v1/endpoints/get_profiles', method='post',
                body=body,
            )

    def restore(self, *,
                accept_encoding: Union[str, None, UnsetType] = UNSET,
                file_hash: Union[str, None, UnsetType] = UNSET,
                endpoint_id: Union[str, None, UnsetType] = UNSET,
                incident_id: Union[int, None, UnsetType] = UNSET) -> Any:
        """Restore File

        POST /public_api/v1/endpoints/restore
        Available in Cortex XDR 3.x, 5.x.
        Returns the complete JSON response, bytes for downloads, or None for an empty response.
        Omit optional fields with UNSET; explicit None is sent as JSON null.
        :param accept_encoding: header field Accept-Encoding.
        :param file_hash: body field file_hash.
        :param endpoint_id: body field endpoint_id.
        :param incident_id: body field incident_id.
        """
        self._require_versions((3, 5))
        if self._api_version == APIVersion.V3:
            body = self._values({'file_hash': file_hash, 'endpoint_id': endpoint_id, 'incident_id': incident_id})
            body = self._values({'request_data': body, **{}})
            return self._operation(
                '/public_api/v1/endpoints/restore', method='post',
                headers={'Accept-Encoding': accept_encoding},
                body=body,
            )
        elif self._api_version == APIVersion.V5:
            self._reject_fields(accept_encoding=accept_encoding)
            body = self._values({'file_hash': file_hash, 'endpoint_id': endpoint_id, 'incident_id': incident_id})
            body = self._values({'request_data': body, **{}})
            return self._operation(
                '/public_api/v1/endpoints/restore', method='post',
                body=body,
            )

    def quarantine(self, *,
                   accept_encoding: Union[str, None, UnsetType] = UNSET,
                   filters: Union[List[dict], None, UnsetType] = UNSET,
                   file_path: Union[str, None, UnsetType] = UNSET,
                   file_hash: Union[str, None, UnsetType] = UNSET) -> Any:
        """Quarantine Files

        POST /public_api/v1/endpoints/quarantine
        Available in Cortex XDR 3.x, 5.x.
        Returns the complete JSON response, bytes for downloads, or None for an empty response.
        Omit optional fields with UNSET; explicit None is sent as JSON null.
        :param accept_encoding: header field Accept-Encoding.
        :param filters: body field filters.
        :param file_path: body field file_path.
        :param file_hash: body field file_hash.
        """
        self._require_versions((3, 5))
        if self._api_version == APIVersion.V3:
            body = self._values({'filters': filters, 'file_path': file_path, 'file_hash': file_hash})
            body = self._values({'request_data': body, **{}})
            return self._operation(
                '/public_api/v1/endpoints/quarantine', method='post',
                headers={'Accept-Encoding': accept_encoding},
                body=body,
            )
        elif self._api_version == APIVersion.V5:
            self._reject_fields(accept_encoding=accept_encoding)
            body = self._values({'filters': filters, 'file_path': file_path, 'file_hash': file_hash})
            body = self._values({'request_data': body, **{}})
            return self._operation(
                '/public_api/v1/endpoints/quarantine', method='post',
                body=body,
            )

    def unisolate(self, *,
                  accept_encoding: Union[str, None, UnsetType] = UNSET,
                  filters: Union[List[dict], None, UnsetType] = UNSET,
                  endpoint_id: Union[str, None, UnsetType] = UNSET,
                  incident_id: Union[str, None, UnsetType] = UNSET) -> Any:
        """Unisolate Endpoints

        POST /public_api/v1/endpoints/unisolate
        Available in Cortex XDR 3.x, 5.x.
        Returns the complete JSON response, bytes for downloads, or None for an empty response.
        Omit optional fields with UNSET; explicit None is sent as JSON null.
        :param accept_encoding: header field Accept-Encoding.
        :param filters: body field filters.
        :param endpoint_id: body field endpoint_id.
        :param incident_id: body field incident_id.
        """
        self._require_versions((3, 5))
        if self._api_version == APIVersion.V3:
            body = self._values({'filters': filters, 'endpoint_id': endpoint_id, 'incident_id': incident_id})
            body = self._values({'request_data': body, **{}})
            return self._operation(
                '/public_api/v1/endpoints/unisolate', method='post',
                headers={'Accept-Encoding': accept_encoding},
                body=body,
            )
        elif self._api_version == APIVersion.V5:
            self._reject_fields(accept_encoding=accept_encoding)
            body = self._values({'filters': filters, 'endpoint_id': endpoint_id, 'incident_id': incident_id})
            body = self._values({'request_data': body, **{}})
            return self._operation(
                '/public_api/v1/endpoints/unisolate', method='post',
                body=body,
            )

    def abort_scan(self, *,
                   accept_encoding: Union[str, None, UnsetType] = UNSET,
                   filters: Union[List[dict], None, UnsetType] = UNSET,
                   incident_id: Union[str, None, UnsetType] = UNSET) -> Any:
        """Cancel Scan Endpoints

        POST /public_api/v1/endpoints/abort_scan
        Available in Cortex XDR 3.x, 5.x.
        Returns the complete JSON response, bytes for downloads, or None for an empty response.
        Omit optional fields with UNSET; explicit None is sent as JSON null.
        :param accept_encoding: header field Accept-Encoding.
        :param filters: body field filters.
        :param incident_id: body field incident_id.
        """
        self._require_versions((3, 5))
        if self._api_version == APIVersion.V3:
            body = self._values({'filters': filters, 'incident_id': incident_id})
            body = self._values({'request_data': body, **{}})
            return self._operation(
                '/public_api/v1/endpoints/abort_scan', method='post',
                headers={'Accept-Encoding': accept_encoding},
                body=body,
            )
        elif self._api_version == APIVersion.V5:
            self._reject_fields(accept_encoding=accept_encoding)
            body = self._values({'filters': filters, 'incident_id': incident_id})
            body = self._values({'request_data': body, **{}})
            return self._operation(
                '/public_api/v1/endpoints/abort_scan', method='post',
                body=body,
            )

    def scan(self, *,
             filters: Union[dict, None, UnsetType] = UNSET,
             incident_id: Union[str, None, UnsetType] = UNSET) -> Any:
        """Scan Endpoints

        POST /public_api/v1/endpoints/scan
        Available in Cortex XDR 3.x, 5.x.
        Returns the complete JSON response, bytes for downloads, or None for an empty response.
        Omit optional fields with UNSET; explicit None is sent as JSON null.
        :param filters: body field filters.
        :param incident_id: body field incident_id.
        """
        self._require_versions((3, 5))
        if self._api_version == APIVersion.V3:
            body = self._values({'filters': filters, 'incident_id': incident_id})
            body = self._values({'request_data': body, **{}})
            return self._operation(
                '/public_api/v1/endpoints/scan', method='post',
                body=body,
            )
        elif self._api_version == APIVersion.V5:
            body = self._values({'filters': filters, 'incident_id': incident_id})
            body = self._values({'request_data': body, **{}})
            return self._operation(
                '/public_api/v1/endpoints/scan', method='post',
                body=body,
            )

    def file_retrieval(self, *,
                       accept_encoding: Union[str, None, UnsetType] = UNSET,
                       filters: Union[List[dict], None, UnsetType] = UNSET,
                       files: Union[dict, None, UnsetType] = UNSET,
                       incident_id: Union[str, None, UnsetType] = UNSET) -> Any:
        """Retrieve File

        POST /public_api/v1/endpoints/file_retrieval
        Available in Cortex XDR 3.x, 5.x.
        Returns the complete JSON response, bytes for downloads, or None for an empty response.
        Omit optional fields with UNSET; explicit None is sent as JSON null.
        :param accept_encoding: header field Accept-Encoding.
        :param filters: body field filters.
        :param files: body field files.
        :param incident_id: body field incident_id.
        """
        self._require_versions((3, 5))
        if self._api_version == APIVersion.V3:
            body = self._values({'filters': filters, 'files': files, 'incident_id': incident_id})
            body = self._values({'request_data': body, **{}})
            return self._operation(
                '/public_api/v1/endpoints/file_retrieval', method='post',
                headers={'Accept-Encoding': accept_encoding},
                body=body,
            )
        elif self._api_version == APIVersion.V5:
            self._reject_fields(accept_encoding=accept_encoding)
            body = self._values({'filters': filters, 'files': files, 'incident_id': incident_id})
            body = self._values({'request_data': body, **{}})
            return self._operation(
                '/public_api/v1/endpoints/file_retrieval', method='post',
                body=body,
            )

    def isolate(self, *,
                accept_encoding: Union[str, None, UnsetType] = UNSET,
                filters: Union[List[dict], None, UnsetType] = UNSET,
                endpoint_id: Union[str, None, UnsetType] = UNSET,
                incident_id: Union[str, None, UnsetType] = UNSET) -> Any:
        """Isolate Endpoints

        POST /public_api/v1/endpoints/isolate
        Available in Cortex XDR 3.x, 5.x.
        Returns the complete JSON response, bytes for downloads, or None for an empty response.
        Omit optional fields with UNSET; explicit None is sent as JSON null.
        :param accept_encoding: header field Accept-Encoding.
        :param filters: body field filters.
        :param endpoint_id: body field endpoint_id.
        :param incident_id: body field incident_id.
        """
        self._require_versions((3, 5))
        if self._api_version == APIVersion.V3:
            body = self._values({'filters': filters, 'endpoint_id': endpoint_id, 'incident_id': incident_id})
            body = self._values({'request_data': body, **{}})
            return self._operation(
                '/public_api/v1/endpoints/isolate', method='post',
                headers={'Accept-Encoding': accept_encoding},
                body=body,
            )
        elif self._api_version == APIVersion.V5:
            self._reject_fields(accept_encoding=accept_encoding)
            body = self._values({'filters': filters, 'endpoint_id': endpoint_id, 'incident_id': incident_id})
            body = self._values({'request_data': body, **{}})
            return self._operation(
                '/public_api/v1/endpoints/isolate', method='post',
                body=body,
            )

    def upgrade(self, *,
                endpoint_ids: Union[List[str], None, UnsetType] = UNSET,
                target_versions: Union[dict, None, UnsetType] = UNSET,
                upgrade_timeframe_window: Union[dict, None, UnsetType] = UNSET) -> Any:
        """Upgrade Agents

        POST /public_api/v1/endpoints/upgrade
        Available in Cortex XDR 5.x.
        Returns the complete JSON response, bytes for downloads, or None for an empty response.
        Omit optional fields with UNSET; explicit None is sent as JSON null.
        :param endpoint_ids: body field endpoint_ids.
        :param target_versions: body field target_versions.
        :param upgrade_timeframe_window: body field upgrade_timeframe_window.
        """
        self._require_versions((5,))
        body = self._values({'endpoint_ids': endpoint_ids, 'target_versions': target_versions, 'upgrade_timeframe_window': upgrade_timeframe_window})
        body = self._values({'request_data': body, **{}})
        return self._operation(
            '/public_api/v1/endpoints/upgrade', method='post',
            body=body,
        )
