from typing import Any, List, Tuple, Union

from cortex_xdr_client.api.operation import UNSET, UnsetType

from cortex_xdr_client.api.authentication import Authentication
from cortex_xdr_client.api.base_api import BaseAPI
from cortex_xdr_client.api.version import APIVersion


class AuditsAPI(BaseAPI):
    def __init__(self, auth: Authentication, fqdn: str, timeout: Tuple[int, int],
                 api_version: APIVersion = APIVersion.V3) -> None:
        super(AuditsAPI, self).__init__(auth, fqdn, 'audits', timeout, api_version)

    def management_logs(self, *,
                        accept_encoding: Union[str, None, UnsetType] = UNSET,
                        filters: Union[List[dict], None, UnsetType] = UNSET,
                        search_from: Union[int, None, UnsetType] = UNSET,
                        search_to: Union[int, None, UnsetType] = UNSET,
                        sort: Union[dict, None, UnsetType] = UNSET) -> Any:
        """Get Audit Management Log

        POST /public_api/v1/audits/management_logs
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
                '/public_api/v1/audits/management_logs', method='post',
                headers={'Accept-Encoding': accept_encoding},
                body=body,
            )
        elif self._api_version == APIVersion.V5:
            self._reject_fields(accept_encoding=accept_encoding)
            body = self._values({'filters': filters, 'search_from': search_from, 'search_to': search_to, 'sort': sort})
            body = self._values({'request_data': body, **{}})
            return self._operation(
                '/public_api/v1/audits/management_logs', method='post',
                body=body,
            )

    def agents_reports(self, *,
                       accept_encoding: Union[str, None, UnsetType] = UNSET,
                       filters: Union[List[dict], None, UnsetType] = UNSET,
                       search_from: Union[int, None, UnsetType] = UNSET,
                       search_to: Union[int, None, UnsetType] = UNSET,
                       sort: Union[dict, None, UnsetType] = UNSET) -> Any:
        """Get Audit Agent Report

        POST /public_api/v1/audits/agents_reports
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
                '/public_api/v1/audits/agents_reports', method='post',
                headers={'Accept-Encoding': accept_encoding},
                body=body,
            )
        elif self._api_version == APIVersion.V5:
            self._reject_fields(accept_encoding=accept_encoding)
            body = self._values({'filters': filters, 'search_from': search_from, 'search_to': search_to, 'sort': sort})
            body = self._values({'request_data': body, **{}})
            return self._operation(
                '/public_api/v1/audits/agents_reports', method='post',
                body=body,
            )
