from typing import Optional

from src.grid import MazeGrid
from src.config import Config
from .algorithms import GENERATION_ALGORITHMS_CLASSES


class MazeGenerator:
    def __init__(self, algo_name: str):
        try:
            self.algo_class = GENERATION_ALGORITHMS_CLASSES[algo_name]
        except KeyError:
            raise ValueError(
                "Invalid algorithm name ... Valid names: "
                f"{GENERATION_ALGORITHMS_CLASSES.keys()}"
            )

    def generate_maze(
        self,
        size: tuple[int, int],
        start: tuple[int, int],
        end: tuple[int, int],
        is_perfect: bool,
    ) -> Optional[MazeGrid]:
        grid = MazeGrid(*size)
        algo = self.algo_class(
            grid=grid, start=start, end=end, is_perfect=is_perfect
        )
        if algo.run():
            return grid
        return None


def generate_maze(config: Config) -> MazeGrid | None:
    generator = MazeGenerator(algo_name=config.gen_algo)
    if generator is None:
        print("Error durring generator instanciation...")
        return None

    grid = generator.generate_maze(
        size=(config.width, config.height),
        start=config.start,
        end=config.end,
        is_perfect=config.perfect,
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
