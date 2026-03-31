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

    def _get_oposite_direction(self, direction: Direction) -> Direction:
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
            neighbour.break_wall(self._get_oposite_direction())
            return True
        return False
