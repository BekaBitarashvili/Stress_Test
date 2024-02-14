import time
import random
import string
from locust import HttpUser, between, task, TaskSet


class BeforeAuthorization(HttpUser):
    wait_time = between(1, 3)
    host = "http://10.117.27.38:8090"

    def on_start(self):
        self.login()

    def login(self):
        response = self.client.post("/", json={"username": "todatoda", "password": "vardisferiVardi1"})
        if response.status_code == 200:
            self.token = response.json().get("token")
        else:
            self.token = None

    @task
    def access_protected_endpoint(self):
        if self.token:
            headers = {"Authorization": f"Bearer {self.token}"}
            response = self.client.get("/protected_endpoint", headers=headers)
            if response.status_code == 200:
                assert "success" in response.text.lower(), "Unexpected response"
        else:
            self.login()

    @task
    def perform_search(self):
        search_query = random.choice(["query1", "query2", "query3"])
        response = self.client.get("/search", params={"q": search_query})
        assert response.status_code == 200, "Search request failed"

