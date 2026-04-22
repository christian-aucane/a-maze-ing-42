from .grid import MazeGrid
from .common import Direction


def render(grid: MazeGrid, path: list[Direction]) -> str:
