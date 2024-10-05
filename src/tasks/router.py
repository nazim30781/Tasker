from fastapi import APIRouter, Depends
from sqlalchemy import insert, select, update
from sqlalchemy.ext.asyncio import AsyncSession

from .schemas import TaskCreate
from src.tasks.models import Task

from src.database import get_async_session
from ..auth.models import User

router = APIRouter(
    prefix="/tasks",
    tags=["Task"]
)


@router.get("/getAllTasks")
async def get_all_tasks(user_id: int, session: AsyncSession = Depends(get_async_session)):
    query = select(User).where(Task.user_id == user_id)
    result = await session.execute(query)
    return result.mappings().all()


@router.post("/createTask")
async def create_task(new_task: TaskCreate, session: AsyncSession = Depends(get_async_session)):
    stmt = insert(Task).values(**new_task.dict())
    await session.execute(stmt)
    await session.commit()
    return {"status": "success"}


@router.get("/getUnfulfilledTasks")
async def get_unfulfilled_tasks(user_id: int, session: AsyncSession = Depends(get_async_session)):
    query = select(Task).filter(Task.user_id == user_id, Task.is_done == False)
    result = await session.execute(query)
    return result.mappings().all()


@router.get("/CheckTask")
async def check_task(task_id: int, session: AsyncSession = Depends(get_async_session)):
    query = (
        update(Task)
        .values(is_done=True)
        .filter(Task.id == task_id)
    )

    await session.execute(query)
    await session.commit()
    return "gg"

