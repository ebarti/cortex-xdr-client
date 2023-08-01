from datetime import datetime

from pydantic import BaseModel
from enum import Enum
from typing import List, Optional


class ValidationError(BaseModel):
    indicator: str
    error: str


class IOCReturn(BaseModel):
    success: bool
    validation_errors: List[ValidationError]


class IoCReply(BaseModel):
    reply: Optional[IOCReturn]

