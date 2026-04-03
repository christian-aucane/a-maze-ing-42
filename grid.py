from enum import Enum


class Direction(Enum):
    NORTH = (0, -1)
    EAST = (+1, 0)
    SOUTH = (0, +1)
    WEST = (-1, 0)


class OnFtPatternError(Exception):
    pass


class MazeBox:
    @staticmethod
    def _generate_walls() -> dict[Direction, bool]:
        return {
            Direction.NORTH: True,
            Direction.EAST: True,
            Direction.SOUTH: True,
            Direction.WEST: True,
        }

    def _get_bin(self) -> str:
        bin_lst = [f"{int(self.walls[dir])}" for dir in list(Direction)]
        return "".join(bin_lst)

    def _get_hexa(self) -> str:
        hex_values = "0123456789ABCDEF"
        return hex_values[int(self._get_bin(), 2)]

    def __init__(self, x: int, y: int, is_on_ft_pattern: bool = False) -> None:
        self.x = x
        self.y = y
        self.is_on_ft_pattern = is_on_ft_pattern
        self.is_visited = False
        self.walls = self._generate_walls()

    def __str__(self) -> str:
        return f"Box(x={self.x}, y={self.y}, walls_bin={self._get_bin()})"

    def get_output(self) -> str:
        return self._get_hexa()

    def print_debug(self):
        # return "X" if all(self.walls.values()) else "."
        return "X" if self.is_on_ft_pattern else "."

    def break_wall(self, direction: Direction) -> None:
        self.walls[direction] = False

    def is_wall(self, direction: Direction) -> bool:
        return self.walls[direction]

    def get_neighbour_pos(self, direction: Direction) -> tuple[int, int]:
        dx, dy = direction.value
        return (self.x + dx, self.y + dy)

    def get_open_directions(
        self, previous_direction: Direction
    ) -> tuple[Direction, ...]:
        return tuple(
            dir
            for dir, wall in self.walls.items()
            if not wall and dir is not previous_direction
        )


class OutOfBoundError(Exception):
    pass


FT_PATTERN = ["X   XXX", "X     X", "XXX XXX", "  X X  ", "  X XXX"]


class MazeGrid:
    def _is_on_ft_pattern(self, x, y):
        x_correction = int(self.width % 2 == 1)
        y_correction = int(self.height % 2 == 1)
        border_width = (self.width - 7 - x_correction) // 2
        border_height = (self.height - 6 - y_correction) // 2
        x_in_pattern = border_width < x < self.width - border_width - x_correction
        y_in_pattern = border_height < y < self.height - border_height - y_correction
        if x_in_pattern and y_in_pattern:
            x_pattern = x - border_width - 1
            y_pattern = y - border_height - 1
            if FT_PATTERN[y_pattern][x_pattern] == "X":
                return True
        return False

    def _generate_grid(self) -> list[list[MazeBox]]:
        grid = []
        skip_pattern = self.width < 9 or self.height < 7
        if skip_pattern:
            print(
                f"The size (width={self.width}, height={
                    self.height
                }) do not permite to draw '42' pattern in the maze!\nMinimum width required = 9, Mimimum height required = 7"
            )
        for y in range(self.height):
            grid.append(
                [
                    MazeBox(
                        x=x,
                        y=y,
                        is_on_ft_pattern=(
                            self._is_on_ft_pattern(x, y) if not skip_pattern else False
                        ),
                    )
                    for x in range(self.width)
                ]
            )
        return grid

    def _get_neighbour(self, box: MazeBox, direction: Direction) -> MazeBox | None:
        x, y = box.get_neighbour_pos(direction)
        try:
            return self.get_box(x, y)
        except OutOfBoundError:
            return None

    @staticmethod
    def _get_oposite_direction(direction: Direction) -> Direction:
        return {
            Direction.NORTH: Direction.SOUTH,
            Direction.SOUTH: Direction.NORTH,
            Direction.EAST: Direction.WEST,
            Direction.WEST: Direction.EAST,
        }[direction]

    def _is_bounded(self, x: int, y: int) -> bool:
        return 0 <= x < self.width and 0 <= y < self.height

    def __init__(self, width: int, height: int) -> None:
        self.width = width
        self.height = height
        self.grid = self._generate_grid()

    def get_output(self) -> str:
        output_lst = [
            "".join(map(lambda box: box.get_output(), row)) for row in self.grid
        ]
        return "\n".join(output_lst)

    def print_debug(self) -> str:
        output_lst = [
            "".join(map(lambda box: box.print_debug(), row)) for row in self.grid
        ]
        return "\n".join(output_lst)

    def get_box(self, x: int, y: int) -> MazeBox:
        if self._is_bounded(x, y):
            return self.grid[y][x]
        raise OutOfBoundError(f"Grid error at (x={x}, y={y}): Box is out of bound")

    # TODO: use generator instead of list comprehension?
    def get_boxes(self) -> list[MazeBox]:
        return [box for row in self.grid for box in row]

    def break_wall(self, box: MazeBox, direction: Direction) -> bool:
        neighbour = self._get_neighbour(box, direction)
        if neighbour is None:
            return False
        if box.is_on_ft_pattern or neighbour.is_on_ft_pattern:
            return False
        box.break_wall(direction)
        neighbour.break_wall(self._get_oposite_direction(direction))
        return True


if __name__ == "__main__":
    grid = MazeGrid(5, 7)
    print(f"grid before:\n{grid.print_debug()}")
    for box in grid.get_boxes():
        for dir in Direction:
            grid.break_wall(box, dir)
    print(f"grid after:\n{grid.print_debug()}")
