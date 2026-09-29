from typing import List, Optional

from pydantic import Field

from cortex_xdr_client.api.models.base import CortexResponseModel


class Case(CortexResponseModel):
    case_id: Optional[int] = None
    case_name: Optional[str] = None
    is_blocked: Optional[bool] = None
    creation_time: Optional[int] = None
    modification_time: Optional[int] = None
    status_progress: Optional[str] = None
    resolve_reason: Optional[str] = None
    severity: Optional[str] = None
    description: Optional[str] = None
    assigned_user_mail: Optional[str] = None
    assigned_user_pretty_name: Optional[str] = None
    issue_count: Optional[int] = None
    issue_ids: Optional[List[int]] = None
    user_severity: Optional[str] = None
    notes: Optional[str] = None
    resolve_comment: Optional[str] = None
    resolved_timestamp: Optional[int] = None
    xdr_url: Optional[str] = None
    starred: Optional[bool] = None
    hosts: Optional[List[str]] = None
    users: Optional[List[str]] = None
    tags: Optional[List[str]] = None
    custom_fields: Optional[dict] = None
    assets: Optional[List[dict]] = None
    asset_ids: Optional[List[str]] = None
    case_domain: Optional[str] = None
    case_team: Optional[List[dict]] = None
    access_mode: Optional[str] = None


class GetCasesResponseItem(CortexResponseModel):
    total_count: Optional[int] = Field(None, alias='TOTAL_COUNT')
    filter_count: Optional[int] = Field(None, alias='FILTER_COUNT')
    data: List[Case] = Field(..., alias='DATA')


class GetCasesResponse(CortexResponseModel):
    reply: GetCasesResponseItem
