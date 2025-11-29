# Vectra

A high-performance n-dimensional vector operations library for scientific and mathematical computing.

**Author:** Yasser Hosseinzadeh  
**Email:** hosseinzadeh.yasser@gmail.com 

## Overview

**Vectra** provides efficient n-dimensional vector operations with a C++ backend for optimal performance. It's designed for scientific and mathematical applications that require fast, accurate vector computations.

## Features

- **High Performance**: Core operations implemented in C++ for maximum speed
- **Pythonic Interface**: Clean, intuitive Python API
- **Comprehensive Operations**: 
  - Basic arithmetic (addition, subtraction, scalar multiplication)
  - Vector operations (dot product, cross product, normalization)
  - Advanced operations (projections, reflections, rotations)
  - Batch operations for processing multiple vectors efficiently
- **NumPy Integration**: Seamless integration with NumPy arrays
- **Type Safety**: Full type hints for better IDE support

## Requirements

- Python 3.7+
- C++17 compatible compiler (GCC, Clang, or MSVC)
- NumPy 1.20+
- pybind11 (for C++ bindings)

## Installation

### From Source

```bash
# Clone the repository
git clone https://github.com/yasser-hosseinzadeh/vectra.git
cd vectra

# Install dependencies
pip install -r requirements.txt
pip install pybind11

# Build and install
python build.py
pip install -e .
```

### Using pip (when available)

```bash
pip install vectra
```

## Quick Start

```python
from vectors import Vector, add, dot_product, cross_product

# Create vectors
v1 = Vector(1, 2, 3)
v2 = Vector(4, 5, 6)

# Basic operations
v3 = v1 + v2  # Vector addition
scaled = v1 * 2.5  # Scalar multiplication

# Vector operations
dot = v1.dot(v2)  # Dot product
cross = v1.cross(v2)  # Cross product

# Magnitude and normalization
mag = v1.magnitude()
unit = v1.normalize()

# Advanced operations
from vectors import angle_between, distance, projection

angle = angle_between(v1, v2)
dist = distance(v1, v2)
proj = projection(v1, v2)
```

## Advanced Features

### Batch Operations

```python
from vectors import batch_add, batch_dot_product, centroid

vectors1 = [Vector(1, 2, 3), Vector(4, 5, 6)]
vectors2 = [Vector(7, 8, 9), Vector(10, 11, 12)]

# Efficient batch addition
result = batch_add(vectors1, vectors2)

# Batch dot products
dots = batch_dot_product(vectors1, vectors2)

# Calculate centroid
center = centroid([Vector(0, 0, 0), Vector(1, 1, 1), Vector(2, 2, 2)])
```

### NumPy Integration

```python
import numpy as np
from vectors import Vector

# Convert from NumPy array
arr = np.array([1, 2, 3])
v = Vector.from_numpy(arr)

# Convert to NumPy array
array = v.to_numpy()
```

## Architecture

The library is structured as follows:

```
src/
├── vectors/                # Python package
│   ├── __init__.py
│   ├── vector.py           # Vector class
│   └── operations.py       # High-level operations
└── vectors_cpp/            # C++ core
    ├── vector_core.h       # C++ vector implementation
    ├── vector_core.cpp
    └── python_bindings.cpp # pybind11 bindings
```

## Building with CMake

Alternative build using CMake:

```bash
mkdir build && cd build
cmake ..
make
```

## Development

### Running Tests

```bash
pytest tests/
```

### Code Formatting

```bash
black src/
flake8 src/
```

### Type Checking

```bash
mypy src/
```

## Contributing

Contributions are welcome! Please read the contributing guidelines before submitting pull requests.

## License

MIT License - see LICENSE file for details.

## Author

**Yasser Hosseinzadeh**  
Email: one.astro.nerd@gmail.com

## Acknowledgments

Built with pybind11 for seamless C++/Python interop.


