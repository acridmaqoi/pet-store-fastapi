from enum import Enum

from pydantic import BaseModel

from ..internal.models.order import OrderStatus


class OrderCreate(BaseModel):
    user_id: int
    listing_id: int


class Order(BaseModel):
    id: int
    user_id: int
    listing_id: int
    status: OrderStatus

    class Config:
        orm_mode = True
