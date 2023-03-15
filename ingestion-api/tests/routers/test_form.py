# pylint: disable=missing-function-docstring
# pylint: disable=missing-class-docstring

import pytest
from fastapi import FastAPI
from fastapi.testclient import TestClient

from routers import form


class TestHomepage:
    @pytest.fixture(scope="module")
    def client(self):
        app = FastAPI()
        app.include_router(form.router)
        with TestClient(app) as client:
            yield client

    def test_get_homepage(self, client):
        response = client.get("/")
        assert response.status_code == 200
        assert "form" in response.text
        with open("src/templates/form.html", "r", encoding="utf-8") as html_file:
            expected_content = html_file.read()
        assert response.content == expected_content.encode()


class TestFormSubmission:
    @pytest.fixture(scope="module")
    def client(self):
        app = FastAPI()
        app.include_router(form.router)
        with TestClient(app) as client:
            yield client

    def test_post_text_entry(self, client):
        response = client.post("/submit/", data={"text_entry": "Test text"})
        assert response.status_code == 200
        with open("src/templates/result.html", "r", encoding="utf-8") as html_file:
            expected_content = html_file.read()
        assert response.content == expected_content.encode()


class TestResults:
    @pytest.fixture(scope="module")
    def client(self):
        app = FastAPI()
        app.include_router(form.router)
        with TestClient(app) as client:
            yield client

    def test_get_results(self, client):
        response = client.get("/results")
        assert response.status_code == 200
        with open("src/templates/result.html", "r", encoding="utf-8") as html_file:
            expected_content = html_file.read()
        assert response.content == expected_content.encode()
