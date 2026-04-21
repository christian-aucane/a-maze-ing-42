from .abstract import SolvingAlgorithm
from src.common import Direction


class TestSolvingAlgorithm(SolvingAlgorithm):
    def run(self) -> list[Direction] | None:
        return [Direction.SOUTH, Direction.EAST, Direction.SOUTH]
