from src.grid import MazeGrid
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
    def update_grid(grid: MazeGrid, solution: list[Direction]) -> None:
        # TODO: catch OutOfBoundError ??
        current = grid.entry
        for dir in solution:
            current.solution_dir = dir
            current = grid.get_neighbour(current, dir)

    def solve_maze(self, grid: MazeGrid) -> list[Direction] | None:
        algo = self.algo_class(grid=grid)
        solution = algo.run()
        if solution is not None:
            self.update_grid(grid=grid, solution=solution)
        return solution


def solve_maze(maze: MazeGrid, config: Config) -> list[Direction] | None:
    solver = MazeSolver(algo_name=config.solve_algorithm)
    solution = solver.solve_maze(maze)
    if solution is None:
        print("No solution found...")
    return solution
