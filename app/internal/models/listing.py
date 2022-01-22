from sqlalchemy import Boolean, Column, ForeignKey, Integer, Numeric
from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm import Session

from .pet import Pet
from .record import Record, RecordNotFound


class Listing(Record):
    __tablename__ = "listings"

    pet_id = Column(Integer, ForeignKey(Pet.id), nullable=False)
    price = Column(Numeric(10, 2), nullable=False)
    sold = Column(Boolean, nullable=False)

    @classmethod
    def create(cls, db: Session, pet_id, **data):
        return super().create(db, sold=False, pet_id=pet_id, **data)

    @classmethod
    def update(cls, db: Session, pet_id, **data):
        return super().update_by_id(db, sold=False, pet_id=pet_id, **data)
