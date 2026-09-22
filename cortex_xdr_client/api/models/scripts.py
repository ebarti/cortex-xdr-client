from datetime import datetime
from typing import List, Optional, Union

from pydantic import StrictInt

from cortex_xdr_client.api.models.base import CortexResponseModel


class Script(CortexResponseModel):
    script_id: Optional[Union[StrictInt, str]] = None
    name: Optional[str] = None
    description: Optional[str] = None
    modification_date: Optional[int] = None
    created_by: Optional[str] = None
    windows_supported: Optional[bool] = None
    linux_supported: Optional[bool] = None
    macos_supported: Optional[bool] = None
    is_high_risk: Optional[bool] = None
    script_uid: Optional[str] = None


class GetScriptsResponse(CortexResponseModel):
    total_count: Optional[int] = None
    result_count: Optional[int] = None
    scripts: Optional[List[Script]] = None


class GetScriptsExecutionStatus(CortexResponseModel):
    general_status: Optional[str] = None
    endpoints_pending: Optional[int] = None
    endpoints_canceled: Optional[int] = None
    endpoints_in_progress: Optional[int] = None
    endpoints_timeout: Optional[int] = None
    endpoints_failed: Optional[int] = None
    endpoints_completed_successfully: Optional[int] = None
    endpoints_pending_abort: Optional[int] = None
    endpoints_aborted: Optional[int] = None
    endpoints_expired: Optional[int] = None


class ScriptIO(CortexResponseModel):
    name: Optional[str] = None
    value: Optional[str] = None
    type: Optional[str] = None


class GetScriptMetadataResponse(CortexResponseModel):
    script_id: Optional[Union[StrictInt, str]] = None
    name: Optional[str] = None
    description: Optional[str] = None
    modification_date: Optional[int] = None
    created_by: Optional[str] = None
    is_high_risk: Optional[bool] = None
    windows_supported: Optional[bool] = None
    linux_supported: Optional[bool] = None
    macos_supported: Optional[bool] = None
    script_uid: Optional[str] = None
    entry_point: Optional[str] = None
    script_input: Optional[List[ScriptIO]] = None
    script_output_type: Optional[str] = None
    script_output_dictionary_definitions: Optional[List[ScriptIO]] = None


class ScriptExecutionResult(CortexResponseModel):
    endpoint_name: Optional[str] = None
    endpoint_ip_address: Optional[List[str]] = None
    endpoint_status: Optional[str] = None
    domain: Optional[str] = None
    endpoint_id: Optional[str] = None
    execution_status: Optional[str] = None
    standard_output: Union[Optional[str], List[str]] = None
    retrieved_files: Optional[int] = None
    failed_files: Optional[int] = None
    retention_date: Optional[int] = None


class GetScriptExecutionResults(CortexResponseModel):
    script_name: Optional[str] = None
    script_description: Optional[str] = None
    script_parameters: Optional[List[ScriptIO]] = None
    date_created: Optional[datetime] = None
    scope: Optional[str] = None
    error_message: Optional[str] = None
    results: Optional[List[ScriptExecutionResult]] = None
