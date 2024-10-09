from datetime import timedelta

from fastapi import APIRouter, Depends
from fastapi.responses import JSONResponse

from sqlalchemy.ext.asyncio import AsyncSession

from .schemas import UserCreateModel, UserLoginModel
from .service import UserService

from .utils import verify_password, create_access_token
from .dependencies import AccessTokenBearer

from ..database import get_async_session

router = APIRouter(
    prefix="/auth",
    tags=["Auth"]
)

user_service = UserService()

REFRESH_TOKEN_EXPIRY = 2
access_token_bearer = AccessTokenBearer()


@router.post("/signup")
async def create_user_account(user_data: UserCreateModel, 
                              session: AsyncSession = Depends(get_async_session)):
    email = user_data.email

    user_exists = await user_service.user_exists(email, session)

    if user_exists:
        raise 'Error'

    new_user = await user_service.create_user(user_data, session)

    return new_user


@router.post('/login')
async def login_user(login_data: UserLoginModel, 
                     session: AsyncSession = Depends(get_async_session)):
    email = login_data.email
    password = login_data.password

    user = await user_service.get_user_by_email(email, session)
    user = user[0]

    if user is not None:
        password_valid = verify_password(password, user.password)

        if password_valid:
            access_token = create_access_token(
                user_data={
                    'email': user.email,
                    'id': user.id
                }
            )

            refresh_token = create_access_token(
                user_data={
                    'email': user.email,
                    'id': user.id
                },
                refresh=True,
                expiry=timedelta(days=REFRESH_TOKEN_EXPIRY)
            )

            return JSONResponse(
                content={
                    "message": "Login successful",
                    "access_token": access_token,
                    "refresh_token": refresh_token,
                    "user": {
                        "email": user.email,
                        "id": str(user.id)
                    }
                }
            )

    raise "error"


@router.get("/test")
async def test(user_details=Depends(access_token_bearer)):
    print(user_details)

    return user_details

