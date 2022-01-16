from datetime import datetime
from typing import Optional

from pydantic import BaseModel

from ..internal.models.pet import Animal, Gender


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
