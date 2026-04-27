import random

from .config import parse_config_file
from .generator.maze_generator import generate_maze
from .solver.maze_solver import solve_maze
from .render import AsciiRenderer
from .colors import COLORS_WALLS, COLORS_PATTERN


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

    renderer = AsciiRenderer()
    # Print for debug
    print(f"CONFIG:\n{config}\n")
    print(f"MAZE:\n{renderer.render(maze, solution)}\n")
    # print(f"SOLUTION:\n{solution}\n")

    while True:
        nbr = int(
            input(
                "1- Regenerate Maze: \n"
                "2- show and hide solution from entry to exit: \n"
                "3- Change walls color: \n"
                "4- change pattern color: \n"
            )
        )

        if nbr and nbr == 1:
            maze = generate_maze(config=config)
            if maze is None:
                print("Error: failed to generate maze.")
                return 1
            solution = solve_maze(maze=maze, config=config)
            print(f"MAZE:\n{renderer.render(maze=maze, solution=solution)}\n")

        elif nbr and nbr == 2:
            renderer.toggle_display_solution()
            print(f"MAZE: {renderer.render(maze=maze, solution=solution)}")

        elif nbr and nbr == 3:
            color = input("input color: ")
            renderer.walls_color = COLORS_WALLS[color].value
            print(f"MAZE: {renderer.render(maze=maze, solution=solution)}")

        elif nbr and nbr == 4:
            color = input("input color: ")
            renderer.pattern_color = COLORS_PATTERN[color].value
            print(f"MAZE: {renderer.render(maze=maze, solution=solution)}")

            # TODO: write output file, run UI (cli or gui)
            # (move all in ui ? can restart ...etc )
    return 0
