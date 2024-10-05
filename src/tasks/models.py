from sqlalchemy import Column, Integer, String, TIMESTAMP, ForeignKey, Boolean
from sqlalchemy.orm import DeclarativeBase, Mapped, relationship

from src.database import metadata, Base


class Task(Base):
    __tablename__ = "tasks"
    id: int = Column(Integer, primary_key=True)
    title: str = Column(String, nullable=False)
    description: str = Column(String, nullable=True)
    user_id: int = Column(Integer, ForeignKey("user.id"))
    is_done: bool = Column(Boolean, default=False)

