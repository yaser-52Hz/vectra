"""
Advanced Operations Examples for the Vector Library

This script demonstrates advanced vector operations including projections,
reflections, rotations, and batch operations.
"""

import math
from vectors import (
    Vector, projection, reflection, rotate,
    batch_add, batch_dot_product, centroid, weighted_average
)


def main():
    print("=" * 60)
    print("Vector Library - Advanced Operations Examples")
    print("=" * 60)
    
    # Projection
    print("\n1. Vector Projection")
    print("-" * 60)
    v = Vector(3, 4, 0)
    onto = Vector(1, 0, 0)
    proj = projection(v, onto)
    print(f"v = {v}")
    print(f"Project onto = {onto}")
    print(f"Projection of v onto onto = {proj}")
    
    # Reflection
    print("\n2. Vector Reflection")
    print("-" * 60)
    incident = Vector(1, 1, 0)
    normal = Vector(0, 1, 0).normalize()
    reflected = reflection(incident, normal)
    print(f"Incident vector = {incident}")
    print(f"Normal vector = {normal}")
    print(f"Reflected vector = {reflected}")
    
    # Rotation
    print("\n3. Vector Rotation")
    print("-" * 60)
    v_original = Vector(1, 0, 0)
    axis = Vector(0, 0, 1).normalize()
    angle = math.pi / 2  # 90 degrees
    
    rotated = rotate(v_original, axis, angle)
    print(f"Original vector = {v_original}")
    print(f"Rotation axis = {axis}")
    print(f"Rotation angle = {angle * 180 / math.pi:.0f} degrees")
    print(f"Rotated vector = {rotated}")
    
    # Multiple rotations
    print("\n   Multiple rotations:")
    current = v_original
    for i in range(4):
        print(f"   After {i * 90}° rotation: {current}")
        current = rotate(current, axis, angle)
    
    # Batch operations
    print("\n4. Batch Operations")
    print("-" * 60)
    vectors1 = [
        Vector(1, 2, 3),
        Vector(4, 5, 6),
        Vector(7, 8, 9)
    ]
    vectors2 = [
        Vector(10, 11, 12),
        Vector(13, 14, 15),
        Vector(16, 17, 18)
    ]
    
    batch_result = batch_add(vectors1, vectors2)
    print("Batch addition:")
    for i, (v1, v2, result) in enumerate(zip(vectors1, vectors2, batch_result)):
        print(f"  {v1} + {v2} = {result}")
    
    # Batch dot products
    dots = batch_dot_product(vectors1, vectors2)
    print("\nBatch dot products:")
    for i, (v1, v2, dot) in enumerate(zip(vectors1, vectors2, dots)):
        print(f"  {v1} · {v2} = {dot}")
    
    # Centroid
    print("\n5. Centroid Calculation")
    print("-" * 60)
    points = [
        Vector(0, 0, 0),
        Vector(1, 0, 0),
        Vector(0, 1, 0),
        Vector(0, 0, 1)
    ]
    center = centroid(points)
    print("Points:")
    for point in points:
        print(f"  {point}")
    print(f"Centroid = {center}")
    
    # Weighted average
    print("\n6. Weighted Average")
    print("-" * 60)
    data_points = [
        Vector(0, 0),
        Vector(5, 0),
        Vector(0, 5),
        Vector(5, 5)
    ]
    weights = [1, 2, 2, 3]
    
    weighted_avg = weighted_average(data_points, weights)
    print("Data points:")
    for point, weight in zip(data_points, weights):
        print(f"  {point} (weight: {weight})")
    print(f"Weighted average = {weighted_avg}")
    
    print("\n" + "=" * 60)
    print("Advanced examples completed!")
    print("=" * 60)


if __name__ == "__main__":
    main()

