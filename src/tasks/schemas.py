from pydantic import BaseModel


class TaskCreate(BaseModel):
    title: str
    description: str
    user_id: int


class TaskRead(BaseModel):
    title: str
    description: str
    is_done: bool
