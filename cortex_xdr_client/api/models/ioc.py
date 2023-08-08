from enum import Enum
from typing import List, Optional

from pydantic import BaseModel, Field


class ValidationError(BaseModel):
    """
    Validation Error Model
    Represents a validation error.
    """
    indicator: str
    error: str


class IoCResponseItem(BaseModel):
    """
    IoC Response Item Model
    Represents the response item of the IoC API.
    """
    success: bool
    validation_errors: List[ValidationError]


class IoCResponse(BaseModel):
    """
    IoC Response Model
    Represents the response of the IoC API.
    """
    reply: Optional[IoCResponseItem]


class Reputation(str, Enum):
    """
    Reputation Enum
    Represents the reputation.
    """
    GOOD: str = 'GOOD'
    BAD: str = 'BAD'
    SUSPICIOUS: str = 'SUSPICIOUS'
    UNKNOWN: str = 'UNKNOWN'


class Vendor(BaseModel):
    """
    Vendor Model
    Represents a vendor.
    """
    vendor_name: str
    reliability: str
    reputation: Reputation

    class Config:
        use_enum_values = True


class IoCReliability(str, Enum):
    """
    IoC Reliability Enum
    Represents the reliability of an IoC in a scale of A (best) to F (least)
    """
    A: str = 'A'
    B: str = 'B'
    C: str = 'C'
    D: str = 'D'
    E: str = 'E'
    F: str = 'F'


class IoCSeverity(str, Enum):
    """
    IoC Severity Enum
    Represents the indicator's severity. Valid values are: informational, low, medium, high, critical, or unknown
    """
    informational: str = 'INFORMATIONAL'
    low: str = 'LOW'
    medium: str = 'MEDIUM'
    high: str = 'HIGH'
    critical: str = 'CRITICAL'
    unknown: str = 'UNKNOWN'


class IoCType(str, Enum):
    """
    IoC Type Enum
    Represents the type of indicator. Allowed values:HASH, IP, DOMAIN_NAME, FILENAME
    """
    HASH: str = 'HASH'
    IP: str = 'IP'
    DOMAIN_NAME: str = 'DOMAIN_NAME'
    FILENAME: str = 'FILENAME'


class IoC(BaseModel):
    """
    IoC Model
    Represents an Indicator of Compromise (IoC).
    The expiration_date is an integer representing the indicator's expiration timestamp. This is a Unix epoch timestamp value, in milliseconds. If this indicator has no expiration, use Never. If this value is NULL, the indicator receives the indicator's type value with the default expiration date. Valid values are: 7 days, 30 days, 90 days, or 180 days
    """
    indicator: str
    type: IoCType
    expiration_date: Optional[int]
    comment: str
    reputation: Reputation
    reliability: IoCReliability
    severity: IoCSeverity
    vendors: List[Vendor]
    class_: str = Field(str, alias='class')

    class Config:
        use_enum_values = True
