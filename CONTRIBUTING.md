# Contributing Guide

Thank you for your interest in contributing to Vectra!

**Author:** Yasser Hosseinzadeh  
**Email:** one.astro.nerd@gmail.com

## Getting Started

1. Fork the repository
2. Clone your fork
3. Create a new branch for your changes
4. Make your changes
5. Add tests
6. Submit a pull request

## Development Setup

### Prerequisites

- Python 3.7+
- C++17 compatible compiler
- pybind11

### Setup

```bash
# Install development dependencies
pip install -r requirements-dev.txt

# Install the library in development mode
pip install -e .
```

## Code Style

### Python

- Follow PEP 8
- Use type hints
- Maximum line length: 100 characters
- Use Black for formatting
- Use flake8 for linting

### C++

- Follow the existing code style
- Use meaningful variable names
- Add comments for complex operations
- Maximum line length: 100 characters

## Testing

### Running Tests

```bash
# Run all tests
pytest

# Run with coverage
pytest --cov=vectors --cov-report=html

# Run specific test file
pytest tests/test_vector.py
```

### Writing Tests

- Add tests for all new features
- Maintain or improve coverage
- Test edge cases
- Test error conditions

## Pull Request Process

1. Update documentation as needed
2. Add tests for new functionality
3. Ensure all tests pass
4. Update CHANGELOG.md
5. Submit PR with clear description

## Commit Messages

- Use clear, descriptive messages
- Reference issue numbers when applicable
- Follow conventional commits format:
  - `feat:` for new features
  - `fix:` for bug fixes
  - `docs:` for documentation
  - `test:` for tests
  - `refactor:` for code changes
  - `perf:` for performance improvements

## Code Review

All code must be reviewed before merging. Reviewers will check for:
- Code correctness
- Test coverage
- Documentation updates
- Performance considerations

## Questions?

Open an issue or contact: **one.astro.nerd@gmail.com**

