from pydantic import BaseModel, Integer, String  #pydantic — библиотека для проверки данных
from datetime import datetime


class User(BaseModel):
    email: str
    password: str


class UserCreate(BaseModel):
    id: int
    email: str
    password: str
    created_at: datetime


class UserResponse(BaseModel):
    id: int
    email: str
    password: str
    created_at: datetime


class UserCreate(BaseModel):
    id: int
    email: str
    password: str
    created_at: datetime