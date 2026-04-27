from .abstract import SolvingAlgorithm
from src.common import Direction
from src.grid import MazeBox, MazeGrid


from src.grid import OutOfBoundError


class DFSSolver(SolvingAlgorithm):
    def run(self) -> list[Direction]:
        if self.perfect:
            # pile du chemin
            for row in self.grid.grid:
                for box in row:
                    box.is_visited = False

            stack: list[MazeBox] = [self.current_box]
            self.current_box.is_visited = True
            solutions: list[Direction] = []

            while stack:
                # sommet de la pile
                current = stack[-1]
                self.current_box = current
                if self.current_box == self.grid.exit:
                    break

                found: bool = False

                for direction, value in self.current_box.walls.items():
                    if not value:
                        try:
                            neighbour = self.grid.get_neighbour(current,
                                                                direction)
                            if not neighbour.is_visited:
                                neighbour.is_visited = True
                                stack.append(neighbour)
                                solutions.append(direction)
                                found = True
                                break
                        except OutOfBoundError:
                            pass

                if not found:
                    stack.pop()
                    if solutions:
                        solutions.pop()

            return solutions

        elif not self.perfect:
            oposite = MazeGrid._get_oposite_direction
            # remetre les cellu non visité
            for row in self.grid.grid:
                for box in row:
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
            print("current: ", current)
            neighbours_rev: list[MazeBox] = []
            solution: list[Direction] = []
            while current != self.grid.entry:

                neighbours_rev = []
                for direction, value in current.walls.items():
                    if not value:
                        try:
                            neighbour = self.grid.get_neighbour(current,
                                                                direction)
                            if current.id == neighbour.id + 1:
                                current = neighbour
                                neighbours_rev.append(neighbour)
                                solution.append(oposite(direction))
                        except OutOfBoundError:
                            pass
                # if neighbours_rev:
                #     current = min(neighbours_rev, key=lambda box: box.id)

        return solution[::-1]
