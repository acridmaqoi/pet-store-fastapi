from sqlalchemy import Column, Integer, String

from ..database import Base
from .record import Record


class User(Record):
    __tablename__ = "users"

    username = Column(String, nullable=False)
    hashed_password = Column(String, nullable=False)
    email = Column(String, nullable=False)
    name = Column(String, nullable=False)
