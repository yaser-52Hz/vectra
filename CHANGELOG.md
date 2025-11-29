# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

### Added
- N-dimensional vector support (2D, 3D, and beyond)
- Intelligent operator overloading:
  - `v1 * v2` for dot product
  - `v1 @ v2` for cross product
  - `abs(v)` for ||v|| notation (norm)
- Element-wise operations
- Statistical operations on vectors

## [0.1.0] - 2024

### Planned
- Performance optimizations with SIMD
- GPU acceleration support
- 4D vector support
- Matrix operations

## [0.1.0] - Initial Infrastructure Release

### Added
- Basic Vector class with 2D and 3D support
- Arithmetic operations (add, subtract, multiply, divide)
- Vector operations (dot product, cross product)
- Normalization and magnitude calculation
- Distance and angle calculations
- Advanced operations (projection, reflection, rotation)
- Batch operations for efficient processing
- NumPy integration
- Comprehensive test suite
- Example code and documentation
- C++ backend with pybind11 bindings

### Infrastructure
- Python package structure
- C++ core implementation
- Build system (setup.py, pyproject.toml, CMakeLists.txt)
- CI/CD configuration
- Documentation structure

