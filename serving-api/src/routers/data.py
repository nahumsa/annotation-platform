from typing import Annotated
import argilla as rg
from fastapi import APIRouter, Query, Depends

from src.configs import read_config_file
from src.models.dataset_return import DatasetReturn
from src.repositories.argilla import ArgillaTextRepositories

router = APIRouter()
configs = read_config_file("src/configs.toml")

async def fetch_argilla_dataset(num_toxic_texts: int = Query(description="Number of toxic texts to fetch", gt=0),
    num_non_toxic_texts: int = Query(
        description="Number of non toxic texts to fetch", gt=0
    )):
    rg.init(**configs.argilla.dict())
    argilla_repository = ArgillaTextRepositories(dataset_name=configs.dataset.name)

    toxic_texts = argilla_repository.get_batch_df(
        annotation="toxic", num_entries=num_toxic_texts
    )
    non_toxic_texts = argilla_repository.get_batch_df(
        annotation="not_toxic", num_entries=num_non_toxic_texts
    )

    return DatasetReturn(
        toxic_texts=toxic_texts["text"].to_list(),
        non_toxic_texts=non_toxic_texts["text"].to_list(),
        metadata={},
    )

@router.get("/fetch_dataset", tags=["serving"])
async def get_data(
    repository: Annotated[DatasetReturn, Depends(fetch_argilla_dataset)]
) -> DatasetReturn:
    return repository

