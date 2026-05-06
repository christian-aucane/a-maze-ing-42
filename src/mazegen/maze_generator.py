from typing import Optional
import random

from .grid import MazeGrid, MazeBox
from .gen_algo import GENERATION_ALGORITHMS_CLASSES, GenerationAlgorithm
from .solve_algo import SOLVING_ALGORITHMS_CLASSES, SolvingAlgorithm
from .common import Direction


class MazeGenerator:
    """
    Algo sample
    'dfs': {
        'class': DfsAlgorithm,
        'args': [args...],     # Optionnal
        'kwargs': {kwargs...}  # Optionnal
    """

    gen_algo_class: type[GenerationAlgorithm]
    solve_algo_class: type[SolvingAlgorithm]

    # TODO: separer l'algo et faire de la composition ?
    def __init__(self, width: int,
                 height: int,
                 seed: int | None = None,
                 is_perfect: bool = False,
                 entry: tuple[int, int] = (0, 0),
                 exit: tuple[int, int] | None = None,
                 gen_algo_name: str = "dfs",
                 solve_algo_name: str = "BFS") -> None:

        self.width = width
        self.height = height
        self.entry = entry
        self.exit = self.get_exit(exit, width, height)
        self.is_perfect = is_perfect
        self.seed = seed
        try:
            self.gen_algo_class = GENERATION_ALGORITHMS_CLASSES[
                gen_algo_name.lower()]
        except KeyError:
            raise ValueError(
                f"Invalid algorithm name '{gen_algo_name}' ... Valid names: "
                f"{GENERATION_ALGORITHMS_CLASSES.keys()}"
            )
        try:
            self.solve_algo_class = SOLVING_ALGORITHMS_CLASSES[
                solve_algo_name.lower()]
        except KeyError:
            raise ValueError(
                "Invalid algorithm name ... Valid names: "
                f"{SOLVING_ALGORITHMS_CLASSES.keys()}"
            )

    def get_exit(self, exit: tuple[int, int] | None, width: int,
                 height: int) -> tuple[int, int]:
        if not exit:
            return (width - 1, height - 1)
        return exit

    def generate(self) -> Optional[MazeGrid]:
        if self.seed:
            random.seed(self.seed)
        grid = MazeGrid(self.width, self.height, self.entry, self.exit)
        algo = self.gen_algo_class(grid=grid, is_perfect=self.is_perfect)
        if algo.run():
            return grid
        return None

    # solve methode
    @staticmethod
    def _get_solution_dict(grid: MazeGrid,
                           solution: list[Direction]
                           ) -> dict[MazeBox, Direction]:
        # TODO: catch OutOfBoundError ??
        output = {}
        current = grid.entry
        for dir in solution:
            output[current] = dir
            current = grid.get_neighbour(current, dir)
        return output

    def solve(self, grid: MazeGrid) -> dict[MazeBox, Direction] | None:
        algo = self.solve_algo_class(grid=grid)
        solution = algo.run()
        if solution is not None:
            return self._get_solution_dict(grid, solution)
