import time
from locust import HttpUser, between, task


class WebsiteUser(HttpUser):
    wait_time = between(1, 5)
    host = "https://www.google.com"

    @task
    def index_page(self):
        self.client.get(url="/")

    @task
    def view_item(self):
        self.client.get(url="/search/howsearchworks/?fg=1/")
