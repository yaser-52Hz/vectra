"""
Basic Usage Examples for the Vector Library

This script demonstrates the fundamental operations of the vector library.
"""

from vectors import Vector, add, subtract, multiply, divide
from vectors import dot_product, cross_product, magnitude, normalize
from vectors import distance, angle_between


def main():
    print("=" * 60)
    print("Vector Library - Basic Usage Examples")
    print("=" * 60)
    
    # Create vectors
    print("\n1. Creating Vectors")
    print("-" * 60)
    v1 = Vector(1, 2, 3)
    v2 = Vector(4, 5, 6)
    print(f"v1 = {v1}")
    print(f"v2 = {v2}")
    
    # Arithmetic operations
    print("\n2. Arithmetic Operations")
    print("-" * 60)
    v3 = v1 + v2
    print(f"v1 + v2 = {v3}")
    
    v4 = v2 - v1
    print(f"v2 - v1 = {v4}")
    
    v5 = v1 * 2.5
    print(f"v1 * 2.5 = {v5}")
    
    v6 = v2 / 2
    print(f"v2 / 2 = {v6}")
    
    # Vector operations
    print("\n3. Vector Operations")
    print("-" * 60)
    dot = v1.dot(v2)
    print(f"v1 · v2 = {dot}")
    
    cross = v1.cross(v2)
    print(f"v1 × v2 = {cross}")
    
    mag = v1.magnitude()
    print(f"|v1| = {mag}")
    
    normalized = v1.normalize()
    print(f"v1 normalized = {normalized}")
    print(f"Magnitude of normalized v1 = {normalized.magnitude()}")
    
    # Distance and angle
    print("\n4. Distance and Angle")
    print("-" * 60)
    dist = distance(v1, v2)
    print(f"Distance between v1 and v2 = {dist}")
    
    angle = angle_between(v1, v2)
    print(f"Angle between v1 and v2 = {angle} radians")
    print(f"Angle between v1 and v2 = {angle * 180 / 3.14159:.2f} degrees")
    
    # Using functional API
    print("\n5. Functional API")
    print("-" * 60)
    v_sum = add(v1, v2)
    print(f"add(v1, v2) = {v_sum}")
    
    v_diff = subtract(v2, v1)
    print(f"subtract(v2, v1) = {v_diff}")
    
    dot_func = dot_product(v1, v2)
    print(f"dot_product(v1, v2) = {dot_func}")
    
    cross_func = cross_product(v1, v2)
    print(f"cross_product(v1, v2) = {cross_func}")
    
    print("\n" + "=" * 60)
    print("Examples completed!")
    print("=" * 60)


if __name__ == "__main__":
    main()

