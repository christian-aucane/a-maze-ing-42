from typing import Optional
from enum import Enum

from pydantic import BaseModel


class Direction(Enum):
    # Ready to merge on an other branch
    NORTH = (0, -1)
    EAST = (+1, 0)
    SOUTH = (0, +1)
    WEST = (-1, 0)


class Config(BaseModel):
    # TODO: use Field for config validation
    solve_algo: str = "..."
    gen_algo: str = "..."
    width: int = 20
    height: int = 20
    start: tuple[int, int] = (0, 0)
    end: tuple[int, int] = (19, 19)

    ...

    @staticmethod
    def read_file(path: str) -> Optional["Config"]:
        # TODO: read file and instanciate a config or raise error
        return Config()
        ...
