from fastapi import HTTPException
from sqlalchemy.orm import Session
from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy.sql.functions import current_user
from app.models.orders import Orders
from app.core.enum import OrderStatus
from app.models.users import Users
from app.schemas.orders_schema import OrderCreate, OrderUpdate
from app.models.orders import Orders
from typing import Optional,List
class OrderService:
    def __init__(self, db: Session):
        self.db = db
    def create_order(self, current_user: Users, data: OrderCreate) -> Orders:
        new_order = Orders(
            user_id=current_user.id,
            pizza_size=data.pizza_size,
            quantity=data.quantity,
        )
        self.db.add(new_order)
        self.db.commit()
        self.db.refresh(new_order)
        return new_order

    def get_users_orders(self,user_id:int) -> List[Orders]:
        user_orders = self.db.query(Orders).filter(Orders.user_id == user_id).all()
        return user_orders

    def get_order_by_id(self, order_id : int) -> Optional[Orders]:
        orders_id = self.db.query(Orders).filter(Orders.id == order_id).first()
        return orders_id

    def update_orders_by_user(self,order_id:int,data) -> Orders:
        try:
            order = (
                self.db.query(Orders).with_for_update()
                .filter(Orders.id == order_id)
                .one_or_none()
            )
            if not order:
                raise HTTPException(status_code=404, detail="Order not found")
            if order.order_status not in (OrderStatus.pending):
                raise ValueError("Order cannot be edited at this stage")
            if getattr(data, "quantity", None) is not None:
                order.quantity = data.quantity
            if getattr(data, "pizza_size", None) is not None:
                order.pizza_size = data.pizza_size
            self.db.commit()
            self.db.refresh(order)
            return order
        except SQLAlchemyError:
            self.db.rollback()
            raise

