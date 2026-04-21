from .abstract import SolvingAlgorithm
from .test_algo import TestSolvingAlgorithm

"""
Algo sample
'dfs': DfsAlgorithm
"""

SOLVING_ALGORITHMS_CLASSES: dict[str, type[SolvingAlgorithm]] = {
    "test": TestSolvingAlgorithm
}

__all__ = ["SOLVING_ALGORITHMS_CLASSES", "SolvingAlgorithm"]
