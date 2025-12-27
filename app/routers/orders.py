from fastapi import APIRouter, Depends, HTTPException,status
from sqlalchemy.orm import Session
from app.database.session import get_database
from app.models.users import Users
from app.schemas.orders_schema import OrderCreate,OrderRead
from app.routers.dependencies import get_current_user
from app.services.order_services import OrderService

order_router = APIRouter(prefix="/api",tags=["orders"])

@order_router.post("/orders", response_model=OrderRead)
async def place_an_order(order:OrderCreate,
                         current_user:Users = Depends(get_current_user),
                         db:Session = Depends(get_database)):
    order_service = OrderService(db)
    new_order = order_service.create_order(current_user, order)
    return new_order


