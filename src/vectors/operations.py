"""
Vector Operations - High-level mathematical operations on vectors

This module provides various vector operations optimized for n-dimensional vectors.
The C++ backend provides high performance for these operations.
"""

from .vector import Vector
from typing import Tuple, List, Union, Optional
import numpy as np


def add(v1: Vector, v2: Vector) -> Vector:
    """
    Add two vectors.
    
    Args:
        v1: First vector
        v2: Second vector
    
    Returns:
        Vector: The sum of the two vectors
    
    Examples:
        >>> v1 = Vector(1, 2, 3)
        >>> v2 = Vector(4, 5, 6)
        >>> add(v1, v2)
        Vector(5, 7, 9)
    """
    # TODO: Implement using C++ backend
    return v1 + v2


def subtract(v1: Vector, v2: Vector) -> Vector:
    """
    Subtract one vector from another.
    
    Args:
        v1: First vector
        v2: Second vector
    
    Returns:
        Vector: The difference of the two vectors
    """
    # TODO: Implement using C++ backend
    return v1 - v2


def multiply(v: Vector, scalar: float) -> Vector:
    """
    Multiply a vector by a scalar.
    
    Args:
        v: Vector to multiply
        scalar: Scalar value
    
    Returns:
        Vector: The scaled vector
    """
    # TODO: Implement using C++ backend
    return v * scalar


def divide(v: Vector, scalar: float) -> Vector:
    """
    Divide a vector by a scalar.
    
    Args:
        v: Vector to divide
        scalar: Scalar value
    
    Returns:
        Vector: The divided vector
    """
    # TODO: Implement using C++ backend
    return v / scalar


def dot_product(v1: Vector, v2: Vector) -> float:
    """
    Calculate the dot product of two vectors.
    
    Args:
        v1: First vector
        v2: Second vector
    
    Returns:
        float: The dot product
    """
    # TODO: Implement using C++ backend
    return v1.dot(v2)


def cross_product(v1: Vector, v2: Vector) -> Vector:
    """
    Calculate the cross product of two vectors.
    
    Args:
        v1: First vector
        v2: Second vector
    
    Returns:
        Vector: The cross product
    """
    # TODO: Implement using C++ backend
    return v1.cross(v2)


def magnitude(v: Vector) -> float:
    """
    Calculate the magnitude (length) of a vector.
    
    Args:
        v: Vector
    
    Returns:
        float: The magnitude
    """
    # TODO: Implement using C++ backend
    return v.magnitude()


def normalize(v: Vector) -> Vector:
    """
    Normalize a vector to unit length.
    
    Args:
        v: Vector to normalize
    
    Returns:
        Vector: The normalized vector
    """
    # TODO: Implement using C++ backend
    return v.normalize()


def distance(v1: Vector, v2: Vector) -> float:
    """
    Calculate the Euclidean distance between two vectors.
    
    Args:
        v1: First vector
        v2: Second vector
    
    Returns:
        float: The distance
    """
    # TODO: Implement using C++ backend
    diff = v1 - v2
    return diff.magnitude()


def angle_between(v1: Vector, v2: Vector) -> float:
    """
    Calculate the angle between two vectors in radians.
    
    Args:
        v1: First vector
        v2: Second vector
    
    Returns:
        float: The angle in radians
    """
    # TODO: Implement using C++ backend
    import math
    dot = v1.dot(v2)
    mag1 = v1.magnitude()
    mag2 = v2.magnitude()
    if mag1 == 0 or mag2 == 0:
        raise ValueError("Cannot calculate angle with zero vector")
    cos_angle = dot / (mag1 * mag2)
    cos_angle = max(-1.0, min(1.0, cos_angle))  # Clamp to [-1, 1]
    return math.acos(cos_angle)


def projection(v1: Vector, v2: Vector) -> Vector:
    """
    Calculate the projection of v1 onto v2.
    
    Args:
        v1: Vector to project
        v2: Vector to project onto
    
    Returns:
        Vector: The projection of v1 onto v2
    """
    # TODO: Implement using C++ backend
    mag2 = v2.magnitude()
    if mag2 == 0:
        raise ValueError("Cannot project onto zero vector")
    scalar = v1.dot(v2) / (mag2 * mag2)
    return v2 * scalar


def reflection(v: Vector, normal: Vector) -> Vector:
    """
    Calculate the reflection of a vector about a normal.
    
    Args:
        v: Vector to reflect
        normal: Normal vector (should be normalized)
    
    Returns:
        Vector: The reflected vector
    """
    # TODO: Implement using C++ backend
    return v - 2 * (v.dot(normal)) * normal


def rotate(v: Vector, axis: Vector, angle: float) -> Vector:
    """
    Rotate a vector around an axis by a given angle (3D only).
    
    Args:
        v: Vector to rotate
        axis: Rotation axis (should be normalized)
        angle: Rotation angle in radians
    
    Returns:
        Vector: The rotated vector
    """
    if not v.is_3d() or not axis.is_3d():
        raise ValueError("Rotation only supported for 3D vectors")
    
    # Rodrigues rotation formula
    import math
    cos_a = math.cos(angle)
    sin_a = math.sin(angle)
    
    term1 = v * cos_a
    term2 = v.cross(axis) * sin_a
    term3 = axis * (axis.dot(v) * (1 - cos_a))
    
    return term1 + term2 + term3


