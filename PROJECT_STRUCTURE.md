# Project Structure

## Overview

This document describes the structure of **Vectra** - a high-performance vector mathematics library.

**Author:** Yasser Hosseinzadeh  
**Email:** one.astro.nerd@gmail.com

## Directory Layout

```
.
├── README.md                    # Main project documentation
├── LICENSE                       # MIT License
├── CONTRIBUTING.md              # Contribution guidelines
├── CHANGELOG.md                 # Version history
├── PROJECT_STRUCTURE.md         # This file
│
├── setup.py                     # setuptools build configuration
├── pyproject.toml               # Modern Python packaging config
├── CMakeLists.txt               # CMake build configuration
├── build.py                     # Convenient build script
├── Makefile                     # Make commands for development
├── MANIFEST.in                  # Files to include in distribution
│
├── requirements.txt             # Runtime dependencies
├── requirements-dev.txt         # Development dependencies
├── .gitignore                   # Git ignore rules
├── .gitattributes              # Git attribute rules
│
├── src/                         # Source code
│   ├── vectors/                 # Python package
│   │   ├── __init__.py          # Package initialization
│   │   ├── vector.py            # Vector class implementation
│   │   └── operations.py        # High-level operations
│   │
│   └── vectors_cpp/             # C++ core
│       ├── vector_core.h        # Vector class interface
│       ├── vector_core.cpp      # Vector implementation
│       └── python_bindings.cpp  # pybind11 bindings
│
├── tests/                       # Test suite
│   ├── __init__.py              # Test package initialization
│   ├── conftest.py              # pytest configuration and fixtures
│   ├── test_vector.py           # Vector class tests
│   └── test_operations.py       # Operations tests
│
├── examples/                    # Example code
│   ├── basic_usage.py           # Basic operations demo
│   ├── advanced_operations.py  # Advanced features demo
│   └── physics_simulation.py   # Physics simulation example
│
└── docs/                        # Documentation
    ├── README.md                # Documentation overview
    ├── architecture.md          # Architecture documentation
    └── API_reference.md          # API reference

```

## Component Descriptions

### Python Package (`src/vectors/`)

- **`__init__.py`**: Package initialization, version info, and public API exports
- **`vector.py`**: Main Vector class with operator overloads and convenience methods
- **`operations.py`**: High-level mathematical operations and batch processing functions

### C++ Core (`src/vectors_cpp/`)

- **`vector_core.h`**: C++ Vector3D class interface with all operation signatures
- **`vector_core.cpp`**: Implementation of all vector operations in C++17
- **`python_bindings.cpp`**: pybind11 bindings to expose C++ code to Python

### Build System

- **`setup.py`**: Traditional setuptools configuration for building the extension
- **`pyproject.toml`**: Modern Python packaging configuration (PEP 518)
- **`CMakeLists.txt`**: Alternative CMake-based build system
- **`build.py`**: Simplified build script for development
- **`Makefile`**: Convenient make commands for common tasks

### Testing

- **`tests/`**: Comprehensive test suite using pytest
- All components have corresponding unit tests
- Includes fixtures for common test scenarios

### Examples

- **`examples/`**: Three example scripts demonstrating different use cases
- Covers basic operations, advanced features, and real-world applications (physics)

### Documentation

- **`docs/`**: Technical documentation including architecture and API reference
- **`README.md`**: Quick start guide and overview
- **`CONTRIBUTING.md`**: Guidelines for contributors
- **`CHANGELOG.md`**: Version history

## Key Features

### Performance
- C++ backend for maximum speed
- Optimized batch operations
- Ready for SIMD optimizations

### Usability
- Pythonic interface with type hints
- Functional and object-oriented APIs
- NumPy integration
- Comprehensive documentation

### Maintainability
- Clean architecture with separation of concerns
- Extensive test coverage
- Multiple build options
- Clear contribution guidelines

## Development Workflow

1. **Setup**: `make dev-setup` or `pip install -e .`
2. **Develop**: Edit code in `src/`
3. **Test**: `make test` or `pytest`
4. **Build**: `make build` or `python build.py`
5. **Format**: `make format` or `black src/`
6. **Lint**: `make lint`

## Next Steps

See [Architecture Documentation](docs/architecture.md) for detailed technical information.

