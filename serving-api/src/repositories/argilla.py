from __future__ import annotations

import argilla as rg
import pandas as pd


class ArgillaTextRepositories:
    def __init__(self, dataset_name: str) -> None:
        self._dataset_name = dataset_name

    def get_batch_df(self, annotation: str, num_entries: int) -> pd.DataFrame:
        return rg.load(
            self._dataset_name, query=f"annotated_as:{annotation}", limit=num_entries
        ).to_pandas()
