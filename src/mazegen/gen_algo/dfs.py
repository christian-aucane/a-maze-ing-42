from .abstract import GenerationAlgorithm
from ..common import Direction
from typing import Any
import random

from ..grid import OutOfBoundError


class DFS(GenerationAlgorithm):
    def run(self) -> bool:
        # pile du chemin
        stack = [self.current_box]
        self.current_box.is_visited = True
        print(f"DFS start: entry={self.grid.entry}, exit={self.grid.exit}")

        while stack:
            # sommet de la pile
            current = stack[-1]
            self.current_box = current

            # directions vers des voisins non visitésh
            neighbours: list[Any] = []
            for direction in Direction:
                try:
                    neighbour = self.grid.get_neighbour(current, direction)
                    if (
                        not neighbour.is_visited
                        and not neighbour.is_on_ft_pattern
                    ):
                        neighbours.append((direction, neighbour))
                except OutOfBoundError:
                    pass

            if neighbours:
                # on choisit un voisin au hasard
                direction, neighbour = random.choice(neighbours)
                if self.grid.break_wall(current, direction):
                    neighbour.is_visited = True
                    # on avance
                    stack.append(neighbour)
                else:
                    pass
            else:
                # cul-de-sac on recule
                stack.pop()

        if not self.is_perfect:
            n: int = 0
            while n <= 10:
                box = random.choice(self.grid.get_boxes())
                directions = list(Direction)
                random.shuffle(directions)

                for direction in directions:
                    try:
                        neighbour = self.grid.get_neighbour(box, direction)
                        if box.walls[direction]:
                            self.grid.break_wall(box, direction)
                            break
                    except OutOfBoundError:
                        pass
                n += 1

        return True
