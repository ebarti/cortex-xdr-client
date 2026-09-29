from typing import List, Tuple
from urllib.parse import quote

from cortex_xdr_client.api.authentication import Authentication
from cortex_xdr_client.api.base_api import BaseAPI
from cortex_xdr_client.api.models.cases import GetCasesResponse
from cortex_xdr_client.api.models.filters import new_request_data
from cortex_xdr_client.api.version import APIVersion


class CasesAPI(BaseAPI):
    def __init__(self, auth: Authentication, fqdn: str, timeout: Tuple[int, int],
                 api_version: APIVersion = APIVersion.V5) -> None:
        super(CasesAPI, self).__init__(auth, fqdn, "case", timeout, api_version)

    def get_cases(self, filters: List[dict] = None, search_from: int = None,
                  search_to: int = None, sort: dict = None) -> GetCasesResponse:
        """Search cases using the v5 case filter names, sorting and pagination."""
        request_data = new_request_data(filters=filters, search_from=search_from,
                                        search_to=search_to, sort=sort)
        response = self._call("search", json_value=request_data)
        return GetCasesResponse.parse_obj(response.json())

    def update_case(self, case_id: int, update_data: dict) -> None:
        """Update one case. Successful updates return HTTP 204 without a body."""
        request_data = new_request_data(other={'update_data': update_data})
        self._call(f"update/{quote(str(case_id), safe='')}", json_value=request_data)

    def get_case_artifacts(self, case_id: int) -> List[dict]:
        """Get file and network artifacts; the response is an unwrapped list."""
        response = self._call(f"artifacts/{quote(str(case_id), safe='')}/", method="get")
        return response.json()

    def get_cases_schema(self) -> dict:
        """Get the available case fields, including tenant custom fields."""
        return self._call("schema", method="get").json()

    def get_case_timeline(self, case_id: int, filters: List[dict] = None,
                          search_from: int = None, search_to: int = None, sort: dict = None) -> dict:
        """Get timeline records using the timeline API's filters and sort values."""
        request_data = new_request_data(filters=filters, search_from=search_from,
                                        search_to=search_to, sort=sort)
        response = self._call(f"timeline/{quote(str(case_id), safe='')}/", json_value=request_data)
        return response.json()

    def add_case_timeline_record(self, case_id: int, record: dict) -> dict:
        """Add a record containing record_type, record_name and occurred_at."""
        response = self._call(f"timeline/{quote(str(case_id), safe='')}/add_record/",
                              json_value=new_request_data(other=record))
        return response.json()
