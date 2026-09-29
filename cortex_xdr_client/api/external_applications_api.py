"""Explicit operations from the pinned Cortex XDR documentation snapshot."""
from typing import Any, Tuple, Union

from cortex_xdr_client.api.operation import UNSET, UnsetType
from cortex_xdr_client.api.authentication import Authentication
from cortex_xdr_client.api.base_api import BaseAPI
from cortex_xdr_client.api.version import APIVersion


class ExternalApplicationsAPI(BaseAPI):
    def __init__(self, auth: Authentication, fqdn: str, timeout: Tuple[int, int],
                 api_version: APIVersion = APIVersion.V3) -> None:
        super(ExternalApplicationsAPI, self).__init__(auth, fqdn, 'external_applications', timeout, api_version)

    def list_applications(self) -> Any:
        """List all applications

        GET /platform/integration/v1/external-application
        Available in Cortex XDR 5.x.
        Returns the complete JSON response, text, bytes, or None for an empty response.
        Optional fields use UNSET for omission; None is explicit null.
        The source snapshot records this operation and its parameter schema.
        """
        self._require_versions((5,))
        body = UNSET
        return self._operation(
            '/platform/integration/v1/external-application', method='get',
            body=body,
        )

    def create_application(self, *,
            request_data: dict,
            last_modified_by: Union[Any, None, UnsetType] = UNSET) -> Any:
        """Create a new application

        POST /platform/integration/v1/external-application
        Available in Cortex XDR 5.x.
        Returns the complete JSON response, text, bytes, or None for an empty response.
        Optional fields use UNSET for omission; None is explicit null.
        The source snapshot records this operation and its parameter schema.
        :param request_data: body field request_data.
        :param last_modified_by: body field last_modified_by.
        """
        self._require_versions((5,))
        body = self._values({'request_data': request_data, 'last_modified_by': last_modified_by})
        return self._operation(
            '/platform/integration/v1/external-application', method='post',
            body=body,
        )

    def update_application(self, *,
            application_id: str,
            application_type: str,
            connection_config: dict,
            name: str,
            description: Union[str, None, UnsetType] = UNSET) -> Any:
        """Update an existing application (full replacement)

        PUT /platform/integration/v1/external-application/{application_id}
        Available in Cortex XDR 5.x.
        Returns the complete JSON response, text, bytes, or None for an empty response.
        Optional fields use UNSET for omission; None is explicit null.
        The source snapshot records this operation and its parameter schema.
        :param application_id: path field application_id.
        :param application_type: body field application_type.
        :param connection_config: body field connection_config.
        :param name: body field name.
        :param description: body field description.
        """
        self._require_versions((5,))
        body = self._values({
            'application_type': application_type,
            'connection_config': connection_config,
            'name': name,
            'description': description,
        })
        body = {'request_data': body}
        return self._operation(
            '/platform/integration/v1/external-application/{application_id}', method='put',
            path_params={'application_id': application_id},
            body=body,
        )

    def get_external_application_by_id(self, *, application_id: str, application_type: str) -> Any:
        """Get External Application details by ID

        GET /platform/integration/v1/external-application/{application_type}/id/{application_id}
        Available in Cortex XDR 5.x.
        Returns the complete JSON response, text, bytes, or None for an empty response.
        Optional fields use UNSET for omission; None is explicit null.
        The source snapshot records this operation and its parameter schema.
        :param application_id: path field application_id.
        :param application_type: path field application_type.
        """
        self._require_versions((5,))
        body = UNSET
        return self._operation(
            '/platform/integration/v1/external-application/{application_type}/id/{application_id}', method='get',
            path_params={'application_id': application_id, 'application_type': application_type},
            body=body,
        )

    def delete_application(self, *, application_id: str, application_type: str) -> Any:
        """Delete an application

        DELETE /platform/integration/v1/external-application/{application_type}/id/{application_id}
        Available in Cortex XDR 5.x.
        Returns the complete JSON response, text, bytes, or None for an empty response.
        Optional fields use UNSET for omission; None is explicit null.
        The source snapshot records this operation and its parameter schema.
        :param application_id: path field application_id.
        :param application_type: path field application_type.
        """
        self._require_versions((5,))
        body = UNSET
        return self._operation(
            '/platform/integration/v1/external-application/{application_type}/id/{application_id}', method='delete',
            path_params={'application_id': application_id, 'application_type': application_type},
            body=body,
        )
