from pydantic import BaseModel
from datetime import datetime


class HabitCreate(BaseModel):
    title: str
    description: str


class HabitResponse(BaseModel):
    id: int
    title: str
    description: str
    created_at: datetime
    user_id: int


class HabitUpdate(BaseModel):
    title: str
    description: str
