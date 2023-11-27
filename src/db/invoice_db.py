from typing import List, Optional
from uuid import UUID, uuid4
from pydantic import BaseModel


class Invoice(BaseModel):
    id: Optional[UUID] = uuid4()
    customer: str
    supplier: str
    data: dict


class UpdateInvoice(BaseModel):
    id: Optional[UUID] = uuid4()
    customer: str
    supplier: str
    data: dict


invoices_db: List[Invoice] = [
    Invoice(
        id=uuid4(),
        customer="Atea",
        supplier="WACAB AB",
        data={"data": "some_data"}
    ),
    Invoice(
        id=uuid4(),
        customer="Rexel",
        supplier="COLORAMA BOLLNÄS",
        data={"data": "some_data"}
    ),
    Invoice(
        id=uuid4(),
        customer="Aqua Dental",
        supplier="LEDVANCE AB",
        data={"data": "some_data"}
    ),
]
