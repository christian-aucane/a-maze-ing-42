from src.grid import MazeGrid, MazeBox
from src.common import Direction
from src.config import Config
from .algorithms import SOLVING_ALGORITHMS_CLASSES, SolvingAlgorithm


class MazeSolver:
    algo_class: type[SolvingAlgorithm]

    def __init__(self, algo_name: str):
        try:
            self.algo_class = SOLVING_ALGORITHMS_CLASSES[algo_name]
        except KeyError:
            raise ValueError(
                "Invalid algorithm name ... Valid names: "
                f"{SOLVING_ALGORITHMS_CLASSES.keys()}"
            )

    @staticmethod
    def _get_solution_dict(
        grid: MazeGrid, solution: dict[MazeBox, Direction]
    ) -> None:
        # TODO: catch OutOfBoundError ??
        output = {}
        current = grid.entry
        for dir in solution:
            output[current] = dir
            current = grid.get_neighbour(current, dir)
        return output

    def solve_maze(self, grid: MazeGrid) -> dict[MazeBox, Direction] | None:
        algo = self.algo_class(grid=grid)
        solution = algo.run()
        if solution is not None:
            return self._get_solution_dict(grid, solution)


def solve_maze(
    maze: MazeGrid, config: Config
) -> dict[MazeBox, Direction] | None:
    solver = MazeSolver(algo_name=config.solve_algorithm)
    solution = solver.solve_maze(maze)
    if solution is None:
        print("No solution found...")
    return solution
