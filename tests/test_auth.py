from sqlalchemy import insert, select

from conftest import client, async_session_maker
from src.tasks.models import Task


def test_register():
    response = client.post("/auth/register", json={
        "email": "string",
        "password": "nm2221723456",
        "is_active": True,
        "is_superuser": False,
        "is_verify": True,
        "username": "nazim"
    })

    assert response.status_code == 201


# def test_register_used_email():
#     response = client.post("/auth/register", json={
#         "email": "string",
#         "password": "nm2221723456",
#         "is_active": True,
#         "is_superuser": False,
#         "is_verify": True,
#         "username": "nazim"
#     })
#
#     assert response.status_code == 201


# async def test_task_create():
#     async with async_session_maker() as session:
#         stmt = insert(Task).values(
#             id=1,
#             title="test",
#             description="aaaa",
#             user_id=1
#         )
#     await session.execute(stmt)
#     await session.commit()
#
#     query = select(Task)
#     result = await session.execute(query)
#     assert result.mapping().all() == [(1, "test", "aaaa", 1, False)]
