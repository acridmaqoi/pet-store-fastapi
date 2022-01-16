import bcrypt
from sqlalchemy.orm import Session

from ..schemas import user
from .models.user import User


def get_user(db: Session, user_id: int):
    return db.query(User).filter(User.id == user_id).first()


def create_user(db: Session, user: user.UserCreate):
    hashed_password = bcrypt.hashpw(user.password, bcrypt.gensalt(8))
    db_user = User(
        username=user.username,
        hashed_password=hashed_password,
        email=user.email,
        name=user.name,
    )
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user


def delete_user(db: Session, user_id: int):
    db_user = db.query(User).filter(User.id == user_id).first()
    db.delete(db_user)
    db.commit()