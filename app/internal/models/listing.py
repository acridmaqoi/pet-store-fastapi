from sqlalchemy import Boolean, Column, ForeignKey, Integer, Numeric
from sqlalchemy.orm import Session

from .pet import Pet
from .record import Record


class Listing(Record):
    __tablename__ = "listings"

    pet_id = Column(Integer, ForeignKey(Pet.id), nullable=False)
    price = Column(Numeric(10, 2), nullable=False)
    sold = Column(Boolean, nullable=False)

    @classmethod
    def create(cls, db: Session, **data):
        return super().create(db, sold=False, **data)
