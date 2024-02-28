import time
import random
import string
from _winapi import NULL

from locust import HttpUser, between, task, TaskSet, constant


class Auth(HttpUser):
    wait_time = between(10, 20)
    host = "http://10.117.27.38:8000"
    session_key = "1A88694E-9999-46C6-A494-8658F364747B"

    @task
    def test_01_login(self):
        payload = {
            "username": "testOnline",
            "password": "Zvikilo13!"
        }
        headers = {
            "Content-Type": "application/json"
        }
        response = self.client.post("/api/login", json=payload, headers=headers)
        print(f"{self.test_01_login.__name__} - {response.status_code}")

        if response.status_code == 200:
            json_data = response.json()
            self.session_key = json_data.get("session_key", None)
            print(f"New session key: {self.session_key}")
        else:
            print("ERROR")

        return self.session_key

    @task
    def test_02_authenticate(self):
        session_key = self.test_01_login()
        payload = {
            "otp": "1234"
        }
        headers = {
            "Content-Type": "application/json",
            "session-key": session_key
        }
        response = self.client.post("/api/authenticate", headers=headers, json=payload)
        print(f"{self.test_02_authenticate.__name__} - {response.status_code}")

    @task
    def test_03_reset_password(self):
        expected_response = {
            "personal_id": "60001095996",
            "phone": "599458903"
        }
        headers = {
            "Content-Type": "application/json"
        }
        response = self.client.post("/api/reset_password", json=expected_response, headers=headers)
        print(f"{self.test_03_reset_password.__name__} - {response.status_code}")
        if response.status_code == 200:
            json_data = response.json()
            self.session_key = json_data.get("session_key", None)
            print(f"Reset session key: {self.session_key}")
        else:
            print("ERROR")

        return self.session_key

    @task
    def test_04_restore_password_otp(self):
        session_key = self.test_03_reset_password()
        payload = {
            "otp": "000000"
        }
        headers = {
            "Content-Type": "application/json",
            "session-key": session_key
        }
        response = self.client.post("/api/restore_password_otp", json=payload, headers=headers)
        print(f"{self.test_04_restore_password_otp.__name__} - {response.status_code}")

    @task
    def test_05_create_account(self):
        session_key = self.test_01_login()
        payload = {
            "personal_id": "35001105092",
            "phone": "598962796",
            "lang": "ka",
            "client_status": "3"
        }
        headers = {
            "Content-Type": "application/json",
            "session-key": session_key
        }
        response = self.client.post(url="/api/create_account", json=payload, headers=headers)
        print(f"{self.test_05_create_account.__name__} - {response.status_code}")


class Auth2(HttpUser):
    wait_time = between(1, 3)
    host = "http://10.117.27.38:8000"
    session_key = "1A88694E-9999-46C6-A494-8658F364747B"

    @task
    def update_password(self):
        pass

    @task
    def create(self):
        pass

    @task
    def log_out(self):
        pass

    @task
    def change_password(self):
        pass

    @task
    def change_username(self):
        pass

    @task
    def check_customer(self):
        session_key = self.session_key
        payload = {
            "personal_id": "60001095996",
            "phone": "599458903"
        }
        headers = {
            "Content-Type": "application/json",
            "Authorization": f"Bearer {session_key}"
        }
        response = self.client.post("/api/check_customer", json=payload, headers=headers)
        print(f"{self.check_customer.__name__} - {response.status_code}")

    @task
    def check_username(self):
        session_key = self.session_key
        payload = {
            "username": "AkidoTest"
        }
        headers = {
            "Content-Type": "application/json",
            "Authorization": f"Bearer {session_key}"
        }
        response = self.client.post("/api/check_username", json=payload, headers=headers)
        print(f"{self.check_username.__name__} - {response.status_code}")

    # @task
    # def check_create_account(self):
    #     session_key = self.session_key
    #     payload = {
    #         "opt": "000000"
    #     }
    #     headers = {
    #         "Content-Type": "application/json",
    #         "Authorization": f"Bearer {session_key}"
    #     }
    #     response = self.client.post("/api/check_create_account", json=payload, headers=headers)
    #     print(f"{self.check_create_account.__name__} - {response.status_code}")


class SDA(HttpUser):
    wait_time = between(5, 10)
    host = "http://10.117.27.38:8000"
    session_key = "1B4267E1-8E53-4379-9060-F6347958C6A2"

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
        if response.status_code == 200:
            print(f'{self.get_personal_info.__name__} - {response.status_code}')
        else:
            print(f'{response.reason} - {response.status_code} - {response.text}')


class AltaLayer(HttpUser):
    wait_time = between(5, 10)
    host = "http://10.117.27.38:8000"
    session_key = "CEE11FD3-15B9-4912-9A0A-1FB51C85C1D8"

    @task
    def get_loans(self):
        headers = {
            "Content-Type": "application/json",
            "session-key": self.session_key,
            "accept": "application/json"
        }
        response = self.client.get("/api/AltaLayer/get_client_loans", headers=headers)
        if response.status_code == 200:
            print(f'{self.get_loans.__name__} - {response.status_code}')
        else:
            print(f'{response.reason} - {response.status_code} - {response.text}')

    @task
    def get_currency(self):
        headers = {
            "Content-Type": "application/json",
            "session-key": self.session_key,
            "accept": "application/json"
        }
        response = self.client.get("/api/AltaLayer/get_currency", headers=headers)
        if response.status_code == 200:
            print(f'{self.get_currency.__name__} - {response.status_code}')
        else:
            print(f'{response.reason} - {response.status_code} - {response.text}')