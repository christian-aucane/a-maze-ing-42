*This activity has been created as part of
the 42 curriculum by osamet, caucane.*

# A_maze_ing

## 🔀 Pull Request & Workflow
Follow these steps when working on a feature and creating a Pull Request.

### 📌 Branch Naming

- Name branches according to the **objective** and your **login**:
```
<branch-objective>-login42
```
- Examples:
  - `init-repo-caucane`
  - `update-readme-caucane`
  - `generator-osamet`
- One branch = one goal / one PR

---
### 📌 Before creating the PR (important)

Make sure your branch is up to date with `main`:

```bash
git checkout <your-branch>
git fetch origin
git rebase origin/main
```

If there are conflicts:
- Resolve them manually
- Then continue the rebase:
```bash
git add .
git rebase --continue
```

Finally, push your branch:
```bash
git push origin <your-branch> --force
```

---

### 🔀 Pull Request Template
Use the following template when creating a Pull Request:

```
### 📌 Description
Briefly describe what this PR does.

### 🎯 Objectives
- What problem does this solve?
- What feature is added or modified?

### 🛠️ Changes
- List of main modifications:
  - 
  - 
  - 

### ✅ Validation
- [ ] Code compiles / runs
- [ ] `make lint` passes
- [ ] `make lint-strict` passes (if relevant)

### 🧪 Tests
- Describe how this was tested:
  - 

### 📎 Notes
- Any additional information for the reviewer
```

---

### 🔁 Merge process (after PR is approved)

Once the PR is approved and CI passes:

1. Ensure the branch is still up to date:
```bash
git checkout <your-branch>
git fetch origin
git rebase origin/main
git push origin <your-branch> --force
```

2. Merge on GitHub using:
- ✅ **Squash and merge**

3. Delete the branch after merge (recommended)

---

### ⚠️ Rules

- ❌ Do not push directly to `main`
- ❌ Do not merge without PR
- ✅ Always rebase before PR and before merge
- ✅ Keep commits clean and meaningful

## 👥 Work Distribution

Each team member must clearly indicate their contributions.

### osamet
- Implemented parsing of the config.txt file to create the configuration object
- Created terminal rendering for the maze grid and its solution
- Added support for changing grid and pattern colors
- Implemented the DFS-based maze generation algorithm
- Implemented the BFS-based maze solver algorithm 
-

### caucane
- Initial project setup
- Repository structure (modules: grid, generator, solver, render, parser, main)
- Makefile implementation (venv, install, run, lint)
- CI setup (lint workflow)
- Config system (config.txt.example)
- Entry point implementation (a_maze_ing.py + main.run)
- Linting setup (flake8, mypy)
-

> This section must be updated throughout the project to reflect actual contributions.
## Use Module GenerateMaze

The reusable maze generator is provided as a standalone Python package named `mazegen`.

It exposes a main class:

```python
from mazegen import MazeGenerator
```

### Installation

### From source (development)

```bash
pip install -e .
```

### From built package

Build the package:
```bash
python3 -m build
```
Install the generated wheel:
```bash
pip install dist/mazegen-1.0.1-py3-none-any.whl
```

### Basic Usage

Minimal example:
```python
from mazegen import MazeGenerator

# Create generator
generator = MazeGenerator(width=15, height=10)

# Generate maze
maze = generator.generate()
```

### Custom Parameters

You can configure the generator using custom arguments.

Example:
```python
from mazegen import MazeGenerator

generator = MazeGenerator(
    width=20,
    height=15,
    seed=42,
    is_perfect=True
)
```
### Available parameters

| Parameter	| Type |	Description |
|---------|------|--------------|
| width | int | Maze width |
| height | int | Maze height |
| seed | int or None | Optional deterministic seed |
| is_perfect | bool | Generate a perfect maze |

### Access Maze Structure

The generated maze returns a reusable internal structure.

Example:
```python
maze = generator.generate()

for row in maze.iterrows():
    for cell in row:
        print(cell.x, cell.y, cell.walls)
```

Each cell contains:
- coordinates
- walls
- neighbor relations

### Access Maze Solution

The module also provides access to a solution path.

Example:
```python
solution = generator.solve(maze)

for cell, direction in solution.items():
    print(f"From ({cell.x},{cell.y}) go {direction}")
```
Returned format:
```python
dict[MazeBox, Direction]
```
This structure gives the path from entry to exit.

### Minimal Example for Evaluation

```python
from mazegen import MazeGenerator

# Instantiate with size and seed
gen = MazeGenerator(width=15, height=10, seed=42)

# Generate maze
maze = gen.generate()

# Access structure
for row in maze.iterrows():
    for cell in row:
        print(cell.x, cell.y, cell.walls)

# Get solution
solution = gen.solve(maze)

for cell, direction in solution.items():
    print(f"From ({cell.x},{cell.y}) go {direction}")
```