from fastapi import APIRouter, Depends, HTTPException, Response, status
from sqlalchemy.orm import Session

from ..internal.database import get_db
from ..internal.models.user import User
from ..schemas import user

router = APIRouter()


@router.post("", response_model=user.User)
def create_user(user: user.UserCreate, db: Session = Depends(get_db)):
    return User.create(db=db, **user.dict())


@router.get("/{user_id}", response_model=user.User)
def get_user(user_id: int, db: Session = Depends(get_db)):
    return User.get_by_id(db=db, id=user_id)


@router.put("/{user_id}", response_model=user.User)
def update_user(
    user_id: int, updated_user: user.UserUpdate, db: Session = Depends(get_db)
):
    return User.update_by_id(db=db, id=user_id, **updated_user.dict())


@router.delete("/{user_id}")
def delete_user(user_id: int, db: Session = Depends(get_db)):
    User.delete_by_id(db=db, user_id=user_id)
    return {"ok": True}
