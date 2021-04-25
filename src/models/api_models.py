from typing import Optional, List

from pydantic import BaseModel

from src.entities.order_entities import Item, Toppings, OrderDetails


class OrderDetailsRequestModel(BaseModel):
    item: Item
    toppings: Optional[List[Toppings]]


class PlaceOrderRequestModel(BaseModel):
    orders: Optional[List[OrderDetailsRequestModel]]


class PlaceOrderResponseModel(BaseModel):
    orderNumber: int


class GetOrderDetailsResponseModel(BaseModel):
    orders: Optional[List[OrderDetails]]


class UpdateOrderStatusRequest(BaseModel):
    orderNumbers: List[int]

