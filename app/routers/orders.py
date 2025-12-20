from base import Base
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy_utils.types import ChoiceType

class Orders(Base):
    ORDER_STATUS = (
    ("PENDING", "pending"),
    ("IN-TRANSACTION", "in_transaction"),
    ("DELIVERED", "delivered"),
    )

    PIZZA_SIZES = (
    ("SMALL","small"),
    ("MEDIUM","medium"),
    ("LARGE","large"),
    ("EXTERA-LARGE","extera-large"),
    )
    __tablename__ = 'orders'
    id = Column(Integer, primary_key=True)
    quantity = Column(Integer,nullable=False)
    order_status = Column(ChoiceType(choices=ORDER_STATUS),default=ORDER_STATUS[0][0])
    pizza_size = Column(ChoiceType(choices=PIZZA_SIZES),default=PIZZA_SIZES[0][0])
    flavour = Column(String)
    user_id = Column(Integer, ForeignKey("users.id"))
    user = relationship("Users",back_populates="orders")

    def __repr__(self):
        return f"Order Details(id={self.id}, quantity={self.quantity}, order_status={self.order_status})"