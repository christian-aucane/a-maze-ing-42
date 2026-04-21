from .abstract import SolvingAlgorithm
from src.common import Direction
from typing import Any
import random

from src.grid import OutOfBoundError


class DFSSolver(SolvingAlgorithm):
    def run(self) -> list[dict]:
        # pile du chemin
        stack = [self.current_box]
        solutions: list[Direction] = []
        # self.current_box.is_visited = True
        # print(f"DFS Solver start: entry={self.grid.entry}, exit={self.grid.exit}")
        print("self.grid :", self.grid)
        # for row in self.grid:
        #     for cell in row:
        #         cell.is_visited = False

        while stack:
            # sommet de la pile
            current = stack[-1]
            self.current_box = current
            if current == self.grid.exit:
                break

            # directions vers des voisins non visitésh
            neighbours: list[Any] = []
            for direction, value in self.current_box.walls.items():
                if not value:
                    try:
                        neighbour = self.grid.get_neighbour(current, direction)
                        neighbours.append((direction, neighbour))
                        # print("neighbour: ", neighbour)
                    except OutOfBoundError:
                        pass

            if neighbours:
                # on choisit un voisin au hasard
                direction, neighbour = random.choice(neighbours)
                solutions.append(direction)
                stack.append(neighbour)

            else:
                # cul-de-sac on recule
                stack[-1].solution_dir = None
                stack.pop()
                solutions.pop()

        return solutions
