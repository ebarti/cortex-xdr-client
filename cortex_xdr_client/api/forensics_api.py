"""Explicit operations from the pinned Cortex XDR documentation snapshot."""
from typing import Any, Tuple, Union

from cortex_xdr_client.api.operation import UNSET, UnsetType
from cortex_xdr_client.api.authentication import Authentication
from cortex_xdr_client.api.base_api import BaseAPI
from cortex_xdr_client.api.version import APIVersion


class ForensicsAPI(BaseAPI):
    def __init__(self, auth: Authentication, fqdn: str, timeout: Tuple[int, int],
                 api_version: APIVersion = APIVersion.V3) -> None:
        super(ForensicsAPI, self).__init__(auth, fqdn, 'forensics', timeout, api_version)

    def get_forensics_investigations(self) -> Any:
        """List forensic investigations

        POST /public_api/v1/forensics/investigations
        Available in Cortex XDR 5.x.
        Returns the complete JSON response, text, bytes, or None for an empty response.
        Optional fields use UNSET for omission; None is explicit null.
        The source snapshot records this operation and its parameter schema.
        """
        self._require_versions((5,))
        body = {'request_data': {}}
        return self._operation(
            '/public_api/v1/forensics/investigations', method='post',
            body=body,
        )

    def get_forensics_investigation_collections(self, *, investigation_id: str) -> Any:
        """List collections in an investigation

        POST /public_api/v1/forensics/investigations/collections
        Available in Cortex XDR 5.x.
        Returns the complete JSON response, text, bytes, or None for an empty response.
        Optional fields use UNSET for omission; None is explicit null.
        The source snapshot records this operation and its parameter schema.
        :param investigation_id: body field investigation_id.
        """
        self._require_versions((5,))
        body = self._values({'investigation_id': investigation_id})
        body = {'request_data': body}
        return self._operation(
            '/public_api/v1/forensics/investigations/collections', method='post',
            body=body,
        )

    def get_forensics_hunt_results(self, *,
            collection_id: dict,
            investigation_id: str,
            search_id: dict) -> Any:
        """List results of a hunt search

        POST /public_api/v1/forensics/investigations/collections/hunt
        Available in Cortex XDR 5.x.
        Returns the complete JSON response, text, bytes, or None for an empty response.
        Optional fields use UNSET for omission; None is explicit null.
        The source snapshot records this operation and its parameter schema.
        :param collection_id: body field collection_id.
        :param investigation_id: body field investigation_id.
        :param search_id: body field search_id.
        """
        self._require_versions((5,))
        body = self._values({
            'collection_id': collection_id,
            'investigation_id': investigation_id,
            'search_id': search_id,
        })
        body = {'request_data': body}
        return self._operation(
            '/public_api/v1/forensics/investigations/collections/hunt', method='post',
            body=body,
        )

    def get_forensics_triage_results(self, *,
            agent_id: dict,
            collection_id: dict,
            investigation_id: str) -> Any:
        """List triage results for an agent

        POST /public_api/v1/forensics/investigations/collections/triage
        Available in Cortex XDR 5.x.
        Returns the complete JSON response, text, bytes, or None for an empty response.
        Optional fields use UNSET for omission; None is explicit null.
        The source snapshot records this operation and its parameter schema.
        :param agent_id: body field agent_id.
        :param collection_id: body field collection_id.
        :param investigation_id: body field investigation_id.
        """
        self._require_versions((5,))
        body = self._values({
            'agent_id': agent_id,
            'collection_id': collection_id,
            'investigation_id': investigation_id,
        })
        body = {'request_data': body}
        return self._operation(
            '/public_api/v1/forensics/investigations/collections/triage', method='post',
            body=body,
        )

    def get_forensics_collection_data(self, *,
            artifact_type: str,
            collection_id: str,
            investigation_id: str,
            agent_id: Union[dict, None, UnsetType] = UNSET,
            search_from: Union[int, None, UnsetType] = UNSET,
            search_id: Union[dict, None, UnsetType] = UNSET,
            search_to: Union[int, None, UnsetType] = UNSET) -> Any:
        """Get artifact data rows from a collection

        POST /public_api/v1/forensics/investigations/collections/get_data
        Available in Cortex XDR 5.x.
        Returns the complete JSON response, text, bytes, or None for an empty response.
        Optional fields use UNSET for omission; None is explicit null.
        The source snapshot records this operation and its parameter schema.
        :param artifact_type: body field artifact_type.
        :param collection_id: body field collection_id.
        :param investigation_id: body field investigation_id.
        :param agent_id: body field agent_id.
        :param search_from: body field search_from.
        :param search_id: body field search_id.
        :param search_to: body field search_to.
        """
        self._require_versions((5,))
        body = self._values({
            'artifact_type': artifact_type,
            'collection_id': collection_id,
            'investigation_id': investigation_id,
            'agent_id': agent_id,
            'search_from': search_from,
            'search_id': search_id,
            'search_to': search_to,
        })
        body = {'request_data': body}
        return self._operation(
            '/public_api/v1/forensics/investigations/collections/get_data', method='post',
            body=body,
        )

    def get_forensics_host_timeline(self, *,
            agent_id: str,
            collection_id: dict,
            investigation_id: str,
            search_from: Union[int, None, UnsetType] = UNSET,
            search_to: Union[int, None, UnsetType] = UNSET) -> Any:
        """Get host timeline rows for an agent

        POST /public_api/v1/forensics/investigations/collections/triage/host_timeline
        Available in Cortex XDR 5.x.
        Returns the complete JSON response, text, bytes, or None for an empty response.
        Optional fields use UNSET for omission; None is explicit null.
        The source snapshot records this operation and its parameter schema.
        :param agent_id: body field agent_id.
        :param collection_id: body field collection_id.
        :param investigation_id: body field investigation_id.
        :param search_from: body field search_from.
        :param search_to: body field search_to.
        """
        self._require_versions((5,))
        body = self._values({
            'agent_id': agent_id,
            'collection_id': collection_id,
            'investigation_id': investigation_id,
            'search_from': search_from,
            'search_to': search_to,
        })
        body = {'request_data': body}
        return self._operation(
            '/public_api/v1/forensics/investigations/collections/triage/host_timeline', method='post',
            body=body,
        )

    def get_forensics_triage_files(self, *,
            agent_id: str,
            artifact_type: dict,
            collection_id: dict,
            investigation_id: str) -> Any:
        """List files collected by a triage artifact

        POST /public_api/v1/forensics/investigations/collections/triage/get_files
        Available in Cortex XDR 5.x.
        Returns the complete JSON response, text, bytes, or None for an empty response.
        Optional fields use UNSET for omission; None is explicit null.
        The source snapshot records this operation and its parameter schema.
        :param agent_id: body field agent_id.
        :param artifact_type: body field artifact_type.
        :param collection_id: body field collection_id.
        :param investigation_id: body field investigation_id.
        """
        self._require_versions((5,))
        body = self._values({
            'agent_id': agent_id,
            'artifact_type': artifact_type,
            'collection_id': collection_id,
            'investigation_id': investigation_id,
        })
        body = {'request_data': body}
        return self._operation(
            '/public_api/v1/forensics/investigations/collections/triage/get_files', method='post',
            body=body,
        )
