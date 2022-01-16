from sqlalchemy import Column, String, Integer, DateTime, Enum as sqlEnum
from base import Base

from datetime import datetime
from enum import Enum


class Gender(Enum):
    MALE = 1
    FEMALE = 2


class Animal(Enum):
    CAT = 1
    DOG = 2


class Pet(Base):
    __tablename__ = "pet"

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    animal = Column(sqlEnum(Animal), nullable=False)
    gender = Column(sqlEnum(Gender))
    born = Column(DateTime, default=datetime.utcnow)
