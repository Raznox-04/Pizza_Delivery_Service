from app.database.base import Base
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy import Enum as SAEnum
from app.core.enum import OrderStatus,PizzaSize
from sqlalchemy.orm import relationship
class Orders(Base):

    __tablename__ = 'orders'
    id = Column(Integer, primary_key=True)
    quantity = Column(Integer,nullable=False)
    order_status = Column(SAEnum(OrderStatus,name="order_status"),default=OrderStatus.pending,nullable=False)
    pizza_size = Column(SAEnum(PizzaSize,name="pizza_size"),nullable=False)
    flavour = Column(String,nullable=True)
    user_id = Column(Integer, ForeignKey("users.id"))
    user = relationship("Users",back_populates="orders")



    def __repr__(self):
        return f"Order Details(id={self.id}, quantity={self.quantity}, order_status={self.order_status})"