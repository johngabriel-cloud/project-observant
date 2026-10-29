from enum import Enum
from typing import Literal
from pydantic import BaseModel, Field, HttpUrl, field_validator

class CheckType(str, Enum):
    HTTP = 'http'

class ServiceCreate(BaseModel):
    name: str = Field(min_length=8, max_length=32)

    #field validator is used for custom validation
    @field_validator('name')
    #classmethod defines a method that is bound to the class not the instance of the class, and can be called on the class itself.
    @classmethod
    def name_validator(cls, name: str) -> str:
        if name.strip() == "":
            raise ValueError('Name must not be empty or whitespace only')
        if name != name.strip():
            raise ValueError('Name must not contain leading or trailing whitespace')
        return name
    
    url: HttpUrl
    check_type: CheckType
    interval: Literal[30, 60, 300]