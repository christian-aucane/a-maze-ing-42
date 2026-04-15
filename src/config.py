from typing import Optional

from pydantic import BaseModel


class Config(BaseModel):
    # TODO: use Field for config validation
    solve_algo: str = "..."
    gen_algo: str = "test"
    width: int = 20
    height: int = 20
    start: tuple[int, int] = (0, 0)
    end: tuple[int, int] = (19, 19)
    perfect: bool = True

    ...

    @staticmethod
    def read_file(path: str) -> Optional["Config"]:
        # TODO: read file and instanciate a config or raise error
        return Config()
        ...


def parse_config_file(config_file_path: str) -> Config | None:
    config = Config.read_file(config_file_path)
    if config is None:
        print(f"Config file '{config_file_path}' doesn't exist...")
    return config
