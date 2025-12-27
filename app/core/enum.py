from enum import Enum

class PizzaSize(str, Enum):
    small = "small"
    medium = "medium"
    large = "large"
    extra_large = "extra-large"

class OrderStatus(str, Enum):
    pending = "pending"
    in_transaction = "in-transaction"
    delivered = "delivered"
