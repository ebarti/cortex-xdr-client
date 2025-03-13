

from pydantic import BaseModel, Extra

# Define a global base class with custom configuration
class CustomBaseModel(BaseModel):
    class Config:
        extra = Extra.allow
        use_enum_values = True