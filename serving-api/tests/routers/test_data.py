# pylint: disable=missing-function-docstring
# pylint: disable=missing-class-docstring

import pytest
from fastapi import FastAPI
from fastapi.testclient import TestClient
from src.routers import data

async def mock_fetch_argilla_dataset():
    return {
    "toxic_texts": [
    "ABCDEFG"
    ],
    "non_toxic_texts": [
    "teste 123"
    ],
    "metadata": {}
    }


class TestFormSubmission:
    @pytest.fixture(scope="module")
    def client(self):
        app = FastAPI()
        app.include_router(data.router)
        app.dependency_overrides[data.fetch_argilla_dataset] = mock_fetch_argilla_dataset
        with TestClient(app) as client:
            yield client

    @pytest.mark.parametrize(
        "num_toxic_texts, num_non_toxic_texts", [(1, 1)]
    )
    def test_post_text_entry(
        self, client, num_toxic_texts, num_non_toxic_texts
    ):



        response = client.get(
            f"/fetch_dataset?num_toxic_texts={num_toxic_texts}&num_non_toxic_texts={num_non_toxic_texts}"
        )
        response = client.get(
            f"/fetch_dataset?num_toxic_texts={num_toxic_texts}&num_non_toxic_texts={num_non_toxic_texts}"
        )
        assert response.status_code == 200
        data = response.json()
        assert len(data["toxic_texts"]) == num_toxic_texts
        assert len(data["non_toxic_texts"]) == num_non_toxic_texts
        assert data["metadata"] == {}
