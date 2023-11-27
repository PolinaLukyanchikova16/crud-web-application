from typing import List, Optional
from uuid import UUID, uuid4
from enum import Enum
from pydantic import BaseModel


class Role(str, Enum):
    customer = "customer"
    supplier = "supplier"


class User(BaseModel):
    id: Optional[UUID] = uuid4()
    name: str
    role: List[Role]


class UpdateUser(BaseModel):
    name: Optional[str]
    roles: Optional[List[Role]]


user_db: List[User] = [
    User(
        id=uuid4(),
        name="John",
        role=[Role.customer],
    ),
    User(
        id=uuid4(),
        name="Jane",
        role=[Role.supplier],
    ),
    User(
        id=uuid4(),
        name="James",
        role=[Role.supplier],
    ),
    User(
        id=uuid4(),
        name="Eunit",
        role=[Role.customer],
    ),
]
