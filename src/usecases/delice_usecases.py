import json
from datetime import datetime
from typing import List

from src.configs.constants import ORDER_FILE_PATH, ORDERS
from src.entities.order_entities import OrderDetails, OrderStatus
from src.models.api_models import PlaceOrderRequestModel, PlaceOrderResponseModel


def get_order_details() -> List[OrderDetails]:
    with open(ORDER_FILE_PATH) as f:
        order_details = json.loads(f.read())
    if ORDERS not in order_details:
        return []

    orders = []
    update_orders = []
    for order in order_details.get(ORDERS):
        if order['status'] == OrderStatus.INITIATED:
            orders.append(order)
            order['status'] = OrderStatus.IN_PROCESS
        update_orders.append(order)

    _update_orders(update_orders)
    return orders


def update_order_status(orders: List[int]):
    with open(ORDER_FILE_PATH) as f:
        order_details = json.loads(f.read())
    update_orders = []
    for order in order_details.get(ORDERS):
        if order.get("orderNumber") in orders:
            order['status'] = OrderStatus.COMPLETED
        update_orders.append(order)
    _update_orders(update_orders)
    return "Success"


def place_order(order_request: PlaceOrderRequestModel) -> PlaceOrderResponseModel:
    order_number = _save_order_requests(order_request)
    return PlaceOrderResponseModel(orderNumber=order_number)


def _save_order_requests(order_request: PlaceOrderRequestModel) -> int:
    order_number = _get_order_number()
    with open(ORDER_FILE_PATH) as f:
        order_details = json.loads(f.read())
    orders = order_details.get("orders") if "orders" in order_details else []
    orders.append(OrderDetails(orderNumber=order_number,
                               datestamp=str(datetime.now()),
                               item=order_request.item,
                               toppings=order_request.toppings,
                               status=OrderStatus.INITIATED).dict())
    _update_orders(orders)
    # order_details["orders"] = orders
    # with open(ORDER_FILE_PATH, 'w') as f:
    #     json.dump(order_details, f)
    return order_number


def _get_order_number() -> int:
    with open(ORDER_FILE_PATH) as f:
        order_details = json.loads(f.read())
    if not order_details:
        return 1
    return len(order_details.get(ORDERS)) + 1


# update order status in file
def _update_orders(update_orders):
    with open(ORDER_FILE_PATH) as f:
        order_details = json.loads(f.read())

    order_details["orders"] = update_orders
    with open(ORDER_FILE_PATH, 'w') as f:
        json.dump(order_details, f)
