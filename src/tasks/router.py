from fastapi import APIRouter, Depends
from sqlalchemy import insert, select, update
from sqlalchemy.ext.asyncio import AsyncSession

from src.auth.utils import decode_token
from src.database import get_async_session
from .service import TasksService
from .models import Task
from .schemas import TaskCreate
from ..auth.models import User
from ..auth.dependencies import AccessTokenBearer
from ..logger import logger

access_toke_bearer = AccessTokenBearer()

router = APIRouter(
    prefix="/tasks",
    tags=["Task"]
)


@router.get("/getAllTasks")
async def get_all_tasks(user_details = Depends(access_toke_bearer), 
                        session: AsyncSession = Depends(get_async_session)):

    user_id = TasksService.get_user_id(user_details)

    query = select(Task).filter(
        Task.user_id == user_id,
        Task.is_done == False
    )

    response = await session.execute(query)

    response = response.all()[0][0]

    logger.info(response.__dict__)

    return response
    


@router.post("/createTask")
async def create_task(new_task: TaskCreate, 
                      user_details = Depends(access_toke_bearer),
                      session: AsyncSession = Depends(get_async_session)):
    
    user_id = TasksService.get_user_id(user_details)
    
    task_data = dict(new_task)
    task_data['user_id'] = user_id

    logger.info(task_data)

    stmt = insert(Task).values(**task_data)
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
