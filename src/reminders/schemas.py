from datetime import datetime

from pydantic import BaseModel


class ReminderCreate(BaseModel):
    title: str
    description: str
    time: datetime
    user_id: int
