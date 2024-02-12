import time
from locust import HttpUser, between, task


class WebsiteUser(HttpUser):
    wait_time = between(1, 5)
    host = "http://10.117.27.38:8090"

    @task
    def index_page(self):
        self.client.get(url="/")

    @task
    def view_item(self):
        self.client.get(url="/auth/forgotData/")
