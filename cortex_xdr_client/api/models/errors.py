from typing import List, Optional
from pydantic import BaseModel


class GetError(BaseModel):
    err_code: Optional[int]
    err_msg: Optional[str]
    err_extra: Optional[str]


class GetAllErrors(BaseModel):
    reply: GetError
