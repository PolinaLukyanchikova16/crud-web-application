# pydantic models

from pydantic import BaseModel
from typing import Optional, List


class CreateUserSchema(BaseModel):
    name: str
    surname: str
    email: str
    phone_number: int
    gender: str


class CreateUserResponse(BaseModel):
    id: str


class UpdateUserSchema(BaseModel):
    name: Optional[str]
    surname: Optional[str]
    email: Optional[str]
    phone_number: Optional[int]
    gender: Optional[str]


class UpdateUserResponse(BaseModel):
    id: str
    name: str
    surname: str
    email: str
    phone_number: int
    gender: str


class GetUserResponse(BaseModel):
    name: str
    surname: str
    email: str
    phone_number: int
    gender: str
