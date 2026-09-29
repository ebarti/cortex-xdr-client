from typing import Any, List, Tuple, Union

from cortex_xdr_client.api.operation import UNSET, UnsetType

from cortex_xdr_client.api.authentication import Authentication
from cortex_xdr_client.api.base_api import BaseAPI
from cortex_xdr_client.api.version import APIVersion


class SystemAPI(BaseAPI):
    def __init__(self, auth: Authentication, fqdn: str, timeout: Tuple[int, int],
                 api_version: APIVersion = APIVersion.V3) -> None:
        super(SystemAPI, self).__init__(auth, fqdn, 'system', timeout, api_version)

    def healthcheck(self, *,
                    accept_encoding: Union[str, None, UnsetType] = UNSET) -> Any:
        """System Health Check

        GET /public_api/v1/healthcheck
        Available in Cortex XDR 3.x, 5.x.
        Returns the complete JSON response, bytes for downloads, or None for an empty response.
        Omit optional fields with UNSET; explicit None is sent as JSON null.
        :param accept_encoding: header field Accept-Encoding.
        """
        self._require_versions((3, 5))
        if self._api_version == APIVersion.V3:
            body = UNSET
            return self._operation(
                '/public_api/v1/healthcheck', method='get',
                headers={'Accept-Encoding': accept_encoding},
                body=body,
            )
        elif self._api_version == APIVersion.V5:
            self._reject_fields(accept_encoding=accept_encoding)
            body = UNSET
            return self._operation(
                '/public_api/v1/healthcheck', method='get',
                body=body,
            )

    def get_tenant_info(self, *,
                        accept_encoding: Union[str, None, UnsetType] = UNSET,
                        request_data: Union[dict, None, UnsetType] = UNSET) -> Any:
        """Get Tenant Info

        POST /public_api/v1/system/get_tenant_info
        Available in Cortex XDR 3.x, 5.x.
        Returns the complete JSON response, bytes for downloads, or None for an empty response.
        Omit optional fields with UNSET; explicit None is sent as JSON null.
        :param accept_encoding: header field Accept-Encoding.
        :param request_data: payload field request_data.
        """
        self._require_versions((3, 5))
        if self._api_version == APIVersion.V3:
            body = request_data
            body = self._values({'request_data': body, **{}})
            return self._operation(
                '/public_api/v1/system/get_tenant_info', method='post',
                headers={'Accept-Encoding': accept_encoding},
                body=body,
            )
        elif self._api_version == APIVersion.V5:
            self._reject_fields(accept_encoding=accept_encoding)
            body = request_data
            body = self._values({'request_data': body, **{}})
            return self._operation(
                '/public_api/v1/system/get_tenant_info', method='post',
                body=body,
            )

    def triage_endpoint(self, *,
                        accept_encoding: Union[str, None, UnsetType] = UNSET,
                        agent_ids: Union[List[str], None, UnsetType] = UNSET,
                        collector_uuid: Union[str, None, UnsetType] = UNSET) -> Any:
        """Initiate Forensics Triage

        POST /public_api/v1/triage_endpoint
        Available in Cortex XDR 3.x, 5.x.
        Returns the complete JSON response, bytes for downloads, or None for an empty response.
        Omit optional fields with UNSET; explicit None is sent as JSON null.
        :param accept_encoding: header field Accept-Encoding.
        :param agent_ids: body field agent_ids.
        :param collector_uuid: body field collector_uuid.
        """
        self._require_versions((3, 5))
        if self._api_version == APIVersion.V3:
            body = self._values({'agent_ids': agent_ids, 'collector_uuid': collector_uuid})
            body = self._values({'request_data': body, **{}})
            return self._operation(
                '/public_api/v1/triage_endpoint', method='post',
                headers={'Accept-Encoding': accept_encoding},
                body=body,
            )
        elif self._api_version == APIVersion.V5:
            self._reject_fields(accept_encoding=accept_encoding)
            body = self._values({'agent_ids': agent_ids, 'collector_uuid': collector_uuid})
            body = self._values({'request_data': body, **{}})
            return self._operation(
                '/public_api/v1/triage_endpoint', method='post',
                body=body,
            )

    def get_triage_presets(self, *,
                           accept_encoding: Union[str, None, UnsetType] = UNSET,
                           request_data: Union[dict, None, UnsetType] = UNSET) -> Any:
        """Get triage presets

        POST /public_api/v1/get_triage_presets
        Available in Cortex XDR 3.x, 5.x.
        Returns the complete JSON response, bytes for downloads, or None for an empty response.
        Omit optional fields with UNSET; explicit None is sent as JSON null.
        :param accept_encoding: header field Accept-Encoding.
        :param request_data: payload field request_data.
        """
        self._require_versions((3, 5))
        if self._api_version == APIVersion.V3:
            body = request_data
            body = self._values({'request_data': body, **{}})
            return self._operation(
                '/public_api/v1/get_triage_presets', method='post',
                headers={'Accept-Encoding': accept_encoding},
                body=body,
            )
        elif self._api_version == APIVersion.V5:
            self._reject_fields(accept_encoding=accept_encoding)
            body = request_data
            body = self._values({'request_data': body, **{}})
            return self._operation(
                '/public_api/v1/get_triage_presets', method='post',
                body=body,
            )

    def assets(self, *,
               filters: Union[Any, None, UnsetType] = UNSET,
               on_demand_fields: Union[List[str], None, UnsetType] = UNSET,
               sort: Union[List[dict], None, UnsetType] = UNSET,
               search_from: Union[int, None, UnsetType] = UNSET,
               search_to: Union[int, None, UnsetType] = UNSET) -> Any:
        """Get all or filtered assets

        POST /public_api/v1/assets
        Available in Cortex XDR 5.x.
        Returns the complete JSON response, bytes for downloads, or None for an empty response.
        Omit optional fields with UNSET; explicit None is sent as JSON null.
        :param filters: body field filters.
        :param on_demand_fields: body field on_demand_fields.
        :param sort: body field sort.
        :param search_from: body field search_from.
        :param search_to: body field search_to.
        """
        self._require_versions((5,))
        body = self._values({'filters': filters, 'on_demand_fields': on_demand_fields, 'sort': sort, 'search_from': search_from, 'search_to': search_to})
        body = {'request_data': body}
        return self._operation(
            '/public_api/v1/assets', method='post',
            body=body,
        )

    def asset_groups(self, *,
                     filters: Union[Any, None, UnsetType] = UNSET,
                     sort: Union[List[dict], None, UnsetType] = UNSET,
                     search_from: Union[int, None, UnsetType] = UNSET,
                     search_to: Union[int, None, UnsetType] = UNSET) -> Any:
        """Get all or filtered asset groups

        POST /public_api/v1/asset-groups
        Available in Cortex XDR 5.x.
        Returns the complete JSON response, bytes for downloads, or None for an empty response.
        Omit optional fields with UNSET; explicit None is sent as JSON null.
        :param filters: body field filters.
        :param sort: body field sort.
        :param search_from: body field search_from.
        :param search_to: body field search_to.
        """
        self._require_versions((5,))
        body = self._values({'filters': filters, 'sort': sort, 'search_from': search_from, 'search_to': search_to})
        body = self._values({'request_data': body, **{}})
        return self._operation(
            '/public_api/v1/asset-groups', method='post',
            body=body,
        )
