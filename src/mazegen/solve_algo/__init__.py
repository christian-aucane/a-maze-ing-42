from .abstract import SolvingAlgorithm
from .bfs import BFS
from .a_star import AStar

"""
Algo sample
'dfs': DfsAlgorithm
"""

SOLVING_ALGORITHMS_CLASSES: dict[str, type[SolvingAlgorithm]] = {
    "bfs": BFS,
    "A*": AStar,
}

__all__ = ["SOLVING_ALGORITHMS_CLASSES", "SolvingAlgorithm"]
