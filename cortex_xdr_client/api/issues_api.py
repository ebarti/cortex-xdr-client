from typing import List, Tuple
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
        return GetIssuesResponse.parse_obj(response.json())

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
