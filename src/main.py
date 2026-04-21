
from .config import parse_config_file
from .generator.maze_generator import generate_maze
from .solver import solve_maze


def run(config_file_path: str) -> int:
    # Parse configuration
    config = parse_config_file(config_file_path=config_file_path)
    if config is None:
        print("Error: failed to parse config file.")
        return 1

    # Generate maze
    maze = generate_maze(config=config)
    if maze is None:
        print("Error: failed to generate maze.")
        return 1
    print(f"grid after:\n{maze.get_debug()}")

    # Solve maze
    solution = solve_maze(maze=maze, config=config)
    if solution is None:
        print("Error: failed to solve maze.")
        return 1

    # Print for debug
    print(f"CONFIG:\n{config}\n")
    print(f"MAZE:\n{maze}\n")
    print(f"SOLUTION:\n{solution}\n")

    # TODO: write output file, run UI (cli or gui)
    # (move all in ui ? can restart ...etc )
    return 0
