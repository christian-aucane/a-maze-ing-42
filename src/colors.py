from enum import Enum
from .grid import MazeGrid


class Colors(Enum):
    WIGHT = ""
    RED = "\033[0;31m"
    GREEN = "\033[0;32m"
    BROWN = "\033[0;33m"
    BLUE = "\033[0;34m"
    PURPLE = "\033[0;35m"
    CYAN = "\033[0;36m"
    LIGHT_GRAY = "\033[0;37m"
    DARK_GRAY = "\033[1;30m"
    LIGHT_RED = "\033[1;31m"
    LIGHT_GREEN = "\033[1;32m"
    YELLOW = "\033[1;33m"
    LIGHT_BLUE = "\033[1;34m"
    LIGHT_PURPLE = "\033[1;35m"
    LIGHT_CYAN = "\033[1;36m"
    LIGHT_WHITE = "\033[1;37m"


def change_colors_walls(colors: str, grid: MazeGrid) -> MazeGrid:
    for color in Colors:
        if colors.upper() == color.name:
            for row in grid.grid:
                for box in row:
                    box.walls_color = color
    return grid


if __name__ == "__main__":
    grid = MazeGrid(20, 10, (0, 0), (14, 9))
    grid = change_colors_walls("yellow", grid)
    for row in grid.grid:
        for box in row:
            print(box.walls_color)
