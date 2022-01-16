from typing import Optional
from datetime import datetime
from enum import Enum

from pydantic import BaseModel

from .models import Gender, Animal


class PetCreate(BaseModel):
    name: str
    animal: Animal
    gender: Gender
    born: Optional[datetime]


class Pet(BaseModel):
    id: int
    name: str
    animal: Animal
    gender: Gender
    born: Optional[datetime]

    class Config:
        orm_mode = True
