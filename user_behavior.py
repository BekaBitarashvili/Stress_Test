import time
import random
import string
from _winapi import NULL

from locust import HttpUser, between, task, TaskSet, constant, RateLimiter


class User1(HttpUser):
    wait_time = between(5, 10, lambda: random.uniform(5, 10))
    host = "http://10.117.27.38:8000"
    session_key = "F014373B-C969-45C4-9B2D-BB1336C845B6"

    rate_limiter = RateLimiter(3)

    @task(weight=2)
    def login_user(self):
        payload = {
            "account_id": "156507",
            "session_key": "F24141E3-D32A-40CB-BD21-779B24C5069E",
            "phone": "599****62"
        }
        headers = {
            "Content-Type": "application/json"
        }
        response = self.client.post("/api/login", json=payload, headers=headers)
        print(f"{self.login_user.__name__} - {response.status_code}")

    @task(weight=1)
    def reset_password(self):
        payload = {
            "account_id": "90492",
            "session_key": "2A8BDCCD-F7E9-42A9-BA52-FDCB14530214",
            "phone": "599****03"
        }
        headers = {
            "Content-Type": "application/json"
        }
        response = self.client.post("/api/reset_password", json=payload, headers=headers)
        print(f"{self.reset_password.__name__} - {response.status_code}")

    @task
    def update_password(self):
        payload = {
            "password": "Dato1234",
            "re_enter_password": "Dato1234"
        }
        headers = {
            "Content-Type": "application/json",
            "session-key": self.session_key
        }
        response = self.client.post("/api/update_password", json=payload, headers=headers)
        print(f"{self.update_password.__name__} - {response.status_code} - {self.session_key}")

    @task
    def check_customer(self):
        payload = {
            "clientStatus": 1,
            "customer": None,
        }
        headers = {
            "Content-Type": "application/json"
        }
        response = self.client.post("/api/check_customer", json=payload, headers=headers)
        print(f"{self.check_customer.__name__} - {response.status_code}")

    @task
    def create_account(self):
        payload = {
            "message": "The lang field is required. (and 1 more error)",
            "errors": {
                "lang": [
                    "The lang field is required."
                ],
                "client_status": [
                    "The client status field is required."
                ]
            }
        }
        headers = {
            "Content-Type": "application/json"
        }
        response = self.client.post(url="/api/create_account", json=payload, headers=headers)
        print(f"{self.create_account.__name__} - {response.status_code}")
