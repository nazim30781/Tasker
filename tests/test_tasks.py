from conftest import client, headers

from src.tasks.schemas import TaskCreate

def test_create_task():
    data = {
        "title": "test",
        "description": "test",
    }

    response = client.post("/tasks/createTask", json=data, headers=headers)

    assert response.status_code == 200

def test_get_all_tasks():
    response = client.get("/tasks/getAllTasks", headers=headers)

    assert response.status_code == 200
