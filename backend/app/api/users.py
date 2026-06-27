from fastapi import APIRouter
from app.schemas.user import UserCreate, UserResponse, UserUpdate


router = APIRouter()  # группировка роутеров для пользователей (контейнер)

@router.post('/users', response_model=UserResponse)
def create_user(user: UserCreate):  # создание новых пользователей
    return {
        'id': 1,
        'email': user.email,
        'created_at': '2026-01-01T00:00:00Z'
    }

@router.get('/'users/{user_id}', responce_model=UserResponse)
def get_user(user_id: int):  #получи user_id из URL
    return {
        'id': user_id,
        'email': 'test@emample.com',
        'created_at': '2026-01-01T00:00:00Z'
    }

@router.put('/users/{user_id}', response_model=UserResponse) # замена существующего
def update_user(user_id: int, user: UserUpdate):
    return {
        'id': user_id,
        'email': user.email,
        'created_at': '2026-01-01T00:00:00Z'
    }
