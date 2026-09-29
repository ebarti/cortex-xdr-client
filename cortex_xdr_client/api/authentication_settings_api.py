from typing import Any, List, Tuple, Union

from cortex_xdr_client.api.operation import UNSET, UnsetType

from cortex_xdr_client.api.authentication import Authentication
from cortex_xdr_client.api.base_api import BaseAPI
from cortex_xdr_client.api.version import APIVersion


class AuthenticationSettingsAPI(BaseAPI):
    def __init__(self, auth: Authentication, fqdn: str, timeout: Tuple[int, int],
                 api_version: APIVersion = APIVersion.V3) -> None:
        super(AuthenticationSettingsAPI, self).__init__(auth, fqdn, 'authentication_settings', timeout, api_version)

    def create(self, *,
               name: Union[str, None, UnsetType] = UNSET,
               default_role: Union[str, None, UnsetType] = UNSET,
               is_account_role: Union[bool, None, UnsetType] = UNSET,
               domain: Union[str, None, UnsetType] = UNSET,
               mappings: Union[dict, None, UnsetType] = UNSET,
               advanced_settings: Union[dict, None, UnsetType] = UNSET,
               idp_sso_url: Union[str, None, UnsetType] = UNSET,
               idp_certificate: Union[str, None, UnsetType] = UNSET,
               idp_issuer: Union[str, None, UnsetType] = UNSET,
               metadata_url: Union[str, None, UnsetType] = UNSET) -> Any:
        """Create authentication settings for IdP SSO or metadata URL

        POST /public_api/v1/authentication-settings/create
        Available in Cortex XDR 3.x, 5.x.
        Returns the complete JSON response, bytes for downloads, or None for an empty response.
        Omit optional fields with UNSET; explicit None is sent as JSON null.
        :param name: body field name.
        :param default_role: body field default_role.
        :param is_account_role: body field is_account_role.
        :param domain: body field domain.
        :param mappings: body field mappings.
        :param advanced_settings: body field advanced_settings.
        :param idp_sso_url: body field idp_sso_url.
        :param idp_certificate: body field idp_certificate.
        :param idp_issuer: body field idp_issuer.
        :param metadata_url: body field metadata_url.
        """
        self._require_versions((3, 5))
        if self._api_version == APIVersion.V3:
            body = self._values({'name': name, 'default_role': default_role, 'is_account_role': is_account_role, 'domain': domain, 'mappings': mappings, 'advanced_settings': advanced_settings, 'idp_sso_url': idp_sso_url, 'idp_certificate': idp_certificate, 'idp_issuer': idp_issuer, 'metadata_url': metadata_url})
            body = self._values({'request_data': body, **{}})
            return self._operation(
                '/public_api/v1/authentication-settings/create', method='post',
                body=body,
            )
        elif self._api_version == APIVersion.V5:
            body = self._values({'name': name, 'default_role': default_role, 'is_account_role': is_account_role, 'domain': domain, 'mappings': mappings, 'advanced_settings': advanced_settings, 'idp_sso_url': idp_sso_url, 'idp_certificate': idp_certificate, 'idp_issuer': idp_issuer, 'metadata_url': metadata_url})
            body = self._values({'request_data': body, **{}})
            return self._operation(
                '/public_api/v1/authentication-settings/create', method='post',
                body=body,
            )

    def update(self, *,
               name: Union[str, None, UnsetType] = UNSET,
               default_role: Union[str, None, UnsetType] = UNSET,
               is_account_role: Union[bool, None, UnsetType] = UNSET,
               current_domain_value: Union[str, None, UnsetType] = UNSET,
               new_domain_value: Union[str, None, UnsetType] = UNSET,
               mappings: Union[dict, None, UnsetType] = UNSET,
               advanced_settings: Union[dict, None, UnsetType] = UNSET,
               idp_sso_url: Union[str, None, UnsetType] = UNSET,
               idp_certificate: Union[str, None, UnsetType] = UNSET,
               idp_issuer: Union[str, None, UnsetType] = UNSET,
               metadata_url: Union[str, None, UnsetType] = UNSET) -> Any:
        """Update authentication settings

        POST /public_api/v1/authentication-settings/update
        Available in Cortex XDR 3.x, 5.x.
        Returns the complete JSON response, bytes for downloads, or None for an empty response.
        Omit optional fields with UNSET; explicit None is sent as JSON null.
        :param name: body field name.
        :param default_role: body field default_role.
        :param is_account_role: body field is_account_role.
        :param current_domain_value: body field current_domain_value.
        :param new_domain_value: body field new_domain_value.
        :param mappings: body field mappings.
        :param advanced_settings: body field advanced_settings.
        :param idp_sso_url: body field idp_sso_url.
        :param idp_certificate: body field idp_certificate.
        :param idp_issuer: body field idp_issuer.
        :param metadata_url: body field metadata_url.
        """
        self._require_versions((3, 5))
        if self._api_version == APIVersion.V3:
            body = self._values({'name': name, 'default_role': default_role, 'is_account_role': is_account_role, 'current_domain_value': current_domain_value, 'new_domain_value': new_domain_value, 'mappings': mappings, 'advanced_settings': advanced_settings, 'idp_sso_url': idp_sso_url, 'idp_certificate': idp_certificate, 'idp_issuer': idp_issuer, 'metadata_url': metadata_url})
            body = self._values({'request_data': body, **{}})
            return self._operation(
                '/public_api/v1/authentication-settings/update', method='post',
                body=body,
            )
        elif self._api_version == APIVersion.V5:
            body = self._values({'name': name, 'default_role': default_role, 'is_account_role': is_account_role, 'current_domain_value': current_domain_value, 'new_domain_value': new_domain_value, 'mappings': mappings, 'advanced_settings': advanced_settings, 'idp_sso_url': idp_sso_url, 'idp_certificate': idp_certificate, 'idp_issuer': idp_issuer, 'metadata_url': metadata_url})
            body = self._values({'request_data': body, **{}})
            return self._operation(
                '/public_api/v1/authentication-settings/update', method='post',
                body=body,
            )

    def delete(self, *,
               domain: Union[str, None, UnsetType] = UNSET) -> Any:
        """Delete authentication settings by domain

        POST /public_api/v1/authentication-settings/delete
        Available in Cortex XDR 3.x, 5.x.
        Returns the complete JSON response, bytes for downloads, or None for an empty response.
        Omit optional fields with UNSET; explicit None is sent as JSON null.
        :param domain: body field domain.
        """
        self._require_versions((3, 5))
        if self._api_version == APIVersion.V3:
            body = self._values({'domain': domain})
            body = self._values({'request_data': body, **{}})
            return self._operation(
                '/public_api/v1/authentication-settings/delete', method='post',
                body=body,
            )
        elif self._api_version == APIVersion.V5:
            body = self._values({'domain': domain})
            body = self._values({'request_data': body, **{}})
            return self._operation(
                '/public_api/v1/authentication-settings/delete', method='post',
                body=body,
            )

    def get_settings(self, *,
                     request_data: Union[dict, None, UnsetType] = UNSET) -> Any:
        """Get authentication settings for all configured domains

        POST /public_api/v1/authentication-settings/get/settings
        Available in Cortex XDR 3.x, 5.x.
        Returns the complete JSON response, bytes for downloads, or None for an empty response.
        Omit optional fields with UNSET; explicit None is sent as JSON null.
        :param request_data: payload field request_data.
        """
        self._require_versions((3, 5))
        if self._api_version == APIVersion.V3:
            body = request_data
            body = self._values({'request_data': body, **{}})
            return self._operation(
                '/public_api/v1/authentication-settings/get/settings', method='post',
                body=body,
            )
        elif self._api_version == APIVersion.V5:
            body = request_data
            body = self._values({'request_data': body, **{}})
            return self._operation(
                '/public_api/v1/authentication-settings/get/settings', method='post',
                body=body,
            )

    def get_metadata(self, *,
                     request_data: Union[dict, None, UnsetType] = UNSET) -> Any:
        """Get IdP metadata

        POST /public_api/v1/authentication-settings/get/metadata
        Available in Cortex XDR 3.x, 5.x.
        Returns the complete JSON response, bytes for downloads, or None for an empty response.
        Omit optional fields with UNSET; explicit None is sent as JSON null.
        :param request_data: payload field request_data.
        """
        self._require_versions((3, 5))
        if self._api_version == APIVersion.V3:
            body = request_data
            body = self._values({'request_data': body, **{}})
            return self._operation(
                '/public_api/v1/authentication-settings/get/metadata', method='post',
                body=body,
            )
        elif self._api_version == APIVersion.V5:
            body = request_data
            body = self._values({'request_data': body, **{}})
            return self._operation(
                '/public_api/v1/authentication-settings/get/metadata', method='post',
                body=body,
            )
