# API Reference - Vectra

**Vectra** - High-performance n-dimensional vector operations library.

**Author:** Yasser Hosseinzadeh  
**Email:** one.astro.nerd@gmail.com

## Vector Class

### Vector(x, y, z=0.0)

Creates a 3D vector with components (x, y, z). If z is omitted, creates a 2D vector.

**Parameters:**
- `x` (float): X component
- `y` (float): Y component  
- `z` (float, optional): Z component, default 0.0

**Returns:**
- `Vector`: A new vector instance

### Properties

#### x, y, z
Get or set vector components.

### Methods

#### magnitude() -> float
Calculate the magnitude (length) of the vector.

#### normalize() -> Vector
Return a normalized (unit) vector. Raises ValueError if the vector is zero.

#### dot(other: Vector) -> float
Calculate the dot product with another vector.

#### cross(other: Vector) -> Vector
Calculate the cross product with another vector.

#### to_list() -> List[float]
Convert vector to a list [x, y, z].

#### to_tuple() -> Tuple[float, float, float]
Convert vector to a tuple (x, y, z).

#### to_numpy() -> numpy.ndarray
Convert vector to a NumPy array.

### Operators

- `+` : Vector addition
- `-` : Vector subtraction
- `*` : Scalar multiplication
- `/` : Scalar division
- `==` : Equality check
- `-v` : Negation

### Class Methods

#### from_list(data: List[float]) -> Vector
Create a vector from a list [x, y] or [x, y, z].

#### from_numpy(array: numpy.ndarray) -> Vector
Create a vector from a NumPy array.

## Basic Operations

### add(v1: Vector, v2: Vector) -> Vector
Add two vectors.

### subtract(v1: Vector, v2: Vector) -> Vector
Subtract one vector from another.

### multiply(v: Vector, scalar: float) -> Vector
Multiply a vector by a scalar.

### divide(v: Vector, scalar: float) -> Vector
Divide a vector by a scalar.

### dot_product(v1: Vector, v2: Vector) -> float
Calculate the dot product of two vectors.

### cross_product(v1: Vector, v2: Vector) -> Vector
Calculate the cross product of two vectors.

### magnitude(v: Vector) -> float
Calculate the magnitude of a vector.

### normalize(v: Vector) -> Vector
Normalize a vector to unit length.

### distance(v1: Vector, v2: Vector) -> float
Calculate the Euclidean distance between two vectors.

### angle_between(v1: Vector, v2: Vector) -> float
Calculate the angle between two vectors in radians.

## Advanced Operations

### projection(v1: Vector, v2: Vector) -> Vector
Calculate the projection of v1 onto v2.

### reflection(v: Vector, normal: Vector) -> Vector
Calculate the reflection of a vector about a normal.

### rotate(v: Vector, axis: Vector, angle: float) -> Vector
Rotate a vector around an axis by a given angle (in radians).

### batch_add(vectors1: List[Vector], vectors2: List[Vector]) -> List[Vector]
Add multiple pairs of vectors efficiently.

### batch_dot_product(vectors1: List[Vector], vectors2: List[Vector]) -> List[float]
Calculate dot products for multiple pairs of vectors.

### centroid(vectors: List[Vector]) -> Vector
Calculate the centroid (average) of multiple vectors.

### weighted_average(vectors: List[Vector], weights: List[float]) -> Vector
Calculate the weighted average of multiple vectors.

## Usage Examples

### Basic Usage

```python
from vectors import Vector

# Create vectors
v1 = Vector(1, 2, 3)
v2 = Vector(4, 5, 6)

# Arithmetic
result = v1 + v2
scaled = v1 * 2.5

# Vector operations
dot = v1.dot(v2)
cross = v1.cross(v2)
mag = v1.magnitude()
unit = v1.normalize()
```

### Functional API

```python
from vectors import add, dot_product, distance

v1 = Vector(1, 2, 3)
v2 = Vector(4, 5, 6)

sum_vec = add(v1, v2)
dot = dot_product(v1, v2)
dist = distance(v1, v2)
```

### Batch Operations

```python
from vectors import batch_add, batch_dot_product

vectors1 = [Vector(1, 2), Vector(3, 4)]
vectors2 = [Vector(5, 6), Vector(7, 8)]

results = batch_add(vectors1, vectors2)
dots = batch_dot_product(vectors1, vectors2)
```

### NumPy Integration

```python
import numpy as np
from vectors import Vector

# From NumPy
arr = np.array([1, 2, 3])
v = Vector.from_numpy(arr)

# To NumPy
array = v.to_numpy()
```

