from abc import ABC, abstractmethod
from typing import Any, Optional

from src.grid import MazeGrid
from src.config import Config


class GenerationAlgorithm(ABC):
    def __init__(self, is_perfect: bool, *args: Any, **kwargs: Any):
        self.is_perfect = is_perfect

    @abstractmethod
    def run(
        self, grid: MazeGrid, start: tuple[int, int], end: tuple[int, int]
    ) -> bool: ...


class MazeGenerator:
    """
    Algo sample
    'dfs': {
        'class': DfsAlgorithm,
        'args': [args...],     # Optionnal
        'kwargs': {kwargs...}  # Optionnal
    """

    ALGORITHMS = {"...": {"class": GenerationAlgorithm}}
    # TODO: separer l'algo et faire de la composition ?

    def __init__(self, algo: GenerationAlgorithm):
        self.algo = algo

    def generate_maze(
        self,
        size: tuple[int, int],
        start: tuple[int, int],
        end: tuple[int, int],
    ) -> Optional[MazeGrid]:
        grid = MazeGrid(*size)
        if self.algo.run(grid=grid, start=start, end=end):
            return grid
        return None

    @classmethod
    def get_generator(
        cls, algo_name: str, is_perfect: bool
    ) -> Optional["MazeGenerator"]:
        try:
            algo_dict = cls.ALGORITHMS[algo_name]
            algo = algo_dict["class"](
                is_perfect=is_perfect,
                *algo_dict.get("args", []),
                **algo_dict.get("kwargs", {}),
            )
            return cls(algo=algo)
        except KeyError:
            return None


def generate_maze(config: Config) -> MazeGrid | None:
    generator = MazeGenerator.get_generator(
        algo_name=config.gen_algo, is_perfect=config.perfect
    )
    if generator is None:
        print("Error durring generator instanciation...")
        return None

    grid = generator.generate_maze(
        size=(config.width, config.height), start=config.start, end=config.end
    )
    if grid is None:
        print("Error durring maze generation...")
        return None
    return grid


if __name__ == "__main__":
    generator = MazeGenerator(algo_name="test")
    maze = generator.generate_maze(
        size=(15, 15), start=(0, 0), end=(14, 14), is_perfect=True
    )
    if maze is not None:
        print(f"maze:\n{maze.get_debug()}")
