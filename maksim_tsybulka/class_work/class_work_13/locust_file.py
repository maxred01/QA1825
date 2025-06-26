from locust import HttpUser, task, between

class WebsiteUser(HttpUser):
    host = "https://pilicam.com" # Replace with your target website URL
    wait_time = between(1, 5) # Users wait between 1 and 5 seconds between tasks

    @task
    def index_page(self):
        self.client.get("/") # Makes a GET request to the root path

    @task
    def about_page(self):
        self.client.get("/about") # Makes a GET request to the /about path