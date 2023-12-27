from uuid import UUID

from fastapi import APIRouter, HTTPException


router = APIRouter(
    tags=["customer"],
    responses={404: {"description": "Not found"}},)


# @router.get("/api/v1/customers")
# async def get_customers():
#     return customers_db
#
#
# @router.get("/api/v1/customers/{id}")
# async def get_customer(customer_id: UUID):
#     for customer in customers_db:
#         if customer.id == customer_id:
#             return customer
#     raise HTTPException(status_code=404, detail=f"Could not find a customer with id: {customer_id}")
#
#
# @router.post("/api/v1/customers")
# async def create_customer(customer: Customer):
#     customers_db.append(customer)
#     return {"id": customer.id}
#
#
# @router.put("/api/v1/customers/{id}")
# async def update_customer(customer_update: UpdateCustomer, customer_id: UUID):
#     for customer in customers_db:
#         if customer.id == customer:
#             if customer_update.name is not None:
#                 customer.name = customer_update.name
#             if customer_update.id is not None:
#                 customer.id = customer_update.id
#             if customer_update.org_id is not None:
#                 customer.org_id = customer_update.org_id
#             return customer.id
#     raise HTTPException(status_code=404, detail=f"Could not find a customer with id: {customer_id}")
#
#
# @router.delete("/api/v1/customers/{id}")
# async def delete_customer(customer_id: UUID):
#     for customer in customers_db:
#         if customer.id == customer_id:
#             customers_db.remove(customer)
#             return
#     raise HTTPException(status_code=404, detail=f"Delete customer failed, id {customer_id} not found.")
