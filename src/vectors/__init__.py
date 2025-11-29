"""
Vectra - High-performance n-dimensional vector operations with C++ backend

A professional vector mathematics library for scientific and mathematical computing.
The core implementation is in C++ for maximum performance, exposed through Python bindings.

Author: Yasser Hosseinzadeh
Email: one.astro.nerd@gmail.com
"""

__version__ = "0.2.0"
__author__ = "Yasser Hosseinzadeh"
__email__ = "one.astro.nerd@gmail.com"

from .vector import Vector
from .operations import (
    add,
    subtract,
    multiply,
    divide,
    dot_product,
    cross_product,
    magnitude,
    normalize,
    distance,
    angle_between,
    projection,
    reflection,
    rotate,
    batch_add,
    batch_dot_product,
    centroid,
    weighted_average,
    element_wise_multiply,
    element_wise_divide,
    sum_elements,
    max_element,
    min_element,
    mean_element,
)

__all__ = [
    "Vector",
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

