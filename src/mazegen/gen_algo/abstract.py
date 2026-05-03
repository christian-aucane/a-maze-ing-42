from abc import ABC, abstractmethod

from ..common import Direction
from ..grid import MazeGrid, OutOfBoundError


class GenerationAlgorithm(ABC):
    def __init__(
        self,
        grid: MazeGrid,
        is_perfect: bool,
    ):
        self.grid = grid
        self.current_box = self.grid.entry
        self.is_perfect = is_perfect
        self.movements: list[Direction] = []

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
        return n_moves

    def break_and_move(self, direction: Direction) -> bool:
        if not self.grid.break_wall(box=self.current_box, direction=direction):
            return False
        self._move(direction=direction)
        return True

    @abstractmethod
    def run(self) -> bool: ...
