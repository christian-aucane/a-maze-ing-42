from enum import Enum


class Direction(Enum):
    NORTH = (0, -1)
    EAST = (+1, 0)
    SOUTH = (0, +1)
    WEST = (-1, 0)

    def __str__(self) -> str:
        return {
            "NORTH": "↑",
            "SOUTH": "↓",
            "EAST": "→",
            "WEST": "←"
        }[self.name]

    def get_oposite(self) -> "Direction":
        return {
            Direction.NORTH: Direction.SOUTH,
            Direction.SOUTH: Direction.NORTH,
            Direction.EAST: Direction.WEST,
            Direction.WEST: Direction.EAST,
        }[self]

    def get_output(self) -> str:
        return self.name[0]
