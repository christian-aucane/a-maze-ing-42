from .abstract import SolvingAlgorithm
from .test_algo import TestSolvingAlgorithm
from .a_star import AStar

"""
Algo sample
'dfs': DfsAlgorithm
"""

SOLVING_ALGORITHMS_CLASSES: dict[str, type[SolvingAlgorithm]] = {
    "test": TestSolvingAlgorithm,
    "A*": AStar,
}

__all__ = ["SOLVING_ALGORITHMS_CLASSES", "SolvingAlgorithm"]
