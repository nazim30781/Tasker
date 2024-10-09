from datetime import datetime

from sqlalchemy import Column, Integer, String, Boolean, TIMESTAMP

from src.database import Base


class User(Base):
    __tablename__ = "users"

    id: int = Column(Integer, primary_key=True)
    username: str = Column(String, nullable=False, unique=True)
    email: str = Column(String, nullable=False, unique=False)
    password: str = Column(String, nullable=False)
    is_verified: bool = Column(Boolean, default=False)
    created_at: datetime = Column(TIMESTAMP, default=datetime.now)

    def __repr__(self):
        return f"<User {self.username}>"
