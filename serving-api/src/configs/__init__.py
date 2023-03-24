from pathlib import Path

import toml
from pydantic import BaseModel, ValidationError, parse_obj_as


class ArgillaConfig(BaseModel):
    """Base configuration settings for Argilla."""

    api_url: str
    api_key: str


class DatasetConfig(BaseModel):
    """Base configuration settings for the dataset."""

    name: str
    labels: list[str]
    tags: dict[str, str]
    background: bool


class MainConfig(BaseModel):
    """Base main configuration."""

    argilla: ArgillaConfig
    dataset: DatasetConfig


class ConfigFileError(Exception):
    pass


def read_config_file(file_path: str | Path) -> MainConfig:
    """Reads a config file based on the `file_path`.

    Args:
        file_path (str | Path): path for the config file.

    Raises:
        Exception: When there is a validation error.

    Returns:
        MainConfig: Config loaded from `file_path`.
    """
    try:
        with open(file_path, "r") as file:
            config_data = toml.load(file)

        return MainConfig.parse_obj(config_data)

    except ValidationError as error:
        raise ConfigFileError(f"Invalid configuration: {error}") from error
