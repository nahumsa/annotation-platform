import uuid
from locust import HttpUser, task

class IngestionAPIUser(HttpUser):
    host = "http://localhost:8080"
    @task
    def submit_text_entry(self):
        headers = {
            'accept': 'application/json',
            'Content-Type': 'application/x-www-form-urlencoded',
        }

        data = {
            'text_entry': f'teste {uuid.uuid4()}',
        }

        self.client.post('/submit/', headers=headers, data=data)

class ServingAPIUser(HttpUser):
    host = "http://localhost:9000"

    @task
    def fetch_data(self):
        self.client.get('/fetch_dataset?num_toxic_texts=100&num_non_toxic_texts=100')