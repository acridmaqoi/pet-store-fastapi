from sqlalchemy import Boolean, Column, Integer, Numeric

from .pet import Pet
from .record import Record


class Listing(Record):
    __tablename__ = "listings"

    price = Column(Numeric(10, 2), nullable=False)
    sold = Column(Boolean, nullable=False)
    pet = Column(Pet, nullable=False)
