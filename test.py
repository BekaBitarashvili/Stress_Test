import time
import random
import string
from _winapi import NULL

from locust import HttpUser, between, task, TaskSet, constant


class User1(HttpUser):
    wait_time = between(1, 1)
    host = "https://reqres.in"
    # session_key = "F014373B-C969-45C4-9B2D-BB1336C845B6"

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
        print(f"{self.create_user.__name__} - {response.status_code}")