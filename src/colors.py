from enum import Enum


class ColorsWalls(Enum):
    WHITE = ""
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


class ColorsPattern(Enum):
    WHITE = ""
    RED = "\033[41m"
    GREEN = "\033[42m"
    BROWN = "\033[43m"
    BLUE = "\033[44m"
    PURPLE = "\033[45m"
    CYAN = "\033[46m"
    LIGHT_GRAY = "\033[47m"
    DARK_GRAY = "\033[100m"
    LIGHT_RED = "\033[101m"
    LIGHT_GREEN = "\033[102m"
    YELLOW = "\033[103m"
    LIGHT_BLUE = "\033[104m"
    LIGHT_PURPLE = "\033[105m"
    LIGHT_CYAN = "\033[106m"
    LIGHT_WHITE = "\033[107m"


COLORS_WALLS: dict[str, ColorsWalls] = {
    "white": ColorsWalls.WHITE,
    "red": ColorsWalls.RED,
    "green": ColorsWalls.GREEN,
    "brown": ColorsWalls.BROWN,
    "blue": ColorsWalls.BLUE,
    "purple": ColorsWalls.PURPLE,
    "cyan": ColorsWalls.CYAN,
    "light_gray": ColorsWalls.LIGHT_GRAY,
    "dark_gray": ColorsWalls.DARK_GRAY,
    "light_red": ColorsWalls.LIGHT_RED,
    "light_green": ColorsWalls.LIGHT_GREEN,
    "yellow": ColorsWalls.YELLOW,
    "light_blue": ColorsWalls.LIGHT_BLUE,
    "light_purple": ColorsWalls.LIGHT_PURPLE,
    "light_cyan": ColorsWalls.LIGHT_CYAN,
    "light_white": ColorsWalls.LIGHT_WHITE,
}

COLORS_PATTERN: dict[str, ColorsPattern] = {
    "white": ColorsPattern.WHITE,
    "red": ColorsPattern.RED,
    "green": ColorsPattern.GREEN,
    "brown": ColorsPattern.BROWN,
    "blue": ColorsPattern.BLUE,
    "purple": ColorsPattern.PURPLE,
    "cyan": ColorsPattern.CYAN,
    "light_gray": ColorsPattern.LIGHT_GRAY,
    "dark_gray": ColorsPattern.DARK_GRAY,
    "light_red": ColorsPattern.LIGHT_RED,
    "light_green": ColorsPattern.LIGHT_GREEN,
    "yellow": ColorsPattern.YELLOW,
    "light_blue": ColorsPattern.LIGHT_BLUE,
    "light_purple": ColorsPattern.LIGHT_PURPLE,
    "light_cyan": ColorsPattern.LIGHT_CYAN,
    "light_white": ColorsPattern.LIGHT_WHITE,
}
