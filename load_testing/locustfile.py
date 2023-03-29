import uuid
from locust import HttpUser, task

class IngestionAPI(HttpUser):
    @task
    def submit_text_entry(self):
        headers = {
            'accept': 'application/json',
            'Content-Type': 'application/x-www-form-urlencoded',
        }

        data = {
            'text_entry': f'teste {uuid.UUID()}',
        }

        self.client.post('/submit/', headers=headers, data=data)