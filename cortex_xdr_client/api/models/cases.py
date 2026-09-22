from typing import List, Optional

from pydantic import BaseModel, Field


class Case(BaseModel):
    case_id: Optional[int]
    case_name: Optional[str]
    is_blocked: Optional[bool]
    creation_time: Optional[int]
    modification_time: Optional[int]
    status_progress: Optional[str]
    resolve_reason: Optional[str]
    severity: Optional[str]
    description: Optional[str]
    assigned_user_mail: Optional[str]
    assigned_user_pretty_name: Optional[str]
    issue_count: Optional[int]
    issue_ids: Optional[List[int]]
    user_severity: Optional[str]
    notes: Optional[str]
    resolve_comment: Optional[str]
    resolved_timestamp: Optional[int]
    xdr_url: Optional[str]
    starred: Optional[bool]
    hosts: Optional[List[str]]
    users: Optional[List[str]]
    tags: Optional[List[str]]
    custom_fields: Optional[dict]
    assets: Optional[List[dict]]
    asset_ids: Optional[List[str]]
    case_domain: Optional[str]
    case_team: Optional[List[dict]]
    access_mode: Optional[str]

    class Config:
        extra = 'allow'


class GetCasesResponseItem(BaseModel):
    total_count: Optional[int] = Field(None, alias='TOTAL_COUNT')
    filter_count: Optional[int] = Field(None, alias='FILTER_COUNT')
    data: List[Case] = Field(..., alias='DATA')


class GetCasesResponse(BaseModel):
    reply: GetCasesResponseItem
