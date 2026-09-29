from typing import Any, List, Optional, Tuple, Union

from cortex_xdr_client.api.operation import UNSET, UnsetType


from cortex_xdr_client.api.authentication import Authentication
from cortex_xdr_client.api.base_api import BaseAPI
from cortex_xdr_client.api.version import APIVersion
from cortex_xdr_client.api.models.action_status import GetActionStatus
from cortex_xdr_client.api.models.filters import new_request_data


class ActionsAPI(BaseAPI):
    def __init__(self, auth: Authentication, fqdn: str, timeout: Tuple[int, int],
                 api_version: APIVersion = APIVersion.V3) -> None:
        super(ActionsAPI, self).__init__(auth, fqdn, "actions", timeout, api_version)

    # https://docs.paloaltonetworks.com/cortex/cortex-xdr/cortex-xdr-api/cortex-xdr-apis/response-actions/get-action-status.html
    def get_action_status(self,
                          group_action_id: int
                          ) -> Optional[GetActionStatus]:
        """
        Retrieve the status of the requested actions according to the action ID.

        :param group_action_id: String the represents the Action ID of the selected request.
        :return: Returns a GetActionStatus object if successful.
        """
        request_data = new_request_data(other={'group_action_id': group_action_id})

        response = self._call(call_name="get_action_status",
                              json_value=request_data)
        return GetActionStatus.model_validate(response.json())

    # https://docs-cortex.paloaltonetworks.com/r/Cortex-XDR/Cortex-XDR-API-Reference/File-Retrieval-Details
    def get_file_retrieval_details(self,
                                   group_action_id: int
                                   ) -> Optional[GetActionStatus]:
        """
        Retrieve the status of the requested file retrieval action.

        :param group_action_id: String the represents the Action ID of the selected request.
        :return: Returns a GetActionStatus object if successful.
        """
        request_data = new_request_data(other={'group_action_id': group_action_id})

        response = self._call(call_name="file_retrieval_details",
                              json_value=request_data)
        return GetActionStatus.model_validate(response.json())


    def file_retrieval_details(self, *,
                               accept_encoding: Union[str, None, UnsetType] = UNSET,
                               group_action_id: Union[str, None, UnsetType] = UNSET) -> Any:
        """File Retrieval Details

        POST /public_api/v1/actions/file_retrieval_details
        Available in Cortex XDR 3.x, 5.x.
        Returns the complete JSON response, bytes for downloads, or None for an empty response.
        Omit optional fields with UNSET; explicit None is sent as JSON null.
        :param accept_encoding: header field Accept-Encoding.
        :param group_action_id: body field group_action_id.
        """
        self._require_versions((3, 5))
        if self._api_version == APIVersion.V3:
            body = self._values({'group_action_id': group_action_id})
            body = self._values({'request_data': body, **{}})
            return self._operation(
                '/public_api/v1/actions/file_retrieval_details', method='post',
                headers={'Accept-Encoding': accept_encoding},
                body=body,
            )
        elif self._api_version == APIVersion.V5:
            self._reject_fields(accept_encoding=accept_encoding)
            body = self._values({'group_action_id': group_action_id})
            body = self._values({'request_data': body, **{}})
            return self._operation(
                '/public_api/v1/actions/file_retrieval_details', method='post',
                body=body,
            )

    def get_action_status_request(self, *,
                                  accept_encoding: Union[str, None, UnsetType] = UNSET,
                                  group_action_id: Union[int, None, UnsetType] = UNSET) -> Any:
        """Get Action Status

        POST /public_api/v1/actions/get_action_status
        Available in Cortex XDR 3.x, 5.x.
        Returns the complete JSON response, bytes for downloads, or None for an empty response.
        Omit optional fields with UNSET; explicit None is sent as JSON null.
        :param accept_encoding: header field Accept-Encoding.
        :param group_action_id: body field group_action_id.
        """
        self._require_versions((3, 5))
        if self._api_version == APIVersion.V3:
            body = self._values({'group_action_id': group_action_id})
            body = self._values({'request_data': body, **{}})
            return self._operation(
                '/public_api/v1/actions/get_action_status', method='post',
                headers={'Accept-Encoding': accept_encoding},
                body=body,
            )
        elif self._api_version == APIVersion.V5:
            self._reject_fields(accept_encoding=accept_encoding)
            body = self._values({'group_action_id': group_action_id})
            body = self._values({'request_data': body, **{}})
            return self._operation(
                '/public_api/v1/actions/get_action_status', method='post',
                body=body,
            )
