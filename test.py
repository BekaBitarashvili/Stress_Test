import time
import random
import string
from locust import HttpUser, task, between


class MyUser(HttpUser):
    wait_time = between(1, 1)
    session_key = ''.join(random.choices(string.ascii_uppercase + string.digits, k=32))
    host = "http://10.117.27.38:8000"

    @task
    def login_user(self):
        payload = {
            "account_id": "156507",
            "session_key": self.session_key,
            "phone": "599****62"
        }
        headers = {
            "Content-Type": "application/json"
        }
        response = self.client.post("/api/login", json=payload, headers=headers)
        print(f"{self.login_user.__name__} - {response.status_code}")
