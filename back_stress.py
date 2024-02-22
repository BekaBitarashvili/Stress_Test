import time
import random
import string
from _winapi import NULL

from locust import HttpUser, between, task, TaskSet, constant


class Auth(HttpUser):
    wait_time = between(1, 1)
    host = "http://10.117.27.38:8000"
    session_key = "CA7E94EF-8860-4628-904C-1F0FA0324558"

    def reset_password(self):
        expected_response = {
            "personal_id": "60001095996",
            "phone": "599458903"
        }
        headers = {
            "Content-Type": "application/json",
            "session-key": self.session_key
        }
        with self.client.post("/api/reset_password", catch_response=True, json=expected_response,
                              headers=headers) as response:
            if response.status_code == expected_response:
                response.success()
            else:
                response.failure("Failed to reset password")
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
    def restore_password_otp(self):
        payload = {
            "otp": "000000"
        }
        headers = {
            "Content-Type": "application/json",
            "session-key": self.session_key
        }
        response = self.client.post("/api/restore_password_otp", json=payload, headers=headers)
        print(f"{self.restore_password_otp.__name__} - {response.status_code}")

    @task
    def check_customer(self):
        payload = {
            "personal_id": "31001025372",
            "phone": "558349904",
        }
        headers = {
            "Content-Type": "application/json"
        }
        response = self.client.post("/api/check_customer", json=payload, headers=headers)
        print(f"{self.check_customer.__name__} - {response.status_code}")

    @task
    def create_account(self):
        payload = {
            "personal_id": "35001105092",
            "phone": "598962796"
        }
        headers = {
            "Content-Type": "application/json",
            "session-key": self.session_key
        }
        response = self.client.post(url="/api/create_account", json=payload, headers=headers)
        print(f"{self.create_account.__name__} - {response.status_code}")

    @task
    def check_create_account(self):
        payload = {
            "opt": "000000"
        }
        headers = {
            "Content-Type": "application/json",
            "session-key": self.session_key
        }
        response = self.client.post("/api/check_create_account", json=payload, headers=headers)
        print(f"{self.check_create_account.__name__} - {response.status_code}")

    @task
    def check_username(self):
        payload = {
            "username": "AkidoTest"
        }
        headers = {
            "Content-Type": "application/json",
            "session-key": self.session_key
        }
        response = self.client.post("/api/check_username", json=payload, headers=headers)
        print(f"{self.check_username.__name__} - {response.status_code}")


class SDA(HttpUser):
    wait_time = between(10, 20)
    host = "http://10.117.27.38:8000"
    session_key = "FB35E783-C2A4-47C0-BCD7-3B815B7ED8AD"

    @task
    def get_personal_info(self):
        payload = {
            "PersonalID": "00000001751",
            "DocumentNumber": "00II00528"
        }
        headers = {
            "Content-Type": "application/json",
            "session-key": self.session_key
        }
        response = self.client.post("/api/SDA/get_personal_info", headers=headers, json=payload)
        print(f"{self.get_personal_info.__name__} - {response.status_code}")