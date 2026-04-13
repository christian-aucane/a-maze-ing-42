from enum import Enum


class Direction(Enum):
    # Ready to merge on an other branch
    NORTH = (0, -1)
    EAST = (+1, 0)
    SOUTH = (0, +1)
    WEST = (-1, 0)
