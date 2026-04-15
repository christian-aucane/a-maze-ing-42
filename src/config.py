"""Parse config."""
from typing import Any
from pydantic import BaseModel, Field, field_validator


class Config(BaseModel):
    # TODO: use Field for config validation
    width: int = Field(...)
    height: int = Field(...)
    entry: tuple[int, int] = Field(...)
    exit: tuple[int, int] = Field(...)
    perfect: bool = Field(...)
    output_file: str = Field(...)
    seed: int | None = Field(default=None)
    gen_algorithm: str = Field(default="...")
    solve_algorithm: str = Field(default="DFS")
    display_mode: str = Field(default="...")

    @field_validator('entry', 'exit', mode="before")
    @classmethod
    def entry_exit(cls, value: str) -> tuple[int, int]:
        x, y = map(int, value.split(","))
        return (x, y)


def parse_config_file(config_file_path: str) -> Config | None:
    """Parse config data."""
    config_dict: dict[str, Any] = {}
    try:
        with open(config_file_path, "r") as f:
            if not f:
                raise FileNotFoundError(f"Config file '{config_file_path}'"
                                        " doesn't exist...")
            for line in f:
                line = line.strip()
                if not line or line.startswith("#"):
                    continue
                key, value = line.split("=")
                config_dict[key.lower()] = value
        config = Config(**config_dict)
        print(config)
        return config
    except (FileNotFoundError, ValueError, KeyError) as e:
        print(e)
    return None


if __name__ == "__main__":
    parse_config_file("../config.txt")
