from .grid import MazeGrid
from .config import Config


class MazeGenerator:
    # TODO: separer l'algo et faire de la composition ?
    def __init__(self, algo: str):
        self._algo = algo

    def generate_maze(
        self, grid: MazeGrid, start: tuple[int, int], end: tuple[int, int]
    ) -> bool:
        return True


def generate_maze(config: Config) -> MazeGrid | None:
    grid = MazeGrid(width=config.width, height=config.height)
    generator = MazeGenerator(algo=config.gen_algorithm)
    if not generator.generate_maze(
        grid=grid,
        start=config.entry,
        end=config.exit
    ):
        print("Error during maze generation...")
        return None
    return grid
