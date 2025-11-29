"""
Vector class - Main n-dimensional vector interface

This module provides the Vector class and its operations.
The actual implementation is in C++ for performance.
"""

from typing import List, Tuple, Union, Optional, overload
import numpy as np

class Vector:
    """
    A high-performance n-dimensional vector class for scientific computing.
    
    This class wraps the C++ implementation for efficient vector operations.
    Supports vectors of any dimension (2D, 3D, nD).
    
    Attributes:
        components: List of vector components
    
    Examples:
        >>> v1 = Vector([1, 2, 3])  # 3D vector
        >>> v2 = Vector([1, 2])      # 2D vector
        >>> v3 = Vector(10)          # 10-dimensional vector
    """
    
    def __init__(self, *args):
        """
        Initialize a Vector.
        
        Args can be:
        - Single integer: Create zero vector of that dimension
        - List/tuple of numbers: Create vector from components
        - Multiple floats: Create vector from arguments
        - NumPy array: Create vector from array
        
        Examples:
            >>> v1 = Vector(1, 2, 3)     # 3D from args
            >>> v2 = Vector([1, 2, 3])   # 3D from list
            >>> v3 = Vector(10)           # 10D zero vector
            >>> v4 = Vector(np.array([1, 2]))
        """
        if len(args) == 0:
            # Default to 3D zero vector for backward compatibility
            self._components = [0.0, 0.0, 0.0]
            self._dim = 3
        elif len(args) == 1:
            arg = args[0]
            # Handle single integer (dimension)
            if isinstance(arg, int):
                self._dim = arg
                self._components = [0.0] * arg
            # Handle list/tuple
            elif isinstance(arg, (list, tuple)):
                self._components = [float(x) for x in arg]
                self._dim = len(self._components)
            # Handle NumPy array
            elif isinstance(arg, np.ndarray):
                self._components = arg.flatten().tolist()
                self._dim = len(self._components)
            else:
                # Single value -> treat as 1D
                self._components = [float(arg)]
                self._dim = 1
        else:
            # Multiple arguments -> components
            self._components = [float(x) for x in args]
            self._dim = len(self._components)
    
    def __len__(self):
        """Return the dimension of the vector."""
        return self._dim
    
    @property
    def components(self):
        """Get all components as a list."""
        return self._components
    
    @property
    def x(self):
        """Get x component (first component)."""
        return self._components[0] if self._dim > 0 else 0.0
    
    @x.setter
    def x(self, value):
        if self._dim > 0:
            self._components[0] = float(value)
    
    @property
    def y(self):
        """Get y component (second component)."""
        return self._components[1] if self._dim > 1 else 0.0
    
    @y.setter
    def y(self, value):
        if self._dim > 1:
            self._components[1] = float(value)
    
    @property
    def z(self):
        """Get z component (third component)."""
        return self._components[2] if self._dim > 2 else 0.0
    
    @z.setter
    def z(self, value):
        if self._dim > 2:
            self._components[2] = float(value)
    
    @property
    def dimension(self):
        """Get the dimension of the vector."""
        return self._dim
    
    def __getitem__(self, index):
        """Get component by index."""
        return self._components[index]
    
    def __setitem__(self, index, value):
        """Set component by index."""
        self._components[index] = float(value)
    
    def __repr__(self):
        """Return string representation of the vector."""
        return f"Vector({self._components})"
    
    def __str__(self):
        """Return human-readable string representation."""
        return f"{tuple(self._components)}"
    
    def __add__(self, other: 'Vector') -> 'Vector':
        """Add two vectors."""
        if self._dim != other._dim:
            raise ValueError(
                f"Dimension mismatch: {self._dim}D + {other._dim}D"
            )
        result = Vector(self._dim)
        for i in range(self._dim):
            result[i] = self._components[i] + other._components[i]
        return result
    
    def __sub__(self, other: 'Vector') -> 'Vector':
        """Subtract two vectors."""
        if self._dim != other._dim:
            raise ValueError(
                f"Dimension mismatch: {self._dim}D - {other._dim}D"
            )
        result = Vector(self._dim)
        for i in range(self._dim):
            result[i] = self._components[i] - other._components[i]
        return result
    
    def __mul__(self, other) -> Union['Vector', float]:
        """
        Multiply operator * with intelligent behavior:
        - If other is a number: scalar multiplication (returns Vector)
        - If other is a Vector: dot product (returns float)
        
        Syntax: 
            v * scalar    -> Vector (scalar multiplication)
            v1 * v2       -> float  (dot product)
        
        Examples:
            >>> v = Vector(1, 2, 3)
            >>> v * 2.5   # Scalar multiplication
            Vector([2.5, 5.0, 7.5])
            >>> v1 = Vector(1, 2, 3)
            >>> v2 = Vector(4, 5, 6)
            >>> v1 * v2   # Dot product
            32.0
        """
        # If other is a number, do scalar multiplication
        if isinstance(other, (int, float)):
            result = Vector(self._dim)
            for i in range(self._dim):
                result[i] = self._components[i] * other
            return result
        # If other is a Vector, do dot product
        elif isinstance(other, Vector):
            return self.dot(other)
        else:
            raise TypeError(f"Unsupported type for multiplication: {type(other)}")
    
    def __rmul__(self, other) -> Union['Vector', float]:
        """
        Reverse multiplication - handles scalar multiplication from the left.
        
        Examples:
            >>> 2.5 * v      # Scalar multiplication from left
            Vector([2.5, 5.0, 7.5])
        """
        # Only support scalar multiplication from the left
        if isinstance(other, (int, float)):
            return self.__mul__(other)
        raise TypeError(f"Unsupported type for reverse multiplication: {type(other)}")
    
    def __truediv__(self, other) -> 'Vector':
        """
        Divide vector by a scalar.
        
        Note: Division of two vectors (v1 / v2) is not mathematically defined.
        Use element_wise_divide() if you need element-wise division.
        
        Examples:
            >>> v = Vector(4, 6, 8)
            >>> v / 2
            Vector([2.0, 3.0, 4.0])
        """
        # Check if trying to divide by another vector
        if isinstance(other, Vector):
            raise TypeError(
                "Vector division (v1 / v2) is not mathematically defined. "
                "If you need element-wise division, use element_wise_divide(v1, v2)."
            )
        
        # Scalar division
        if not isinstance(other, (int, float)):
            raise TypeError(f"Cannot divide by type: {type(other)}")
        
        if other == 0:
            raise ValueError("Cannot divide by zero")
        
        return self * (1.0 / other)
    
    def __matmul__(self, other) -> 'Vector':
        """
        Matrix multiplication operator @ for cross product.
        
        Syntax: v1 @ v2  returns cross product
        
        Example:
            >>> v1 = Vector(1, 0, 0)
            >>> v2 = Vector(0, 1, 0)
            >>> v1 @ v2  # Returns cross product
            Vector([0, 0, 1])
        """
        return self.cross(other)
    
    def __abs__(self) -> float:
        """
        Magnitude of the vector using ||V|| notation.
        
        Syntax: ||v|| or abs(v)
        
        Example:
            >>> v = Vector(3, 4)
            >>> abs(v)  # Returns 5.0
            5.0
            >>> ||v||  # Note: Python doesn't support ||, use abs(v)
        """
        return self.magnitude()
    
    def __eq__(self, other: 'Vector') -> bool:
        """Check if two vectors are equal."""
        if self._dim != other._dim:
            return False
        eps = 1e-9
        for i in range(self._dim):
            if abs(self._components[i] - other._components[i]) >= eps:
                return False
        return True
    
    def __ne__(self, other: 'Vector') -> bool:
        """Check if two vectors are not equal."""
        return not self.__eq__(other)
    
    def __neg__(self) -> 'Vector':
        """Negate the vector."""
        result = Vector(self._dim)
        for i in range(self._dim):
            result[i] = -self._components[i]
        return result
    
    def magnitude(self) -> float:
        """
        Calculate the magnitude (length) of the vector.
        
        Also available via abs() function representing ||V|| notation.
        
        Examples:
            >>> v = Vector(3, 4)
            >>> v.magnitude()  # Returns 5.0
            5.0
            >>> abs(v)         # Same, representing ||v||
            5.0
        """
        sum_sq = sum(x*x for x in self._components)
        return sum_sq ** 0.5
    
    def magnitude_squared(self) -> float:
        """Calculate the squared magnitude (faster for comparisons)."""
        return sum(x*x for x in self._components)
    
    def normalize(self) -> 'Vector':
        """Return a normalized (unit) vector."""
        mag = self.magnitude()
        if mag == 0:
            raise ValueError("Cannot normalize zero vector")
        return self / mag
    
    def dot(self, other: 'Vector') -> float:
        """
        Calculate the dot product with another vector.
        
        Syntax: v1.dot(v2)
        
        Examples:
            >>> v1 = Vector(1, 2, 3)
            >>> v2 = Vector(4, 5, 6)
            >>> v1.dot(v2)  # Returns 32.0 (1*4 + 2*5 + 3*6)
            32.0
        """
        if self._dim != other._dim:
            raise ValueError(
                f"Dimension mismatch in dot product: {self._dim}D and {other._dim}D"
            )
        return sum(self._components[i] * other._components[i] 
                   for i in range(self._dim))
    
    def cross(self, other: 'Vector') -> 'Vector':
        """
        Calculate the cross product with another vector (3D only).
        
        Also available via @ operator: v1 @ v2
        
        Examples:
            >>> v1 = Vector(1, 0, 0)
            >>> v2 = Vector(0, 1, 0)
            >>> v1.cross(v2)  # Returns [0, 0, 1]
            >>> v1 @ v2        # Same as above using @ operator
        """
        if self._dim != 3 or other._dim != 3:
            raise ValueError("Cross product only defined for 3D vectors")
        
        return Vector(
            self.y * other.z - self.z * other.y,
            self.z * other.x - self.x * other.z,
            self.x * other.y - self.y * other.x
        )
    
    def is_3d(self) -> bool:
        """Check if this is a 3D vector."""
        return self._dim == 3
    
    def distance(self, other: 'Vector') -> float:
        """Calculate Euclidean distance to another vector."""
        return (self - other).magnitude()
    
    def distance_squared(self, other: 'Vector') -> float:
        """Calculate squared Euclidean distance (faster)."""
        return (self - other).magnitude_squared()
    
    def angle_between(self, other: 'Vector') -> float:
        """Calculate the angle between this and another vector (in radians)."""
        import math
        dot_prod = self.dot(other)
        mag1 = self.magnitude()
        mag2 = other.magnitude()
        
        if mag1 == 0 or mag2 == 0:
            raise ValueError("Cannot calculate angle with zero vector")
        
        cos_angle = dot_prod / (mag1 * mag2)
        cos_angle = max(-1.0, min(1.0, cos_angle))  # Clamp to [-1, 1]
        return math.acos(cos_angle)
    
    def projection(self, other: 'Vector') -> 'Vector':
        """Project this vector onto another vector."""
        mag2_sq = other.magnitude_squared()
        if mag2_sq == 0:
            raise ValueError("Cannot project onto zero vector")
        scalar = self.dot(other) / mag2_sq
        return other * scalar
    
    def reflection(self, normal: 'Vector') -> 'Vector':
        """Reflect this vector about a normal."""
        return self - normal * (2.0 * self.dot(normal))
    
    def lerp(self, other: 'Vector', t: float) -> 'Vector':
        """Linear interpolation between this and another vector."""
        if self._dim != other._dim:
            raise ValueError("Dimension mismatch in lerp")
        t = max(0.0, min(1.0, t))  # Clamp t to [0, 1]
        return self + (other - self) * t
    
    def cosine_similarity(self, other: 'Vector') -> float:
        """Calculate cosine similarity between vectors."""
        return self.angle_between(other)
    
    def clamp(self, min_val: float, max_val: float) -> 'Vector':
        """Clamp all components to [min_val, max_val]."""
        if min_val > max_val:
            raise ValueError("min_val must be <= max_val")
        result = Vector(self._dim)
        for i in range(self._dim):
            result[i] = max(min_val, min(max_val, self._components[i]))
        return result
    
    def to_list(self) -> List[float]:
        """Convert vector to a list."""
        return list(self._components)
    
    def to_tuple(self) -> Tuple[float, ...]:
        """Convert vector to a tuple."""
        return tuple(self._components)
    
    @classmethod
    def from_list(cls, data: List[float]) -> 'Vector':
        """Create a vector from a list."""
        return cls(data)
    
    @classmethod
    def from_numpy(cls, array: np.ndarray) -> 'Vector':
        """Create a vector from a numpy array."""
        return cls(array.flatten())
    
    def to_numpy(self) -> np.ndarray:
        """Convert vector to a numpy array."""
        return np.array(self._components)
    
    def get(self, index: int) -> float:
        """Get component at index."""
        if 0 <= index < self._dim:
            return self._components[index]
        raise IndexError(f"Index {index} out of range for {self._dim}D vector")
    
    def set(self, index: int, value: float):
        """Set component at index."""
        if 0 <= index < self._dim:
            self._components[index] = float(value)
        else:
            raise IndexError(f"Index {index} out of range for {self._dim}D vector")
    
    def resize(self, new_size: int, fill_value: float = 0.0):
        """Resize the vector to a new dimension."""
        if new_size < 0:
            raise ValueError("Dimension must be non-negative")
        
        if new_size == self._dim:
            return
        
        if new_size > self._dim:
            # Expand: pad with fill_value
            self._components.extend([fill_value] * (new_size - self._dim))
        else:
            # Shrink: truncate
            self._components = self._components[:new_size]
        
        self._dim = new_size
