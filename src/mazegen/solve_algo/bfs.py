from .abstract import SolvingAlgorithm
from ..common import Direction
from ..grid import MazeBox, OutOfBoundError


class BFS(SolvingAlgorithm):
    def run(self) -> list[Direction]:

        # remetre les cellu non visité
        for box in self.grid.get_boxes():
            box.is_visited = False
        self.grid.entry.id = 1
        self.grid.entry.is_visited = True
        queue: list[MazeBox] = [self.grid.entry]
        neighbours: list[MazeBox] = []
        while queue:
            neighbours = []
            for box in queue:
                for direction, value in box.walls.items():
                    if not value:
                        try:
                            neighbour = self.grid.get_neighbour(box,
                                                                direction)
                            if not neighbour.is_visited:
                                neighbour.is_visited = True
                                neighbour.id = box.id + 1
                                neighbours.append(neighbour)
                        except OutOfBoundError:
                            pass
            queue = neighbours
        current = self.grid.exit
        solution: list[Direction] = []

        while current != self.grid.entry:
            found = False

            for direction, value in current.walls.items():
                if value:
                    continue
                try:
                    neighbour = self.grid.get_neighbour(current,
                                                        direction)
                except OutOfBoundError:
                    continue

                if current.id == neighbour.id + 1:
                    current = neighbour
                    solution.append(direction.get_oposite())
                    found = True
                    break

            if not found:
                raise RuntimeError(f"No path found from {current} to entry")

        return solution[::-1]
