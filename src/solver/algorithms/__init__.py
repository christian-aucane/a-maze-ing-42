from .abstract import SolvingAlgorithm
from .dfs_solver import DFSSolver
from .test_algo import TestSolvingAlgorithm

"""
Algo sample
'dfs': DfsAlgorithm
"""

SOLVING_ALGORITHMS_CLASSES: dict[str, type[SolvingAlgorithm]] = {
    "test": TestSolvingAlgorithm,
    "dfs_solver": DFSSolver
}

__all__ = ["SOLVING_ALGORITHMS_CLASSES", "SolvingAlgorithm"]
