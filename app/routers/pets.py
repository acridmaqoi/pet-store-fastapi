from enum import Enum
from datetime import date, datetime

from fastapi import APIRouter
from pydantic import BaseModel


class Gender(Enum):
    MALE = "male"
    FEMALE = "female"


class Animal(Enum):
    CAT = "cat"
    DOG = "dog"


class Pet(BaseModel):
    name: str
    animal: Animal
    gender: Gender
    born: datetime


router = APIRouter()


@router.get("/{pet_id}")
async def get_pet(pet_id: int):
    pass


@router.post("")
async def add_pet(pet: Pet):
    pass


@router.put("/{pet_id}")
async def update_pet(pet_id: int, pet: Pet):
    pass
