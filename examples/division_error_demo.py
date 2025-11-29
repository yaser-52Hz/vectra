"""
Division Error Handling Demo

Demonstrates proper error handling when attempting vector division.
"""

from vectors import Vector, element_wise_divide


def main():
    print("=" * 70)
    print("Vector Division Error Handling Demo")
    print("=" * 70)
    
    print("\n1. Scalar Division (VALID)")
    print("-" * 70)
    
    v = Vector(4, 6, 8)
    result = v / 2
    print(f"v = {v}")
    print(f"v / 2 = {result}")
    print("✓ Scalar division works perfectly!")
    
    print("\n\n2. Vector Division Attempt (INVALID)")
    print("-" * 70)
    
    v1 = Vector(4, 6, 8)
    v2 = Vector(2, 3, 4)
    
    print(f"v1 = {v1}")
    print(f"v2 = {v2}")
    print("\nAttempting: v1 / v2")
    
    try:
        result = v1 / v2  # This will raise an error
        print(f"Result: {result}")
    except TypeError as e:
        print(f"✗ Error caught: {e}")
        print("\n   Explanation: Vector division is not mathematically defined!")
        print("   The operation v1 / v2 doesn't have a clear mathematical meaning.")
    
    print("\n\n3. What to Use Instead?")
    print("-" * 70)
    print("If you need element-wise division, use the function:")
    
    v1 = Vector(6, 9, 12)
    v2 = Vector(2, 3, 4)
    
    try:
        result = element_wise_divide(v1, v2)
        print(f"\nv1 = {v1}")
        print(f"v2 = {v2}")
        print(f"element_wise_divide(v1, v2) = {result}")
        print("✓ Element-wise division works!")
    except Exception as e:
        print(f"Error: {e}")
    
    print("\n\n4. Why is Vector Division Not Defined?")
    print("-" * 70)
    print("""
    In mathematics, division between two vectors doesn't have a standard definition
    because:
    
    1. Division is the inverse of multiplication
    2. For vectors, we have:
       - Dot product: v1 · v2 (returns scalar)
       - Cross product: v1 × v2 (returns vector, only 3D)
    
    3. Neither has a clear inverse operation that would be "division"
    
    4. What you might want:
       - Element-wise division: [a1/b1, a2/b2, ...]
       - This is NOT standard vector division
    
    5. The correct approach:
       - Use element_wise_divide(v1, v2) if you need component-wise division
       - But don't think of it as "v1 divided by v2" as a vector operation
    """)
    
    print("\n\n5. Other Invalid Operations")
    print("-" * 70)
    
    # Try different edge cases
    cases = [
        ("Vector / string", lambda: Vector(1, 2) / "hello"),
        ("Vector / None", lambda: Vector(1, 2) / None),
    ]
    
    for description, operation in cases:
        print(f"\n{description}:")
        try:
            result = operation()
            print(f"  ✓ No error: {result}")
        except Exception as e:
            print(f"  ✗ Error: {type(e).__name__}: {e}")
    
    print("\n\n6. Zero Division Protection")
    print("-" * 70)
    
    v = Vector(1, 2, 3)
    print(f"v = {v}")
    print("Attempting: v / 0")
    
    try:
        result = v / 0
        print(f"Result: {result}")
    except ValueError as e:
        print(f"✗ Error caught: {e}")
        print("✓ Zero division is properly protected!")
    
    print("\n" + "=" * 70)
    print("Summary:")
    print("  ✓ v / scalar     → Works (scalar division)")
    print("  ✗ v1 / v2        → Error (not mathematically defined)")
    print("  ✓ element_wise_divide(v1, v2) → Works (if you need it)")
    print("=" * 70)


if __name__ == "__main__":
    main()

