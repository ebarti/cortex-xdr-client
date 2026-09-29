from typing import Any, List, Optional, Tuple, Union

from cortex_xdr_client.api.operation import UNSET, UnsetType


from cortex_xdr_client.api.authentication import Authentication
from cortex_xdr_client.api.base_api import BaseAPI
from cortex_xdr_client.api.version import APIVersion
from cortex_xdr_client.api.models.exceptions import InvalidResponseException
from cortex_xdr_client.api.models.filters import (new_request_data, request_gte_lte_filter, request_in_contains_filter)
from cortex_xdr_client.api.models.scripts import (GetScriptExecutionResults,
                                                  GetScriptMetadataResponse,
                                                  GetScriptsExecutionStatus,
                                                  GetScriptsResponse,
                                                  )


class ScriptsAPI(BaseAPI):
    def __init__(self, auth: Authentication, fqdn: str, timeout: Tuple[int, int],
                 api_version: APIVersion = APIVersion.V3) -> None:
        super(ScriptsAPI, self).__init__(auth, fqdn, "scripts", timeout, api_version)

    @staticmethod
    def _get_scripts_filters(name: List[str] = None,
                             description: List[str] = None,
                             created_by: List[str] = None,
                             script_uid: List[str] = None,
                             modification_time: int = None,
                             after_modification: bool = False,
                             windows_supported: bool = None,
                             linux_supported: bool = None,
                             macos_supported: bool = None,
                             is_high_risk: bool = None,
                             ) -> List[dict]:
        filters = []
        if name:
            filters.append(request_in_contains_filter("name", name, False))
        if description:
            filters.append(request_in_contains_filter("description", description, False))
        if created_by:
            filters.append(request_in_contains_filter("created_by", created_by, False))
        if script_uid:
            filters.append(request_in_contains_filter("script_uid", script_uid, False))
        if modification_time is not None:
            filters.append(request_gte_lte_filter("modification_date", modification_time, after_modification))
        if windows_supported is not None:
            filters.append(request_in_contains_filter("windows_supported", [str(windows_supported).lower()], False))
        if linux_supported is not None:
            filters.append(request_in_contains_filter("linux_supported", [str(linux_supported).lower()], False))
        if macos_supported is not None:
            filters.append(request_in_contains_filter("macos_supported", [str(macos_supported).lower()], False))
        if is_high_risk is not None:
            filters.append(request_in_contains_filter("is_high_risk", [str(is_high_risk).lower()], False))
        return filters

    # https://docs.paloaltonetworks.com/cortex/cortex-xdr/cortex-xdr-api/cortex-xdr-apis/script-execution/get-scripts.html
    def get_scripts(self,
                    name: List[str] = None,
                    description: List[str] = None,
                    created_by: List[str] = None,
                    script_uid: List[str] = None,
                    modification_time: int = None,
                    after_modification: bool = False,
                    windows_supported: bool = None,
                    linux_supported: bool = None,
                    macos_supported: bool = None,
                    is_high_risk: bool = None,
                    ) -> Optional[GetScriptsResponse]:
        """
        Get a list of scripts available in the scripts library.

        :param name: Script names
        :param description: Script descriptions
        :param created_by: Username(s) of who created the script(s).
        :param script_uid: GUID, global ID of the script(s), used to identify the script(s) when executing.
        :param modification_time: Datetime of when the script was last modified.
        :param after_modification: If the modification date will be the upper or lower bound limit.
        :param windows_supported: Whether the script can be executed on Windows operating system.
        :param linux_supported: Whether the script can be executed on Linux operating system.
        :param macos_supported: Whether the script can be executed on Mac operating system.
        :param is_high_risk: Whether the script has a high-risk outcome.
        :return: An object of type GetScriptsResponse if successful.
        """
        filters = self._get_scripts_filters(name, description, created_by, script_uid, modification_time,
                                            after_modification, windows_supported, linux_supported, macos_supported,
                                            is_high_risk)
        request_data = new_request_data(filters=filters or (["all"] if self._api_version == APIVersion.V3 else None))
        response = self._call("get_scripts", json_value=request_data)
        resp_json = response.json()
        if "reply" not in resp_json:
            raise InvalidResponseException(response, ["reply"])
        reply = resp_json["reply"]

        return GetScriptsResponse.model_validate(reply)

    # https://docs.paloaltonetworks.com/cortex/cortex-xdr/cortex-xdr-api/cortex-xdr-apis/script-execution/get-script-metadata.html
    def get_script_metadata(self, script_uid: str) -> Optional[GetScriptMetadataResponse]:
        """
        Get the full definitions of a specific script in the scripts library.

        :param script_uid: Unique identifier of the script, returned by the Get Scripts API per script.
        :return: An object of type GetScriptMetadataResponse if successful.
        """
        request_data = new_request_data(other={"script_uid": script_uid})
        response = self._call("get_script_metadata", json_value=request_data)
        resp_json = response.json()
        if "reply" not in resp_json:
            raise InvalidResponseException(response, ["reply"])
        reply = resp_json["reply"]
        return GetScriptMetadataResponse.model_validate(reply)

    # https://docs.paloaltonetworks.com/cortex/cortex-xdr/cortex-xdr-api/cortex-xdr-apis/script-execution/get-script-execution-status.html
    def get_script_execution_status(self, action_id: int) -> Optional[GetScriptsExecutionStatus]:
        """
        Retrieve the status of a script execution action.

        :param action_id: Integer, identifier of the action
        :return: An object of type GetScriptsExecutionStatus if successful.
        """
        request_data = new_request_data(other={"action_id": action_id})
        response = self._call("get_script_execution_status", json_value=request_data)
        resp_json = response.json()
        if "reply" not in resp_json:
            raise InvalidResponseException(response, ["reply"])
        reply = resp_json["reply"]
        return GetScriptsExecutionStatus.model_validate(reply)

    # https://docs.paloaltonetworks.com/cortex/cortex-xdr/cortex-xdr-api/cortex-xdr-apis/script-execution/get-script-execution-results.html
    def get_script_execution_results(self, action_id: int) -> Optional[GetScriptExecutionResults]:
        """
        Retrieve the results of a script execution action.
        :param action_id: Integer, identifier of the action
        :return: The results of a script execution action.
        """
        request_data = new_request_data(other={"action_id": action_id})
        response = self._call("get_script_execution_results", json_value=request_data)
        resp_json = response.json()
        if "reply" not in resp_json:
            raise InvalidResponseException(response, ["reply"])
        reply = resp_json["reply"]
        for result in reply.get('results') or []:
            if result.get('_return_value') is not None:
                result['standard_output'] = result['_return_value']
        return GetScriptExecutionResults.model_validate(reply)

    # https://docs.paloaltonetworks.com/cortex/cortex-xdr/cortex-xdr-api/cortex-xdr-apis/script-execution/get-script-execution-result-files.html
    def get_script_execution_result_files(self, action_id: int, endpoint_id: str) -> Optional[str]:
        """
        Get the files retrieved from a specific endpoint during a script execution.

        :param action_id: Integer, identifier of the action
        :param endpoint_id: String, endpoint ID.
        :return: A signed public link to a zip file containing the retrieved files. Link expires after 10 minutes.
        """
        request_data = new_request_data(other={"action_id": action_id, "endpoint_id": endpoint_id})
        response = self._call("get_script_execution_results_files", json_value=request_data)
        resp_json = response.json()
        if "reply" not in resp_json:
            raise InvalidResponseException(response, ["reply"])
        if "DATA" not in resp_json["reply"]:
            raise InvalidResponseException(response, ["DATA"])
        return resp_json["reply"]["DATA"]

    # https://docs.paloaltonetworks.com/cortex/cortex-xdr/cortex-xdr-api/cortex-xdr-apis/script-execution/run-script.html
    def run_script(self,
                   script_uid: str,
                   parameters_values: dict,
                   endpoint_id_list: List[str],
                   timeout: int = 600,
                   incident_id: str = None,
                   ) -> Optional[dict]:
        """
        Initiate a new endpoint script execution action using a script from the script library.

        :param script_uid: GUID, unique identifier of the script, returned by the Get Scripts API per script
        :param parameters_values: Dictionary, contains the parameter name, key and its value for this execution, value. You can locate these values by running Get Script Metadata
        :param endpoint_id_list: List of endpoint IDs.
        :param timeout: Integer, represents the timeout in seconds for this execution. Default value is 600.
        :param incident_id: String representing the incident ID. When included in the request, the Run Script action will appear in the Cortex XDR Incident View Timeline tab.
        :return: A dict containing action_id, status and endpoints_count.
        """
        filters = [request_in_contains_filter("endpoint_id_list", endpoint_id_list, False)]
        request_data = new_request_data(filters=filters,
                                        other={"script_uid": script_uid, "parameters_values": parameters_values,
                                               "timeout":    timeout, "incident_id": incident_id})
        if incident_id is None:
            request_data["request_data"].pop("incident_id")
        if parameters_values is None:
            request_data["request_data"].pop("parameters_values")
        response = self._call("run_script", json_value=request_data)
        resp_json = response.json()
        if "reply" not in resp_json:
            raise InvalidResponseException(response, ["reply"])
        return resp_json["reply"]

    # https://docs.paloaltonetworks.com/cortex/cortex-xdr/cortex-xdr-api/cortex-xdr-apis/script-execution/run-snippet-code-script.html
    def run_snippet_code_script(self,
                                snippet_code: str,
                                endpoint_id_list: List[str],
                                timeout: int = 600,
                                incident_id: str = None,
                                ) -> Optional[dict]:
        """
        Initiate a new endpoint script execution action using a snippet code.

        :param snippet_code: String, contains the snippet code to be executed.
        :param endpoint_id_list: List of endpoint IDs.
        :param timeout: Integer, represents the timeout in seconds for this execution. Default value is 600.
        :param incident_id: String representing the incident ID. When included in the request, the Run Script action will appear in the Cortex XDR Incident View Timeline tab.
        :return: A dict containing action_id and endpoints_count.
        """
        filters = [request_in_contains_filter("endpoint_id_list", endpoint_id_list, False)]
        request_data = new_request_data(filters=filters, other={"snippet_code": snippet_code, "timeout": timeout,
                                                                "incident_id":  incident_id})
        if incident_id is None:
            request_data["request_data"].pop("incident_id")
        response = self._call("run_snippet_code_script", json_value=request_data)
        resp_json = response.json()
        if "reply" not in resp_json:
            raise InvalidResponseException(response, ["reply"])
        return resp_json["reply"]


    def run_snippet_code_script_request(self, *,
                                        accept_encoding: Union[str, None, UnsetType] = UNSET,
                                        filters: Union[List[dict], None, UnsetType] = UNSET,
                                        timeout: Union[int, None, UnsetType] = UNSET,
                                        snippet_code: Union[str, None, UnsetType] = UNSET,
                                        incident_id: Union[str, None, UnsetType] = UNSET) -> Any:
        """Run Snippet Code Script

        POST /public_api/v1/scripts/run_snippet_code_script
        Available in Cortex XDR 3.x, 5.x.
        Returns the complete JSON response, bytes for downloads, or None for an empty response.
        Omit optional fields with UNSET; explicit None is sent as JSON null.
        :param accept_encoding: header field Accept-Encoding.
        :param filters: body field filters.
        :param timeout: body field timeout.
        :param snippet_code: body field snippet_code.
        :param incident_id: body field incident_id.
        """
        self._require_versions((3, 5))
        if self._api_version == APIVersion.V3:
            body = self._values({'filters': filters, 'timeout': timeout, 'snippet_code': snippet_code, 'incident_id': incident_id})
            body = self._values({'request_data': body, **{}})
            return self._operation(
                '/public_api/v1/scripts/run_snippet_code_script', method='post',
                headers={'Accept-Encoding': accept_encoding},
                body=body,
            )
        elif self._api_version == APIVersion.V5:
            self._reject_fields(accept_encoding=accept_encoding)
            body = self._values({'filters': filters, 'timeout': timeout, 'snippet_code': snippet_code, 'incident_id': incident_id})
            body = self._values({'request_data': body, **{}})
            return self._operation(
                '/public_api/v1/scripts/run_snippet_code_script', method='post',
                body=body,
            )

    def run_script_request(self, *,
                           accept_encoding: Union[str, None, UnsetType] = UNSET,
                           filters: Union[List[dict], None, UnsetType] = UNSET,
                           script_uid: Union[str, None, UnsetType] = UNSET,
                           parameters_values: Union[dict, None, UnsetType] = UNSET,
                           timeout: Union[int, None, UnsetType] = UNSET,
                           incident_id: Union[str, None, UnsetType] = UNSET) -> Any:
        """Run Script

        POST /public_api/v1/scripts/run_script
        Available in Cortex XDR 3.x, 5.x.
        Returns the complete JSON response, bytes for downloads, or None for an empty response.
        Omit optional fields with UNSET; explicit None is sent as JSON null.
        :param accept_encoding: header field Accept-Encoding.
        :param filters: body field filters.
        :param script_uid: body field script_uid.
        :param parameters_values: body field parameters_values.
        :param timeout: body field timeout.
        :param incident_id: body field incident_id.
        """
        self._require_versions((3, 5))
        if self._api_version == APIVersion.V3:
            body = self._values({'filters': filters, 'script_uid': script_uid, 'parameters_values': parameters_values, 'timeout': timeout, 'incident_id': incident_id})
            body = self._values({'request_data': body, **{}})
            return self._operation(
                '/public_api/v1/scripts/run_script', method='post',
                headers={'Accept-Encoding': accept_encoding},
                body=body,
            )
        elif self._api_version == APIVersion.V5:
            self._reject_fields(accept_encoding=accept_encoding)
            body = self._values({'filters': filters, 'script_uid': script_uid, 'parameters_values': parameters_values, 'timeout': timeout, 'incident_id': incident_id})
            body = self._values({'request_data': body, **{}})
            return self._operation(
                '/public_api/v1/scripts/run_script', method='post',
                body=body,
            )

    def get_script_metadata_request(self, *,
                                    accept_encoding: Union[str, None, UnsetType] = UNSET,
                                    script_uid: Union[str, None, UnsetType] = UNSET) -> Any:
        """Get Script Metadata

        POST /public_api/v1/scripts/get_script_metadata
        Available in Cortex XDR 3.x, 5.x.
        Returns the complete JSON response, bytes for downloads, or None for an empty response.
        Omit optional fields with UNSET; explicit None is sent as JSON null.
        :param accept_encoding: header field Accept-Encoding.
        :param script_uid: body field script_uid.
        """
        self._require_versions((3, 5))
        if self._api_version == APIVersion.V3:
            body = self._values({'script_uid': script_uid})
            body = self._values({'request_data': body, **{}})
            return self._operation(
                '/public_api/v1/scripts/get_script_metadata', method='post',
                headers={'Accept-Encoding': accept_encoding},
                body=body,
            )
        elif self._api_version == APIVersion.V5:
            self._reject_fields(accept_encoding=accept_encoding)
            body = self._values({'script_uid': script_uid})
            body = self._values({'request_data': body, **{}})
            return self._operation(
                '/public_api/v1/scripts/get_script_metadata', method='post',
                body=body,
            )

    def get_scripts_request(self, *,
                            accept_encoding: Union[str, None, UnsetType] = UNSET,
                            filters: Union[List[dict], None, UnsetType] = UNSET) -> Any:
        """Get Scripts

        POST /public_api/v1/scripts/get_scripts
        Available in Cortex XDR 3.x, 5.x.
        Returns the complete JSON response, bytes for downloads, or None for an empty response.
        Omit optional fields with UNSET; explicit None is sent as JSON null.
        :param accept_encoding: header field Accept-Encoding.
        :param filters: body field filters.
        """
        self._require_versions((3, 5))
        if self._api_version == APIVersion.V3:
            body = self._values({'filters': filters})
            body = self._values({'request_data': body, **{}})
            return self._operation(
                '/public_api/v1/scripts/get_scripts', method='post',
                headers={'Accept-Encoding': accept_encoding},
                body=body,
            )
        elif self._api_version == APIVersion.V5:
            self._reject_fields(accept_encoding=accept_encoding)
            body = self._values({'filters': filters})
            body = self._values({'request_data': body, **{}})
            return self._operation(
                '/public_api/v1/scripts/get_scripts', method='post',
                body=body,
            )

    def get_script_execution_status_request(self, *,
                                            accept_encoding: Union[str, None, UnsetType] = UNSET,
                                            action_id: Union[str, None, UnsetType] = UNSET) -> Any:
        """Get Script Execution Status

        POST /public_api/v1/scripts/get_script_execution_status
        Available in Cortex XDR 3.x, 5.x.
        Returns the complete JSON response, bytes for downloads, or None for an empty response.
        Omit optional fields with UNSET; explicit None is sent as JSON null.
        :param accept_encoding: header field Accept-Encoding.
        :param action_id: body field action_id.
        """
        self._require_versions((3, 5))
        if self._api_version == APIVersion.V3:
            body = self._values({'action_id': action_id})
            body = self._values({'request_data': body, **{}})
            return self._operation(
                '/public_api/v1/scripts/get_script_execution_status', method='post',
                headers={'Accept-Encoding': accept_encoding},
                body=body,
            )
        elif self._api_version == APIVersion.V5:
            self._reject_fields(accept_encoding=accept_encoding)
            body = self._values({'action_id': action_id})
            body = self._values({'request_data': body, **{}})
            return self._operation(
                '/public_api/v1/scripts/get_script_execution_status', method='post',
                body=body,
            )

    def get_script_execution_results_request(self, *,
                                             accept_encoding: Union[str, None, UnsetType] = UNSET,
                                             action_id: Union[str, None, UnsetType] = UNSET) -> Any:
        """Get Script Execution Results

        POST /public_api/v1/scripts/get_script_execution_results
        Available in Cortex XDR 3.x, 5.x.
        Returns the complete JSON response, bytes for downloads, or None for an empty response.
        Omit optional fields with UNSET; explicit None is sent as JSON null.
        :param accept_encoding: header field Accept-Encoding.
        :param action_id: body field action_id.
        """
        self._require_versions((3, 5))
        if self._api_version == APIVersion.V3:
            body = self._values({'action_id': action_id})
            body = self._values({'request_data': body, **{}})
            return self._operation(
                '/public_api/v1/scripts/get_script_execution_results', method='post',
                headers={'Accept-Encoding': accept_encoding},
                body=body,
            )
        elif self._api_version == APIVersion.V5:
            self._reject_fields(accept_encoding=accept_encoding)
            body = self._values({'action_id': action_id})
            body = self._values({'request_data': body, **{}})
            return self._operation(
                '/public_api/v1/scripts/get_script_execution_results', method='post',
                body=body,
            )

    def get_script_execution_results_files(self, *,
                                           accept_encoding: Union[str, None, UnsetType] = UNSET,
                                           action_id: Union[str, None, UnsetType] = UNSET,
                                           endpoint_id: Union[str, None, UnsetType] = UNSET) -> Any:
        """Get Script Execution Result Files

        POST /public_api/v1/scripts/get_script_execution_results_files
        Available in Cortex XDR 3.x, 5.x.
        Returns the complete JSON response, bytes for downloads, or None for an empty response.
        Omit optional fields with UNSET; explicit None is sent as JSON null.
        :param accept_encoding: header field Accept-Encoding.
        :param action_id: body field action_id.
        :param endpoint_id: body field endpoint_id.
        """
        self._require_versions((3, 5))
        if self._api_version == APIVersion.V3:
            body = self._values({'action_id': action_id, 'endpoint_id': endpoint_id})
            body = self._values({'request_data': body, **{}})
            return self._operation(
                '/public_api/v1/scripts/get_script_execution_results_files', method='post',
                headers={'Accept-Encoding': accept_encoding},
                body=body,
            )
        elif self._api_version == APIVersion.V5:
            self._reject_fields(accept_encoding=accept_encoding)
            body = self._values({'action_id': action_id, 'endpoint_id': endpoint_id})
            body = self._values({'request_data': body, **{}})
            return self._operation(
                '/public_api/v1/scripts/get_script_execution_results_files', method='post',
                body=body,
            )

    def get_script_code(self, *,
                        accept_encoding: Union[str, None, UnsetType] = UNSET,
                        script_uid: Union[str, None, UnsetType] = UNSET) -> Any:
        """Get Script Code

        POST /public_api/v1/scripts/get_script_code
        Available in Cortex XDR 3.x, 5.x.
        Returns the complete JSON response, bytes for downloads, or None for an empty response.
        Omit optional fields with UNSET; explicit None is sent as JSON null.
        :param accept_encoding: header field Accept-Encoding.
        :param script_uid: body field script_uid.
        """
        self._require_versions((3, 5))
        if self._api_version == APIVersion.V3:
            body = self._values({'script_uid': script_uid})
            body = self._values({'request_data': body, **{}})
            return self._operation(
                '/public_api/v1/scripts/get_script_code', method='post',
                headers={'Accept-Encoding': accept_encoding},
                body=body,
            )
        elif self._api_version == APIVersion.V5:
            self._reject_fields(accept_encoding=accept_encoding)
            body = self._values({'script_uid': script_uid})
            body = self._values({'request_data': body, **{}})
            return self._operation(
                '/public_api/v1/scripts/get_script_code', method='post',
                body=body,
            )

    def get(self, *,
            filter: Union[dict, None, UnsetType] = UNSET) -> Any:
        """Get a script

        POST /public_api/v1/scripts/get
        Available in Cortex XDR 5.x.
        Returns the complete JSON response, bytes for downloads, or None for an empty response.
        Omit optional fields with UNSET; explicit None is sent as JSON null.
        :param filter: body field filter.
        """
        self._require_versions((5,))
        body = self._values({'filter': filter})
        body = self._values({'request_data': body, **{}})
        return self._operation(
            '/public_api/v1/scripts/get', method='post',
            body=body,
        )

    def insert(self, *,
               file: Union[Any, None, UnsetType] = UNSET) -> Any:
        """Insert or update a script

        POST /public_api/v1/scripts/insert
        Available in Cortex XDR 5.x.
        Returns the complete JSON response, bytes for downloads, or None for an empty response.
        Omit optional fields with UNSET; explicit None is sent as JSON null.
        :param file: file field file.
        """
        self._require_versions((5,))
        body = self._values({})
        return self._operation(
            '/public_api/v1/scripts/insert', method='post',
            data=body, files={'file': file},
        )

    def delete(self, *,
               filter: Union[dict, None, UnsetType] = UNSET) -> Any:
        """Delete a script

        POST /public_api/v1/scripts/delete
        Available in Cortex XDR 5.x.
        Returns the complete JSON response, bytes for downloads, or None for an empty response.
        Omit optional fields with UNSET; explicit None is sent as JSON null.
        :param filter: body field filter.
        """
        self._require_versions((5,))
        body = self._values({'filter': filter})
        body = self._values({'request_data': body, **{}})
        return self._operation(
            '/public_api/v1/scripts/delete', method='post',
            body=body,
        )
