from conftest import client, headers
from logger import logger


def test_register():
    response = client.post("/auth/signup", json={
        "username": "nazim",
        "email": "nazim30781@gmail.com",
        "password": "nm222173456"
    })


def test_login():
    response = client.post("/auth/login", json={
        "email": "nazim30781@gmail.com",
        "password": "nm222173456"
    })

    logger.info(response)

    assert response.status_code == 200


def test_access_token():
    response = client.get("/auth/test", headers=headers)

    print("_________________________________________________")
    print(response)

    assert response.status_code == 200
