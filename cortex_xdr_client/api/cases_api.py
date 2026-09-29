from typing import Any, List, Tuple, Union

from cortex_xdr_client.api.operation import UNSET, UnsetType

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
        return GetCasesResponse.model_validate(response.json())

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


    def get_cases_request(self, *,
                          filters: Union[List[dict], None, UnsetType] = UNSET,
                          search_from: Union[int, None, UnsetType] = UNSET,
                          search_to: Union[int, None, UnsetType] = UNSET,
                          sort: Union[dict, None, UnsetType] = UNSET) -> Any:
        """Retrieve cases based on filters

        POST /public_api/v1/case/search
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
            '/public_api/v1/case/search', method='post',
            body=body,
        )

    def update_case_request(self, *,
                            case_id: int,
                            update_data: Union[dict, None, UnsetType] = UNSET) -> Any:
        """Update existing case

        POST /public_api/v1/case/update/{case-id}
        Available in Cortex XDR 5.x.
        Returns the complete JSON response, bytes for downloads, or None for an empty response.
        Omit optional fields with UNSET; explicit None is sent as JSON null.
        :param case_id: path field case-id.
        :param update_data: body field update_data.
        """
        self._require_versions((5,))
        body = self._values({'update_data': update_data})
        body = self._values({'request_data': body, **{}})
        return self._operation(
            '/public_api/v1/case/update/{case-id}', method='post',
            path_params={'case-id': case_id},
            body=body,
        )

    def get_case_artifacts_request(self, *,
                                   case_id: int) -> Any:
        """Retrieve case artifacts

        GET /public_api/v1/case/artifacts/{case-id}/
        Available in Cortex XDR 5.x.
        Returns the complete JSON response, bytes for downloads, or None for an empty response.
        Omit optional fields with UNSET; explicit None is sent as JSON null.
        :param case_id: path field case-id.
        """
        self._require_versions((5,))
        body = UNSET
        return self._operation(
            '/public_api/v1/case/artifacts/{case-id}/', method='get',
            path_params={'case-id': case_id},
            body=body,
        )

    def get_cases_schema_request(self) -> Any:
        """Get cases schema

        GET /public_api/v1/case/schema
        Available in Cortex XDR 5.x.
        Returns the complete JSON response, bytes for downloads, or None for an empty response.
        Omit optional fields with UNSET; explicit None is sent as JSON null.
        """
        self._require_versions((5,))
        body = UNSET
        return self._operation(
            '/public_api/v1/case/schema', method='get',
            body=body,
        )

    def get_case_timeline_request(self, *,
                                  case_id: str,
                                  filters: Union[List[dict], None, UnsetType] = UNSET,
                                  search_from: Union[int, None, UnsetType] = UNSET,
                                  search_to: Union[int, None, UnsetType] = UNSET,
                                  sort: Union[dict, None, UnsetType] = UNSET) -> Any:
        """Retrieve case timeline records

        POST /public_api/v1/case/timeline/{case-id}/
        Available in Cortex XDR 5.x.
        Returns the complete JSON response, bytes for downloads, or None for an empty response.
        Omit optional fields with UNSET; explicit None is sent as JSON null.
        :param case_id: path field case-id.
        :param filters: body field filters.
        :param search_from: body field search_from.
        :param search_to: body field search_to.
        :param sort: body field sort.
        """
        self._require_versions((5,))
        body = self._values({'filters': filters, 'search_from': search_from, 'search_to': search_to, 'sort': sort})
        body = self._values({'request_data': body, **{}})
        return self._operation(
            '/public_api/v1/case/timeline/{case-id}/', method='post',
            path_params={'case-id': case_id},
            body=body,
        )

    def add_case_timeline_record_request(self, *,
                                         case_id: str,
                                         record_type: Union[str, None, UnsetType] = UNSET,
                                         record_name: Union[str, None, UnsetType] = UNSET,
                                         occurred_at: Union[int, None, UnsetType] = UNSET,
                                         description: Union[str, None, UnsetType] = UNSET,
                                         is_evidence: Union[bool, None, UnsetType] = UNSET,
                                         evidence_comment: Union[str, None, UnsetType] = UNSET,
                                         tags: Union[List[str], None, UnsetType] = UNSET,
                                         timelines: Union[List[str], None, UnsetType] = UNSET) -> Any:
        """Add a case timeline record

        POST /public_api/v1/case/timeline/{case-id}/add_record/
        Available in Cortex XDR 5.x.
        Returns the complete JSON response, bytes for downloads, or None for an empty response.
        Omit optional fields with UNSET; explicit None is sent as JSON null.
        :param case_id: path field case-id.
        :param record_type: body field record_type.
        :param record_name: body field record_name.
        :param occurred_at: body field occurred_at.
        :param description: body field description.
        :param is_evidence: body field is_evidence.
        :param evidence_comment: body field evidence_comment.
        :param tags: body field tags.
        :param timelines: body field timelines.
        """
        self._require_versions((5,))
        body = self._values({'record_type': record_type, 'record_name': record_name, 'occurred_at': occurred_at, 'description': description, 'is_evidence': is_evidence, 'evidence_comment': evidence_comment, 'tags': tags, 'timelines': timelines})
        body = self._values({'request_data': body, **{}})
        return self._operation(
            '/public_api/v1/case/timeline/{case-id}/add_record/', method='post',
            path_params={'case-id': case_id},
            body=body,
        )

    def post_public_api_v1_entries_get(self, *,
                                       id: Union[str, None, UnsetType] = UNSET,
                                       filter: Union[dict, None, UnsetType] = UNSET) -> Any:
        """Get War Room entries

        POST /public_api/v1/entries/get
        Available in Cortex XDR 5.x.
        Returns the complete JSON response, bytes for downloads, or None for an empty response.
        Omit optional fields with UNSET; explicit None is sent as JSON null.
        :param id: body field id.
        :param filter: body field filter.
        """
        self._require_versions((5,))
        body = self._values({'id': id, 'filter': filter})
        return self._operation(
            '/public_api/v1/entries/get', method='post',
            body=body,
        )

    def post_public_api_v1_entries_insert(self, *,
                                          id: Union[str, None, UnsetType] = UNSET,
                                          data: Union[str, None, UnsetType] = UNSET) -> Any:
        """Add War Room entries

        POST /public_api/v1/entries/insert
        Available in Cortex XDR 5.x.
        Returns the complete JSON response, bytes for downloads, or None for an empty response.
        Omit optional fields with UNSET; explicit None is sent as JSON null.
        :param id: body field id.
        :param data: body field data.
        """
        self._require_versions((5,))
        body = self._values({'id': id, 'data': data})
        return self._operation(
            '/public_api/v1/entries/insert', method='post',
            body=body,
        )
