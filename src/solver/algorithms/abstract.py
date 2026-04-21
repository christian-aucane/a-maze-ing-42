from abc import ABC, abstractmethod
from src.common import Direction
from src.grid import MazeGrid


class SolvingAlgorithm(ABC):
    def __init__(self, grid: MazeGrid):
        self.grid = grid
        self.current_box = grid.entry

    @abstractmethod
    def run(self) -> list[Direction] | None: ...
