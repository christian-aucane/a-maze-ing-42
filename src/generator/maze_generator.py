from typing import Optional

from src.grid import MazeGrid
from src.config import Config
from .algorithms import GENERATION_ALGORITHMS_CLASSES, GenerationAlgorithm


class MazeGenerator:
    """
    Algo sample
    'dfs': {
        'class': DfsAlgorithm,
        'args': [args...],     # Optionnal
        'kwargs': {kwargs...}  # Optionnal
    """

    algo_class: type[GenerationAlgorithm]

    # TODO: separer l'algo et faire de la composition ?
    def __init__(self, algo_name: str):
        try:
            self.algo_class = GENERATION_ALGORITHMS_CLASSES[algo_name]
        except KeyError:
            raise ValueError(
                f"Invalid algorithm name '{algo_name}' ... Valid names: "
                f"{GENERATION_ALGORITHMS_CLASSES.keys()}"
            )

    def generate_maze(
        self,
        size: tuple[int, int],
        entry: tuple[int, int],
        exit: tuple[int, int],
        is_perfect: bool,
    ) -> Optional[MazeGrid]:
        grid = MazeGrid(*size, entry, exit)
        algo = self.algo_class(grid=grid, is_perfect=is_perfect)
        if algo.run():
            return grid
        return None


def generate_maze(config: Config) -> MazeGrid | None:
    try:
        generator = MazeGenerator(algo_name=config.gen_algorithm)
    except ValueError:
        print("Error durring generator instanciation...")
        return None

    grid = generator.generate_maze(
        size=(config.width, config.height),
        entry=config.entry,
        exit=config.exit,
        is_perfect=config.perfect,
    )
    if grid is None:
        print("Error durring maze generation...")
        return None
    return grid


if __name__ == "__main__":
    generator = MazeGenerator(algo_name="test")
    maze = generator.generate_maze(
        size=(40, 15), entry=(0, 0), exit=(14, 14), is_perfect=True
    )
    if maze is not None:
        print(f"maze:\n{maze.get_debug()}")
