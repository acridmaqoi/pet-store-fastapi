from decimal import Decimal
from uuid import UUID

from pydantic import BaseModel


class ListingCreate(BaseModel):
    price: Decimal
    pet_id: UUID


class Listing(BaseModel):
    id: int
    price: Decimal
    pet_id: UUID
