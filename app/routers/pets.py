from datetime import date, datetime

from fastapi import APIRouter, Depends, HTTPException, Response, status
from sqlalchemy.orm import Session

from ..internal import pet_utils
from ..internal.database import get_db
from ..schemas import pet

router = APIRouter()


@router.post("")
def create_pet(pet: pet.PetCreate, db: Session = Depends(get_db)):
    return pet_utils.create_pet(db=db, pet=pet)


@router.get("/{pet_id}", response_model=pet.Pet)
def get_pet(pet_id: int, db: Session = Depends(get_db)):
    db_pet = pet_utils.get_pet(db=db, pet_id=pet_id)
    if db_pet is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)
    return db_pet


@router.put("/{pet_id}")
def update_pet(pet_id: int, pet: pet.PetCreate, db: Session = Depends(get_db)):
    db_pet = pet_utils.get_pet(db=db, pet_id=pet_id)
    if db_pet is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)
    return pet_utils.update_pet(db=db, pet_id=pet_id, pet=pet)


@router.delete("/{pet_id}")
def delete_pet(pet_id: int, db: Session = Depends(get_db)):
    db_pet = pet_utils.get_pet(db=db, pet_id=pet_id)
    if db_pet is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)
    pet_utils.delete_pet(db=db, pet_id=pet_id)
    return Response(status_code=status.HTTP_204_NO_CONTENT)
