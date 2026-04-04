from .parser import parse_config_file
from .generator import generate_maze
from .solver import solve_maze


def run(config_file_path: str) -> int:
    if config := parse_config_file(config_file_path=config_file_path) is None:
        return 1
    if maze := generate_maze(config=config) is None:
        return 1
    if solution := solve_maze(maze=maze) is None:
        return 1
    print(f"CONFIG:\n{config}\n")
    print(f"MAZE:\n{maze}\n")
    print(f"SOLUTION:\n{solution}")
    # TODO: write output file, and run UI (gui or cli)
    return 0
