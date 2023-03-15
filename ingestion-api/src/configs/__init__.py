from pathlib import Path
from pydantic import BaseModel, parse_obj_as, ValidationError
import toml

class ArgillaConfig(BaseModel):
    api_url: str
    api_key: str

class DatasetConfig(BaseModel):
    name: str
    labels: list[str]
    tags: dict[str, str]
    background: bool

class MainConfig(BaseModel):
    argilla: ArgillaConfig
    dataset: DatasetConfig

def read_config_file(filename: str | Path) -> MainConfig:
    try:

        with open(filename, "r") as f:
            config_data = toml.load(f)

        return MainConfig.parse_obj(config_data)

    except ValidationError as e:
        raise Exception(f"Invalid configuration: {e}")
