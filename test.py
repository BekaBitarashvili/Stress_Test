import time
import random
import string
from _winapi import NULL

from locust import HttpUser, between, task, TaskSet, constant, constant_pacing


class User1(HttpUser):
    wait_time = constant_pacing(5)
    host = "http://10.117.27.38:8090"

    def on_start(self):
        print("START")

    @task
    def index_page(self):
        response = self.client.get(url="/")
        print(f"{self.index_page.__name__} - {response.status_code} - Code is Runnning")

    @task
    def get_failure(self):
        expected_response = 404
        with self.client.get(url="/", catch_response=True, name="404") as response:
            if response.status_code == expected_response:
                response.success()
            else:
                response.failure("Failed to get 404")

    def on_stop(self):
        print("STOP")