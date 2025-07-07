PYTHON := python3
PIP := python3 -m pip

.PHONY: all clean build test artifact

# Main targets that match CI requirements
build:
	@echo "=== Building Utility ==="
	$(PIP) install --upgrade pip
	$(PIP) install -r requirements.txt
	$(PIP) install -e .

test:
	@echo "=== Running Test Suite ==="
	pytest tests/ -v --cov=src/dictionary_cli --cov-report=term-missing

artifact:
	@echo "=== Producing Runtime Artifact ==="
	$(PYTHON) setup.py sdist bdist_wheel
	@echo "Artifacts created in dist/:"
	@ls -l dist/

# Combined target
all: clean build test artifact

# Utility targets
clean:
	rm -rf build/
	rm -rf dist/
	rm -rf *.egg-info
	rm -rf .coverage
	rm -rf .pytest_cache
	rm -rf __pycache__
	find . -type d -name __pycache__ -exec rm -rf {} +

# Install for development
install: build
	$(PIP) install -e .

