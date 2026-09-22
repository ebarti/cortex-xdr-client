from typing import Dict, Optional, Union

from pydantic import RootModel

from cortex_xdr_client.api.models.base import CortexResponseModel


class ActionStatuStr(RootModel[Dict[Union[str, None], Union[str, None]]]):
    # Since we don't know what the returned key of <agent ID>/<endpoint ID> will be.
    pass


class GetActionStatusItem(CortexResponseModel):
    data: Optional[ActionStatuStr] = None


class GetActionStatus(CortexResponseModel):
    reply: GetActionStatusItem
