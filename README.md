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
