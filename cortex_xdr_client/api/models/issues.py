from typing import List, Optional

from pydantic import Field

from cortex_xdr_client.api.models.base import CortexResponseModel


class Issue(CortexResponseModel):
    id: Optional[int] = None
    insert_time: Optional[int] = Field(None, alias='_insert_time')
    external_id: Optional[str] = None
    name: Optional[str] = None
    description: Optional[str] = None
    observation_time: Optional[int] = None
    domain: Optional[str] = None
    detection_method: Optional[str] = Field(None, alias='detection.method')
    detection_rule_id: Optional[str] = Field(None, alias='detection.rule_id')
    category: Optional[str] = None
    severity: Optional[str] = None
    status_progress: Optional[str] = Field(None, alias='status.progress')
    status_resolution_reason: Optional[str] = Field(None, alias='status.resolution_reason')
    status_resolution_comment: Optional[str] = Field(None, alias='status.resolution_comment')
    assigned_to: Optional[str] = None
    assigned_to_pretty: Optional[str] = None
    case_ids: Optional[List[int]] = None
    asset_ids: Optional[List[str]] = None
    asset_names: Optional[List[str]] = None
    tags: Optional[List[str]] = None
    normalized_fields: Optional[dict] = None
    custom_fields: Optional[dict] = None
    evidences: Optional[List[dict]] = None
    actions: Optional[List[dict]] = None


class GetIssuesResponseItem(CortexResponseModel):
    total_count: Optional[int] = Field(None, alias='TOTAL_COUNT')
    filter_count: Optional[int] = Field(None, alias='FILTER_COUNT')
    data: List[Issue] = Field(..., alias='DATA')


class GetIssuesResponse(CortexResponseModel):
    reply: GetIssuesResponseItem
