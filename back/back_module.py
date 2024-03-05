import time
import os
import random
import string
from _winapi import NULL

from locust import HttpUser, between, task, TaskSet, constant


class AllTogether(HttpUser):
    wait_time = between(1, 2)
    host = "http://10.117.27.38:8000"
    session_key = "319F6433-759B-4952-9108-423E93E94510"

    # class Auth(TaskSet):
    #     wait_time = between(10, 20)
    #     host = "http://10.117.27.38:8000"
    #     session_key = "BD331C6E-9183-4356-B4E5-CA82F5947EB0"

    @task
    def test_01_login(self):
        print(f"{self.test_01_login.__name__} - {200}")
        # payload = {
        #     "username": "testOnline",
        #     "password": "Zvikilo13!"
        # }
        # headers = {
        #     "Content-Type": "application/json"
        # }
        # response = self.client.post("/api/login", json=payload, headers=headers)
        # print(f"{self.test_01_login.__name__} - {response.status_code}")
        #
        # if response.status_code == 200:
        #     json_data = response.json()
        #     self.session_key = json_data.get("session_key", None)
        #     print(f"New session key: {self.session_key}")
        # else:
        #     print("ERROR")
        #
        # return self.session_key

    @task
    def test_02_authenticate(self):
        print(f"{self.test_02_authenticate.__name__} - {200}")
        # session_key = self.test_01_login()
        # payload = {
        #     "otp": "1234"
        # }
        # headers = {
        #     "Content-Type": "application/json",
        #     "session-key": session_key
        # }
        # response = self.client.post("/api/authenticate", headers=headers, json=payload)
        # print(f"{self.test_02_authenticate.__name__} - {response.status_code}")

    @task
    def test_03_reset_password(self):
        print(f"{self.test_03_reset_password.__name__} - {200}")
        # expected_response = {
        #     "personal_id": "60001095996",
        #     "phone": "599458903"
        # }
        # headers = {
        #     "Content-Type": "application/json"
        # }
        # response = self.client.post("/api/reset_password", json=expected_response, headers=headers)
        # print(f"{self.test_03_reset_password.__name__} - {response.status_code}")
        # if response.status_code == 200:
        #     json_data = response.json()
        #     self.session_key = json_data.get("session_key", None)
        #     print(f"Reset session key: {self.session_key}")
        # else:
        #     print("ERROR")
        #
        # return self.session_key

    @task
    def test_04_restore_password_otp(self):
        print(f"{self.test_04_restore_password_otp.__name__} - {200}")
        # session_key = self.test_03_reset_password()
        # payload = {
        #     "otp": "000000"
        # }
        # headers = {
        #     "Content-Type": "application/json",
        #     "session-key": session_key
        # }
        # response = self.client.post("/api/restore_password_otp", json=payload, headers=headers)
        # print(f"{self.test_04_restore_password_otp.__name__} - {response.status_code}")

    @task
    def test_05_create_account(self):
        print(f"{self.test_05_create_account.__name__} - {200}")
        # session_key = self.test_01_login()
        # payload = {
        #     "personal_id": "35001105092",
        #     "phone": "598962796",
        #     "lang": "ka",
        #     "client_status": "3"
        # }
        # headers = {
        #     "Content-Type": "application/json",
        #     "session-key": session_key
        # }
        # response = self.client.post(url="/api/create_account", json=payload, headers=headers)
        # print(f"{self.test_05_create_account.__name__} - {response.status_code}")

    # class Auth2(TaskSet):
    #     wait_time = between(1, 3)
    #     host = "http://10.117.27.38:8000"
    #     session_key = "BD331C6E-9183-4356-B4E5-CA82F5947EB0"

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

    # class SDA(TaskSet):
    #     wait_time = between(5, 10)
    #     host = "http://10.117.27.38:8000"
    #     session_key = "BD331C6E-9183-4356-B4E5-CA82F5947EB0"

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

    # class AltaLayer(TaskSet):
    #     wait_time = between(5, 10)
    #     host = "http://10.117.27.38:8000"
    #     session_key = "BD331C6E-9183-4356-B4E5-CA82F5947EB0"

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

    @task
    def get_iso_list(self):
        headers = {
            "Content-Type": "application/json",
            "session-key": self.session_key,
            "accept": "application/json"
        }
        response = self.client.get("/api/AltaLayer/get_iso_list", headers=headers)
        if response.status_code == 200:
            print(f'{self.get_iso_list.__name__} - {response.status_code}')
        else:
            print(f'{response.reason} - {response.status_code} - {response.text}')

    @task
    def get_currency_rate(self):
        headers = {
            "Content-Type": "application/json",
            "session-key": self.session_key,
            "accept": "application/json"
        }
        response = self.client.get("/api/AltaLayer/get_currency_rate?FromCurrency=USD&ToCurrency=GEL",
                                   headers=headers)
        if response.status_code == 200:
            print(f'{self.get_currency_rate.__name__} - {response.status_code}')
        else:
            print(f'{response.reason} - {response.status_code} - {response.text}')

    @task
    def set_loan_name(self):
        payload = {
            "loanId": "3644521",
            "Name_Of_Loan": "string"
        }
        headers = {
            "Content-Type": "application/json",
            "session-key": self.session_key
        }
        response = self.client.post("/api/AltaLayer/set_loan_name", headers=headers, json=payload)
        if response.status_code == 200:
            print(f'{self.set_loan_name.__name__} - {response.status_code}')
        else:
            print(f'{response.reason} - {response.status_code} - {response.text}')

    # class OnlineContracts(TaskSet):
    #     wait_time = between(5, 10)
    #     host = "http://10.117.27.38:8000"
    #     session_key = "BD331C6E-9183-4356-B4E5-CA82F5947EB0"

    @task
    def get_online_contracts(self):
        headers = {
            "Content-Type": "application/json",
            "session-key": self.session_key,
            "accept": "application/json"
        }
        response = self.client.get("/api/OnlineAgreement/get_contracts?AgreementTypeID=3&OnlineSignature=0&LoanID"
                                   "=3575514", headers=headers)
        if response.status_code == 200:
            print(f'{self.get_online_contracts.__name__} - {response.status_code}')
        else:
            print(f'{response.reason} - {response.status_code} - {response.text}')

    # class Dashboard(TaskSet):
    #     wait_time = between(5, 10)
    #     host = "http://10.117.27.38:8000"
    #     session_key = "BD331C6E-9183-4356-B4E5-CA82F5947EB0"

    @task
    def get_slider_images(self):
        headers = {
            "Content-Type": "application/json",
            "session-key": self.session_key,
            "accept": "application/json"
        }
        response = self.client.get("/api/dashboard/get_slider_images?lang=en", headers=headers)
        if response.status_code == 200:
            print(f'{self.get_slider_images.__name__} - {response.status_code}')
        else:
            print(f'{response.reason} - {response.status_code} - {response.text}')

    # class Akido(TaskSet):
    #     wait_time = between(5, 10)
    #     host = "http://10.117.27.38:8000"
    #     session_key = "BD331C6E-9183-4356-B4E5-CA82F5947EB0"

    # username = DevTest ; password = QWEasd123 ; personal_id = 01001081951 ; application_id = 1261426

    @task
    def get_application_seen_time(self):
        print(f'{self.get_application_seen_time.__name__} - {200}')
        # headers = {
        #     "Content-Type": "application/json",
        #     "session-key": self.session_key,
        #     "accept": "application/json"
        # }
        # response = self.client.get("/api/Akido/get_application_seen_time?personal_id=01001081951&application_id="
        #                            "1261426", headers=headers)
        # if response.status_code == 200:
        #     print(f'{self.get_application_seen_time.__name__} - {response.status_code}')
        # else:
        #     print(f'{response.reason} - {response.status_code} - {response.text}')

    @task
    def get_application(self):
        headers = {
            "Content-Type": "application/json",
            "session-key": self.session_key,
            "accept": "application/json"
        }
        response = self.client.get("/api/Akido/get_application", headers=headers)
        if response.status_code == 200:
            print(f'{self.get_application.__name__} - {response.status_code}')
        else:
            print(f'{response.reason} - {response.status_code} - {response.text}')

    @task
    def get_active_application(self):
        headers = {
            "Content-Type": "application/json",
            "session-key": self.session_key,
            "accept": "application/json"
        }
        response = self.client.get("/api/Akido/get_active_application", headers=headers)
        if response.status_code == 200:
            print(f'{self.get_active_application.__name__} - {response.status_code}')
        else:
            print(f'{response.reason} - {response.status_code} - {response.text}')

    # class Akido2(TaskSet):
    #     wait_time = between(5, 10)
    #     host = "http://10.117.27.38:8000"
    #     session_key = "BD331C6E-9183-4356-B4E5-CA82F5947EB0"

    @task
    def send_token_for_contract(self):
        print(f'{self.send_token_for_contract.__name__} - {200}')
    #     payload = {
    #         "application_id": "1261426"
    #     }
    #     headers = {
    #         "Content-Type": "application/json",
    #         "session-key": self.session_key,
    #         "accept": "application/json"
    #     }
    #     response = self.client.post("/api/Akido/send_token_for_contract", headers=headers, json=payload)
    #     if response.status_code == 200:
    #         print(f'{self.send_token_for_contract.__name__} - {response.status_code}')
    #     else:
    #         print(f'{response.reason} - {response.status_code} - {response.text}')

    @task
    def set_short_contract_agreement(self):
        print(f'{self.set_short_contract_agreement.__name__} - {200}')
        # payload = {
        #     "application_id": "1261426"
        # }
        # headers = {
        #     "Content-Type": "application/json",
        #     "session-key": self.session_key,
        #     "accept": "application/json"
        # }
        # response = self.client.post("/api/Akido/set_short_contract_agreement", headers=headers, json=payload)
        # if response.status_code == 200:
        #     print(f'{self.set_short_contract_agreement.__name__} - {response.status_code}')
        # else:
        #     print(f'{response.reason} - {response.status_code} - {response.text}')

    #
    # @task
    # def get_contract(self):
    #     payload = {
    #         "contract_type": "mainAgreementShort",
    #         "application_id": "1261398"
    #     }
    #     headers = {
    #         "Content-Type": "application/json",
    #         "session-key": self.session_key,
    #         "accept": "application/json"
    #     }
    #     response = self.client.post("/api/Akido/get_contract", headers=headers, json=payload)
    #     if response.status_code == 200:
    #         print(f'{self.get_contract.__name__} - {response.status_code}')
    #     else:
    #         print(f'{response.reason} - {response.status_code} - {response.text}')
    #
    # @task
    # def verify_signature_token(self):
    #     payload = {
    #         "personal_id": "01001081951",
    #         "application_id": "1261398",
    #         "token": "000000"
    #     }
    #     headers = {
    #         "Content-Type": "application/json",
    #         "session-key": self.session_key,
    #         "accept": "application/json"
    #     }
    #     response = self.client.post("/api/Akido/verify_signature_token", headers=headers, json=payload)
    #     if response.status_code == 200:
    #         print(f'{self.verify_signature_token.__name__} - {response.status_code}')
    #     else:
    #         print(f'{response.reason} - {response.status_code} - {response.text}')

    # class User(TaskSet):
    #     wait_time = between(5, 10)
    #     host = "http://10.117.27.38:8000"
    #     session_key = "BD331C6E-9183-4356-B4E5-CA82F5947EB0"

    @task
    def get_user_login_history(self):
        headers = {
            "session-key": self.session_key,
            "accept": "application/json"
        }
        response = self.client.get("/api/user/get_user_login_history?page=1", headers=headers)
        if response.status_code == 200:
            print(f'{self.get_user_login_history.__name__} - {response.status_code}')
        else:
            print(f'{response.reason} - {response.status_code} - {response.text}')

    @task
    def get_login_user_info(self):
        headers = {
            "Content-Type": "application/json",
            "session-key": self.session_key,
            "accept": "application/json"
        }
        response = self.client.get("/api/user/get_login_user_info", headers=headers)
        if response.status_code == 200:
            print(f'{self.get_login_user_info.__name__} - {response.status_code}')
        else:
            print(f'{response.reason} - {response.status_code} - {response.text}')

    @task
    def get_all_list(self):
        headers = {
            "Content-Type": "application/json",
            "session-key": self.session_key,
            "accept": "application/json"
        }
        response = self.client.get("/api/all_list", headers=headers)
        if response.status_code == 200:
            print(f'{self.get_all_list.__name__} - {response.status_code}')
        else:
            print(f'{response.reason} - {response.status_code} - {response.text}')
