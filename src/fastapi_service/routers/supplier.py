from uuid import UUID

from fastapi import APIRouter, HTTPException


router = APIRouter(
    tags=["supplier"],
    responses={404: {"description": "Not found"}},)


# @router.get("/api/v1/suppliers")
# async def get_suppliers():
#     return suppliers_db
#
#
# @router.get("/api/v1/suppliers/{id}")
# async def get_supplier(supplier_id: UUID):
#     for supplier in suppliers_db:
#         if supplier.id == supplier_id:
#             return supplier
#     raise HTTPException(status_code=404, detail=f"Could not find a supplier with id: {supplier_id}")
#
#
# @router.post("/api/v1/suppliers")
# async def create_supplier(supplier: Supplier):
#     suppliers_db.append(supplier)
#     return {"id": supplier.id}
#
#
# @router.put("/api/v1/suppliers/{id}")
# async def update_supplier(supplier_update: UpdateSupplier, supplier_id: UUID):
#     for supplier in suppliers_db:
#         if supplier.id == supplier:
#             if supplier_update.name is not None:
#                 supplier.name = supplier_update.name
#             if supplier_update.id is not None:
#                 supplier.id = supplier_update.id
#             if supplier_update.org_id is not None:
#                 supplier.org_id = supplier_update.org_id
#             return supplier.id
#     raise HTTPException(status_code=404, detail=f"Could not find a supplier with id: {supplier_id}")
#
#
# @router.delete("/api/v1/suppliers/{id}")
# async def delete_supplier(supplier_id: UUID):
#     for supplier in suppliers_db:
#         if supplier.id == supplier_id:
#             suppliers_db.remove(supplier)
#             return
#     raise HTTPException(status_code=404, detail=f"Delete supplier failed, id {supplier_id} not found.")
