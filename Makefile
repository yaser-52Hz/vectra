.PHONY: help clean build install test format lint type-check docs examples run-examples

help:  ## Display this help message
	@echo "Available commands:"
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | sort | awk 'BEGIN {FS = ":.*?## "}; {printf "\033[36m%-15s\033[0m %s\n", $$1, $$2}'

clean:  ## Clean build artifacts
	rm -rf build/
	rm -rf dist/
	rm -rf *.egg-info/
	rm -rf **/__pycache__/
	rm -rf .pytest_cache/
	rm -rf htmlcov/
	find . -type f -name "*.pyc" -delete
	find . -type f -name "*.so" -delete
	find . -type d -name "*.egg-info" -exec rm -rf {} +

build:  ## Build the extension
	python build.py

install:  ## Install the package in development mode
	pip install -e .

test:  ## Run tests
	pytest tests/ -v

test-cov:  ## Run tests with coverage
	pytest tests/ --cov=vectors --cov-report=html --cov-report=term

format:  ## Format code with black
	black src/ tests/ examples/

lint:  ## Run linters
	flake8 src/ tests/ examples/
	pylint src/

type-check:  ## Run type checking
	mypy src/

examples:  ## Run all examples
	python examples/basic_usage.py
	python examples/advanced_operations.py
	python examples/physics_simulation.py

run-examples: examples  ## Alias for examples

docs:  ## Generate documentation
	@echo "Documentation is in docs/ directory"

all: clean build install test  ## Clean, build, install, and test

dev-setup:  ## Setup development environment
	pip install -r requirements-dev.txt
	pip install -e .

.DEFAULT_GOAL := help

