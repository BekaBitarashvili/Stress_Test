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
            "username": "testSaxeli13",
            "password": "Zvikilo13!"
        }
        headers = {
            "Content-Type": "application/json",
            "session-key": self.session_key
        }
        response = self.client.post("/api/login", json=payload, headers=headers)
        print(f"{self.login_user.__name__} - {response.status_code}")

    @task
    def authenticate(self):
        payload = {
            "otp": "1234"
        }
        headers = {
            "Content-Type": "application/json",
            "session-key": self.session_key
        }
        response = self.client.post("/api/authenticate", json=payload, headers=headers)
        for _ in range(1):
            if response.status_code == 200:
                break
        print(f"{self.authenticate.__name__} - {response.status_code}")