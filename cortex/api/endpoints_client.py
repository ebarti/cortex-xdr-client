from typing import List, Optional

from cortex.api.base_api import BaseAPI
from cortex.api.models.filters import Filter, new_filter_request_data
from cortex.api.utils.constants import Constants


# noinspection DuplicatedCode
class EndpointsAPI(BaseAPI):
    def __init__(self, api_key_id: str, api_key: str, fqdn: str, timeout: tuple[int, int]):
        super().__init__(api_key_id, api_key, fqdn, "endpoints", timeout)

    @staticmethod
    def _endpoint_id_list_filter(value: List[str]) -> Filter:
        return Filter("endpoint_id_list", "in", value)

    @staticmethod
    def _endpoint_status_filter(value: List[str]) -> Filter:
        return Filter("endpoint_status", "in", value)

    @staticmethod
    def _dist_name_filter(value: List[str]) -> Filter:
        return Filter("dist_name", "in", value)

    @staticmethod
    def _first_seen_filter(first_seen: int, after: bool) -> Filter:
        if after:
            return Filter("first_seen", "gte", first_seen)
        return Filter("first_seen", "lte", first_seen)

    @staticmethod
    def _last_seen_filter(last_seen: int, after: bool) -> Filter:
        if after:
            return Filter("last_seen", "gte", last_seen)
        return Filter("last_seen", "lte", last_seen)

    @staticmethod
    def _ip_list_filter(value: List[str]) -> Filter:
        return Filter("ip_list", "in", value)

    @staticmethod
    def _group_name_filter(value: List[str]) -> Filter:
        return Filter("group_name", "in", value)

    @staticmethod
    def _alias_filter(value: List[str]) -> Filter:
        return Filter("alias", "in", value)

    @staticmethod
    def _hostname_filter(value: List[str]) -> Filter:
        return Filter("hostname", "in", value)

    @staticmethod
    def _username_filter(value: List[str]) -> Filter:
        return Filter("username", "in", value)

    @staticmethod
    def _isolate_filter(value: List[str]) -> Filter:
        return Filter("isolate", "in", value)

    @staticmethod
    def _are_endpoint_status_valid(value: List[str]) -> bool:
        return all(x in Constants.ENDPOINT_STATUS for x in value)

    @staticmethod
    def _are_platforms_valid(value: List[str]) -> bool:
        return all(x in Constants.PLATFORMS for x in value)

    @staticmethod
    def _are_scan_status_valid(value: List[str]) -> bool:
        return all(x in Constants.SCAN_STATUS for x in value)

    def get_all_endpoints(self) -> Optional[dict]:
        response = self._call(call_name="get_endpoints")
        if response.ok:
            return response.json()
        return None

    def get_endpoint(self,
                     endpoint_id_list: List[str] = None,
                     endpoint_status: List[str] = None,
                     dist_name: List[str] = None,
                     first_seen: int = None,
                     after_first_seen: bool = False,
                     last_seen: int = None,
                     after_last_seen: bool = False,
                     ip_list: List[str] = None,
                     group_name: List[str] = None,
                     alias: List[str] = None,
                     hostname: List[str] = None,
                     username: List[str] = None,
                     ) -> Optional[dict]:
        filters = []
        if endpoint_id_list is not None:
            filters.append(self._endpoint_id_list_filter(endpoint_id_list))
        if endpoint_status is not None:
            filters.append(self._endpoint_status_filter(endpoint_status))
        if dist_name is not None:
            filters.append(self._dist_name_filter(dist_name))
        if first_seen is not None:
            filters.append(self._first_seen_filter(first_seen, after_first_seen))
        if last_seen is not None:
            filters.append(self._last_seen_filter(last_seen, after_last_seen))
        if ip_list is not None:
            filters.append(self._ip_list_filter(ip_list))
        if group_name is not None:
            filters.append(self._group_name_filter(group_name))
        if alias is not None:
            filters.append(self._alias_filter(alias))
        if hostname is not None:
            filters.append(self._hostname_filter(hostname))
        if username is not None:
            filters.append(self._username_filter(username))

        request_data = new_filter_request_data(filters=filters)

        response = self._call(call_name="get_endpoint",
                              request_data=request_data)
        if response.ok:
            return response.json()
        return None

    # https://docs.paloaltonetworks.com/cortex/cortex-xdr/cortex-xdr-api/cortex-xdr-apis/response-actions/isolate-endpoints.html
    def isolate_endpoints(self,
                          endpoint_id_list: List[str] = None,
                          ) -> Optional[dict]:
        request_data = new_filter_request_data([self._endpoint_id_list_filter(endpoint_id_list)])
        response = self._call(call_name="isolate",
                              request_data=request_data)
        if response.ok:
            return response.json()
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
                       alias: List[str] = None,
                       isolate: List[str] = None,
                       hostname: List[str] = None,
                       ) -> Optional[dict]:
        filters = []
        if endpoint_id_list is not None:
            filters.append(self._endpoint_id_list_filter(endpoint_id_list))
        if dist_name is not None:
            filters.append(self._dist_name_filter(dist_name))
        if first_seen is not None:
            filters.append(self._first_seen_filter(first_seen, after_first_seen))
        if last_seen is not None:
            filters.append(self._last_seen_filter(last_seen, after_last_seen))
        if ip_list is not None:
            filters.append(self._ip_list_filter(ip_list))
        if group_name is not None:
            filters.append(self._group_name_filter(group_name))
        if alias is not None:
            filters.append(self._alias_filter(alias))
        if isolate is not None:
            filters.append(self._isolate_filter(isolate))
        if hostname is not None:
            filters.append(self._hostname_filter(hostname))

        request_data = new_filter_request_data(filters=filters)

        response = self._call(call_name="scan",
                              request_data=request_data)
        if response.ok:
            return response.json()
        return None

    def scan_all_endpoints(self) -> Optional[dict]:
        request_data = {
            "request_data": {
                "filters": "all"
            }
        }
        response = self._call(call_name="scan",
                              request_data=request_data)
        if response.ok:
            return response.json()
        return None
