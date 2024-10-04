from pydantic import BaseModel


class Task(BaseModel):
    id: int
    title: str
    description: str
    user_id: int
    is_done: bool