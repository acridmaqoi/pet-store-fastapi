from typing import Optional

from pydantic import BaseModel


class UserBase(BaseModel):
    username: str
    email: str
    name: str


class UserCreate(UserBase):
    password: str


class UserUpdate(UserBase):
    password: Optional[str]


class User(UserBase):
    id: int

    class Config:
        orm_mode = True
