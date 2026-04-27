from typing import Generator
from .common import Direction


class OutOfBoundError(Exception):
    pass


class MazeBox:
    def _get_bin(self) -> str:
        bin_lst = [f"{int(self.walls[dir])}" for dir in list(Direction)]
        return "".join(bin_lst)

    def _get_hexa(self) -> str:
        hex_values = "0123456789ABCDEF"
        return hex_values[int(self._get_bin(), 2)]

    def __init__(
        self,
        x: int,
        y: int,
        is_on_ft_pattern: bool = False,
        is_entry: bool = False,
        is_exit: bool = False,
    ) -> None:
        self.x = x
        self.y = y
        self.id: int = 0
        self.is_on_ft_pattern = is_on_ft_pattern
        self.is_visited = False
        self.is_entry = is_entry
        self.is_exit = is_exit
        self.walls = {direction: True for direction in Direction}

    def __str__(self) -> str:
        return f"Box(x={self.x}, y={self.y}, walls_bin={self._get_bin()})"

    def get_output(self) -> str:
        return self._get_hexa()

    def break_wall(self, direction: Direction) -> None:
        self.walls[direction] = False

    def is_wall(self, direction: Direction) -> bool:
        return self.walls[direction]

    def get_neighbour_pos(self, direction: Direction) -> tuple[int, int]:
        dx, dy = direction.value
        return (self.x + dx, self.y + dy)

    def get_open_directions(
        self, previous_direction: Direction | None = None
    ) -> tuple[Direction, ...]:
        return tuple(
            dir
            for dir, wall in self.walls.items()
            if not wall and dir is not previous_direction
        )


class MazeGrid:
    FT_PATTERN = ["X   XXX", "X     X", "XXX XXX", "  X X  ", "  X XXX"]

    def _is_on_ft_pattern(self, x: int, y: int) -> bool:
        x_correction = int(self.width % 2 == 1)
        y_correction = int(self.height % 2 == 1)
        border_width = (self.width - 7 - x_correction) // 2
        border_height = (self.height - 5 - y_correction) // 2
        x_in_pattern = (
            border_width < x < self.width - border_width - x_correction
        )
        y_in_pattern = (
            border_height < y < self.height - border_height - y_correction
        )
        if x_in_pattern and y_in_pattern:
            x_pattern = x - border_width - 1
            y_pattern = y - border_height - 1
            if self.FT_PATTERN[y_pattern][x_pattern] == "X":
                return True
        return False

    def _generate_grid(
        self, entry: tuple[int, int], exit: tuple[int, int]
    ) -> list[list[MazeBox]]:
        skip_pattern = self.width < 9 or self.height < 7
        if skip_pattern:
            print(
                f"The size (width={self.width}, "
                f"height={self.height}) "
                "do not permite to draw '42' pattern in the maze!\n"
                "Minimum width required = 9, Mimimum height required = 7"
            )
        grid = []
        for y in range(self.height):
            row = []
            for x in range(self.width):
                row.append(
                    MazeBox(
                        x=x,
                        y=y,
                        is_on_ft_pattern=self._is_on_ft_pattern(x, y)
                        if not skip_pattern
                        else False,
                        is_entry=(x, y) == entry,
                        is_exit=(x, y) == exit,
                    )
                )
            grid.append(row)
        return grid

    def get_neighbour(self, box: MazeBox, direction: Direction) -> MazeBox:
        x, y = box.get_neighbour_pos(direction)
        return self.get_box(x, y)

    def _is_bounded(self, x: int, y: int) -> bool:
        return 0 <= x < self.width and 0 <= y < self.height

    def __init__(
        self,
        width: int,
        height: int,
        entry: tuple[int, int],
        exit: tuple[int, int],
    ) -> None:
        self._width = width
        self._height = height
        self._grid = self._generate_grid(entry, exit)
        self._entry = self.get_box(*entry)
        self._exit = self.get_box(*exit)

    @property
    def width(self) -> int:
        return self._width

    @property
    def height(self) -> int:
        return self._height

    @property
    def entry(self) -> MazeBox:
        return self._entry

    @property
    def exit(self) -> MazeBox:
        return self._exit

    def iterrows(self) -> Generator[list[MazeBox]]:
        for row in self._grid:
            yield row[:]

    def get_output(self) -> str:
        output_lst = [
            "".join(map(lambda box: box.get_output(), row))
            for row in self._grid
        ]
        return "\n".join(output_lst)

    def get_box(self, x: int, y: int) -> MazeBox:
        if self._is_bounded(x, y):
            return self._grid[y][x]
        raise OutOfBoundError(
            f"Grid error at (x={x}, y={y}): Box is out of bound"
        )

    def get_boxes(self) -> list[MazeBox]:
        return [box for row in self._grid for box in row]

    def break_wall(self, box: MazeBox, direction: Direction) -> bool:
        try:
            neighbour = self.get_neighbour(box, direction)
        except OutOfBoundError:
            return False
        if box.is_on_ft_pattern or neighbour.is_on_ft_pattern:
            return False
        box.break_wall(direction)
        neighbour.break_wall(direction.get_oposite())
        return True

    def get_open_neighbours(self, box: MazeBox) -> list[MazeBox]:
        neighbours = []
        for dir in box.get_open_directions():
            try:
                neighbours.append(self.get_neighbour(box, dir))
            except OutOfBoundError:
                continue
        return neighbours
