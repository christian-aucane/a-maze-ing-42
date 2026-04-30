from .grid import MazeGrid, MazeBox
from .colors import ColorsPattern, ColorsWalls
from .common import Direction


class AsciiRenderer:
    END_COLOR = "\033[0m"

    def __init__(
        self,
        walls_color: ColorsWalls = ColorsWalls.WHITE,
        pattern_color: ColorsPattern = ColorsPattern.RED,
    ) -> None:
        self.walls_color = walls_color.value
        self.pattern_color = pattern_color.value
        self.display_solution = False

    def toggle_display_solution(self) -> None:
        self.display_solution = not self.display_solution

    def _get_north_wall(self, cell: MazeBox) -> str:
        return (
            f"{self.walls_color}+---{self.END_COLOR}"
            if cell.walls[Direction.NORTH]
            else f"{self.walls_color}+   {self.END_COLOR}"
        )

    def _get_south_wall(self, cell: MazeBox) -> str:
        return (
            f"{self.walls_color}+---{self.END_COLOR}"
            if cell.walls[Direction.SOUTH]
            else f"{self.walls_color}+   {self.END_COLOR}"
        )

    def _get_cell_center(
        self, cell: MazeBox, solution_dir: Direction | None = None
    ) -> str:
        wall_left = "|" if cell.walls[Direction.WEST] else " "
        if cell.is_on_ft_pattern:
            return (
                f"{self.walls_color}{wall_left}{self.END_COLOR}"
                f"{self.pattern_color}   {self.END_COLOR}"
            )
        elif cell.is_entry:
            return f"{self.walls_color}{wall_left} 0 {self.END_COLOR}"
        elif cell.is_exit:
            return f"{self.walls_color}{wall_left} - {self.END_COLOR}"
        elif self.display_solution and solution_dir is not None:
            return (
                f"{self.walls_color}{wall_left}{self.END_COLOR} {solution_dir} "
            )
        else:
            return f"{self.walls_color}{wall_left}   {self.END_COLOR}"

    def render(self, maze: MazeGrid, solution: dict[MazeBox, Direction]) -> str:
        output_lst: list[str] = []
        for row in maze.iterrows():
            output_lst.append(
                "".join(self._get_north_wall(cell) for cell in row)
                + f"{self.walls_color}+{self.END_COLOR}"
            )

            output_lst.append(
                "".join(
                    self._get_cell_center(
                        cell=cell, solution_dir=solution.get(cell)
                    )
                    for cell in row
                )
                + f"{self.walls_color}|{self.END_COLOR}"
            )
        output_lst.append(
            "".join(self._get_south_wall(cell) for cell in row)
            + f"{self.walls_color}+{self.END_COLOR}"
        )

        return "\n".join(output_lst)
