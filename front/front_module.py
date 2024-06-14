import time
import random
import string
import os
import json
from locust import HttpUser, between, task, TaskSet, constant_pacing, constant, SequentialTaskSet


class First(TaskSet):
    wait_time = constant_pacing(5)
    session_key = ""

    @task
    def index_page(self):
        actions = ['click_link', 'submit_form', 'scroll_down']
        selected_action = random.choice(actions)

        if selected_action == 'click_link':
            self.click_link()
        elif selected_action == 'submit_form':
            self.submit_form()
        elif selected_action == 'scroll_down':
            self.scroll_down()

        # response = self.client.get(url="/")
        # print(f"{self.index_page.__name__} - {response.status_code}")
        # self.interrupt()

    def click_link(self):
        response = self.client.get(url="/")
        print(f"{self.click_link.__name__} - {response.status_code}")
        self.interrupt()

    def submit_form(self):
        payload = {
            "username": "devtest3",
            "password": "QWEasd123!"
        }
        response = self.client.get(url="/", json=payload)
        print(f"{self.submit_form.__name__} - {response.status_code}")
        self.interrupt()

    def scroll_down(self):
        response = self.client.get(url="/")
        print(f"{self.scroll_down.__name__} - {response.status_code}")
        self.interrupt()

    @task
    def forgot_data(self):
        scenario = random.choice(["valid_email", "invalid_email", "network_error"])
        selected_scenario = random.choice(scenario)
        response = self.client.get(url=f"/auth/forgotData")
        print(f"{self.forgot_data.__name__} - {response.status_code}")
        self.interrupt()

        if selected_scenario == "valid_email":
            self.send_valid_email()
        elif selected_scenario == "invalid_email":
            self.send_invalid_email()
        elif selected_scenario == "network_error":
            self.handle_network_error()

    def send_valid_email(self):
        response = self.client.get(url=f"/auth/forgotData")
        print(f"{self.send_valid_email.__name__} - {response.status_code}")
        if response.status_code == 400:
            print("Invalid email")
        else:
            print("Unexpected error")
        self.interrupt()

    def send_invalid_email(self):
        email = "invalid_email"
        response = self.client.get(url=f"/auth/forgotData/?email={email}")
        print(f"{self.send_invalid_email.__name__} - {response.status_code}")
        if response.status_code == 400:
            print("Invalid email")
        else:
            print("Unexpected error")
        self.interrupt()

    def handle_network_error(self):
        with self.client.get(url="auth/forgotData/", catch_response=True) as response:
            if response.error:
                print("Network error")
                response.failure("Network error")
            else:
                print("Request successful")
        self.interrupt()

    @task
    def registration(self):
        registration_data = {
            "personal_id": "01001049031",
            "phone": "579374499"
        }
        response = self.client.get(url="/auth/registration/", json=registration_data)
        print(f"{self.registration.__name__} - {response.status_code}")

        if response.status_code == 200:
            print("Registration successful")
        else:
            print("Registration failed")
            if response.status_code == 400:
                print("Bad request")
            elif response.status_code == 409:
                print("Conflict")
        self.interrupt()

        # response = self.client.get(url="/auth/registration/")
        # print(f"{self.registration.__name__} - {response.status_code}")
        # self.interrupt()

    @task
    def about(self):
        response = self.client.get(url="/about/")
        print(f"{self.about.__name__} - {response.status_code}")
        self.interrupt()

    @task
    def address(self):
        response = self.client.get(url="/address/")
        print(f"{self.address.__name__} - {response.status_code}")
        self.interrupt()

    @task
    def faq(self):
        response = self.client.get(url="/faq/")
        print(f"{self.faq.__name__} - {response.status_code}")
        self.interrupt()


class Second(TaskSet):
    wait_time = constant_pacing(5)
    session_key = ""

    def login(self):
        payload = {
            "username": "devtest3",
            "password": "QWEasd123"
        }
        response = self.client.post("/login", json=payload)
        if response.status_code == 200:
            self.session_key = response.json().get("session_key")
        else:
            print("Failed to login")
        self.interrupt()

    @task
    def dashboard(self):
        actions = ['click_link', 'scroll_down']
        selected_action = random.choice(actions)
        response = self.client.get(url="/dashboard")
        print(f"{self.dashboard.__name__} - {response.status_code}")
        self.interrupt()

        if selected_action == 'click_link':
            self.click_link()
        elif selected_action == 'scroll_down':
            self.scroll_down()

    def click_link(self):
        response = self.client.get(url="/dashboard")
        print(f"{self.click_link.__name__} - {response.status_code}")
        self.interrupt()

    def scroll_down(self):
        response = self.client.get(url="/dashboard")
        print(f"{self.scroll_down.__name__} - {response.status_code}")
        self.interrupt()

    @task
    def loans(self):
        actions = ['click_link', 'scroll_down']
        selected_action = random.choice(actions)

        if selected_action == 'click_link':
            self.click_link()
        elif selected_action == 'scroll_down':
            self.scroll_down()

    def click_link(self):
        response = self.client.get(url="/loans")
        print(f"{self.click_link.__name__} - {response.status_code}")
        self.interrupt()

    def scroll_down(self):
        response = self.client.get(url="/loans")
        print(f"{self.scroll_down.__name__} - {response.status_code}")
        self.interrupt()

        # response = self.client.get(url="/loans")
        # print(f"{self.loans.__name__} - {response.status_code}")
        # self.interrupt()

    @task
    def statementstoconfirm(self):
        response = self.client.get(url="/statementsToConfirm")
        print(f"{self.statementstoconfirm.__name__} - {response.status_code}")
        self.interrupt()

    @task
    def currency(self):
        response = self.client.get(url="/currency")
        print(f"{self.currency.__name__} - {response.status_code}")
        self.interrupt()

    @task
    def currency2(self):
        response = self.client.get(url="/en/currency")
        print(f"{self.currency.__name__} - {response.status_code}")
        self.interrupt()

    @task
    def profile(self):
        response = self.client.get(url="/profile")
        print(f"{self.profile.__name__} - {response.status_code}")
        self.interrupt()


class MainClass(HttpUser):
    wait_time = between(1, 3)
    tasks = [First, Second]
    host = "http://dev.crystalone.ge/ka"
    session_key = "A51271FA-7F45-49E4-BC67-C178ADB42F63"
