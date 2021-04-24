from fastapi import APIRouter, Body

from src.configs.routes import ORDER_URL, UPDATE_ORDER_STATUS
from src.models.api_models import PlaceOrderRequestModel, PlaceOrderResponseModel, GetOrderDetailsResponseModel, \
    UpdateOrderStatusRequest
from src.usecases import delice_usecases

router = APIRouter()


@router.post(ORDER_URL)
def place_order(
        body: PlaceOrderRequestModel = Body(...)
) -> PlaceOrderResponseModel:
    return delice_usecases.place_order(body)


@router.get(ORDER_URL)
def get_orders_details() -> GetOrderDetailsResponseModel:
    return delice_usecases.get_order_details()


@router.post(UPDATE_ORDER_STATUS)
def update_order_status(
        body: UpdateOrderStatusRequest = Body(...)
):
    return delice_usecases.update_order_status(body.orderNumbers)

