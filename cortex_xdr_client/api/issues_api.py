from typing import Any, List, Tuple, Union

from cortex_xdr_client.api.operation import UNSET, UnsetType

from urllib.parse import quote

from cortex_xdr_client.api.authentication import Authentication
from cortex_xdr_client.api.base_api import BaseAPI
from cortex_xdr_client.api.models.filters import new_request_data
from cortex_xdr_client.api.models.issues import GetIssuesResponse
from cortex_xdr_client.api.version import APIVersion


class IssuesAPI(BaseAPI):
    def __init__(self, auth: Authentication, fqdn: str, timeout: Tuple[int, int],
                 api_version: APIVersion = APIVersion.V5) -> None:
        super(IssuesAPI, self).__init__(auth, fqdn, "issue", timeout, api_version)

    def get_issues(self, filters: List[dict] = None, search_from: int = None,
                   search_to: int = None, sort: dict = None, include_fields: List[str] = None,
                   include_evidences: bool = None, include_actions: bool = None) -> GetIssuesResponse:
        """Search issues using v5 field names (for example status.progress)."""
        other = {}
        if include_fields is not None:
            other['include_fields'] = include_fields
        if include_evidences is not None:
            other['include_evidences'] = include_evidences
        if include_actions is not None:
            other['include_actions'] = include_actions
        request_data = new_request_data(filters=filters, search_from=search_from,
                                        search_to=search_to, sort=sort, other=other)
        response = self._call("search", json_value=request_data)
        return GetIssuesResponse.model_validate(response.json())

    def create_issue(self, issue: dict) -> dict:
        """Create an issue; returns external_id and detection_method (HTTP 202)."""
        self._require_version(APIVersion.V5)
        response = self.request("/public_api/v1/issue",
                                 json_value=new_request_data(other={'issue': issue}))
        return response.json()

    def update_issue(self, issue_id: int, update_data: dict) -> None:
        """Update issue severity/status. HTTP 204 has no response body."""
        self._call(quote(str(issue_id), safe=''),
                    json_value=new_request_data(other={'update_data': update_data}))

    def get_issues_schema(self) -> dict:
        """Get issue fields and their types. This schema endpoint uses POST."""
        return self._call("schema/").json()

    def create_issue_exception(self, exception: dict) -> dict:
        """Create an issue exception using the documented exception fields."""
        self._require_version(APIVersion.V5)
        return self.request("/public_api/v1/issue_exceptions/",
                             json_value=new_request_data(other=exception)).json()

    def disable_issue_exception(self, exception_id: int) -> dict:
        """Disable an issue exception by ID."""
        self._require_version(APIVersion.V5)
        return self.request("/public_api/v1/issue_exceptions/disable/",
                             json_value=new_request_data(other={'exception_id': exception_id})).json()

    def get_issue_exceptions(self, filters: dict = None, search_from: int = None,
                             search_to: int = None, sort: dict = None) -> dict:
        """Search exceptions using their SEARCH_FIELD/SEARCH_TYPE filter structure."""
        self._require_version(APIVersion.V5)
        request_data = new_request_data(search_from=search_from, search_to=search_to, sort=sort)
        if filters is not None:
            request_data['request_data']['filters'] = filters
        return self.request("/public_api/v1/issue_exceptions/search/", json_value=request_data).json()


    def create_issue_request(self, *,
                             issue: Union[dict, None, UnsetType] = UNSET) -> Any:
        """Create a new issue

        POST /public_api/v1/issue
        Available in Cortex XDR 5.x.
        Returns the complete JSON response, bytes for downloads, or None for an empty response.
        Omit optional fields with UNSET; explicit None is sent as JSON null.
        :param issue: body field issue.
        """
        self._require_versions((5,))
        body = self._values({'issue': issue})
        body = self._values({'request_data': body, **{}})
        return self._operation(
            '/public_api/v1/issue', method='post',
            body=body,
        )

    def get_issues_request(self, *,
                           filters: Union[List[dict], None, UnsetType] = UNSET,
                           search_from: Union[int, None, UnsetType] = UNSET,
                           search_to: Union[int, None, UnsetType] = UNSET,
                           sort: Union[dict, None, UnsetType] = UNSET,
                           include_fields: Union[List[str], None, UnsetType] = UNSET,
                           include_evidences: Union[bool, None, UnsetType] = UNSET,
                           include_actions: Union[bool, None, UnsetType] = UNSET) -> Any:
        """Retrieve issues based on filters

        POST /public_api/v1/issue/search
        Available in Cortex XDR 5.x.
        Returns the complete JSON response, bytes for downloads, or None for an empty response.
        Omit optional fields with UNSET; explicit None is sent as JSON null.
        :param filters: body field filters.
        :param search_from: body field search_from.
        :param search_to: body field search_to.
        :param sort: body field sort.
        :param include_fields: body field include_fields.
        :param include_evidences: body field include_evidences.
        :param include_actions: body field include_actions.
        """
        self._require_versions((5,))
        body = self._values({'filters': filters, 'search_from': search_from, 'search_to': search_to, 'sort': sort, 'include_fields': include_fields, 'include_evidences': include_evidences, 'include_actions': include_actions})
        body = self._values({'request_data': body, **{}})
        return self._operation(
            '/public_api/v1/issue/search', method='post',
            body=body,
        )

    def update_issue_request(self, *,
                             issue_id: int,
                             update_data: Union[dict, None, UnsetType] = UNSET) -> Any:
        """Update existing issue

        POST /public_api/v1/issue/{issue-id}
        Available in Cortex XDR 5.x.
        Returns the complete JSON response, bytes for downloads, or None for an empty response.
        Omit optional fields with UNSET; explicit None is sent as JSON null.
        :param issue_id: path field issue-id.
        :param update_data: body field update_data.
        """
        self._require_versions((5,))
        body = self._values({'update_data': update_data})
        body = self._values({'request_data': body, **{}})
        return self._operation(
            '/public_api/v1/issue/{issue-id}', method='post',
            path_params={'issue-id': issue_id},
            body=body,
        )

    def get_issue_schema(self) -> Any:
        """Retrieve issue schema

        POST /public_api/v1/issue/schema/
        Available in Cortex XDR 5.x.
        Returns the complete JSON response, bytes for downloads, or None for an empty response.
        Omit optional fields with UNSET; explicit None is sent as JSON null.
        """
        self._require_versions((5,))
        body = UNSET
        return self._operation(
            '/public_api/v1/issue/schema/', method='post',
            body=body,
        )

    def create_issue_exception_request(self, *,
                                       name: Union[str, None, UnsetType] = UNSET,
                                       external_exception_id: Union[str, None, UnsetType] = UNSET,
                                       rule: Union[str, None, UnsetType] = UNSET,
                                       justification_text: Union[str, None, UnsetType] = UNSET,
                                       justification_category: Union[str, None, UnsetType] = UNSET,
                                       approval_justification: Union[str, None, UnsetType] = UNSET,
                                       approver_email: Union[str, None, UnsetType] = UNSET,
                                       expiration_ts: Union[str, None, UnsetType] = UNSET) -> Any:
        """Create a new issue exception

        POST /public_api/v1/issue_exceptions/
        Available in Cortex XDR 5.x.
        Returns the complete JSON response, bytes for downloads, or None for an empty response.
        Omit optional fields with UNSET; explicit None is sent as JSON null.
        :param name: body field name.
        :param external_exception_id: body field external_exception_id.
        :param rule: body field rule.
        :param justification_text: body field justification_text.
        :param justification_category: body field justification_category.
        :param approval_justification: body field approval_justification.
        :param approver_email: body field approver_email.
        :param expiration_ts: body field expiration_ts.
        """
        self._require_versions((5,))
        body = self._values({'name': name, 'external_exception_id': external_exception_id, 'rule': rule, 'justification_text': justification_text, 'justification_category': justification_category, 'approval_justification': approval_justification, 'approver_email': approver_email, 'expiration_ts': expiration_ts})
        body = self._values({'request_data': body, **{}})
        return self._operation(
            '/public_api/v1/issue_exceptions/', method='post',
            body=body,
        )

    def disable_issue_exception_request(self, *,
                                        exception_id: Union[int, None, UnsetType] = UNSET) -> Any:
        """Disable an issue exception

        POST /public_api/v1/issue_exceptions/disable/
        Available in Cortex XDR 5.x.
        Returns the complete JSON response, bytes for downloads, or None for an empty response.
        Omit optional fields with UNSET; explicit None is sent as JSON null.
        :param exception_id: body field exception_id.
        """
        self._require_versions((5,))
        body = self._values({'exception_id': exception_id})
        body = self._values({'request_data': body, **{}})
        return self._operation(
            '/public_api/v1/issue_exceptions/disable/', method='post',
            body=body,
        )

    def search_issue_exceptions(self, *,
                                filters: Union[dict, None, UnsetType] = UNSET,
                                search_from: Union[int, None, UnsetType] = UNSET,
                                search_to: Union[int, None, UnsetType] = UNSET,
                                sort: Union[dict, None, UnsetType] = UNSET) -> Any:
        """Retrieve issue exceptions based on filters

        POST /public_api/v1/issue_exceptions/search/
        Available in Cortex XDR 5.x.
        Returns the complete JSON response, bytes for downloads, or None for an empty response.
        Omit optional fields with UNSET; explicit None is sent as JSON null.
        :param filters: body field filters.
        :param search_from: body field search_from.
        :param search_to: body field search_to.
        :param sort: body field sort.
        """
        self._require_versions((5,))
        body = self._values({'filters': filters, 'search_from': search_from, 'search_to': search_to, 'sort': sort})
        body = self._values({'request_data': body, **{}})
        return self._operation(
            '/public_api/v1/issue_exceptions/search/', method='post',
            body=body,
        )
