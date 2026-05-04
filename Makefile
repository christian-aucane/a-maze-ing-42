.PHONY: install run debug clean lint lint-strict

VENV=.venv
PYTHON=$(VENV)/bin/python
PIP=$(VENV)/bin/pip
CONFIG=config.txt
CONFIG_EXAMPLE=config.txt.example

# -------------------------------
# Install: create venv, copy config, install requirements
# -------------------------------
install:
	@echo "Setting up virtual environment..."
	@test -d $(VENV) || python -m venv $(VENV)
	@echo "Installing dependencies..."
	$(PIP) install --upgrade pip
	$(PIP) install -r requirements.txt
	@echo "Copying config.txt if missing..."
	@test -f $(CONFIG) || cp $(CONFIG_EXAMPLE) $(CONFIG)
	$(PIP) install -e .
	$(PYTHON) -m build
	$(PIP) install dist/mazegen-1.0.1-py3-none-any.wh

# -------------------------------
# Run the main script inside venv
# -------------------------------
run:
	$(PYTHON) a_maze_ing.py $(CONFIG)

# -------------------------------
# Run in debug mode (pdb)
# -------------------------------
debug:
	$(PYTHON) -m pdb a_maze_ing.py $(CONFIG)

# -------------------------------
# Clean temporary files
# -------------------------------
clean:
	find . -name "__pycache__" -type d -exec rm -rf {} +
	find . -name ".mypy_cache" -type d -exec rm -rf {} +
	find . -name "*.pyc" -type f -delete

# -------------------------------
# Lint and type checking
# -------------------------------
lint:
	$(PYTHON) -m flake8 .
	$(PYTHON) -m mypy . --warn-return-any --warn-unused-ignores --ignore-missing-imports \
	--disallow-untyped-defs --check-untyped-defs

# -------------------------------
# Strict linting (optional)
# -------------------------------
lint-strict:
	$(PYTHON) -m flake8 .
	$(PYTHON) -m mypy . --strict
