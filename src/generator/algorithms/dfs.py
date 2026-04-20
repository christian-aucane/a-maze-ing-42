from .abstract import GenerationAlgorithm
from src.grid import MazeGrid, OutOfBoundError, MazeBox
from src.common import Direction
import random


class DFS(GenerationAlgorithm):

    def run(self) -> bool:
        if self.grid.seed:
            random.seed(self.grid.seed)

        # pile du chemin
        stack = [self.entry]
        self.entry.is_visited = True
        print(f"DFS start: entry={self.entry}, exit={self.exit}")

        while stack:
            # sommet de la pile
            current = stack[-1]
            self.current_box = current

            # directions vers des voisins non visités
            neighbours: list[Direction, MazeBox] = []
            for direction in Direction:
                try:
                    neighbour = self.grid.get_neighbour(current, direction)
                    if not neighbour.is_visited:
                        neighbours.append((direction, neighbour))
                except Exception:
                    pass

            if neighbours:
                # on choisit un voisin au hasard
                direction, neighbour = random.choice(neighbours)
                self.grid.break_wall(current, direction)
                neighbour.is_visited = True
                # on avance
                stack.append(neighbour)
            else:
                # cul-de-sac → on recule
                stack.pop()

        visited = sum(1 for box in self.grid.get_boxes() if box.is_visited)
        print(f"DFS end: {visited}/{self.grid.width * self.grid.height} cases visitées")

        broken_east_west = sum(
            1 for box in self.grid.get_boxes()
            if not box.walls[Direction.EAST] or not box.walls[Direction.WEST])
        broken_north_south = sum(
            1 for box in self.grid.get_boxes()
            if not box.walls[Direction.NORTH] or not box.walls[Direction.SOUTH])
        print(f"Murs E/W cassés: {broken_east_west}")
        print(f"Murs N/S cassés: {broken_north_south}")
        print(f"walls box(0,0): {self.grid.get_box(0,0).walls}")
        print(f"walls box(1,0): {self.grid.get_box(1,0).walls}")

        return True
        # self.current_box = self.entry
        # i: int = 0
        # list_direction: list[Direction] = list(Direction)
        # while self.current_box != self.exit:
        #     self.current_box.is_visited = True
        #     direction = random.choice(list_direction)
            
        #     print("direction :", direction)
        #     if self.break_and_move(direction=direction):
        #         list_direction: list[Direction] = list(Direction)
        #     list_direction.remove(direction)
        #     if len(list_direction) == 0:
        #         self.reverse(1)
        #     i += 1
        # return True

# self.current_box != self.exit