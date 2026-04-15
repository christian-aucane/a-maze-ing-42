from abc import ABC, abstractmethod

from src.common import Direction
from src.grid import MazeGrid, OutOfBoundError


class GenerationAlgorithm(ABC):
    def __init__(self, is_perfect: bool):
        self.is_perfect = is_perfect
        self.is_configured = False
        self.grid = None
        self.start = None
        self.end = None
        self.current_box = None
        self.movements = []

    def configure(
        self, grid: MazeGrid, start: tuple[int, int], end: tuple[int, int]
    ):
        self.grid = grid  # TODO: utiliser une copie et retourner dans run la grille modifiee ??
        self.start = grid.get_box(*start)
        self.end = grid.get_box(*end)
        self.current_box = self.start
        self.is_configured = True

    def _move(self, direction: Direction) -> bool:
        try:
            self.current_box = self.grid.get_neighbour(
                box=self.current_box, direction=direction
            )
            self.movements.append(direction)
            return True
        except OutOfBoundError:
            return False

    def reverse(self, n_moves: int = 1) -> int:
        n_moves = min(n_moves, len(self.movements))
        for _ in range(n_moves):
            dir = self.movements[-1]
            self._move(dir)

    def break_and_move(self, direction: Direction) -> bool:
        if not self.grid.break_wall(box=self.current_box, direction=direction):
            return False
        self._move(direction=direction)
        return True

    @abstractmethod
    def run(self) -> bool: ...
