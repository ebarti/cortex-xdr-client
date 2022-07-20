from enum import Enum

from typing import List, Optional, Tuple

from cortex_xdr_client.api.base_api import BaseAPI
from cortex_xdr_client.api.models.action_status import (
    GetActionStatus
)
from cortex_xdr_client.api.models.filters import (
    new_request_data,
)


class ActionsAPI(BaseAPI):
    def __init__(self, api_key_id: int, api_key: str, fqdn: str, timeout: Tuple[int, int]) -> None:
        super(ActionsAPI, self).__init__(api_key_id, api_key, fqdn, "actions", timeout)

    # https://docs.paloaltonetworks.com/cortex/cortex-xdr/cortex-xdr-api/cortex-xdr-apis/response-actions/get-action-status.html
    def get_action_status(self,
                   group_action_id: int
                   ) -> Optional[GetActionStatus]:
        """
        Retrieve the status of the requested actions according to the action ID.

        :param group_action_id: String the represents the Action ID of the selected request.
        :return: Returns a GetActionStatus object if successful.
        """
        request_data = new_request_data(other={'group_action_id':group_action_id})

        response = self._call(call_name="get_action_status",
                              json_value=request_data)
        return GetActionStatus.parse_obj(response.json())
