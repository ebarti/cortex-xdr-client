from typing import List, Optional
from pydantic import BaseModel


class GetError(BaseModel):
    err_code: Optional[int]
    err_msg: Optional[str]
    err_extra: Optional[str]


class GetAllErrors(BaseModel):
    reply: GetError


class BaseException(Exception):
    def __init__(self, response):
        self.response = response
        super().__init__(self.response)

    def __str__(self):
        return f'{GetAllErrors.parse_obj(self.response.json())}'


class EndpointException(BaseException):
    pass


class IncidentException(BaseException):
    pass


class AlertException(BaseException):
    pass


class ScriptException(BaseException):
    pass


class XQLException(BaseException):
    pass
