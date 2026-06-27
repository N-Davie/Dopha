from fastapi import APIRouter
from app.schemas.habit import HabitCreate, HabitResponse, HabitUpdate

router = APIRouter()

@router.post('/habits', response_model=HabitResponse)
def create_habit(habit: HabitCreate):
    pass

@router.get('/habits/{habit_id}', response_model=HabitResponse)
def get_habit(habit_id: int):
    pass

@router.put('/habits/{habit_id}', response_model=HabitResponse)
def update_habit(habit_id: int, habit: HabitUpdate):
    pass
