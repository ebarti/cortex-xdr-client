from typing import List, Optional

from pydantic import BaseModel, Field


class Issue(BaseModel):
    id: Optional[int]
    insert_time: Optional[int] = Field(None, alias='_insert_time')
    external_id: Optional[str]
    name: Optional[str]
    description: Optional[str]
    observation_time: Optional[int]
    domain: Optional[str]
    detection_method: Optional[str] = Field(None, alias='detection.method')
    detection_rule_id: Optional[str] = Field(None, alias='detection.rule_id')
    category: Optional[str]
    severity: Optional[str]
    status_progress: Optional[str] = Field(None, alias='status.progress')
    status_resolution_reason: Optional[str] = Field(None, alias='status.resolution_reason')
    status_resolution_comment: Optional[str] = Field(None, alias='status.resolution_comment')
    assigned_to: Optional[str]
    assigned_to_pretty: Optional[str]
    case_ids: Optional[List[int]]
    asset_ids: Optional[List[str]]
    asset_names: Optional[List[str]]
    tags: Optional[List[str]]
    normalized_fields: Optional[dict]
    custom_fields: Optional[dict]
    evidences: Optional[List[dict]]
    actions: Optional[List[dict]]

    class Config:
        extra = 'allow'


class GetIssuesResponseItem(BaseModel):
    total_count: Optional[int] = Field(None, alias='TOTAL_COUNT')
    filter_count: Optional[int] = Field(None, alias='FILTER_COUNT')
    data: List[Issue] = Field(..., alias='DATA')


class GetIssuesResponse(BaseModel):
    reply: GetIssuesResponseItem
