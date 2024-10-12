from datetime import datetime
from typing import Optional

from pydantic import BaseModel


class ReminderCreate(BaseModel):
    title: str
    description: str
    time: Optional[datetime] = datetime.now()
    user_id: Optional[int] = None
