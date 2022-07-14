from enum import Enum
from typing import Any, List, Optional, Union, Dict

from pydantic import BaseModel
import json


class ActionStatuStr(BaseModel):
    # Since we don't know what the returned key of <agent ID> will be.
    __root__: Dict[str, str]


class GetActionStatusItem(BaseModel):
    data: Optional[ActionStatuStr]


class GetActionStatus(BaseModel):
    reply: GetActionStatusItem
