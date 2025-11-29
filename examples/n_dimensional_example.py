"""
N-Dimensional Vector Example

This script demonstrates the n-dimensional capabilities of the vector library.
You can create vectors of any dimension, not just 2D or 3D.
"""

from vectors import Vector, dot_product, distance, magnitude


def main():
    print("=" * 60)
    print("N-Dimensional Vector Examples")
    print("=" * 60)
    
    # Different ways to create vectors
    print("\n1. Creating N-Dimensional Vectors")
    print("-" * 60)
    
    # 2D vector
    v2d = Vector(1, 2)
    print(f"2D Vector: {v2d} (dimension: {len(v2d)})")
    
    # 3D vector (default for backward compatibility)
    v3d = Vector(1, 2, 3)
    print(f"3D Vector: {v3d} (dimension: {len(v3d)})")
    
    # 4D vector
    v4d = Vector(1, 2, 3, 4)
    print(f"4D Vector: {v4d} (dimension: {len(v4d)})")
    
    # 5D vector from list
    v5d = Vector([1, 2, 3, 4, 5])
    print(f"5D Vector: {v5d} (dimension: {len(v5d)})")
    
    # 10D vector
    v10d = Vector([i for i in range(1, 11)])
    print(f"10D Vector: {v10d}")
    print(f"  Components: {list(v10d.components)}")
    
    # Create zero vector of specific dimension
    zero_5d = Vector(5)  # 5-dimensional zero vector
    print(f"5D Zero Vector: {zero_5d}")
    
    # Operations with different dimensions
    print("\n2. Operations with N-Dimensional Vectors")
    print("-" * 60)
    
    # Create two 4D vectors
    u = Vector(1, 2, 3, 4)
    v = Vector(5, 6, 7, 8)
    
    # Basic operations
    result = u + v
    print(f"u + v = {result}")
    
    result = v - u
    print(f"v - u = {result}")
    
    result = u * 2.5
    print(f"u * 2.5 = {result}")
    
    # Dot product
    dot = u.dot(v)
    print(f"u · v = {dot}")
    
    # Magnitude
    mag = magnitude(u)
    print(f"|u| = {mag}")
    
    # Distance
    dist = distance(u, v)
    print(f"Distance between u and v = {dist}")
    
    # Normalized vector
    normalized = u.normalize()
    print(f"Normalized u = {normalized}")
    print(f"Magnitude of normalized u = {magnitude(normalized)}")
    
    # Element access
    print("\n3. Element Access")
    print("-" * 60)
    print(f"u[0] = {u[0]}")
    print(f"u[1] = {u[1]}")
    print(f"u[2] = {u[2]}")
    print(f"u[3] = {u[3]}")
    
    # Modify element
    u[0] = 10
    print(f"After u[0] = 10: u = {u}")
    
    # High-dimensional examples
    print("\n4. High-Dimensional Examples")
    print("-" * 60)
    
    # 100D vectors
    large_a = Vector(list(range(100)))
    large_b = Vector(list(range(100, 200)))
    
    print(f"Created two 100D vectors")
    print(f"Dot product: {large_a.dot(large_b)}")
    print(f"Magnitude of first: {magnitude(large_a)}")
    
    # Element-wise operations
    print("\n5. Element-wise Operations")
    print("-" * 60)
    from vectors import element_wise_multiply, element_wise_divide
    
    a = Vector(1, 2, 3, 4, 5)
    b = Vector(2, 3, 4, 5, 6)
    
    elem_mult = element_wise_multiply(a, b)
    print(f"a = {a}")
    print(f"b = {b}")
    print(f"Element-wise multiply: {elem_mult}")
    
    elem_div = element_wise_divide(b, a)
    print(f"Element-wise divide (b/a): {elem_div}")
    
    # Statistical operations
    print("\n6. Statistical Operations")
    print("-" * 60)
    from vectors import sum_elements, max_element, min_element, mean_element
    
    stats_vector = Vector([1, 5, 3, 9, 2, 7, 4])
    print(f"Vector: {stats_vector}")
    print(f"Sum: {sum_elements(stats_vector)}")
    print(f"Max: {max_element(stats_vector)}")
    print(f"Min: {min_element(stats_vector)}")
    print(f"Mean: {mean_element(stats_vector)}")
    
    # Clamping
    print("\n7. Clamping Values")
    print("-" * 60)
    unclamped = Vector([-5, 15, 3, 8, -2, 10])
    print(f"Original: {unclamped}")
    clamped = unclamped.clamp(0, 5)
    print(f"Clamped to [0, 5]: {clamped}")
    
    # Linear interpolation
    print("\n8. Linear Interpolation")
    print("-" * 60)
    start = Vector(0, 0, 0, 0)
    end = Vector(10, 20, 30, 40)
    
    interpolated = start.lerp(end, 0.5)
    print(f"Start: {start}")
    print(f"End: {end}")
    print(f"Lerp at t=0.5: {interpolated}")
    print(f"Lerp at t=0.25: {start.lerp(end, 0.25)}")
    print(f"Lerp at t=0.75: {start.lerp(end, 0.75)}")
    
    print("\n" + "=" * 60)
    print("N-dimensional examples completed!")
    print("=" * 60)


if __name__ == "__main__":
    main()

