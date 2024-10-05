from datetime import datetime

from sqlalchemy import Column, Integer, String, TIMESTAMP, Boolean, ForeignKey

from src.database import Base


class Reminder(Base):
    id: int = Column(Integer, primary_key=True)
    title: str = Column(String, nullable=False)
    description: str = Column(String, nullable=True)
    time: datetime = Column(TIMESTAMP, nullable=False)
    is_done: bool = Column(Boolean, default=False)
    user_id: int = Column(Integer, ForeignKey("user.id"))
