from datetime import date, datetime

from fastapi import APIRouter, Depends, HTTPException, Response, status
from sqlalchemy.orm import Session

from ..internal.database import get_db
from ..internal.models.pet import Pet
from ..schemas import pet

router = APIRouter()


@router.post("", response_model=pet.Pet)
def create_pet(pet: pet.PetCreate, db: Session = Depends(get_db)):
    return Pet.create(db=db, **pet.dict())


@router.get("/{pet_id}", response_model=pet.Pet)
def get_pet(pet_id: int, db: Session = Depends(get_db)):
    db_pet = Pet.get_by_id(db=db, id=pet_id)
    if db_pet is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)
    return db_pet


@router.put("/{pet_id}")
def update_pet(pet_id: int, pet: pet.PetCreate, db: Session = Depends(get_db)):
    db_pet = Pet.get_by_id(db=db, id=pet_id)
    if db_pet is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)
    return Pet.update_by_id(db=db, id=pet_id, **pet.dict())


@router.delete("/{pet_id}")
def delete_pet(pet_id: int, db: Session = Depends(get_db)):
    db_pet = Pet.get_by_id(db=db, id=pet_id)
    if db_pet is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)
    Pet.delete_by_id(db=db, id=db_pet.id)
    return Response(status_code=status.HTTP_204_NO_CONTENT)
