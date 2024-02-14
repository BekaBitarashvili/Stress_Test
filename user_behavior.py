from locust import HttpUser, between, task
import random


class WebsiteUser(HttpUser):
    wait_time = between(1, 3)
    host = "http://10.117.27.38:8090"

    def generate_random_product_id(self):
        return random.randint(1, 100)

    @task
    def view_random_product(self):
        product_id = self.generate_random_product_id()
        self.client.get(f"/product/{product_id}")

    @task
    def search_with_keyword(self):
        keywords = ["apple", "banana", "orange", "grape"]
        keyword = random.choice(keywords)
        self.client.get(f"/search?q={keyword}")
