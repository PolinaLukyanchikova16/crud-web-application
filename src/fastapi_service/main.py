import uvicorn
from routers import user, customer, supplier, invoice

import config
from fastapi import FastAPI

app = FastAPI()
app.include_router(user.router)
app.include_router(customer.router)
app.include_router(supplier.router)
app.include_router(invoice.router)


if __name__ == "__main__":
    uvicorn.run(
        app="main:app",
        host=config.HOST,
        port=config.PORT
    )
