from datetime import timedelta
from fastapi import APIRouter, Depends
from sqlalchemy import insert, select
from sqlalchemy.ext.asyncio import AsyncSession

from ..auth.dependencies import AccessTokenBearer
from .schemas import ReminderCreate
from .models import Reminder
from .service import ReminderService
from ..database import get_async_session
from ..logger import logger
from ..celery_tasks.tasks import send_email

access_toke_bearer = AccessTokenBearer()

router = APIRouter(
    prefix="/reminders",
    tags=["Reminder"]
)

@router.get("/getAllRemiders")
async def get_all_reminders(user_details = Depends(access_toke_bearer), 
                            session: AsyncSession = Depends(get_async_session)):
    user_id = ReminderService.get_user_id(user_details)

    query = select(Reminder).where(Reminder.user_id == user_id)
    response = await session.execute(query)
    response = response.all()[0][0]

    logger.info(response.__dict__)

    return response


@router.post("/createReminder")
async def create_reminder(reminder_data: ReminderCreate,
                           user_details = Depends(access_toke_bearer),
                           session: AsyncSession = Depends(get_async_session)):
    user_id = ReminderService.get_user_id(user_details)

    reminder_data = reminder_data.model_dump()
    reminder_data['user_id'] = user_id

    send_email.apply_async(eta=reminder_data['time'])
    # send_email("toptikitok2@gmail.com")

    logger.info(reminder_data)

    stmt = insert(Reminder).values(**reminder_data)

    response = await session.execute(stmt)
    await session.commit()

    return response
