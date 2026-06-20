from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy.orm import declarative_base
from datetime import datetime, timezone

Base = declarative_base()  # спецкласс от к будут наслед таблицы(sqlalchemy).
# связывает классы пайтон с таблицами БД


class User(Base):  # наследует инструкции от Base
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    email = Column(String, unique=True)
    hashed_password = Column(String)
    created_at = Column(
        DateTime,
        default=lambda: datetime.now(timezone.utc)
    )
