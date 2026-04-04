from .grid import MazeGrid
from .common import Direction, Config


class MazeSolver:
    # TODO: separer l'algo et faire de la composition ?
    def __init__(self, algo: str):
        self.algo = algo

    def solve_maze(self, maze: MazeGrid) -> list[Direction] | None: ...


def solve_maze(maze: MazeGrid, config: Config) -> list[Direction] | None:
    solver = MazeSolver(algo=config.solve_algo)
    solution = solver.solve_maze(maze)
    if solution is None:
        print("No solution found...")
    return solution