# Advanced operations for scientific computing


def batch_add(vectors1: List[Vector], vectors2: List[Vector]) -> List[Vector]:
    """
    Add multiple pairs of vectors efficiently.
    
    Args:
        vectors1: First list of vectors
        vectors2: Second list of vectors
    
    Returns:
        List[Vector]: List of added vectors
    """
    # TODO: Implement using C++ backend with batch processing
    if len(vectors1) != len(vectors2):
        raise ValueError("Vector lists must have the same length")
    return [v1 + v2 for v1, v2 in zip(vectors1, vectors2)]


def batch_dot_product(vectors1: List[Vector], vectors2: List[Vector]) -> List[float]:
    """
    Calculate dot products for multiple pairs of vectors efficiently.
    
    Args:
        vectors1: First list of vectors
        vectors2: Second list of vectors
    
    Returns:
        List[float]: List of dot products
    """
    # TODO: Implement using C++ backend with SIMD optimizations
    if len(vectors1) != len(vectors2):
        raise ValueError("Vector lists must have the same length")
    return [v1.dot(v2) for v1, v2 in zip(vectors1, vectors2)]


def centroid(vectors: List[Vector]) -> Vector:
    """
    Calculate the centroid (average) of multiple vectors.
    
    Args:
        vectors: List of vectors
    
    Returns:
        Vector: The centroid vector
    """
    # TODO: Implement using C++ backend
    if not vectors:
        raise ValueError("Cannot calculate centroid of empty list")
    sum_vec = Vector(0, 0, 0)
    for v in vectors:
        sum_vec = sum_vec + v
    return sum_vec / len(vectors)


def weighted_average(vectors: List[Vector], weights: List[float]) -> Vector:
    """
    Calculate the weighted average of multiple vectors.
    
    Args:
        vectors: List of vectors
        weights: List of weights
    
    Returns:
        Vector: The weighted average vector
    """
    # TODO: Implement using C++ backend
    if len(vectors) != len(weights):
        raise ValueError("Vectors and weights must have the same length")
    if not vectors:
        raise ValueError("Cannot calculate weighted average of empty list")
    
    total_weight = sum(weights)
    if total_weight == 0:
        raise ValueError("Total weight cannot be zero")
    
    sum_vec = Vector(0, 0, 0)
    for v, w in zip(vectors, weights):
        sum_vec = sum_vec + (v * w)
    
    return sum_vec / total_weight


def element_wise_multiply(v1: Vector, v2: Vector) -> Vector:
    """
    Multiply two vectors element-wise (Hadamard product).
    
    Args:
        v1: First vector
        v2: Second vector
    
    Returns:
        Vector: Element-wise product
    """
    if len(v1) != len(v2):
        raise ValueError("Vectors must have the same dimension for element-wise multiply")
    return Vector([v1[i] * v2[i] for i in range(len(v1))])


def element_wise_divide(v1: Vector, v2: Vector) -> Vector:
    """
    Divide two vectors element-wise.
    
    Args:
        v1: Numerator vector
        v2: Denominator vector
    
    Returns:
        Vector: Element-wise quotient
    """
    if len(v1) != len(v2):
        raise ValueError("Vectors must have the same dimension for element-wise divide")
    return Vector([v1[i] / v2[i] for i in range(len(v1))])


def sum_elements(v: Vector) -> float:
    """
    Calculate the sum of all vector elements.
    
    Args:
        v: Vector
    
    Returns:
        float: Sum of all components
    """
    return sum(v.components)


def max_element(v: Vector) -> float:
    """
    Find the maximum element in the vector.
    
    Args:
        v: Vector
    
    Returns:
        float: Maximum component value
    """
    if len(v) == 0:
        raise ValueError("Cannot find max of empty vector")
    return max(v.components)


def min_element(v: Vector) -> float:
    """
    Find the minimum element in the vector.
    
    Args:
        v: Vector
    
    Returns:
        float: Minimum component value
    """
    if len(v) == 0:
        raise ValueError("Cannot find min of empty vector")
    return min(v.components)


def mean_element(v: Vector) -> float:
    """
    Calculate the mean of vector elements.
    
    Args:
        v: Vector
    
    Returns:
        float: Mean of components
    """
    if len(v) == 0:
        raise ValueError("Cannot find mean of empty vector")
    return sum_elements(v) / len(v)


__all__ = [
    "add",
    "subtract",
    "multiply",
    "divide",
    "dot_product",
    "cross_product",
    "magnitude",
    "normalize",
    "distance",
    "angle_between",
    "projection",
    "reflection",
    "rotate",
    "batch_add",
    "batch_dot_product",
    "centroid",
    "weighted_average",
    "element_wise_multiply",
    "element_wise_divide",
    "sum_elements",
    "max_element",
    "min_element",
    "mean_element",
]

