from enum import Enum, auto

from sqlalchemy import Column
from sqlalchemy import Enum as SqlEnum
from sqlalchemy import ForeignKey, Integer
from sqlalchemy.orm import Session

from .listing import Listing
from .record import Record
from .user import User


class OrderStatus(str, Enum):
    PROCESSING = "processing"
    READY = "ready"
    COLLECTED = "collected"


class Order(Record):
    __tablename__ = "orders"

    user_id = Column(Integer, ForeignKey(User.id), nullable=False)
    listing_id = Column(Integer, ForeignKey(Listing.id), nullable=False)
    status = Column(SqlEnum(OrderStatus), nullable=False)

    @classmethod
    def create(cls, db: Session, **data):
        return super().create(db, status=OrderStatus.PROCESSING, **data)
