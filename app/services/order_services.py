from sqlalchemy.orm import Session
from app.models.orders import Orders
from app.models.users import Users
from app.schemas.orders_schema import OrderCreate
from app.models.orders import Orders
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
