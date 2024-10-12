from typing import Optional
from pydantic import BaseModel


class TaskCreate(BaseModel):
    title: str
    description: str
    user_id: Optional[int] = None


class TaskRead(BaseModel):
    title: str
    description: str
    is_done: bool
