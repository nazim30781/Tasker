from conftest import client

def test_get_all_tasks():
    headers = {
        "Authorization": "Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VyIjp7ImVtYWlsIjoibmF6aW0zMDc4MUBnbWFpbC5jb20iLCJpZCI6MX0sImV4cCI6MTcyODQ5NTUxOSwicmVmcmVzaCI6ZmFsc2V9.9Zoo8vbELPv91kWJmQQir57D6T3B8QIuHstYAwjO3TE"
    }

    response = client.get("/tasks/getAllTasks", headers=headers)


    assert response.status_code == 200