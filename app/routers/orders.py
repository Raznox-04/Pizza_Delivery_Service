from fastapi import APIRouter, Depends, HTTPException,status
from sqlalchemy.orm import Session
from app.database.session import get_database
from app.models.users import Users
from app.schemas.orders_schema import OrderCreate,OrderRead,OrderUpdate
from app.routers.dependencies import get_current_user
from app.services.order_services import OrderService
from typing import List
order_router = APIRouter(prefix="/api",tags=["orders"])
def get_order_service(db: Session = Depends(get_database)) -> OrderService:
    return OrderService(db)
@order_router.post("/orders", response_model=OrderRead)
async def place_an_order(order:OrderCreate,
                         current_user:Users = Depends(get_current_user),
                         order_service:OrderService = Depends(get_order_service)):
    new_order = order_service.create_order(current_user, order)
    return new_order
@order_router.get("/orders", response_model=List[OrderRead])
async def get_all_orders(current_user:Users = Depends(get_current_user),
                         svc: OrderService = Depends(get_order_service)):
    orders = svc.get_users_orders(current_user.id)
    return orders

@order_router.get("/orders/{order_id}", response_model=OrderRead)
async def get_order_by_id(order_id : int,
                          current_user:Users = Depends(get_current_user),
                         svc: OrderService = Depends(get_order_service)) -> OrderRead:
    order = svc.get_order_by_id(order_id)
    return order

@order_router.put("/orders/{order_id}", response_model=OrderUpdate)
async def update_order_by_id(order_id : int,payload: OrderUpdate,
                             current_user:Users = Depends(get_current_user),
                             svc: OrderService = Depends(get_order_service),):
        order = svc.update_orders_by_user(order_id, payload)
        return order
