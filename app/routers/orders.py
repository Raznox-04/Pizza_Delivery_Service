from fastapi import APIRouter, Depends, HTTPException,status
from fastapi_jwt_auth import AuthJWT
from sqlalchemy.orm import Session
from app.database.session import get_database
from jose import JWTError
from app.models.orders import Orders
from app.models.users import Users
from app.schemas.orders_schema import OrderCreate,OrderRead
from app.routers.dependencies import get_current_user
from app.services.order_services import OrderService

order_router = APIRouter(prefix="/api",tags=["orders"])
@order_router.get("/")
async def get_all_orders(authorize: AuthJWT = Depends()):

    try:
        authorize.jwt_required()
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid token",
        )

@order_router.post("/orders", response_model=OrderRead)
async def place_an_order(order:OrderCreate,
                         current_user:Users = Depends(get_current_user),
                         db:Session = Depends(get_database)):
    order_service = OrderService(db)
    new_order = order_service.create_order(current_user, order)
    return new_order


