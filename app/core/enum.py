from enum import Enum
from typing import List

class PizzaSize(List[str], Enum):
    small = ["small","SMALL"]
    large = ["large","LARGE"]
    medium = ["medium","MEDIUM"]
    extera_large = ["extera-large","EXTERA-LARGE"]


class OrderStatus(List[str], Enum):
    pending = ["pending","PENDING"]
    in_transaction = ["in_transaction","IN-TRANSACTION"]
    delivered = ["delivered","DELIVERED"]
