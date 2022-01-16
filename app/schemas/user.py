import string

from pydantic import BaseModel


class UserBase(BaseModel):
    username: str
    email: str
    name: str


class UserCreate(UserBase):
    password: string


class User(UserBase):
    id: int

    class Config:
        orm_mode = True
