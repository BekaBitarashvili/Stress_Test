import time
import random
import string
from locust import HttpUser, between, task, TaskSet, constant_pacing


class BeforeAuthorization(HttpUser):
    wait_time = between(1, 2)
    host = "http://10.117.27.38:8090"
    session_key = "FB35E783-C2A4-47C0-BCD7-3B815B7ED8AD"

    @task
    def index_page(self):
        response = self.client.get(url="/")
        print(f"{self.index_page.__name__} - {response.status_code}")

    @task
    def forgot_data(self):
        response = self.client.get(url="/auth/forgotData/")
        print(f"{self.forgot_data.__name__} - {response.status_code}")

    @task
    def dashboard(self):
        response = self.client.get(url="/auth/registration/")
        print(f"{self.dashboard.__name__} - {response.status_code}")

    @task
    def about(self):
        response = self.client.get(url="/about/")
        print(f"{self.about.__name__} - {response.status_code}")

    @task
    def address(self):
        response = self.client.get(url="/address/")
        print(f"{self.address.__name__} - {response.status_code}")

    @task
    def faq(self):
        response = self.client.get(url="/faq/")
        print(f"{self.faq.__name__} - {response.status_code}")


class AfterAuthorization(HttpUser):
    wait_time = constant_pacing(1)
    host = "http://10.117.27.38:8090"
    session_key = "ED1F7E96-C934-41B6-B476-C1147275105A"

    def login(self):
        payload = {
            "username": "55001028171",
            "password": "oG123456"
        }
        response = self.client.post("/login", json=payload)
        if response.status_code == 200:
            self.session_key = response.json().get("session_key")
        else:
            print("Failed to login")

    @task
    def dashboard(self):
        response = self.client.get(url="/dashboard")
        print(f"{self.dashboard.__name__} - {response.status_code}")

    @task
    def loans(self):
        response = self.client.get(url="/loans")
        print(f"{self.loans.__name__} - {response.status_code}")

    @task
    def statementstoconfirm(self):
        response = self.client.get(url="/statementsToConfirm")
        print(f"{self.statementstoconfirm.__name__} - {response.status_code}")

    @task
    def currency(self):
        response = self.client.get(url="/currency")
        print(f"{self.currency.__name__} - {response.status_code}")

    @task
    def currency2(self):
        response = self.client.get(url="/en/currency")
        print(f"{self.currency.__name__} - {response.status_code}")

    @task
    def profile(self):
        response = self.client.get(url="/profile")
        print(f"{self.profile.__name__} - {response.status_code}")
