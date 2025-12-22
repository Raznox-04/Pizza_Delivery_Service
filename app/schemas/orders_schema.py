from pydantic import BaseModel, Field
from typing import Optional
from app.core.enum import PizzaSize, OrderStatus

class OrderCreate(BaseModel):
    quantity: int
    pizza_size: PizzaSize

    class Config:
        schema_extra = {"example": {"quantity": 2, "pizza_size": "medium"}}

class OrderRead(BaseModel):
    id: int
    user_id: int
    quantity: int
    pizza_size: PizzaSize
    order_status: OrderStatus

    class Config:
        orm_mode = True

