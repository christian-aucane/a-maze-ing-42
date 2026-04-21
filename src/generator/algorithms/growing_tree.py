from .abstract import GenerationAlgorithm
import random


class GrowingTree(GenerationAlgorithm):
    def __init__(self, grid, is_perfect, ratio):
        super().__init__(grid, is_perfect)
        self.ratio = ratio

    def get_current(self, active_list):
        if random.random() <= self.ratio:
            return active_list[-1]
        return random.choice(active_list)

    def run(self) -> bool:
        active_list = [self.grid.entry]
        self.current_box.is_visited = True
        print(
            f"GrowingTree start: entry={self.grid.entry}, exit={self.grid.exit}"
        )

        while active_list:
            current = self.get_current(active_list)
