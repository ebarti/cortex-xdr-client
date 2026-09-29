"""Explicit operations from the pinned Cortex XDR documentation snapshot."""
from typing import Any, Tuple, Union

from cortex_xdr_client.api.operation import UNSET, UnsetType
from cortex_xdr_client.api.authentication import Authentication
from cortex_xdr_client.api.base_api import BaseAPI
from cortex_xdr_client.api.version import APIVersion


class ManagedServicesAPI(BaseAPI):
    def __init__(self, auth: Authentication, fqdn: str, timeout: Tuple[int, int],
                 api_version: APIVersion = APIVersion.V3) -> None:
        super(ManagedServicesAPI, self).__init__(auth, fqdn, 'managed_services', timeout, api_version)

    def post_update_report_assignment(self, *,
            xsoar_source_id: Any,
            user: Union[str, None, UnsetType] = UNSET,
            username: Union[str, None, UnsetType] = UNSET) -> Any:
        """Update report assignment

        POST /public_api/v1/mth/child/report/update/assign
        Available in Cortex XDR 5.x.
        Returns the complete JSON response, text, bytes, or None for an empty response.
        Optional fields use UNSET for omission; None is explicit null.
        The source snapshot records this operation and its parameter schema.
        :param xsoar_source_id: body field xsoar_source_id.
        :param user: body field user.
        :param username: body field username.
        """
        self._require_versions((5,))
        body = self._values({
            'xsoar_source_id': xsoar_source_id,
            'user': user,
            'username': username,
        })
        return self._operation(
            '/public_api/v1/mth/child/report/update/assign', method='post',
            body=body,
        )

    def post_add_comment(self, *,
            comment_created_by: str,
            comment_text: str,
            xsoar_source_id: str,
            extract_zip_file: Union[str, None, UnsetType] = UNSET,
            path_to_file: Union[str, None, UnsetType] = UNSET) -> Any:
        """Add a comment to an MTH/MDR report

        POST /public_api/v1/mth/child/add_comment
        Available in Cortex XDR 5.x.
        Returns the complete JSON response, text, bytes, or None for an empty response.
        Optional fields use UNSET for omission; None is explicit null.
        The source snapshot records this operation and its parameter schema.
        :param comment_created_by: body field comment_created_by.
        :param comment_text: body field comment_text.
        :param xsoar_source_id: body field xsoar_source_id.
        :param extract_zip_file: body field extract_zip_file.
        :param path_to_file: body field path_to_file.
        """
        self._require_versions((5,))
        body = self._values({
            'comment_created_by': comment_created_by,
            'comment_text': comment_text,
            'xsoar_source_id': xsoar_source_id,
            'extract_zip_file': extract_zip_file,
            'path_to_file': path_to_file,
        })
        return self._operation(
            '/public_api/v1/mth/child/add_comment', method='post',
            body=body,
        )

    def post_get_comments(self, *,
            end_time: Union[int, None, UnsetType] = UNSET,
            start_time: Union[int, None, UnsetType] = UNSET,
            xsoar_source_id: Union[str, None, UnsetType] = UNSET) -> Any:
        """Get comments for MTH/MDR reports

        POST /public_api/v1/mth/child/get_comments
        Available in Cortex XDR 5.x.
        Returns the complete JSON response, text, bytes, or None for an empty response.
        Optional fields use UNSET for omission; None is explicit null.
        The source snapshot records this operation and its parameter schema.
        :param end_time: body field end_time.
        :param start_time: body field start_time.
        :param xsoar_source_id: body field xsoar_source_id.
        """
        self._require_versions((5,))
        body = self._values({
            'end_time': end_time,
            'start_time': start_time,
            'xsoar_source_id': xsoar_source_id,
        })
        return self._operation(
            '/public_api/v1/mth/child/get_comments', method='post',
            body=body,
        )

    def post_get_reports_by_source_id(self, *, xsoar_source_ids: Any) -> Any:
        """Get reports by source ID

        POST /public_api/v1/mth/child/get_reports_by_source_id
        Available in Cortex XDR 5.x.
        Returns the complete JSON response, text, bytes, or None for an empty response.
        Optional fields use UNSET for omission; None is explicit null.
        The source snapshot records this operation and its parameter schema.
        :param xsoar_source_ids: body field xsoar_source_ids.
        """
        self._require_versions((5,))
        body = self._values({'xsoar_source_ids': xsoar_source_ids})
        return self._operation(
            '/public_api/v1/mth/child/get_reports_by_source_id', method='post',
            body=body,
        )

    def post_get_reports_by_incident_id(self, *, incident_ids: Any) -> Any:
        """Get reports by incident ID

        POST /public_api/v1/mth/child/get_reports_by_incident_id
        Available in Cortex XDR 5.x.
        Returns the complete JSON response, text, bytes, or None for an empty response.
        Optional fields use UNSET for omission; None is explicit null.
        The source snapshot records this operation and its parameter schema.
        :param incident_ids: body field incident_ids.
        """
        self._require_versions((5,))
        body = self._values({'incident_ids': incident_ids})
        return self._operation(
            '/public_api/v1/mth/child/get_reports_by_incident_id', method='post',
            body=body,
        )

    def post_get_all_reports(self) -> Any:
        """Get all MTH/MDR reports

        POST /public_api/v1/mth/child/get_all_reports
        Available in Cortex XDR 5.x.
        Returns the complete JSON response, text, bytes, or None for an empty response.
        Optional fields use UNSET for omission; None is explicit null.
        The source snapshot records this operation and its parameter schema.
        """
        self._require_versions((5,))
        body = {'request_data': {}}
        return self._operation(
            '/public_api/v1/mth/child/get_all_reports', method='post',
            body=body,
        )

    def post_get_reports_by_statuses(self, *, report_statuses: list) -> Any:
        """Get reports by statuses

        POST /public_api/v1/mth/child/get_reports_by_statuses
        Available in Cortex XDR 5.x.
        Returns the complete JSON response, text, bytes, or None for an empty response.
        Optional fields use UNSET for omission; None is explicit null.
        The source snapshot records this operation and its parameter schema.
        :param report_statuses: body field report_statuses.
        """
        self._require_versions((5,))
        body = self._values({'report_statuses': report_statuses})
        return self._operation(
            '/public_api/v1/mth/child/get_reports_by_statuses', method='post',
            body=body,
        )

    def post_update_report_status(self, *, report_status: str, xsoar_source_id: Any) -> Any:
        """Update report status

        POST /public_api/v1/mth/child/report/update/status
        Available in Cortex XDR 5.x.
        Returns the complete JSON response, text, bytes, or None for an empty response.
        Optional fields use UNSET for omission; None is explicit null.
        The source snapshot records this operation and its parameter schema.
        :param report_status: body field report_status.
        :param xsoar_source_id: body field xsoar_source_id.
        """
        self._require_versions((5,))
        body = self._values({'report_status': report_status, 'xsoar_source_id': xsoar_source_id})
        return self._operation(
            '/public_api/v1/mth/child/report/update/status', method='post',
            body=body,
        )
