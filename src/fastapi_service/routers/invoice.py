from uuid import UUID

from fastapi import APIRouter, HTTPException


router = APIRouter(
    tags=["invoice"],
    responses={404: {"description": "Not found"}},)


# @router.get("/api/v1/invoices")
# async def get_invoices():
#     return invoices_db
#
#
# @router.get("/api/v1/invoices/{id}")
# async def get_invoice(invoice_id: UUID):
#     for invoice in invoices_db:
#         if invoice.id == invoice_id:
#             return invoice
#     raise HTTPException(status_code=404, detail=f"Could not find an invoice with id: {invoice_id}")
#
#
# @router.post("/api/v1/invoices")
# async def create_invoice(invoice: Invoice):
#     invoices_db.append(invoice)
#     return {"id": invoice.id}
#
#
# @router.put("/api/v1/invoices/{id}")
# async def update_invoice(invoice_update: UpdateInvoice, invoice_id: UUID):
#     for invoice in invoices_db:
#         if invoice.id == invoice:
#             if invoice_update.id is not None:
#                 invoice.id = invoice_update.id
#             if invoice_update.customer is not None:
#                 invoice.customer = invoice_update.customer
#             if invoice_update.supplier is not None:
#                 invoice.supplier = invoice_update.supplier
#             return invoice.id
#     raise HTTPException(status_code=404, detail=f"Could not find an invoice with id: {invoice_id}")
#
#
# @router.delete("/api/v1/invoices/{id}")
# async def delete_invoice(invoice_id: UUID):
#     for invoice in invoices_db:
#         if invoice.id == invoice_id:
#             invoices_db.remove(invoice)
#             return
#     raise HTTPException(status_code=404, detail=f"Delete invoice failed, id {invoice_id} not found.")
