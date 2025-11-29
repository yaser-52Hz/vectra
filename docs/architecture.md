# Architecture Documentation

## Overview

**Vectra** is designed with a hybrid architecture combining Python and C++ to provide both ease of use and high performance.

**Author:** Yasser Hosseinzadeh  
**Email:** one.astro.nerd@gmail.com

## Architecture Layers

### 1. Python Interface Layer

Located in `src/vectors/`:
- **vector.py**: Main Vector class with Pythonic interface
- **operations.py**: High-level mathematical operations
- **__init__.py**: Package initialization and exports

This layer provides the user-facing API with:
- Type hints for IDE support
- NumPy integration
- Comprehensive documentation
- Pythonic interfaces

### 2. C++ Core Layer

Located in `src/vectors_cpp/`:
- **vector_core.h/cpp**: Core 3D vector implementation
- **python_bindings.cpp**: pybind11 interface

This layer provides:
- High-performance vector operations
- Optimized batch processing
- Direct memory management
- Future SIMD optimizations

### 3. Build System Layer

- **setup.py**: setuptools configuration for pip installation
- **pyproject.toml**: Modern Python packaging standards
- **CMakeLists.txt**: CMake configuration for alternative builds
- **build.py**: Convenient build script

## Key Design Decisions

### Why C++?

1. **Performance**: C++ allows direct control over memory and CPU instructions
2. **Optimization**: Future SIMD optimizations for batch operations
3. **Predictability**: Deterministic performance characteristics
4. **Interoperability**: Can be used by other C++ libraries

### Why pybind11?

1. **Seamless Integration**: Natural Python/C++ interop
2. **Type Conversion**: Automatic type conversions
3. **Minimal Boilerplate**: Clean binding syntax
4. **NumPy Support**: Direct NumPy array integration

### Performance Considerations

#### Current Implementation
- All operations run in C++
- Batch operations process arrays directly
- Minimal Python overhead

#### Future Optimizations
1. **SIMD**: Use AVX/SSE for batch operations
2. **Parallelization**: Multi-threading for large batches
3. **Memory Pools**: Reduce allocation overhead
4. **Compiler Optimizations**: -O3 and profile-guided optimization

## Module Structure

```
vectors/
├── __init__.py         # Package initialization
├── vector.py           # Vector class (Python wrapper)
└── operations.py       # High-level operations

vectors_cpp/
├── vector_core.h       # C++ vector class interface
├── vector_core.cpp     # C++ implementation
└── python_bindings.cpp # pybind11 bindings

build/
├── _vectors_core.*     # Compiled extension module
└── ...                 # Build artifacts
```

## Extension Points

### Adding New Operations

1. **C++ Core**: Add to `vector_core.h/cpp`
2. **Bindings**: Expose via `python_bindings.cpp`
3. **Python API**: Add wrapper in `operations.py`

### Example: Adding Vector Length

```cpp
// In vector_core.h
double length_squared() const;

// In vector_core.cpp
double Vector3D::length_squared() const {
    return data_[0]*data_[0] + data_[1]*data_[1] + data_[2]*data_[2];
}

// In python_bindings.cpp
.def("length_squared", &Vector3D::length_squared)

// In operations.py
def length_squared(v: Vector) -> float:
    """Calculate squared length (faster than magnitude for comparisons)."""
    return v.x**2 + v.y**2 + v.z**2
```

## Testing Strategy

### Unit Tests
- Python layer: `tests/test_vector.py`
- Operations: `tests/test_operations.py`
- C++ layer: Future C++ tests with Catch2

### Integration Tests
- End-to-end functionality
- Performance benchmarks
- NumPy interoperability

### Benchmarks
- Compare against NumPy operations
- Measure batch operation performance
- Profile C++ operations

## Future Enhancements

1. **4D Vectors**: Quaternion support
2. **Matrix Operations**: Matrix-vector multiplication
3. **GPU Acceleration**: CUDA/OpenCL support
4. **Parallel Batch Processing**: Multi-threaded operations
5. **Sparse Vectors**: Space-efficient storage
6. **Automatic Differentiation**: For machine learning

## Build Process

### Development Build
```bash
python build.py
```

### Production Build
```bash
pip install -e .
```

### CMake Build
```bash
mkdir build && cd build
cmake ..
make
```

## Dependencies

- **Runtime**: NumPy (for integration)
- **Build Time**: pybind11, setuptools
- **Development**: pytest, black, flake8, mypy

## Performance Targets

- Vector operations: < 10ns per operation
- Batch operations: Near theoretical peak
- Memory usage: Minimal overhead vs raw arrays
- NumPy compatibility: Seamless conversion

