from .abstract import GenerationAlgorithm
from src.common import Direction


class TestGenerationAlgorithm(GenerationAlgorithm):
    def run(self) -> bool:
        self.break_and_move(direction=Direction.SOUTH)
        return True
