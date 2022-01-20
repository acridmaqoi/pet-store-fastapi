from sqlalchemy import Column
from sqlalchemy.orm import Session
from sqlalchemy.sql import func
from sqlalchemy.types import DateTime, Integer

from ..database import Base


class Record(Base):
    __abstract__ = True

    id = Column(Integer, primary_key=True)
    time_created = Column(DateTime, server_default=func.now())
    time_updated = Column(DateTime, server_onupdate=func.now())

    @classmethod
    def create(cls, db: Session, **data):
        record = cls(**data)
        db.add(record)
        db.commit()
        db.refresh(record)
        return record

    @classmethod
    def get_by_id(cls, db: Session, id: int):
        return db.query(cls).filter(cls.id == id).first()

    @classmethod
    def get_all(cls, db: Session):
        return db.query(cls).all()

    @classmethod
    def update_by_id(cls, db: Session, id: int, **data):
        record = cls.get_by_id(db, id)
        for key, value in data.items():
            setattr(record, key, value)
        db.add(record)
        db.commit()
        db.refresh(record)
        return record

    @classmethod
    def delete_by_id(cls, db: Session, id: int):
        db.query(cls).filter(cls.id == id).delete()
