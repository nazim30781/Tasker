from conftest import client


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
    assert response.status_code == 200


def test_access_token():
    headers = {
        "Authorization": "Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VyIjp7ImVtYWlsIjoibmF6aW0zMDc4MUBnbWFpbC5jb20iLCJpZCI6MX0sImV4cCI6MTcyODQ5NTUxOSwicmVmcmVzaCI6ZmFsc2V9.9Zoo8vbELPv91kWJmQQir57D6T3B8QIuHstYAwjO3TE"
    }

    response = client.get("/auth/test", headers=headers)

    print("_________________________________________________")
    print(response)

    assert response.status_code == 200
