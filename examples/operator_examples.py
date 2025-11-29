"""
Operator Examples for Vector Library

Demonstrates the intuitive operator syntax:
- Dot product: v1 * v2
- Cross product: v1 @ v2
- Magnitude: abs(v) representing ||v|| notation
- Scalar multiplication: v * scalar still works!
"""

from vectors import Vector


def main():
    print("=" * 70)
    print("Vector Library - Intuitive Operator Syntax")
    print("=" * 70)
    
    print("\n1. Dot Product with * Operator")
    print("-" * 70)
    print("Syntax: v1 * v2  (returns a scalar)")
    print("This is much more intuitive than v1.dot(v2)!")
    
    v1 = Vector(1, 2, 3)
    v2 = Vector(4, 5, 6)
    
    print(f"\nv1 = {v1}")
    print(f"v2 = {v2}")
    print(f"v1 * v2 = {v1 * v2}")
    print(f"Calculation: 1*4 + 2*5 + 3*6 = {v1 * v2}")
    
    # N-dimensional dot product
    print("\n\nN-dimensional example:")
    v3d = Vector([1, 2, 3, 4])
    v4d = Vector([5, 6, 7, 8])
    print(f"4D vectors: {v3d} * {v4d} = {v3d * v4d}")
    
    print("\n\n2. Cross Product with @ Operator")
    print("-" * 70)
    print("Syntax: v1 @ v2  (returns a vector)")
    
    # Standard basis vectors
    i_hat = Vector(1, 0, 0)
    j_hat = Vector(0, 1, 0)
    k_hat = Vector(0, 0, 1)
    
    print(f"\ni = {i_hat}")
    print(f"j = {j_hat}")
    print(f"k = {k_hat}")
    
    # Using @ operator
    result1 = i_hat @ j_hat
    print(f"\ni @ j = {result1}  (should equal k)")
    print(f"result == k: {result1 == k_hat}")
    
    result2 = j_hat @ k_hat
    print(f"j @ k = {result2}  (should equal i)")
    print(f"result == i: {result2 == i_hat}")
    
    result3 = k_hat @ i_hat
    print(f"k @ i = {result3}  (should equal j)")
    print(f"result == j: {result3 == j_hat}")
    
    # Another example
    print("\n\nExample with arbitrary vectors:")
    v1 = Vector(1, 2, 3)
    v2 = Vector(4, 5, 6)
    cross = v1 @ v2
    print(f"v1 = {v1}")
    print(f"v2 = {v2}")
    print(f"v1 @ v2 = {cross}")
    
    print("\n\n3. Magnitude Notation ||V||")
    print("-" * 70)
    print("Meaning: ||V|| is mathematical notation for the norm (magnitude) of vector V")
    print("In Python, we use: abs(v) to represent ||v||")
    print("\nThis is the Euclidean norm (L2 norm): ||v|| = sqrt(v₁² + v₂² + ...)")
    
    v = Vector(3, 4)
    magnitude = abs(v)
    print(f"\nv = {v}")
    print(f"||v|| = abs(v) = {magnitude}")
    print(f"Verification: sqrt(3² + 4²) = sqrt(9 + 16) = sqrt(25) = {magnitude}")
    
    # 3D example
    v3d = Vector(1, 2, 2)
    magnitude3d = abs(v3d)
    print(f"\nv3d = {v3d}")
    print(f"||v3d|| = {magnitude3d}")
    print(f"Verification: sqrt(1² + 2² + 2²) = sqrt(9) = {magnitude3d}")
    
    # N-dimensional example
    v10d = Vector(list(range(1, 11)))
    magnitude10d = abs(v10d)
    print(f"\n10D vector = {v10d}")
    print(f"||v|| = {magnitude10d:.4f}")
    
    # Zero vector
    v_zero = Vector(0, 0, 0)
    print(f"\nZero vector: {v_zero}")
    print(f"||zero|| = {abs(v_zero)}")
    
    print("\n\n4. Scalar Multiplication Still Works!")
    print("-" * 70)
    print("The * operator is smart - it knows when you want dot product vs scalar multiplication:")
    
    v = Vector(1, 2, 3)
    
    # Scalar multiplication
    result = v * 2.5
    print(f"\nv = {v}")
    print(f"v * 2.5 = {result}  (scalar multiplication)")
    
    # Dot product (vector * vector)
    v1 = Vector(1, 2, 3)
    v2 = Vector(4, 5, 6)
    dot = v1 * v2
    print(f"\nv1 = {v1}")
    print(f"v2 = {v2}")
    print(f"v1 * v2 = {dot}  (dot product, returns scalar)")
    
    # Reverse scalar multiplication (from left)
    result_left = 3.0 * v
    print(f"\n3.0 * v = {result_left}  (scalar multiplication from left)")
    
    print("\n\n5. Mathematical Properties")
    print("-" * 70)
    
    # Property: ||v + w|| ≤ ||v|| + ||w|| (Triangle inequality)
    v1 = Vector(1, 2, 3)
    v2 = Vector(4, 5, 6)
    norm_sum = abs(v1 + v2)
    norm_v1_plus_norm_v2 = abs(v1) + abs(v2)
    print(f"Triangle inequality: ||v₁ + v₂|| ≤ ||v₁|| + ||v₂||")
    print(f"||v₁ + v₂|| = {norm_sum:.4f}")
    print(f"||v₁|| + ||v₂|| = {norm_v1_plus_norm_v2:.4f}")
    print(f"Inequality holds: {norm_sum <= norm_v1_plus_norm_v2}")
    
    # Property: ||c·v|| = |c|·||v||
    scalar = 2.5
    v = Vector(1, 2, 3)
    norm_scaled = abs(scalar * v)
    scalar_norm = abs(scalar) * abs(v)
    print(f"\n||c·v|| = |c|·||v||")
    print(f"||c·v|| = {norm_scaled:.4f}")
    print(f"|c|·||v|| = {scalar_norm:.4f}")
    print(f"Equality holds: {abs(norm_scaled - scalar_norm) < 1e-9}")
    
    # Property: v · w = ||v||·||w||·cos(θ)
    import math
    v1 = Vector(1, 0, 0)
    v2 = Vector(1, 1, 0) / math.sqrt(2)
    dot_prod = v1 * v2  # Using * for dot product!
    norm_prod = abs(v1) * abs(v2)
    angle = math.acos(dot_prod / (abs(v1) * abs(v2)))
    print(f"\nv₁ · v₂ = ||v₁||·||v₂||·cos(θ)")
    print(f"Dot product (v1 * v2): {dot_prod:.4f}")
    print(f"Norm product: {norm_prod:.4f}")
    print(f"Angle θ: {math.degrees(angle):.1f}°")
    print(f"Verification: {dot_prod:.4f} ≈ {norm_prod:.4f}·cos({math.degrees(angle):.1f}°)")
    
    print("\n\n6. Complete Example: All Operators Together")
    print("-" * 70)
    
    v = Vector(1, 2, 3)
    w = Vector(4, 5, 6)
    scalar = 2.0
    
    print(f"Given:")
    print(f"  v = {v}")
    print(f"  w = {w}")
    print(f"  scalar = {scalar}")
    print()
    
    print(f"Operations:")
    print(f"  v + w    = {v + w}")
    print(f"  v - w    = {v - w}")
    print(f"  v * w    = {v * w}        (dot product)")
    print(f"  v @ w    = {v @ w}       (cross product)")
    print(f"  v * scalar = {v * scalar}   (scalar multiplication)")
    print(f"  ||v||    = {abs(v)}")
    print(f"  ||w||    = {abs(w)}")
    print(f"  normalized v = {v.normalize()}")
    print(f"  ||normalized v|| = {abs(v.normalize())}")
    
    print("\n\n7. Beautiful Mathematical Notation")
    print("-" * 70)
    print("You can now write mathematical expressions naturally:")
    print()
    
    a = Vector(1, 2, 3)
    b = Vector(4, 5, 6)
    c = 2.0
    
    print("Mathematical: (a · b) × c")
    dot_product = a * b  # a · b
    print(f"  Implementation: (a * b) = {dot_product}")
    
    print("\nMathematical: a × b")
    cross_product = a @ b  # a × b
    print(f"  Implementation: a @ b = {cross_product}")
    
    print("\nMathematical: ||a||")
    norm = abs(a)  # ||a||
    print(f"  Implementation: abs(a) = {norm}")
    
    print("\nMathematical: c·a")
    scaled = c * a  # c·a
    print(f"  Implementation: c * a = {scaled}")
    
    print("\n" + "=" * 70)
    print("All examples completed!")
    print("=" * 70)
    print("\nKey Takeaways:")
    print("  - v1 * v2   → dot product (scalar result)")
    print("  - v1 @ v2   → cross product (vector result)")
    print("  - v * scalar → scalar multiplication")
    print("  - abs(v)    → magnitude (||v||)")


if __name__ == "__main__":
    main()
