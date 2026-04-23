import random

from .config import parse_config_file
from .generator.maze_generator import generate_maze
from .solver.maze_solver import solve_maze


def run(config_file_path: str) -> int:
    # Parse configuration
    config = parse_config_file(config_file_path=config_file_path)
    if config is None:
        print("Error: failed to parse config file.")
        return 1
    if config.seed is not None:
        random.seed(config.seed)

    # Generate maze
    maze = generate_maze(config=config)
    if maze is None:
        print("Error: failed to generate maze.")
        return 1

    # Solve maze
    solution = solve_maze(maze=maze, config=config)
    if solution is None:
        print("Error: failed to solve maze.")
        return 1

    # Print for debug
    print(f"CONFIG:\n{config}\n")
    print(f"MAZE:\n{maze.get_debug()}\n")
    print(f"SOLUTION:\n{solution}\n")

    nbr = input("1- Regenerate Maze: \n"
                "2- Change walls color: \n"
                "3- show solution from entry to exit \n")

    if nbr and nbr == 1:
        config.seed = None
        maze = generate_maze(config=config)
        print(f"MAZE:\n{maze.get_debug()}\n")
        config 

    elif nbr and nbr == 2:
        solution = solve_maze(maze=maze, config=config)
        print(f"SOLUTION:\n{solution}\n")

    elif nbr and nbr == 3:
        color_change = input("input color: ")
        if maze.change_colors_walls(color_change):
            print(f"MAZE:\n{maze.get_debug()}\n")

        # TODO: write output file, run UI (cli or gui)
        # (move all in ui ? can restart ...etc )
    return 0
