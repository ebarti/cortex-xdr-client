from pydantic import BaseModel, ConfigDict


class CortexResponseModel(BaseModel):
    """Preserve additional API response fields without weakening known field types."""
    model_config = ConfigDict(
        extra='allow',
        validate_by_name=True,
        validate_by_alias=True,
    )
