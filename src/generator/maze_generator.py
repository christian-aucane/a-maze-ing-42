from typing import Optional

from src.grid import MazeGrid
from src.config import Config
from .algorithms.abstract import GenerationAlgorithm
from .algorithms.test_algo import TestGenerationAlgorithm

"""
Algo sample
'dfs': DfsAlgorithm
"""


# TODO: deplacer dans common.py ??
GENERATION_ALGORITHMS_CLASSES = {"test": TestGenerationAlgorithm}


class MazeGenerator:
    def __init__(self, algo: GenerationAlgorithm):
        self.algo = algo

    def generate_maze(
        self,
        size: tuple[int, int],
        start: tuple[int, int],
        end: tuple[int, int],
    ) -> Optional[MazeGrid]:
        grid = MazeGrid(*size)
        self.algo.configure(grid=grid, start=start, end=end)
        if self.algo.run():
            return grid
        return None

    @classmethod
    def get_generator(
        cls, algo_name: str, is_perfect: bool
    ) -> Optional["MazeGenerator"]:
        try:
            # TODO: ajouter late import de GENERATION_ALGORITHMS_CLASSES
            algo = GENERATION_ALGORITHMS_CLASSES[algo_name](
                is_perfect=is_perfect,
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
    generator = MazeGenerator.get_generator(algo_name="test", is_perfect=True)
    print("DEBUG", generator)
    maze = generator.generate_maze(size=(15, 15), start=(0, 0), end=(14, 14))
    print(maze)
    print(maze.get_debug())
