from typing import Optional
from pydantic import BaseModel


class Config(BaseModel):
    ...

    @classmethod
    def read_file(path: str) -> Optional["Config"]:
        # TODO: read file and instanciate a config or raise error
        ...


def parse_config_file(config_file_path: str) -> Config | None:
    if config := Config.read_file(config_file_path) is None:
        print(f"Config file '{config_file_path}' doesn't exist...")
    return config
