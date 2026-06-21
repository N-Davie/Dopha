from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
from sqlalchemy.orm import declarative_base
from datetime import datetime, timezone

Base = declarative_base()


class Habit(Base):
    __tablename__ = 'habits'

    id = Column(Integer, primary_key=True)
    title = Column(String)
    description = Column(String(255))
    created_at = Column(
        DateTime,
        default=lambda: datetime.now(timezone.utc)
    )
    user_id = Column(Integer, ForeignKey('users.id'))
