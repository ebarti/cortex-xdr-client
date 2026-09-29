from typing import Any, List, Tuple, Union

from cortex_xdr_client.api.operation import UNSET, UnsetType

from cortex_xdr_client.api.authentication import Authentication
from cortex_xdr_client.api.base_api import BaseAPI
from cortex_xdr_client.api.version import APIVersion


class IntegrationsAPI(BaseAPI):
    def __init__(self, auth: Authentication, fqdn: str, timeout: Tuple[int, int],
                 api_version: APIVersion = APIVersion.V3) -> None:
        super(IntegrationsAPI, self).__init__(auth, fqdn, 'integrations', timeout, api_version)

    def syslog_create(self, *,
                      name: Union[str, None, UnsetType] = UNSET,
                      address: Union[str, None, UnsetType] = UNSET,
                      port: Union[int, None, UnsetType] = UNSET,
                      protocol: Union[Any, None, UnsetType] = UNSET,
                      facility: Union[str, None, UnsetType] = UNSET,
                      security_info: Union[dict, None, UnsetType] = UNSET) -> Any:
        """Create a syslog integration

        POST /public_api/v1/integrations/syslog/create
        Available in Cortex XDR 3.x, 5.x.
        Returns the complete JSON response, bytes for downloads, or None for an empty response.
        Omit optional fields with UNSET; explicit None is sent as JSON null.
        :param name: body field name.
        :param address: body field address.
        :param port: body field port.
        :param protocol: body field protocol.
        :param facility: body field facility.
        :param security_info: body field security_info.
        """
        self._require_versions((3, 5))
        if self._api_version == APIVersion.V3:
            body = self._values({'name': name, 'address': address, 'port': port, 'protocol': protocol, 'facility': facility, 'security_info': security_info})
            body = self._values({'request_data': body, **{}})
            return self._operation(
                '/public_api/v1/integrations/syslog/create', method='post',
                body=body,
            )
        elif self._api_version == APIVersion.V5:
            body = self._values({'name': name, 'address': address, 'port': port, 'protocol': protocol, 'facility': facility, 'security_info': security_info})
            body = self._values({'request_data': body, **{}})
            return self._operation(
                '/public_api/v1/integrations/syslog/create', method='post',
                body=body,
            )

    def syslog_get(self, *,
                   filters: Union[List[dict], None, UnsetType] = UNSET) -> Any:
        """Get all or filtered syslog servers

        POST /public_api/v1/integrations/syslog/get
        Available in Cortex XDR 3.x, 5.x.
        Returns the complete JSON response, bytes for downloads, or None for an empty response.
        Omit optional fields with UNSET; explicit None is sent as JSON null.
        :param filters: body field filters.
        """
        self._require_versions((3, 5))
        if self._api_version == APIVersion.V3:
            body = self._values({'filters': filters})
            body = self._values({'request_data': body, **{}})
            return self._operation(
                '/public_api/v1/integrations/syslog/get', method='post',
                body=body,
            )
        elif self._api_version == APIVersion.V5:
            body = self._values({'filters': filters})
            body = self._values({'request_data': body, **{}})
            return self._operation(
                '/public_api/v1/integrations/syslog/get', method='post',
                body=body,
            )

    def syslog_update(self, *,
                      syslog_id: Union[str, None, UnsetType] = UNSET,
                      name: Union[str, None, UnsetType] = UNSET,
                      address: Union[str, None, UnsetType] = UNSET,
                      port: Union[str, None, UnsetType] = UNSET,
                      protocol: Union[Any, None, UnsetType] = UNSET,
                      facility: Union[str, None, UnsetType] = UNSET,
                      security_info: Union[dict, None, UnsetType] = UNSET) -> Any:
        """Update a syslog integration

        POST /public_api/v1/integrations/syslog/update
        Available in Cortex XDR 3.x, 5.x.
        Returns the complete JSON response, bytes for downloads, or None for an empty response.
        Omit optional fields with UNSET; explicit None is sent as JSON null.
        :param syslog_id: body field syslog_id.
        :param name: body field name.
        :param address: body field address.
        :param port: body field port.
        :param protocol: body field protocol.
        :param facility: body field facility.
        :param security_info: body field security_info.
        """
        self._require_versions((3, 5))
        if self._api_version == APIVersion.V3:
            body = self._values({'syslog_id': syslog_id, 'name': name, 'address': address, 'port': port, 'protocol': protocol, 'facility': facility, 'security_info': security_info})
            body = self._values({'request_data': body, **{}})
            return self._operation(
                '/public_api/v1/integrations/syslog/update', method='post',
                body=body,
            )
        elif self._api_version == APIVersion.V5:
            body = self._values({'syslog_id': syslog_id, 'name': name, 'address': address, 'port': port, 'protocol': protocol, 'facility': facility, 'security_info': security_info})
            body = self._values({'request_data': body, **{}})
            return self._operation(
                '/public_api/v1/integrations/syslog/update', method='post',
                body=body,
            )

    def syslog_delete(self, *,
                      filters: Union[List[dict], None, UnsetType] = UNSET) -> Any:
        """Delete all or filtered syslog integrations

        POST /public_api/v1/integrations/syslog/delete
        Available in Cortex XDR 3.x, 5.x.
        Returns the complete JSON response, bytes for downloads, or None for an empty response.
        Omit optional fields with UNSET; explicit None is sent as JSON null.
        :param filters: body field filters.
        """
        self._require_versions((3, 5))
        if self._api_version == APIVersion.V3:
            body = self._values({'filters': filters})
            body = self._values({'request_data': body, **{}})
            return self._operation(
                '/public_api/v1/integrations/syslog/delete', method='post',
                body=body,
            )
        elif self._api_version == APIVersion.V5:
            body = self._values({'filters': filters})
            body = self._values({'request_data': body, **{}})
            return self._operation(
                '/public_api/v1/integrations/syslog/delete', method='post',
                body=body,
            )

    def syslog_test(self, *,
                    syslog_id: Union[str, None, UnsetType] = UNSET,
                    name: Union[str, None, UnsetType] = UNSET,
                    address: Union[str, None, UnsetType] = UNSET,
                    port: Union[str, None, UnsetType] = UNSET,
                    protocol: Union[Any, None, UnsetType] = UNSET,
                    facility: Union[str, None, UnsetType] = UNSET,
                    security_info: Union[dict, None, UnsetType] = UNSET) -> Any:
        """Test syslog integration

        POST /public_api/v1/integrations/syslog/test
        Available in Cortex XDR 3.x, 5.x.
        Returns the complete JSON response, bytes for downloads, or None for an empty response.
        Omit optional fields with UNSET; explicit None is sent as JSON null.
        :param syslog_id: body field syslog_id.
        :param name: body field name.
        :param address: body field address.
        :param port: body field port.
        :param protocol: body field protocol.
        :param facility: body field facility.
        :param security_info: body field security_info.
        """
        self._require_versions((3, 5))
        if self._api_version == APIVersion.V3:
            body = self._values({'syslog_id': syslog_id, 'name': name, 'address': address, 'port': port, 'protocol': protocol, 'facility': facility, 'security_info': security_info})
            body = self._values({'request_data': body, **{}})
            return self._operation(
                '/public_api/v1/integrations/syslog/test', method='post',
                body=body,
            )
        elif self._api_version == APIVersion.V5:
            body = self._values({'syslog_id': syslog_id, 'name': name, 'address': address, 'port': port, 'protocol': protocol, 'facility': facility, 'security_info': security_info})
            body = self._values({'request_data': body, **{}})
            return self._operation(
                '/public_api/v1/integrations/syslog/test', method='post',
                body=body,
            )
