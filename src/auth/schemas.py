from pydantic import BaseModel, Field


class UserCreateModel(BaseModel):
    username: str
    email: str
    password: str = Field(min_length=8)


class UserLoginModel(BaseModel):
    email: str
    password: str
