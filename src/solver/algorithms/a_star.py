from .abstract import SolvingAlgorithm
from src.common import Direction
from src.grid import MazeGrid, MazeBox


class AStar(SolvingAlgorithm):
    def __init__(self, grid: MazeGrid):
        super().__init__(grid)
        start = self.grid.entry
        self.open_set = {start}
        self.closed_set = set()
        self.g_score = {start: 0}
        self.parents = {start: None}

    def get_h(self, cell: MazeBox):
        return abs(cell.x - self.grid.exit.x) + abs(cell.y - self.grid.exit.y)

    def get_g(self, cell: MazeBox):
        return self.g_score[cell]

    def get_f(self, cell: MazeBox):
        return self.get_h(cell) + self.get_g(cell)

    def get_best_cell(self):
        return min(self.open_set, key=self.get_f)

    def expand(self, current: MazeBox):
        self.open_set.remove(current)
        self.closed_set.add(current)
        for cell in self.grid.get_open_neighbours(current):
            if cell in self.closed_set:
                continue
            g_new = self.get_g(current) + 1
            g_score = self.g_score.get(cell)
            if g_score is not None and g_score <= g_new:
                continue
            self.g_score[cell] = g_new
            self.open_set.add(cell)
            self.parents[cell] = current

    @staticmethod
    def get_direction(cell_a: MazeBox, cell_b: MazeBox) -> Direction | None:
        try:
            return Direction((cell_b.x - cell_a.x, cell_b.y - cell_a.y))
        except ValueError:
            return None
        # TODO: Retrouver la direction !!
        return Direction((cell_b.x - cell_a.x, cell_b.y - cell_a.y))

    def run(self) -> list[Direction]:
        while self.open_set:
            current = self.get_best_cell()
            if current == self.grid.exit:
                break
            self.expand(current)
        if self.grid.exit not in self.parents:
            return []  # TODO:  RETOURNER None en cas de sortie pas trouvee ??
        cells = []
        current = self.grid.exit
        while current is not None:
            cells.insert(0, current)
            current = self.parents[current]
        solution = []
        for i in range(len(cells) - 1):
            solution.append(self.get_direction(cells[i], cells[i + 1]))
        return solution
