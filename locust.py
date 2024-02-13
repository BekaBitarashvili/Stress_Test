import time
import random
import string
from locust import HttpUser, between, task


class WebsiteUser(HttpUser):
    wait_time = between(1, 5)
    host = "http://10.117.27.38:8090"

    @task
    def index_page(self):
        self.client.get(url="/")

    @task
    def forgot_data(self):
        self.client.get(url="/auth/forgotData/")

    @task
    def dashboard(self):
        self.client.get(url="/dashboard/")

    @task
    def login_and_access_dashboard(self):
        # სიმულაცია
        login_response = self.client.post("/auth/login", json={"username": "todatoda", "password": "vardisferiVardi1"})
        if login_response.status_code == 200:
            # სესიის ტოკენი
            session_token = login_response.cookies.get("session_token")
            # სესიის ტოკენის გამოყენება სხვა რექვესტებისთვის
            self.client.get("/dashboard/", headers={"Authorization": f"Bearer {session_token}"})

    @task
    def create_new_data(self):
        # სიმულაცია - შევქმნათ ახალი მონაცემი და გავაგზავნოთ სერვერზე POST მეთოდით
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

    def on_start(self):
        # მეთოდს ვიძახებთ როცა ახალი მომხმარებელი აკეთებს ტასკის EXECUTE-ს
        self.login_and_access_dashboard()
