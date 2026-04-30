from .abstract import SolvingAlgorithm
from .dfs_solver import BFS
from .test_algo import TestSolvingAlgorithm
from .a_star import AStar

"""
Algo sample
'dfs': DfsAlgorithm
"""

SOLVING_ALGORITHMS_CLASSES: dict[str, type[SolvingAlgorithm]] = {
    "test": TestSolvingAlgorithm,
    "bfs": BFS,
    "A*": AStar,
}

__all__ = ["SOLVING_ALGORITHMS_CLASSES", "SolvingAlgorithm"]
