from locust import HttpUser, between, task


class WebsiteUser(HttpUser):
    wait_time = between(1, 3)
    host = "http://10.117.27.38:8090"

    def on_start(self):
        login_response = self.client.post("/login", json={"username": "todatoda", "password": "vardisferiVardi1"})
        if login_response.status_code == 200:
            self.session_token = login_response.cookies.get("session_token")
        else:
            raise Exception("Failed to login")

    @task
    def access_protected_endpoint(self):
        if hasattr(self, "session_token"):
            headers = {"Authorization": f"Bearer {self.session_token}"}
            response = self.client.get("/protected_endpoint", headers=headers)
            if response.status_code != 200:
                self.log_failure("Failed to access protected endpoint")
        else:
            raise Exception("Session token not found")
