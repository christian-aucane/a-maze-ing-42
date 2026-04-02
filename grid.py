from typing import TypedDict
from enum import Enum


class Direction(Enum):
    NORTH = (0, -1)
    EAST = (+1, 0)
    SOUTH = (0, +1)
    WEST = (-1, 0)


class BoxWalls(TypedDict):
    Direction.NORTH: bool
    Direction.EAST: bool
    Direction.SOUTH: bool
    Direction.WEST: bool


class Box:
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

    def __init__(self, x: int, y: int) -> None:
        self.x = x
        self.y = y
        self.is_visited = False
        self.walls = self._generate_walls()

    def __str__(self) -> str:
        return f"Box(x={self.x}, y={self.y}, walls_bin={self._get_bin()})"

    def get_output(self) -> str:
        return self._get_hexa()

    def break_wall(self, direction: Direction):
        self.walls[direction] = False

    def is_wall(self, direction: Direction):
        return self.walls[direction]

    def get_neighbour_pos(self, direction: Direction):
        dx, dy = direction.value
        return (self.x + dx, self.y + dy)

    def get_open_directions(self, box: "Box", previous_direction: Direction):
        return tuple(dir for dir, wall in self.walls.items() if not wall)


class GridError(Exception):
    pass


class Grid:
    def _generate_grid(self) -> list[list[Box]]:
        grid = []
        for y in range(self.height):
            grid.append([Box(x, y) for x in range(self.width)])
        return grid

    def _get_neighbour(self, box: Box, direction: Direction) -> Box | None:
        x, y = box.get_neighbour_pos(direction)
        try:
            return self.get_box(x, y)
        except GridError:
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

    def get_box(self, x: int, y: int) -> Box:
        if self._is_bounded(x, y):
            return self.grid[y][x]
        raise GridError(f"Grid error at (x={x}, y={y}): Box is out of bound")

    def get_boxes(self) -> list[Box]:
        return [box for row in self.grid for box in row]

    def break_wall(self, box: Box, direction: Direction) -> bool:
        neighbour = self._get_neighbour(box, direction)
        if neighbour is not None:
            box.break_wall(direction)
            neighbour.break_wall(self._get_oposite_direction(direction))
            return True
        return False


if __name__ == "__main__":
    grid = Grid(10, 10)
    start = grid.get_box(4, 4)
    print(f"grid before :\n{grid.get_output()}")
    for direction in Direction:
        print(
            f"DEBUG: grid.break_wall({start}, {direction}) -> {
                grid.break_wall(start, direction)
            }"
        )
    print(start)
    print(f"grid after:\n{grid.get_output()}")
