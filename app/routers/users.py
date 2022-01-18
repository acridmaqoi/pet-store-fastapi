from fastapi import APIRouter, Depends, HTTPException, Response, status
from sqlalchemy.orm import Session

from ..internal import user_utils
from ..internal.database import get_db
from ..schemas import user

router = APIRouter()


@router.post("", response_model=user.User)
def create_user(user: user.UserCreate, db: Session = Depends(get_db)):
    return user_utils.create_user(db=db, user=user)


@router.get("/{user_id}", response_model=user.User)
def get_user(user_id: int, db: Session = Depends(get_db)):
    user = user_utils.get_user(db=db, user_id=user_id)
    if user is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)
    return user


@router.put("/{user_id}", response_model=user.User)
def update_user(
    user_id: int, updated_user: user.UserUpdate, db: Session = Depends(get_db)
):
    user = user_utils.get_user(db=db, user_id=user_id)
    if user is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)
    return user_utils.update_user(db=db, user_id=user_id, user=updated_user)


@router.delete("/{user_id}")
def delete_user(user_id: int, db: Session = Depends(get_db)):
    user = user_utils.get_user(db=db, user_id=user_id)
    if user is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)
    user_utils.delete_user(db=db, user_id=user_id)
    return Response(status_code=status.HTTP_204_NO_CONTENT)
