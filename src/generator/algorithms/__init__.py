from .abstract import GenerationAlgorithm
from .dfs import DFS

"""
Algo sample
'dfs': DfsAlgorithm
"""

GENERATION_ALGORITHMS_CLASSES: dict[str, type[GenerationAlgorithm]] = {
    "dfs": DFS}

__all__ = ["GENERATION_ALGORITHMS_CLASSES"]
