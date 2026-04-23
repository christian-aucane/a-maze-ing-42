from enum import Enum


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


COLORS: dict[str, Colors] = {
    "wight": Colors.WIGHT,
    "red": Colors.RED,
    "green": Colors.GREEN,
    "brown": Colors.BROWN,
    "blue": Colors.BLUE,
    "purple": Colors.PURPLE,
    "cyan": Colors.CYAN,
    "light_gray": Colors.LIGHT_GRAY,
    "dark_gray": Colors.DARK_GRAY,
    "light_red": Colors.LIGHT_RED,
    "light_green": Colors.LIGHT_GREEN,
    "yellow": Colors.YELLOW,
    "light_blue": Colors.LIGHT_BLUE,
    "light_purple": Colors.LIGHT_PURPLE,
    "light_cyan": Colors.LIGHT_CYAN,
    "light_white": Colors.LIGHT_WHITE}
