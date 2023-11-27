from typing import List, Optional
from uuid import UUID, uuid4
from pydantic import BaseModel


class Supplier(BaseModel):
    id: Optional[UUID] = uuid4()
    name: str
    org_id: int
    users: list


class UpdateSupplier(BaseModel):
    id: Optional[UUID] = uuid4()
    name: str
    org_id: int
    users: list


suppliers_db: List[Supplier] = [
    Supplier(
        id=uuid4(),
        name="WACAB AB",
        org_id="5678234564",
        users=[2, 3]
    ),
    Supplier(
        id=uuid4(),
        name="COLORAMA BOLLNÄS",
        org_id="0987654321",
        users=[1]
    ),
    Supplier(
        id=uuid4(),
        name="LEDVANCE AB",
        org_id="9348716876",
        users=[3, 4]
    ),
]
