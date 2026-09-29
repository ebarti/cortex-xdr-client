"""Explicit operations from the pinned Cortex XDR documentation snapshot."""
from typing import Any, Union

from cortex_xdr_client.api.operation import OperationAPI, UNSET, UnsetType


class BrokerApplianceOperations(OperationAPI):
    def reset_initial_password(self, *, current_password: str, new_password: str) -> Any:
        """Replace the factory-default admin password

        POST /public_api/v1/auth/reset-initial-password
        Available in Cortex XDR 5.x.
        Returns the complete JSON response, text, bytes, or None for an empty response.
        Optional fields use UNSET for omission; None is explicit null.
        The source snapshot records this operation and its parameter schema.
        :param current_password: body field current_password.
        :param new_password: body field new_password.
        """
        self._require_versions((5,))
        body = self._values({'current_password': current_password, 'new_password': new_password})
        return self._operation(
            '/public_api/v1/auth/reset-initial-password', method='post',
            body=body,
        )

    def generate_token(self, *, password: str) -> Any:
        """Obtain a 10-minute Bearer token

        POST /public_api/v1/auth/token
        Available in Cortex XDR 5.x.
        Returns the complete JSON response, text, bytes, or None for an empty response.
        Optional fields use UNSET for omission; None is explicit null.
        The source snapshot records this operation and its parameter schema.
        :param password: body field password.
        """
        self._require_versions((5,))
        body = self._values({'password': password})
        return self._operation(
            '/public_api/v1/auth/token', method='post',
            body=body,
        )

    def issue_log_bundle(self) -> Any:
        """Stream the on-appliance log bundle

        POST /public_api/v1/logs
        Available in Cortex XDR 5.x.
        Returns the complete JSON response, text, bytes, or None for an empty response.
        Optional fields use UNSET for omission; None is explicit null.
        The source snapshot records this operation and its parameter schema.
        """
        self._require_versions((5,))
        body = UNSET
        return self._operation(
            '/public_api/v1/logs', method='post',
            body=body,
        )

    def set_network_interface(self, *,
            interface_type: str,
            name: str,
            address: Union[str, None, UnsetType] = UNSET,
            dns: Union[list, None, UnsetType] = UNSET,
            gateway: Union[str, None, UnsetType] = UNSET,
            is_admin: Union[bool, None, UnsetType] = UNSET,
            netmask: Union[str, None, UnsetType] = UNSET) -> Any:
        """Configure (or disable) a physical network interface

        POST /public_api/v1/network/interface
        Available in Cortex XDR 5.x.
        Returns the complete JSON response, text, bytes, or None for an empty response.
        Optional fields use UNSET for omission; None is explicit null.
        The source snapshot records this operation and its parameter schema.
        :param interface_type: body field interface_type.
        :param name: body field name.
        :param address: body field address.
        :param dns: body field dns.
        :param gateway: body field gateway.
        :param is_admin: body field is_admin.
        :param netmask: body field netmask.
        """
        self._require_versions((5,))
        body = self._values({
            'interface_type': interface_type,
            'name': name,
            'address': address,
            'dns': dns,
            'gateway': gateway,
            'is_admin': is_admin,
            'netmask': netmask,
        })
        return self._operation(
            '/public_api/v1/network/interface', method='post',
            body=body,
        )

    def set_internal_subnet(self, *, docker_subnet: str) -> Any:
        """Set the Docker internal subnet

        POST /public_api/v1/network/internal_subnet
        Available in Cortex XDR 5.x.
        Returns the complete JSON response, text, bytes, or None for an empty response.
        Optional fields use UNSET for omission; None is explicit null.
        The source snapshot records this operation and its parameter schema.
        :param docker_subnet: body field docker_subnet.
        """
        self._require_versions((5,))
        body = self._values({'docker_subnet': docker_subnet})
        return self._operation(
            '/public_api/v1/network/internal_subnet', method='post',
            body=body,
        )

    def set_proxy(self, *,
            proxy_type: str,
            host: Union[str, None, UnsetType] = UNSET,
            port: Union[int, None, UnsetType] = UNSET,
            pwd: Union[str, None, UnsetType] = UNSET,
            user: Union[str, None, UnsetType] = UNSET) -> Any:
        """Configure the outbound HTTP/SOCKS proxy

        POST /public_api/v1/network/proxy
        Available in Cortex XDR 5.x.
        Returns the complete JSON response, text, bytes, or None for an empty response.
        Optional fields use UNSET for omission; None is explicit null.
        The source snapshot records this operation and its parameter schema.
        :param proxy_type: body field proxy_type.
        :param host: body field host.
        :param port: body field port.
        :param pwd: body field pwd.
        :param user: body field user.
        """
        self._require_versions((5,))
        body = self._values({
            'proxy_type': proxy_type,
            'host': host,
            'port': port,
            'pwd': pwd,
            'user': user,
        })
        return self._operation(
            '/public_api/v1/network/proxy', method='post',
            body=body,
        )

    def set_ntp(self, *, ntp: list) -> Any:
        """Replace the configured NTP servers

        POST /public_api/v1/network/ntp
        Available in Cortex XDR 5.x.
        Returns the complete JSON response, text, bytes, or None for an empty response.
        Optional fields use UNSET for omission; None is explicit null.
        The source snapshot records this operation and its parameter schema.
        :param ntp: body field ntp.
        """
        self._require_versions((5,))
        body = self._values({'ntp': ntp})
        return self._operation(
            '/public_api/v1/network/ntp', method='post',
            body=body,
        )

    def set_ssl_certificate(self, *,
            ssl_cert: str,
            ssl_key: str,
            ssl_key_name: Union[str, None, UnsetType] = UNSET) -> Any:
        """Install a custom SSL serving certificate

        POST /public_api/v1/network/ssl_certificate
        Available in Cortex XDR 5.x.
        Returns the complete JSON response, text, bytes, or None for an empty response.
        Optional fields use UNSET for omission; None is explicit null.
        The source snapshot records this operation and its parameter schema.
        :param ssl_cert: body field ssl_cert.
        :param ssl_key: body field ssl_key.
        :param ssl_key_name: body field ssl_key_name.
        """
        self._require_versions((5,))
        body = self._values({
            'ssl_cert': ssl_cert,
            'ssl_key': ssl_key,
            'ssl_key_name': ssl_key_name,
        })
        return self._operation(
            '/public_api/v1/network/ssl_certificate', method='post',
            body=body,
        )

    def set_trusted_ca(self, *, file: str) -> Any:
        """Install a custom trusted CA bundle

        POST /public_api/v1/network/trusted_ca
        Available in Cortex XDR 5.x.
        Returns the complete JSON response, text, bytes, or None for an empty response.
        Optional fields use UNSET for omission; None is explicit null.
        The source snapshot records this operation and its parameter schema.
        :param file: body field file.
        """
        self._require_versions((5,))
        body = self._values({'file': file})
        return self._operation(
            '/public_api/v1/network/trusted_ca', method='post',
            body=body,
        )

    def register_broker(self, *, token: str) -> Any:
        """Activate the broker against the Cortex tenant

        POST /public_api/v1/register
        Available in Cortex XDR 5.x.
        Returns the complete JSON response, text, bytes, or None for an empty response.
        Optional fields use UNSET for omission; None is explicit null.
        The source snapshot records this operation and its parameter schema.
        :param token: body field token.
        """
        self._require_versions((5,))
        body = self._values({'token': token})
        return self._operation(
            '/public_api/v1/register', method='post',
            body=body,
        )
