from typing import TypedDict


class Direction(Enum):
    NORTH = (0, +1)
    SOUTH = (0, -1)
    EAST = (1, 0)
    WEST = (-1, 0)


class BoxWalls(TypedDict):
    Direction.NORTH: bool
    Direction.SOUTH: bool
    Direction.EAST: bool
    Direction.WEST: bool


class Box:
    @staticmethod
    def _generate_walls():
        return {
            Direction.NORTH: True,
            Direction.SOUTH: True,
            Direction.EAST: True,
            Direction.WEST: True,
        }

    def __init__(self, x: int, y: int):
        self.x = x
        self.y = y
        self.is_visited = False
        self.walls = self._generate_walls()

    def break_wall(self, direction: Direction):
        self.walls[direction] = False

    def is_wall(self, direction: Direction):
        return self.walls[direction]

    def get_neighbour_pos(self, direction: Direction):
        dx, dy = direction.value
        return (self.x + dx, self.y + dy)


class GridError(Exception): ...


class Grid:
    def _generate_grid(self):
        grid = []
        for y in range(self.height):
            grid.append([Box(x, y) for x in range(self.width)])
        return grid

    def is_bounded(self, x: int, y: int) -> bool:
        return 0 <= x < self.width and 0 <= y < height

    def get_box(self, x: int, y: int) -> box:
        if self.is_bounded(x, y):
            return self.grid[y][x]
        raise GridError(f"Grid error at (x={x}, y={y}): Box is out of bound")

    def get_neighbour(self, box: Box, direction: Direction):
        x, y = box.get_neighbour_pos(direction)
        try:
            return self.get_box(x, y)
        except GridError:
            return None

    def break_wall(self, box: Box, direction: Direction): ...

    def __init__(self, width: int, height: int):
        self.width = width
        self.height = height
        self.grid = self._generate_grid()

    ...

    ...


class Grid:
    ...

    ...


class Grid:
    ...

    ...


class Grid: ...
