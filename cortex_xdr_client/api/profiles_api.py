from typing import Any, List, Tuple, Union

from cortex_xdr_client.api.operation import UNSET, UnsetType

from cortex_xdr_client.api.authentication import Authentication
from cortex_xdr_client.api.base_api import BaseAPI
from cortex_xdr_client.api.version import APIVersion


class ProfilesAPI(BaseAPI):
    def __init__(self, auth: Authentication, fqdn: str, timeout: Tuple[int, int],
                 api_version: APIVersion = APIVersion.V3) -> None:
        super(ProfilesAPI, self).__init__(auth, fqdn, 'profiles', timeout, api_version)

    def prevention_add(self, *,
                       name: Union[str, None, UnsetType] = UNSET,
                       profile_type: Union[str, None, UnsetType] = UNSET,
                       platform: Union[str, None, UnsetType] = UNSET,
                       description: Union[str, None, UnsetType] = UNSET,
                       modules: Union[dict, None, UnsetType] = UNSET) -> Any:
        """Add Prevention Profile

        POST /public_api/v1/profiles/prevention/add
        Available in Cortex XDR 3.x, 5.x.
        Returns the complete JSON response, bytes for downloads, or None for an empty response.
        Omit optional fields with UNSET; explicit None is sent as JSON null.
        :param name: body field name.
        :param profile_type: body field profile_type.
        :param platform: body field platform.
        :param description: body field description.
        :param modules: body field modules.
        """
        self._require_versions((3, 5))
        if self._api_version == APIVersion.V3:
            body = self._values({'name': name, 'profile_type': profile_type, 'platform': platform, 'description': description, 'modules': modules})
            return self._operation(
                '/public_api/v1/profiles/prevention/add', method='post',
                body=body,
            )
        elif self._api_version == APIVersion.V5:
            body = self._values({'name': name, 'profile_type': profile_type, 'platform': platform, 'description': description, 'modules': modules})
            body = {'request_data': body}
            return self._operation(
                '/public_api/v1/profiles/prevention/add', method='post',
                body=body,
            )

    def add_signer_cn_to_allowlist(self, *,
                                   profile_name: Union[str, None, UnsetType] = UNSET,
                                   signers: Union[Any, None, UnsetType] = UNSET) -> Any:
        """Add Signer CN to Allowlist

        POST /public_api/v1/profiles/add_signer_cn_to_allowlist
        Available in Cortex XDR 3.x, 5.x.
        Returns the complete JSON response, bytes for downloads, or None for an empty response.
        Omit optional fields with UNSET; explicit None is sent as JSON null.
        :param profile_name: body field profile_name.
        :param signers: body field signers.
        """
        self._require_versions((3, 5))
        if self._api_version == APIVersion.V3:
            body = self._values({'profile_name': profile_name, 'signers': signers})
            return self._operation(
                '/public_api/v1/profiles/add_signer_cn_to_allowlist', method='post',
                body=body,
            )
        elif self._api_version == APIVersion.V5:
            body = self._values({'profile_name': profile_name, 'signers': signers})
            body = {'request_data': body}
            return self._operation(
                '/public_api/v1/profiles/add_signer_cn_to_allowlist', method='post',
                body=body,
            )

    def prevention_edit(self, *,
                        profile_id: Union[int, None, UnsetType] = UNSET,
                        update_data: Union[dict, None, UnsetType] = UNSET) -> Any:
        """Edit Prevention Profile

        POST /public_api/v1/profiles/prevention/edit
        Available in Cortex XDR 3.x, 5.x.
        Returns the complete JSON response, bytes for downloads, or None for an empty response.
        Omit optional fields with UNSET; explicit None is sent as JSON null.
        :param profile_id: body field profile_id.
        :param update_data: body field update_data.
        """
        self._require_versions((3, 5))
        if self._api_version == APIVersion.V3:
            body = self._values({'profile_id': profile_id, 'update_data': update_data})
            return self._operation(
                '/public_api/v1/profiles/prevention/edit', method='post',
                body=body,
            )
        elif self._api_version == APIVersion.V5:
            body = self._values({'profile_id': profile_id, 'update_data': update_data})
            body = {'request_data': body}
            return self._operation(
                '/public_api/v1/profiles/prevention/edit', method='post',
                body=body,
            )

    def prevention_get_modules(self, *,
                               profile_type: Union[str, None, UnsetType] = UNSET,
                               platform: Union[str, None, UnsetType] = UNSET) -> Any:
        """Get Prevention Profile Modules

        POST /public_api/v1/profiles/prevention/get_modules
        Available in Cortex XDR 3.x, 5.x.
        Returns the complete JSON response, bytes for downloads, or None for an empty response.
        Omit optional fields with UNSET; explicit None is sent as JSON null.
        :param profile_type: body field profile_type.
        :param platform: body field platform.
        """
        self._require_versions((3, 5))
        if self._api_version == APIVersion.V3:
            body = self._values({'profile_type': profile_type, 'platform': platform})
            return self._operation(
                '/public_api/v1/profiles/prevention/get_modules', method='post',
                body=body,
            )
        elif self._api_version == APIVersion.V5:
            body = self._values({'profile_type': profile_type, 'platform': platform})
            body = {'request_data': body}
            return self._operation(
                '/public_api/v1/profiles/prevention/get_modules', method='post',
                body=body,
            )
