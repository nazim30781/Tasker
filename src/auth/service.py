from sqlalchemy import select, insert

from .models import User
from .schemas import UserCreateModel
from .utils import generate_passwd_hash, verify_password

from sqlalchemy.ext.asyncio.session import AsyncSession


class UserService:
    async def get_user_by_email(self, email: str, session: AsyncSession):
        query = select(User).where(User.email == email)

        result = await session.execute(query)
        user = result.first()

        return user

    async def user_exists(self, email: str, session: AsyncSession):
        user = await self.get_user_by_email(email, session)

        return True if user is not None else False

    async def create_user(self, user_data: UserCreateModel, session: AsyncSession):

        user_data_dict = user_data.model_dump()
        new_user = User(**user_data_dict)
        print(user_data_dict['password'])
        new_user.password = generate_passwd_hash(user_data_dict['password'])
        print(new_user.password)

        session.add(new_user)
        await session.commit()

        return new_user
