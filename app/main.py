from fastapi import FastAPI
from app.routers.auth import auth_router
from app.routers.orders  import order_router
from app.routers.users import user_router
app = FastAPI(title="Pizza Delivery ElenPizo",summary="Pizza Delivery Web Service")
app.include_router(auth_router,prefix="/auth")
app.include_router(order_router)
app.include_router(user_router)
@app.get("/",tags=["index"])
async def root():
    return {"message": "Welcome to Pizza Delivery Web Sefastrvice its working!!!"}