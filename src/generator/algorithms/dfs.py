from .abstract import GenerationAlgorithm
from src.common import Direction
from typing import Any
import random

from src.grid import OutOfBoundError


class DFS(GenerationAlgorithm):
    def run(self) -> bool:

        # pile du chemin
        stack = [self.current_box]
        self.current_box.is_visited = True
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

            for row in self.grid.grid:
                for box in row:
                    box.is_visited = False
            
            nb: int = 0

            while nb < 10:
                random_row = random.choice(self.grid.grid)
                current = random.choice(random_row)
                for direction, value in current.walls.items():
                    if ((current.x == 0 and direction == Direction.EAST) or
                        (current.x == (len(row) - 1) and direction == Direction.WEST)
                        or (current.y == 0 and direction == Direction.NORTH) or
                        (current.y == (len(self.grid.grid) - 1) and direction == Direction.SOUTH)):
                        continue
                    if value:
                        self.grid.break_wall(current, direction)
                        nb += 1
                
            

            # print("current", self.current_box)
            # self.grid.grid[0][0].walls[Direction.SOUTH] = False
            # self.grid.grid[0][0].walls[Direction.EAST] = False
            # self.current_box = self.grid.grid[0][0]
            # stack = [self.current_box]

            # while stack:
            # # sommet de la pile
            #     current = stack[-1]
            #     self.current_box = current
            #     if self.current_box == self.grid.exit:
            #         break

            #     found: bool = False

            #     for direction, value in self.current_box.walls.items():
            #         if not value:
            #             try:
            #                 neighbour = self.grid.get_neighbour(current, direction)
            #                 if not neighbour.is_visited:
            #                     neighbour.is_visited = True
            #                     stack.append(neighbour)
            #                     found = True
            #                     break
            #             except OutOfBoundError:
            #                 pass

            #     if not found:
            #         if break_bool % 2 == 0:
            #             self.grid.break_wall(current, direction)
            #             break_bool += 1
            #         stack.pop()
        return True
