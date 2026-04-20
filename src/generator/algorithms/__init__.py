from .test_algo import TestGenerationAlgorithm
from .dfs import DFS

"""
Algo sample
'dfs': DfsAlgorithm
"""

GENERATION_ALGORITHMS_CLASSES = {"test": TestGenerationAlgorithm, "dfs": DFS}

__all__ = ["GENERATION_ALGORITHMS_CLASSES"]
