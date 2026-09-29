from typing import Any, List, Optional, Tuple, Union

from cortex_xdr_client.api.operation import UNSET, UnsetType


from cortex_xdr_client.api.authentication import Authentication
from cortex_xdr_client.api.base_api import BaseAPI
from cortex_xdr_client.api.version import APIVersion
from cortex_xdr_client.api.models.ioc import IoC, IoCResponse


class IocAPI(BaseAPI):
    def __init__(self, auth: Authentication, fqdn: str, timeout: Tuple[int, int],
                 api_version: APIVersion = APIVersion.V3) -> None:
        super(IocAPI, self).__init__(auth, fqdn, "indicators", timeout, api_version)

    def insert_json(self, indicators: List[IoC], validate: Optional[bool] = True) -> IoCResponse:
        """
        Upload IOCs as JSON objects that you retrieved from external threat intelligence sources.
        :param indicators: List of IoC objects
        :param validate: Whether to return an array of errors in the case of an unsuccessful update indicator API request.
        :return: Returns an IoCResponse object if successful.
        """
        values = [indicator.model_dump(by_alias=True, exclude_none=True) for indicator in indicators]
        for value in values:
            if value['severity'] == 'INFORMATIONAL':
                value['severity'] = 'INFO'
            elif value['severity'] == 'UNKNOWN':
                if self._api_version == APIVersion.V5:
                    raise ValueError("XDR 5 indicators require INFO, LOW, MEDIUM, HIGH or CRITICAL severity")
                value['severity'] = 'unknown'
        request_data = {
            "request_data": values,
            "validate":     validate
        }
        response = self._call(call_name="insert_jsons", json_value=request_data)
        return IoCResponse.model_validate(response.json())


    def insert_csv(self, *,
                   accept_encoding: Union[str, None, UnsetType] = UNSET,
                   validate: Union[bool, None, UnsetType] = UNSET,
                   request_data: Union[str, None, UnsetType] = UNSET) -> Any:
        """Insert Simple Indicators, CSV

        POST /public_api/v1/indicators/insert_csv
        Available in Cortex XDR 3.x, 5.x.
        Returns the complete JSON response, bytes for downloads, or None for an empty response.
        Omit optional fields with UNSET; explicit None is sent as JSON null.
        :param accept_encoding: header field Accept-Encoding.
        :param validate: outer field validate.
        :param request_data: payload field request_data.
        """
        self._require_versions((3, 5))
        if self._api_version == APIVersion.V3:
            body = request_data
            body = self._values({'request_data': body, **{'validate': validate}})
            return self._operation(
                '/public_api/v1/indicators/insert_csv', method='post',
                headers={'Accept-Encoding': accept_encoding},
                body=body,
            )
        elif self._api_version == APIVersion.V5:
            self._reject_fields(accept_encoding=accept_encoding)
            body = request_data
            body = self._values({'request_data': body, **{'validate': validate}})
            return self._operation(
                '/public_api/v1/indicators/insert_csv', method='post',
                body=body,
            )

    def insert_jsons(self, *,
                     accept_encoding: Union[str, None, UnsetType] = UNSET,
                     validate: Union[bool, None, UnsetType] = UNSET,
                     request_data: Union[List[dict], None, UnsetType] = UNSET) -> Any:
        """Insert Simple Indicators, JSON

        POST /public_api/v1/indicators/insert_jsons
        Available in Cortex XDR 3.x, 5.x.
        Returns the complete JSON response, bytes for downloads, or None for an empty response.
        Omit optional fields with UNSET; explicit None is sent as JSON null.
        :param accept_encoding: header field Accept-Encoding.
        :param validate: outer field validate.
        :param request_data: payload field request_data.
        """
        self._require_versions((3, 5))
        if self._api_version == APIVersion.V3:
            body = request_data
            body = self._values({'request_data': body, **{'validate': validate}})
            return self._operation(
                '/public_api/v1/indicators/insert_jsons', method='post',
                headers={'Accept-Encoding': accept_encoding},
                body=body,
            )
        elif self._api_version == APIVersion.V5:
            self._reject_fields(accept_encoding=accept_encoding)
            body = request_data
            body = self._values({'request_data': body, **{'validate': validate}})
            return self._operation(
                '/public_api/v1/indicators/insert_jsons', method='post',
                body=body,
            )

    def get(self, *,
            extended_view: Union[bool, None, UnsetType] = UNSET,
            filters: Union[List[dict], None, UnsetType] = UNSET,
            search_from: Union[int, None, UnsetType] = UNSET,
            search_to: Union[int, None, UnsetType] = UNSET) -> Any:
        """Get Indicators (IOCs)

        POST /public_api/v1/indicators/get
        Available in Cortex XDR 5.x.
        Returns the complete JSON response, bytes for downloads, or None for an empty response.
        Omit optional fields with UNSET; explicit None is sent as JSON null.
        :param extended_view: body field extended_view.
        :param filters: body field filters.
        :param search_from: body field search_from.
        :param search_to: body field search_to.
        """
        self._require_versions((5,))
        body = self._values({'extended_view': extended_view, 'filters': filters, 'search_from': search_from, 'search_to': search_to})
        body = self._values({'request_data': body, **{}})
        return self._operation(
            '/public_api/v1/indicators/get', method='post',
            body=body,
        )

    def insert(self, *,
               request_data: Union[List[dict], None, UnsetType] = UNSET) -> Any:
        """Insert or update IOCs

        POST /public_api/v1/indicators/insert
        Available in Cortex XDR 5.x.
        Returns the complete JSON response, bytes for downloads, or None for an empty response.
        Omit optional fields with UNSET; explicit None is sent as JSON null.
        :param request_data: payload field request_data.
        """
        self._require_versions((5,))
        body = request_data
        body = self._values({'request_data': body, **{}})
        return self._operation(
            '/public_api/v1/indicators/insert', method='post',
            body=body,
        )

    def delete(self, *,
               filters: Union[List[dict], None, UnsetType] = UNSET) -> Any:
        """Delete Indicators (IOCs)

        POST /public_api/v1/indicators/delete
        Available in Cortex XDR 5.x.
        Returns the complete JSON response, bytes for downloads, or None for an empty response.
        Omit optional fields with UNSET; explicit None is sent as JSON null.
        :param filters: body field filters.
        """
        self._require_versions((5,))
        body = self._values({'filters': filters})
        body = self._values({'request_data': body, **{}})
        return self._operation(
            '/public_api/v1/indicators/delete', method='post',
            body=body,
        )
