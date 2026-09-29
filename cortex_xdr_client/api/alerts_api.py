from typing import Any, List, Optional, Tuple, Union

from cortex_xdr_client.api.operation import UNSET, UnsetType

from enum import Enum

from cortex_xdr_client.api.authentication import Authentication
from cortex_xdr_client.api.base_api import BaseAPI
from cortex_xdr_client.api.version import APIVersion
from cortex_xdr_client.api.models.alerts import (
    AlertSeverity,
    GetAlertsResponse,
)
from cortex_xdr_client.api.models.filters import (
    new_request_data,
    request_filter,
    request_gte_lte_filter,
)


class AlertsAPI(BaseAPI):
    def __init__(self, auth: Authentication, fqdn: str, timeout: Tuple[int, int],
                 api_version: APIVersion = APIVersion.V3) -> None:
        super(AlertsAPI, self).__init__(auth, fqdn, "alerts", timeout, api_version)

    # https://docs.paloaltonetworks.com/cortex/cortex-xdr/cortex-xdr-api/cortex-xdr-apis/incident-management/get-alerts.html
    def get_alerts(self,
                   alert_id_list: List[int] = None,
                   alert_source_list: List[str] = None,
                   severities: List[AlertSeverity] = None,
                   creation_time: int = None,
                   after_creation: bool = False,
                   server_creation_time: int = None,
                   after_server_creation: bool = False,
                   search_from: int = None,
                   search_to: int = None,
                   sort: dict = None,
                   external_id_list: List[str] = None,
                   ) -> Optional[GetAlertsResponse]:
        """
        Get a list of alerts with multiple events.

        :param alert_id_list: List of integers of the Alert ID
        :param alert_source_list: List of strings of the Alert source
        :param severities: List of strings of the Alert severity
        :param creation_time: Timestamp of the Creation time. Also known as detection_timestamp.
        :param after_creation: If the creation date will be the upper or lower bound limit.
        :param server_creation_time: Timestamp of the Server creation time. Also known as local_insert_ts.
        :param after_server_creation: If the server creation date will be the upper or lower bound limit.
        :param search_to: Integer representing the end offset within the result set after which you do not want incidents returned.
        :param search_from: Integer representing the starting offset within the query result set from which you want incidents returned.
        :param sort: Sort field and keyword (asc or desc).
        :param external_id_list: External alert IDs to match.
        :return: Returns a GetAlertsResponse object if successful.
        """
        filters = []

        if alert_id_list is not None:
            filters.append(request_filter("alert_id_list", "in", alert_id_list))

        if alert_source_list is not None:
            filters.append(request_filter("alert_source", "in", alert_source_list))

        if severities is not None and len(severities) > 0:
            filters.append(request_filter("severity", "in", get_enum_values(severities)))

        if creation_time is not None:
            filters.append(request_gte_lte_filter("creation_time", creation_time, after_creation))

        if server_creation_time is not None:
            filters.append(request_gte_lte_filter("server_creation_time", server_creation_time, after_server_creation))

        if external_id_list is not None:
            filters.append(request_filter("external_id_list", "in", external_id_list))

        request_data = new_request_data(filters=filters, search_from=search_from, search_to=search_to, sort=sort)

        response = self._call(call_name="get_alerts_multi_events",
                              json_value=request_data)
        return GetAlertsResponse.model_validate(response.json())


    def get_alerts_request(self, *,
                           accept_encoding: Union[str, None, UnsetType] = UNSET,
                           filters: Union[List[dict], None, UnsetType] = UNSET,
                           search_from: Union[int, None, UnsetType] = UNSET,
                           search_to: Union[int, None, UnsetType] = UNSET,
                           sort: Union[dict, None, UnsetType] = UNSET) -> Any:
        """Get all Alerts

        POST /public_api/v1/alerts/get_alerts
        Available in Cortex XDR 3.x.
        Returns the complete JSON response, bytes for downloads, or None for an empty response.
        Omit optional fields with UNSET; explicit None is sent as JSON null.
        :param accept_encoding: header field Accept-Encoding.
        :param filters: body field filters.
        :param search_from: body field search_from.
        :param search_to: body field search_to.
        :param sort: body field sort.
        """
        self._require_versions((3,))
        body = self._values({'filters': filters, 'search_from': search_from, 'search_to': search_to, 'sort': sort})
        body = self._values({'request_data': body, **{}})
        return self._operation(
            '/public_api/v1/alerts/get_alerts', method='post',
            headers={'Accept-Encoding': accept_encoding},
            body=body,
        )

    def update_alerts(self, *,
                      accept_encoding: Union[str, None, UnsetType] = UNSET,
                      alert_id_list: Union[List[str], None, UnsetType] = UNSET,
                      update_data: Union[dict, None, UnsetType] = UNSET) -> Any:
        """Update Alerts

        POST /public_api/v1/alerts/update_alerts
        Available in Cortex XDR 3.x.
        Returns the complete JSON response, bytes for downloads, or None for an empty response.
        Omit optional fields with UNSET; explicit None is sent as JSON null.
        :param accept_encoding: header field Accept-Encoding.
        :param alert_id_list: body field alert_id_list.
        :param update_data: body field update_data.
        """
        self._require_versions((3,))
        body = self._values({'alert_id_list': alert_id_list, 'update_data': update_data})
        body = self._values({'request_data': body, **{}})
        return self._operation(
            '/public_api/v1/alerts/update_alerts', method='post',
            headers={'Accept-Encoding': accept_encoding},
            body=body,
        )

    def insert_cef_alerts(self, *,
                          accept_encoding: Union[str, None, UnsetType] = UNSET,
                          alerts: Union[List[str], None, UnsetType] = UNSET) -> Any:
        """Insert CEF Alerts

        POST /public_api/v1/alerts/insert_cef_alerts
        Available in Cortex XDR 3.x.
        Returns the complete JSON response, bytes for downloads, or None for an empty response.
        Omit optional fields with UNSET; explicit None is sent as JSON null.
        :param accept_encoding: header field Accept-Encoding.
        :param alerts: body field alerts.
        """
        self._require_versions((3,))
        body = self._values({'alerts': alerts})
        body = self._values({'request_data': body, **{}})
        return self._operation(
            '/public_api/v1/alerts/insert_cef_alerts', method='post',
            headers={'Accept-Encoding': accept_encoding},
            body=body,
        )

    def insert_parsed_alerts(self, *,
                             accept_encoding: Union[str, None, UnsetType] = UNSET,
                             alerts: Union[List[dict], None, UnsetType] = UNSET) -> Any:
        """Insert Parsed Alerts

        POST /public_api/v1/alerts/insert_parsed_alerts
        Available in Cortex XDR 3.x.
        Returns the complete JSON response, bytes for downloads, or None for an empty response.
        Omit optional fields with UNSET; explicit None is sent as JSON null.
        :param accept_encoding: header field Accept-Encoding.
        :param alerts: body field alerts.
        """
        self._require_versions((3,))
        body = self._values({'alerts': alerts})
        body = self._values({'request_data': body, **{}})
        return self._operation(
            '/public_api/v1/alerts/insert_parsed_alerts', method='post',
            headers={'Accept-Encoding': accept_encoding},
            body=body,
        )

    def get_alerts_pcap(self, *,
                        accept_encoding: Union[str, None, UnsetType] = UNSET,
                        filters: Union[List[dict], None, UnsetType] = UNSET,
                        search_from: Union[str, None, UnsetType] = UNSET,
                        search_to: Union[str, None, UnsetType] = UNSET,
                        sort: Union[dict, None, UnsetType] = UNSET) -> Any:
        """Retrieve PCAP Packet

        POST /public_api/v1/alerts/get_alerts_pcap
        Available in Cortex XDR 3.x.
        Returns the complete JSON response, bytes for downloads, or None for an empty response.
        Omit optional fields with UNSET; explicit None is sent as JSON null.
        :param accept_encoding: header field Accept-Encoding.
        :param filters: body field filters.
        :param search_from: body field search_from.
        :param search_to: body field search_to.
        :param sort: body field sort.
        """
        self._require_versions((3,))
        body = self._values({'filters': filters, 'search_from': search_from, 'search_to': search_to, 'sort': sort})
        body = self._values({'request_data': body, **{}})
        return self._operation(
            '/public_api/v1/alerts/get_alerts_pcap', method='post',
            headers={'Accept-Encoding': accept_encoding},
            body=body,
        )

    def get_alerts_multi_events(self, *,
                                accept_encoding: Union[str, None, UnsetType] = UNSET,
                                filters: Union[List[Any], None, UnsetType] = UNSET) -> Any:
        """Get Alerts Multi-Events v2

        POST /public_api/v2/alerts/get_alerts_multi_events
        Available in Cortex XDR 3.x.
        Returns the complete JSON response, bytes for downloads, or None for an empty response.
        Omit optional fields with UNSET; explicit None is sent as JSON null.
        :param accept_encoding: header field Accept-Encoding.
        :param filters: body field filters.
        """
        self._require_versions((3,))
        body = self._values({'filters': filters})
        body = self._values({'request_data': body, **{}})
        return self._operation(
            '/public_api/v2/alerts/get_alerts_multi_events', method='post',
            headers={'Accept-Encoding': accept_encoding},
            body=body,
        )

    def get_alerts_multi_events_v1(self, *,
                                   accept_encoding: Union[str, None, UnsetType] = UNSET,
                                   filters: Union[List[dict], None, UnsetType] = UNSET,
                                   search_from: Union[int, None, UnsetType] = UNSET,
                                   search_to: Union[int, None, UnsetType] = UNSET,
                                   sort: Union[dict, None, UnsetType] = UNSET) -> Any:
        """Get Alerts Multi-Events v1

        POST /public_api/v1/alerts/get_alerts_multi_events
        Available in Cortex XDR 3.x.
        Returns the complete JSON response, bytes for downloads, or None for an empty response.
        Omit optional fields with UNSET; explicit None is sent as JSON null.
        :param accept_encoding: header field Accept-Encoding.
        :param filters: body field filters.
        :param search_from: body field search_from.
        :param search_to: body field search_to.
        :param sort: body field sort.
        """
        self._require_versions((3,))
        body = self._values({'filters': filters, 'search_from': search_from, 'search_to': search_to, 'sort': sort})
        body = self._values({'request_data': body, **{}})
        return self._operation(
            '/public_api/v1/alerts/get_alerts_multi_events', method='post',
            headers={'Accept-Encoding': accept_encoding},
            body=body,
        )


def get_enum_values(p: List[Enum]) -> List[str]:
    return [e.value for e in p]
