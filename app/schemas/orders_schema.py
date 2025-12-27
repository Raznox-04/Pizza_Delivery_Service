from pydantic import BaseModel
from app.core.enum import OrderStatus,PizzaSize
class OrderCreate(BaseModel):
    quantity: int
    pizza_size: PizzaSize

    class Config:
        json_schema_extra = {"example":
                            {
                                "quantity": 2, "pizza_size": "medium"
                            }
                        }

class OrderRead(BaseModel):
    id: int
    user_id: int
    quantity: int
    pizza_size : PizzaSize
    order_status : OrderStatus

    class Config:
        from_attributes = True

