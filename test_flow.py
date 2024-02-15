import time
import random
import string
from locust import HttpUser, between, task, TaskSet, constant


class FirstApi(HttpUser):
    wait_time = constant(1)
    host = "https://reqres.in"

    @task
    def create_user(self):
        payload = {
            "name": "morpheus",
            "job": "leader"
        }
        headers = {
            "Content-Type": "application/json"
        }
        response = self.client.post("/api/users", json=payload, headers=headers)
        print(response.status_code)
