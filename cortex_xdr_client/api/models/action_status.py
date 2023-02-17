from typing import Dict, Optional

from pydantic import BaseModel


class ActionStatuStr(BaseModel):
    # Since we don't know what the returned key of <agent ID>/<endpoint ID> will be.
    __root__: Dict[str, str]


class GetActionStatusItem(BaseModel):
    data: Optional[ActionStatuStr]


class GetActionStatus(BaseModel):
    reply: GetActionStatusItem
