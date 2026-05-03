#!/usr/bin/env python3

import sys
from .src import run


def main() -> None:
    if len(sys.argv) != 2:
        print(f"Usage: {sys.argv[0]} <config_path>")
        sys.exit(1)

    config_path = sys.argv[1]
    sys.exit(run(config_path))


if __name__ == "__main__":
    main()
