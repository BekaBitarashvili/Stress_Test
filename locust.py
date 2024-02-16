import time
import random
import string
from locust import HttpUser, between, task, TaskSet


class BeforeAuthorization(HttpUser):
    wait_time = between(1, 1)
    host = "http://10.117.27.38:8090"

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
    wait_time = between(1, 3)
    host = "http://10.117.27.38:8090"

    @task
    def login_and_access_dashboard(self):
        login_response = self.client.post("/auth/login", json={"username":"todatoda", "password": "vardisferiVardi1"})
        if login_response.status_code == 200:
            session_token = login_response.cookies.get("session_token")
        # სესიის ტოკენის გამოყენება სხვა რექვესტებისთვის
        self.client.get("/dashboard/", headers={"Authorization": f"Bearer {session_token}"})

    @task
    def create_new_data(self):
        payload = {"name": self.generate_random_name(), "email": self.generate_random_email()}
        self.client.post("/data/create", json=payload)

    @task
    def generate_random_name(self):
        first_names = ["Achiko", "Dato", "Beka", "Zvio", "Luka", "Tornike"]
        last_names = ["Beridze", "Toda", "Bitara", "Pirtskhala", "Kakhno", "Lomidze"]
        return random.choice(first_names) + " " + random.choice(last_names)

    @task
    def generate_random_email(self):
        domains = ["gmail.com", "yahoo.com", "hotmail.com", "yandex.com", "test.com"]
        username = ''.join(random.choices(string.ascii_letters + string.digits, k=random.randint(5, 10)))
        domain = random.choice(domains)
        return username + "@" + domain