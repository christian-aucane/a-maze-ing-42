import random

from .abstract import GenerationAlgorithm
from src.common import Direction
from src.grid import OutOfBoundError, MazeBox, MazeGrid


class Kruskal(GenerationAlgorithm):
    def __init__(self, grid: MazeGrid, is_perfect: bool):
        super().__init__(grid=grid, is_perfect=is_perfect)
        self.parents = {box: box for box in self.grid.get_boxes()}

    def find(self, cell: MazeBox):
        current = cell
        while current != self.parents[current]:
            current = self.parents[current]
        return current

    def union(self, cell_a: MazeBox, cell_b: MazeBox):
        root_a = self.find(cell_a)
        root_b = self.find(cell_b)
        self.parents[root_b] = root_a

    def are_connected(self, cell_a, cell_b):
        return self.find(cell_a) == self.find(cell_b)

    def run(self) -> bool:
        print(f"Kruskal start: entry={self.grid.entry}, exit={self.grid.exit}")
        walls = []
        for cell in self.grid.get_boxes():
            if cell.is_on_ft_pattern:
                continue
            for dir in [Direction.SOUTH, Direction.EAST]:
                try:
                    neighbour = self.grid.get_neighbour(box=cell, direction=dir)
                    walls.append((cell, neighbour, dir))
                except OutOfBoundError:
                    continue

        random.shuffle(walls)
        for cell_a, cell_b, dir in walls:
            if self.are_connected(cell_a, cell_b):
                continue
            self.union(cell_a, cell_b)
            self.grid.break_wall(cell_a, dir)

        return True
