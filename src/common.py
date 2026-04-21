from enum import Enum


class Direction(Enum):
    NORTH = (0, -1)
    EAST = (+1, 0)
    SOUTH = (0, +1)
    WEST = (-1, 0)

    def get_debug(self) -> str:
        return {
            "NORTH": "↑",
            "SOUTH": "↓",
            "EAST": "→",
            "WEST": "←"}[self.name]
