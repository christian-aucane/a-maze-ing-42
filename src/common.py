from typing import Optional
from enum import Enum

from pydantic import BaseModel


class Direction(Enum):
    # Ready to merge on an other branch
    ...


class Config(BaseModel):
    solve_algo = "dfs"
    ...

    @staticmethod
    def read_file(path: str) -> Optional["Config"]:
        # TODO: read file and instanciate a config or raise error
        #
        ...
