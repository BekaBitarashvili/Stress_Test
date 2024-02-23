import time
import random
import string
from _winapi import NULL
import logging

from locust import HttpUser, between, task, TaskSet, constant, constant_pacing, SequentialTaskSet


class User1(SequentialTaskSet):

    def __init__(self, parent):
        super().__init__(parent)
        self.jsessionid = ""

    @task
    def index_page(self):
        with self.client.get(url="/", name="Index Page", catch_response=True) as response:
            if response.status_code == 200:
                response.success()
                logging.info("Index Page - 200")
            else:
                response.failure("Failed to get Index Page")
                logging.error("Index Page - Failed")


class LoadTestUser(HttpUser):
    wait_time = constant(1)
    host = "http://10.117.27.38:8090"
    tasks = [User1]
