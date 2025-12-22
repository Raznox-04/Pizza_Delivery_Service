from fastapi import APIRouter
order_router = APIRouter(prefix="/api",tags=["orders"])
@order_router.get("/orders")
async def root():
    return {"message": "its working"}