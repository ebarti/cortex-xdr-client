from typing import Any, List, Tuple, Union

from cortex_xdr_client.api.operation import UNSET, UnsetType

from cortex_xdr_client.api.authentication import Authentication
from cortex_xdr_client.api.base_api import BaseAPI
from cortex_xdr_client.api.version import APIVersion


class RbacAPI(BaseAPI):
    def __init__(self, auth: Authentication, fqdn: str, timeout: Tuple[int, int],
                 api_version: APIVersion = APIVersion.V3) -> None:
        super(RbacAPI, self).__init__(auth, fqdn, 'rbac', timeout, api_version)

    def get_users(self, *,
                  accept_encoding: Union[str, None, UnsetType] = UNSET,
                  body: Union[dict, None, UnsetType] = UNSET) -> Any:
        """Get Users

        POST /public_api/v1/rbac/get_users
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
                '/public_api/v1/rbac/get_users', method='post',
                headers={'Accept-Encoding': accept_encoding},
                body=body,
            )
        elif self._api_version == APIVersion.V5:
            self._reject_fields(accept_encoding=accept_encoding)
            if body is not UNSET:
                body = {'request_data': body}
            return self._operation(
                '/public_api/v1/rbac/get_users', method='post',
                body=body,
            )

    def get_roles(self, *,
                  accept_encoding: Union[str, None, UnsetType] = UNSET,
                  role_names: Union[List[str], None, UnsetType] = UNSET) -> Any:
        """Get Roles

        POST /public_api/v1/rbac/get_roles
        Available in Cortex XDR 3.x, 5.x.
        Returns the complete JSON response, bytes for downloads, or None for an empty response.
        Omit optional fields with UNSET; explicit None is sent as JSON null.
        :param accept_encoding: header field Accept-Encoding.
        :param role_names: body field role_names.
        """
        self._require_versions((3, 5))
        if self._api_version == APIVersion.V3:
            body = self._values({'role_names': role_names})
            body = self._values({'request_data': body, **{}})
            return self._operation(
                '/public_api/v1/rbac/get_roles', method='post',
                headers={'Accept-Encoding': accept_encoding},
                body=body,
            )
        elif self._api_version == APIVersion.V5:
            self._reject_fields(accept_encoding=accept_encoding)
            body = self._values({'role_names': role_names})
            body = self._values({'request_data': body, **{}})
            return self._operation(
                '/public_api/v1/rbac/get_roles', method='post',
                body=body,
            )

    def get_user_group(self, *,
                       accept_encoding: Union[str, None, UnsetType] = UNSET,
                       group_names: Union[List[str], None, UnsetType] = UNSET) -> Any:
        """Get User Groups

        POST /public_api/v1/rbac/get_user_group
        Available in Cortex XDR 3.x, 5.x.
        Returns the complete JSON response, bytes for downloads, or None for an empty response.
        Omit optional fields with UNSET; explicit None is sent as JSON null.
        :param accept_encoding: header field Accept-Encoding.
        :param group_names: body field group_names.
        """
        self._require_versions((3, 5))
        if self._api_version == APIVersion.V3:
            body = self._values({'group_names': group_names})
            body = self._values({'request_data': body, **{}})
            return self._operation(
                '/public_api/v1/rbac/get_user_group', method='post',
                headers={'Accept-Encoding': accept_encoding},
                body=body,
            )
        elif self._api_version == APIVersion.V5:
            self._reject_fields(accept_encoding=accept_encoding)
            body = self._values({'group_names': group_names})
            body = self._values({'request_data': body, **{}})
            return self._operation(
                '/public_api/v1/rbac/get_user_group', method='post',
                body=body,
            )

    def set_user_role(self, *,
                      accept_encoding: Union[str, None, UnsetType] = UNSET,
                      user_emails: Union[List[str], None, UnsetType] = UNSET,
                      role_name: Union[str, None, UnsetType] = UNSET) -> Any:
        """Set a User Role

        POST /public_api/v1/rbac/set_user_role
        Available in Cortex XDR 3.x, 5.x.
        Returns the complete JSON response, bytes for downloads, or None for an empty response.
        Omit optional fields with UNSET; explicit None is sent as JSON null.
        :param accept_encoding: header field Accept-Encoding.
        :param user_emails: body field user_emails.
        :param role_name: body field role_name.
        """
        self._require_versions((3, 5))
        if self._api_version == APIVersion.V3:
            body = self._values({'user_emails': user_emails, 'role_name': role_name})
            body = self._values({'request_data': body, **{}})
            return self._operation(
                '/public_api/v1/rbac/set_user_role', method='post',
                headers={'Accept-Encoding': accept_encoding},
                body=body,
            )
        elif self._api_version == APIVersion.V5:
            self._reject_fields(accept_encoding=accept_encoding)
            body = self._values({'user_emails': user_emails, 'role_name': role_name})
            body = self._values({'request_data': body, **{}})
            return self._operation(
                '/public_api/v1/rbac/set_user_role', method='post',
                body=body,
            )
