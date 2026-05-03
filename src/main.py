from .config import parse_config_file
from mazegen import MazeGenerator, MazeGrid, MazeBox, Direction
from .config import Config
from .render import AsciiRenderer
from .colors import COLORS_WALLS, COLORS_PATTERN
from typing import Generator
import time


def generate_maze(config: Config
                  ) -> tuple[MazeGrid, MazeGenerator] | tuple[None, None]:
    try:
        generator = MazeGenerator(gen_algo_name=config.gen_algorithm,
                                  solve_algo_name=config.solve_algorithm,
                                  width=config.width,
                                  height=config.height,
                                  entry=config.entry,
                                  exit=config.exit,
                                  is_perfect=config.perfect)
    except ValueError:
        print("Error durring generator instanciation...")
        return None, None

    grid = generator.generate()
    if grid is None:
        print("Error durring maze generation...")
        return None, None
    return grid, generator


def gen_and_solve_maze(config: Config
                       ) -> tuple[MazeGrid, dict[
                           MazeBox, Direction]] | tuple[None, None]:
    # Generate maze
    maze, generator = generate_maze(config=config)
    if maze is None or generator is None:
        print("Error: failed to generate maze.")
        return None, None

    # Solve maze
    solution = generator.solve(maze)
    if solution is None:
        print("Error: failed to solve maze.")
        return None, None

    return maze, solution


def write_output_file(
    config: Config, maze: MazeGrid, solution: dict[MazeBox, Direction]
) -> None:
    solution_str = ''.join(
        direction.get_output()
        for direction in solution.values()
    )
    with open(config.output_file, "w") as f:
        f.write(
            f"{maze.get_output()}\n\n"
            f"{config.get_entry_output()}\n{config.get_exit_output()}\n"
            f"{solution_str}"
        )


def itter_solution(solutions: dict[MazeBox, Direction]
                   ) -> Generator[tuple[MazeBox, Direction], None, None]:
    for cell, solution in solutions.items():
        yield (cell, solution)


def clear_terminal() -> None:
    print("\033c", end="")


def run(config_file_path: str) -> int:
    config = parse_config_file(config_file_path=config_file_path)
    if config is None:
        print("Error: failed to parse config file.")
        return 1

    maze, solution = gen_and_solve_maze(config)
    if maze is None:
        print("Error: failed to generate maze.")
        return 1
    if solution is None:
        print("Error: failed to solve maze.")
        return 1

    renderer = AsciiRenderer()
    running = True

    while running and maze and solution:
        if renderer.display_solution:
            solutions: dict[MazeBox, Direction] = {}
            for s in itter_solution(solution):
                cell, direction = s
                if cell.walls[direction]:
                    print("BAD:", cell, direction, cell.walls)
                    break

                solutions[cell] = direction
                clear_terminal()
                print(renderer.render(maze=maze, solution=solutions))
                time.sleep(0.2)
        else:
            clear_terminal()
            print(renderer.render(maze=maze, solution=solution))
        # print(renderer.render(maze=maze, solution=solution))
        choice = input(
            "==== A_MAZE_ING ====\n"
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
