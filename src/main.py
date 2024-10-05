from fastapi import FastAPI

from src.auth.base_config import auth_backend, fastapi_users
from src.auth.schemes import UserRead, UserCreate
from src.tasks.router import router as router_tasks

app = FastAPI()

app.include_router(
    fastapi_users.get_auth_router(auth_backend),
    prefix="/auth/jwt",
    tags=["auth"],
)

app.include_router(
    fastapi_users.get_register_router(UserRead, UserCreate),
    prefix="/auth",
    tags=["auth"],
)

app.include_router(router_tasks)
