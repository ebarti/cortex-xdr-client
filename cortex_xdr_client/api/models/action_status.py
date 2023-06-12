from typing import Dict, Optional, Union

from pydantic import BaseModel


class ActionStatuStr(BaseModel):
    # Since we don't know what the returned key of <agent ID>/<endpoint ID> will be.
    __root__: Dict[Union[str, None], Union[str, None]]


class GetActionStatusItem(BaseModel):
    data: Optional[ActionStatuStr]


class GetActionStatus(BaseModel):
    reply: GetActionStatusItem
