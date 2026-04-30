from .config import parse_config_file
from .generator.maze_generator import generate_maze
from .solver.maze_solver import solve_maze
from .config import Config
from .render import AsciiRenderer
from .colors import COLORS_WALLS, COLORS_PATTERN
from .grid import MazeGrid, MazeBox
from .common import Direction


def gen_and_solve_maze(
    config: Config,
) -> tuple[MazeGrid, dict[MazeBox, Direction]] | tuple[None, None]:
    # Generate maze
    maze = generate_maze(config=config)
    if maze is None:
        print("Error: failed to generate maze.")
        return None, None

    # Solve maze
    solution = solve_maze(maze=maze, config=config)
    if solution is None:
        print("Error: failed to solve maze.")
        return None, None

    return maze, solution


def write_output_file(
    config: Config, maze: MazeGrid, solution: dict[MazeBox, Direction]
) -> None:
    with open(config.output_file, "w") as f:
        f.write(
            f"{maze.get_output()}\n\n"
            f"{config.get_entry_output()}\n{config.get_exit_output()}\n"
            f"{''.join(direction.get_output() for direction in solution.values())}"
        )


def run(config_file_path: str) -> int:
    config = parse_config_file(config_file_path=config_file_path)
    if config is None:
        print("Error: failed to parse config file.")
        return 1

    maze, solution = gen_and_solve_maze(config)
    if maze is None and solution is None:
        return 1

    renderer = AsciiRenderer()
    running = True
    while running:
        print(renderer.render(maze=maze, solution=solution))  # type: ignore
        choice = input(
            "1- Regenerate Maze: \n"
            "2- show and hide solution from entry to exit: \n"
            "3- Change walls color: \n"
            "4- change pattern color: \n"
            "5- quit\n"
            "Choice : "
        )

        if choice == "1":
            maze, solution = gen_and_solve_maze(config)
            if maze is None and solution is None:
                return 1

        elif choice == "2":
            renderer.toggle_display_solution()

        elif choice == "3":
            color = input("input color: ")
            renderer.walls_color = COLORS_WALLS[color].value

        elif choice == "4":
            color = input("input color: ")
            renderer.pattern_color = COLORS_PATTERN[color].value

        elif choice == "5":
            running = False

        else:
            print("Type a valid option...")

    write_output_file(config, maze, solution)  # type: ignore
    print("Good bye!")
    return 0
