from .abstract import GenerationAlgorithm
from .dfs import DFS
from .kruskal import Kruskal

"""
Algo sample
'dfs': DfsAlgorithm
"""

GENERATION_ALGORITHMS_CLASSES: dict[str, type[GenerationAlgorithm]] = {
    "dfs": DFS,
    "kruskal": Kruskal,
}

__all__ = ["GENERATION_ALGORITHMS_CLASSES", "GenerationAlgorithm"]
