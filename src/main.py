from fastapi import FastAPI

from .auth.router import router as router_auth
from .tasks.router import router as router_tasks
from .reminders.router import router as router_reminders

from redis import asyncio as aioredis

app = FastAPI()

app.include_router(router_auth)
app.include_router(router_tasks)
app.include_router(router_reminders)

# @app.on_event("startup")
# async def startup_event():
#     redis = aioredis.from_url("redis://localhost", encoding="utf8", decode_response=True)
