from fastapi import FastAPI
from routers.auth import auth_router
from routers.orders import order_router
app = FastAPI(title="Pizza Delivery ElenPizo",summary="Pizza Delivery Web Service")
app.include_router(auth_router)
app.include_router(order_router)

@app.get("/")
async def root():
    return {"message": "Welcome to Pizza Delivery Web Service its working!!!"}