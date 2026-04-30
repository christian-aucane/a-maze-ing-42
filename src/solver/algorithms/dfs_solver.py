from .abstract import SolvingAlgorithm
from src.common import Direction
from src.grid import MazeBox


from src.grid import OutOfBoundError


class DFSSolver(SolvingAlgorithm):
    def run(self) -> list[Direction]:
        # pile du chemin
        for row in self.grid.iterrows():
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
                        neighbour = self.grid.get_neighbour(current, direction)
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
