# pylint: disable=missing-function-docstring
# pylint: disable=missing-class-docstring
# pylint: disable=import-error

from http import client
import pytest
from fastapi import FastAPI
from fastapi.testclient import TestClient
from src.models.dataset_return import DatasetReturn

from src.routers import data


async def mock_fetch_argilla_dataset():
    return DatasetReturn(
        toxic_texts=["ABCDEFG"],
        non_toxic_texts=["test 123"],
        metadata={},
    )

async def mock_fetch_argilla_no_data():
    return DatasetReturn(
        toxic_texts=[],
        non_toxic_texts=[],
        metadata={},
    )


class TestFormSubmission:
    @pytest.fixture(scope="module")
    def client(self):
        app = FastAPI()
        app.include_router(data.router)
        app.dependency_overrides[
            data.fetch_argilla_dataset
        ] = mock_fetch_argilla_dataset
        with TestClient(app) as client:
            yield client

    @pytest.fixture(scope="module")
    def client_no_data(self):
        app = FastAPI()
        app.include_router(data.router)
        app.dependency_overrides[
            data.fetch_argilla_dataset
        ] = mock_fetch_argilla_no_data
        with TestClient(app) as client:
            yield client

    @pytest.mark.parametrize("num_toxic_texts, num_non_toxic_texts", [(1, 1)])
    def test_get_data(self, client, num_toxic_texts, num_non_toxic_texts):
        response = client.get(
            f"/fetch_dataset?num_toxic_texts={num_toxic_texts}&num_non_toxic_texts={num_non_toxic_texts}"
        )

        assert response.status_code == 200
        data = response.json()
        assert len(data["toxic_texts"]) == num_toxic_texts
        assert len(data["non_toxic_texts"]) == num_non_toxic_texts
        assert data["metadata"] == {}

    @pytest.mark.parametrize("num_toxic_texts, num_non_toxic_texts", [(1, 1)])
    def test_get_no_data(self, client_no_data, num_toxic_texts, num_non_toxic_texts):
        response = client_no_data.get(
            f"/fetch_dataset?num_toxic_texts={num_toxic_texts}&num_non_toxic_texts={num_non_toxic_texts}"
        )

        assert response.status_code == 400
        assert response.json() == {"detail": "No data"}
