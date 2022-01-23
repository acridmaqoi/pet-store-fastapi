from enum import Enum

from sqlalchemy import Column, DateTime
from sqlalchemy import Enum as sqlEnum
from sqlalchemy import Integer, String
from sqlalchemy.orm import backref, relationship

from ..database import Base
from .record import Record


class Gender(str, Enum):
    MALE = "male"
    FEMALE = "female"


class Animal(str, Enum):
    CAT = "cat"
    DOG = "dog"


class Pet(Record):
    __tablename__ = "pets"

    name = Column(String, nullable=False)
    animal = Column(sqlEnum(Animal), nullable=False)
    gender = Column(sqlEnum(Gender))
    born = Column(DateTime)
    listings = relationship(
        "Listing", cascade="all,delete", backref=backref("pet", uselist=False)
    )
