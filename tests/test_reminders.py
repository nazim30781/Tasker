from conftest import headers, client

from datetime import datetime, timedelta

def test_create_reminder():
    reminder_data = {
        "title": "test_reminder",
        "description": "test_reminder",
        "time": (datetime.utcnow() + timedelta(minutes=1)).isoformat()
    }

    response = client.post("reminders/createReminder",
                headers=headers,
                json=reminder_data)
    print(response)
    
    assert response.status_code == 200
