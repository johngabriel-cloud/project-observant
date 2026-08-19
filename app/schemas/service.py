from enum import Enum
from typing import Literal

from pydantic import BaseModel, Field, HttpUrl, field_validator

class CheckType(str, Enum):
    HTTP = "HTTP"

class ServiceCreate(BaseModel):
    name:str = Field(min_length=8, max_length=32)

    @field_validator("name")
    @classmethod
    def name_validator(cls, value):
        if value.strip() == "":
            raise ValueError("Name must not be empty or whitespace")
        
        if value != value.strip():
            raise ValueError("Name must not contain leading or trailing spaces")
        return value

    check_type: CheckType
    url: HttpUrl
    interval: Literal[30, 60, 300]