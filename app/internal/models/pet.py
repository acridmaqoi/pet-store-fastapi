from enum import Enum

from sqlalchemy import Column, DateTime
from sqlalchemy import Enum as sqlEnum
from sqlalchemy import Integer, String

from ..database import Base
from .record import Record


class Gender(Enum):
    MALE = "male"
    FEMALE = "female"


class Animal(Enum):
    CAT = "cat"
    DOG = "dog"


class Pet(Record):
    __tablename__ = "pets"

    name = Column(String, nullable=False)
    animal = Column(sqlEnum(Animal), nullable=False)
    gender = Column(sqlEnum(Gender))
    born = Column(DateTime)
