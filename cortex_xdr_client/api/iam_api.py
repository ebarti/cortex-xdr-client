"""Explicit operations from the pinned Cortex XDR documentation snapshot."""
from typing import Any, Tuple, Union

from cortex_xdr_client.api.operation import UNSET, UnsetType
from cortex_xdr_client.api.authentication import Authentication
from cortex_xdr_client.api.base_api import BaseAPI
from cortex_xdr_client.api.version import APIVersion


class IamAPI(BaseAPI):
    def __init__(self, auth: Authentication, fqdn: str, timeout: Tuple[int, int],
                 api_version: APIVersion = APIVersion.V3) -> None:
        super(IamAPI, self).__init__(auth, fqdn, 'iam', timeout, api_version)

    def get_api_key_by_id(self, *, api_key_id: int) -> Any:
        """Get API Key

        GET /platform/iam/v1/api-key/{api_key_id}
        Available in Cortex XDR 5.x.
        Returns the complete JSON response, text, bytes, or None for an empty response.
        Optional fields use UNSET for omission; None is explicit null.
        The source snapshot records this operation and its parameter schema.
        :param api_key_id: path field api_key_id.
        """
        self._require_versions((5,))
        body = UNSET
        return self._operation(
            '/platform/iam/v1/api-key/{api_key_id}', method='get',
            path_params={'api_key_id': api_key_id},
            body=body,
        )

    def edit_apikey(self, *,
            api_key_id: int,
            roles: list,
            security_level: str,
            comment: Union[str, None, UnsetType] = UNSET) -> Any:
        """Edit an API key

        PUT /platform/iam/v1/api-key/{api_key_id}
        Available in Cortex XDR 5.x.
        Returns the complete JSON response, text, bytes, or None for an empty response.
        Optional fields use UNSET for omission; None is explicit null.
        The source snapshot records this operation and its parameter schema.
        :param api_key_id: path field api_key_id.
        :param roles: body field roles.
        :param security_level: body field security_level.
        :param comment: body field comment.
        """
        self._require_versions((5,))
        body = self._values({'roles': roles, 'security_level': security_level, 'comment': comment})
        body = {'request_data': body}
        return self._operation(
            '/platform/iam/v1/api-key/{api_key_id}', method='put',
            path_params={'api_key_id': api_key_id},
            body=body,
        )

    def list_roles(self) -> Any:
        """List all roles

        GET /platform/iam/v1/role
        Available in Cortex XDR 5.x.
        Returns the complete JSON response, text, bytes, or None for an empty response.
        Optional fields use UNSET for omission; None is explicit null.
        The source snapshot records this operation and its parameter schema.
        """
        self._require_versions((5,))
        body = UNSET
        return self._operation(
            '/platform/iam/v1/role', method='get',
            body=body,
        )

    def create_role(self, *,
            component_permissions: list,
            pretty_name: str,
            dataset_permissions: Union[list, None, UnsetType] = UNSET,
            description: Union[str, None, UnsetType] = UNSET) -> Any:
        """Create a new role

        POST /platform/iam/v1/role
        Available in Cortex XDR 5.x.
        Returns the complete JSON response, text, bytes, or None for an empty response.
        Optional fields use UNSET for omission; None is explicit null.
        The source snapshot records this operation and its parameter schema.
        :param component_permissions: body field component_permissions.
        :param pretty_name: body field pretty_name.
        :param dataset_permissions: body field dataset_permissions.
        :param description: body field description.
        """
        self._require_versions((5,))
        body = self._values({
            'component_permissions': component_permissions,
            'pretty_name': pretty_name,
            'dataset_permissions': dataset_permissions,
            'description': description,
        })
        body = {'request_data': body}
        return self._operation(
            '/platform/iam/v1/role', method='post',
            body=body,
        )

    def delete_role(self, *, role_id: str) -> Any:
        """Delete an existing role

        DELETE /platform/iam/v1/role/{role_id}
        Available in Cortex XDR 5.x.
        Returns the complete JSON response, text, bytes, or None for an empty response.
        Optional fields use UNSET for omission; None is explicit null.
        The source snapshot records this operation and its parameter schema.
        :param role_id: path field role_id.
        """
        self._require_versions((5,))
        body = UNSET
        return self._operation(
            '/platform/iam/v1/role/{role_id}', method='delete',
            path_params={'role_id': role_id},
            body=body,
        )

    def list_permission_configs(self) -> Any:
        """List all permission configs

        GET /platform/iam/v1/role/permission-config
        Available in Cortex XDR 5.x.
        Returns the complete JSON response, text, bytes, or None for an empty response.
        Optional fields use UNSET for omission; None is explicit null.
        The source snapshot records this operation and its parameter schema.
        """
        self._require_versions((5,))
        body = UNSET
        return self._operation(
            '/platform/iam/v1/role/permission-config', method='get',
            body=body,
        )

    def get_scope(self, *, entity_type: str, entity_id: str) -> Any:
        """Retrieve an existing scope

        GET /platform/iam/v1/scope/{entity_type}/{entity_id}
        Available in Cortex XDR 5.x.
        Returns the complete JSON response, text, bytes, or None for an empty response.
        Optional fields use UNSET for omission; None is explicit null.
        The source snapshot records this operation and its parameter schema.
        :param entity_type: path field entity_type.
        :param entity_id: path field entity_id.
        """
        self._require_versions((5,))
        body = UNSET
        return self._operation(
            '/platform/iam/v1/scope/{entity_type}/{entity_id}', method='get',
            path_params={'entity_type': entity_type, 'entity_id': entity_id},
            body=body,
        )

    def edit_scope(self, *,
            entity_type: str,
            entity_id: str,
            assets: Union[dict, None, UnsetType] = UNSET,
            cases_issues: Union[dict, None, UnsetType] = UNSET,
            datasets_rows: Union[dict, None, UnsetType] = UNSET,
            endpoints: Union[dict, None, UnsetType] = UNSET) -> Any:
        """Edit an existing scope

        PUT /platform/iam/v1/scope/{entity_type}/{entity_id}
        Available in Cortex XDR 5.x.
        Returns the complete JSON response, text, bytes, or None for an empty response.
        Optional fields use UNSET for omission; None is explicit null.
        The source snapshot records this operation and its parameter schema.
        :param entity_type: path field entity_type.
        :param entity_id: path field entity_id.
        :param assets: body field assets.
        :param cases_issues: body field cases_issues.
        :param datasets_rows: body field datasets_rows.
        :param endpoints: body field endpoints.
        """
        self._require_versions((5,))
        body = self._values({
            'assets': assets,
            'cases_issues': cases_issues,
            'datasets_rows': datasets_rows,
            'endpoints': endpoints,
        })
        body = {'request_data': body}
        return self._operation(
            '/platform/iam/v1/scope/{entity_type}/{entity_id}', method='put',
            path_params={'entity_type': entity_type, 'entity_id': entity_id},
            body=body,
        )

    def list_user_groups(self) -> Any:
        """List all user groups

        GET /platform/iam/v1/user-group
        Available in Cortex XDR 5.x.
        Returns the complete JSON response, text, bytes, or None for an empty response.
        Optional fields use UNSET for omission; None is explicit null.
        The source snapshot records this operation and its parameter schema.
        """
        self._require_versions((5,))
        body = UNSET
        return self._operation(
            '/platform/iam/v1/user-group', method='get',
            body=body,
        )

    def create_user_group(self, *,
            group_name: str,
            description: Union[str, None, UnsetType] = UNSET,
            idp_groups: Union[list, None, UnsetType] = UNSET,
            nested_group_ids: Union[list, None, UnsetType] = UNSET,
            role_id: Union[str, None, UnsetType] = UNSET,
            users: Union[list, None, UnsetType] = UNSET) -> Any:
        """Create a new user group

        POST /platform/iam/v1/user-group
        Available in Cortex XDR 5.x.
        Returns the complete JSON response, text, bytes, or None for an empty response.
        Optional fields use UNSET for omission; None is explicit null.
        The source snapshot records this operation and its parameter schema.
        :param group_name: body field group_name.
        :param description: body field description.
        :param idp_groups: body field idp_groups.
        :param nested_group_ids: body field nested_group_ids.
        :param role_id: body field role_id.
        :param users: body field users.
        """
        self._require_versions((5,))
        body = self._values({
            'group_name': group_name,
            'description': description,
            'idp_groups': idp_groups,
            'nested_group_ids': nested_group_ids,
            'role_id': role_id,
            'users': users,
        })
        body = {'request_data': body}
        return self._operation(
            '/platform/iam/v1/user-group', method='post',
            body=body,
        )

    def delete_user_group(self, *, group_id: str) -> Any:
        """Delete an existing user group

        DELETE /platform/iam/v1/user-group/{group_id}
        Available in Cortex XDR 5.x.
        Returns the complete JSON response, text, bytes, or None for an empty response.
        Optional fields use UNSET for omission; None is explicit null.
        The source snapshot records this operation and its parameter schema.
        :param group_id: path field group_id.
        """
        self._require_versions((5,))
        body = UNSET
        return self._operation(
            '/platform/iam/v1/user-group/{group_id}', method='delete',
            path_params={'group_id': group_id},
            body=body,
        )

    def edit_user_group(self, *,
            group_id: str,
            description: Union[str, None, UnsetType] = UNSET,
            group_name: Union[str, None, UnsetType] = UNSET,
            idp_groups: Union[list, None, UnsetType] = UNSET,
            nested_group_ids: Union[list, None, UnsetType] = UNSET,
            role_id: Union[str, None, UnsetType] = UNSET,
            users: Union[list, None, UnsetType] = UNSET) -> Any:
        """Edit an existing user group

        PATCH /platform/iam/v1/user-group/{group_id}
        Available in Cortex XDR 5.x.
        Returns the complete JSON response, text, bytes, or None for an empty response.
        Optional fields use UNSET for omission; None is explicit null.
        The source snapshot records this operation and its parameter schema.
        :param group_id: path field group_id.
        :param description: body field description.
        :param group_name: body field group_name.
        :param idp_groups: body field idp_groups.
        :param nested_group_ids: body field nested_group_ids.
        :param role_id: body field role_id.
        :param users: body field users.
        """
        self._require_versions((5,))
        body = self._values({
            'description': description,
            'group_name': group_name,
            'idp_groups': idp_groups,
            'nested_group_ids': nested_group_ids,
            'role_id': role_id,
            'users': users,
        })
        body = {'request_data': body}
        return self._operation(
            '/platform/iam/v1/user-group/{group_id}', method='patch',
            path_params={'group_id': group_id},
            body=body,
        )

    def list_users(self) -> Any:
        """List all users

        GET /platform/iam/v1/user
        Available in Cortex XDR 5.x.
        Returns the complete JSON response, text, bytes, or None for an empty response.
        Optional fields use UNSET for omission; None is explicit null.
        The source snapshot records this operation and its parameter schema.
        """
        self._require_versions((5,))
        body = UNSET
        return self._operation(
            '/platform/iam/v1/user', method='get',
            body=body,
        )

    def get_user_by_email(self, *, user_email: str) -> Any:
        """Get user

        GET /platform/iam/v1/user/{user_email}
        Available in Cortex XDR 5.x.
        Returns the complete JSON response, text, bytes, or None for an empty response.
        Optional fields use UNSET for omission; None is explicit null.
        The source snapshot records this operation and its parameter schema.
        :param user_email: path field user_email.
        """
        self._require_versions((5,))
        body = UNSET
        return self._operation(
            '/platform/iam/v1/user/{user_email}', method='get',
            path_params={'user_email': user_email},
            body=body,
        )

    def edit_user(self, *,
            user_email: str,
            is_hidden: Union[bool, None, UnsetType] = UNSET,
            phone_number: Union[str, None, UnsetType] = UNSET,
            role_id: Union[str, None, UnsetType] = UNSET,
            status: Union[str, None, UnsetType] = UNSET,
            user_first_name: Union[str, None, UnsetType] = UNSET,
            user_groups: Union[list, None, UnsetType] = UNSET,
            user_last_name: Union[str, None, UnsetType] = UNSET) -> Any:
        """Edit an existing user

        PATCH /platform/iam/v1/user/{user_email}
        Available in Cortex XDR 5.x.
        Returns the complete JSON response, text, bytes, or None for an empty response.
        Optional fields use UNSET for omission; None is explicit null.
        The source snapshot records this operation and its parameter schema.
        :param user_email: path field user_email.
        :param is_hidden: body field is_hidden.
        :param phone_number: body field phone_number.
        :param role_id: body field role_id.
        :param status: body field status.
        :param user_first_name: body field user_first_name.
        :param user_groups: body field user_groups.
        :param user_last_name: body field user_last_name.
        """
        self._require_versions((5,))
        body = self._values({
            'is_hidden': is_hidden,
            'phone_number': phone_number,
            'role_id': role_id,
            'status': status,
            'user_first_name': user_first_name,
            'user_groups': user_groups,
            'user_last_name': user_last_name,
        })
        body = {'request_data': body}
        return self._operation(
            '/platform/iam/v1/user/{user_email}', method='patch',
            path_params={'user_email': user_email},
            body=body,
        )
