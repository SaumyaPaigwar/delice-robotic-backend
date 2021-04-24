from enum import Enum
from typing import List, Optional

from pydantic import BaseModel


class OrderStatus(str, Enum):
    INITIATED = "INITIATED"
    IN_PROCESS = "IN_PROCESS"
    COMPLETED = "COMPLETED"


class Toppings(BaseModel):
    toppingName: str
    toppingPrice: float


class Item(BaseModel):
    itemName: str
    itemPrice: float


class OrderDetails(BaseModel):
    orderNumber: int
    datestamp: str
    item: Item
    toppings: Optional[List[Toppings]]
    status: OrderStatus
