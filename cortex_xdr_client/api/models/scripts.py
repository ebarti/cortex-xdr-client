from datetime import datetime
from typing import List, Optional

from pydantic import BaseModel


class Script(BaseModel):
    script_id: Optional[int]
    name: Optional[str]
    description: Optional[str]
    modification_date: Optional[int]
    created_by: Optional[str]
    windows_supported: Optional[bool]
    linux_supported: Optional[bool]
    macos_supported: Optional[bool]
    is_high_risk: Optional[bool]
    script_uid: Optional[str]


class GetScriptsResponse(BaseModel):
    total_count: Optional[int]
    result_count: Optional[int]
    scripts: Optional[List[Script]]


class GetScriptsExecutionStatus(BaseModel):
    general_status: Optional[str]
    endpoints_pending: Optional[int]
    endpoints_canceled: Optional[int]
    endpoints_in_progress: Optional[int]
    endpoints_timeout: Optional[int]
    endpoints_failed: Optional[int]
    endpoints_completed_successfully: Optional[int]
    endpoints_pending_abort: Optional[int]
    endpoints_aborted: Optional[int]
    endpoints_expired: Optional[int]


class ScriptIO(BaseModel):
    name: Optional[str]
    value: Optional[str]
    type: Optional[str]


class GetScriptMetadataResponse(BaseModel):
    script_id: Optional[int]
    name: Optional[str]
    description: Optional[str]
    modification_date: Optional[int]
    created_by: Optional[str]
    is_high_risk: Optional[bool]
    windows_supported: Optional[bool]
    linux_supported: Optional[bool]
    macos_supported: Optional[bool]
    script_uid: Optional[str]
    entry_point: Optional[str]
    script_input: Optional[List[ScriptIO]]
    script_output_type: Optional[str]
    script_output_dictionary_definitions: Optional[List[ScriptIO]]


class ScriptExecutionResult(BaseModel):
    endpoint_name: Optional[str]
    endpoint_ip_address: Optional[List[str]]
    endpoint_status: Optional[str]
    domain: Optional[str]
    endpoint_id: Optional[str]
    execution_status: Optional[str]
    standard_output: Optional[str]
    retrieved_files: Optional[int]
    failed_files: Optional[int]
    retention_date: Optional[int]


class GetScriptExecutionResults(BaseModel):
    script_name: Optional[str]
    script_description: Optional[str]
    script_parameters: Optional[List[ScriptIO]]
    date_created: Optional[datetime]
    scope: Optional[str]
    error_message: Optional[str]
    results: Optional[List[ScriptExecutionResult]]
