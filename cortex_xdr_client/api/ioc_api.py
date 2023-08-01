import json
from typing import Optional, Tuple

from cortex_xdr_client.api.authentication import Authentication
from cortex_xdr_client.api.base_api import BaseAPI
from cortex_xdr_client.api.models.action_status import GetActionStatus
from cortex_xdr_client.api.models.filters import new_request_data

from cortex_xdr_client.api.authentication import Authentication
from cortex_xdr_client.api.base_api import BaseAPI

from cortex_xdr_client.api.models.ioc import IoCReply

from cortex_xdr_client.api.models.exceptions import InvalidResponseException
from cortex_xdr_client.api.models.filters import (new_request_data, request_gte_lte_filter, request_in_contains_filter)

import requests


class IocAPI(BaseAPI):

    def __init__(self, auth: Authentication, fqdn: str, timeout: Tuple[int, int]) -> None:
        super(IocAPI, self).__init__(auth, fqdn, "indicators", timeout)

    def insert_json(self, payload: dict) -> IoCReply:
        response = self._call(call_name="insert_jsons", json_value=payload)
        return IoCReply.parse_obj(response.json())
