from typing import List, Optional
from uuid import UUID, uuid4
from pydantic import BaseModel


class Customer(BaseModel):
    id: Optional[UUID] = uuid4()
    name: str
    org_id: int
    users: list


class UpdateCustomer(BaseModel):
    id: Optional[UUID] = uuid4()
    name: str
    org_id: int
    users: list


customers_db: List[Customer] = [
    Customer(
        id=uuid4(),
        name="Atea",
        org_id="1234567890",
        users=[1]
    ),
    Customer(
        id=uuid4(),
        name="Rexel",
        org_id="0987654321",
        users=[2, 3]
    ),
    Customer(
        id=uuid4(),
        name="Aqua Dental",
        org_id="1122334455",
        users=[4]
    ),
]
