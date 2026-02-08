"""
Exercise 11: Cartesian Product (Bonus)
This exercise demonstrates the Cartesian product of two sets.
The Cartesian product A × B is the set of all ordered pairs (a, b) where a ∈ A and b ∈ B.
"""

from itertools import product


def cartesian_product(set_a, set_b):
    """
    Calculate the Cartesian product of two sets.
    
    Args:
        set_a: First set
        set_b: Second set
    
    Returns:
        Set of tuples representing the Cartesian product
    """
    # Using itertools.product for efficient computation
    return set(product(sorted(set_a), sorted(set_b)))


def main():
    # Define two sets
    A = {1, 2}
    B = {'x', 'y'}
    
    print("Exercise 11: Cartesian Product (Bonus)")
    print("=" * 50)
    print(f"Set A = {sorted(A)}")
    print(f"Set B = {sorted(B)}")
    print()
    
    # a) Calculate A × B
    A_cross_B = cartesian_product(A, B)
    print("a) A × B (Cartesian Product of A and B):")
    print(f"   A × B = {{(a, b) | a ∈ A and b ∈ B}}")
    print(f"   A × B = {sorted(A_cross_B)}")
    print()
    print("   Expanded:")
    for pair in sorted(A_cross_B):
        print(f"     {pair}")
    print()
    
    # b) Calculate B × A
    B_cross_A = cartesian_product(B, A)
    print("b) B × A (Cartesian Product of B and A):")
    print(f"   B × A = {{(b, a) | b ∈ B and a ∈ A}}")
    print(f"   B × A = {sorted(B_cross_A)}")
    print()
    print("   Expanded:")
    for pair in sorted(B_cross_A):
        print(f"     {pair}")
    print()
    
    # c) Check if A × B = B × A
    are_equal = A_cross_B == B_cross_A
    print(f"c) Is A × B = B × A? {are_equal}")
    
    print("\n" + "=" * 50)
    print("Explanation:")
    print("  - The Cartesian product is the set of all ordered pairs")
    print("  - Order matters in ordered pairs: (1, x) ≠ (x, 1)")
    print("  - Therefore, A × B ≠ B × A (not commutative)")
    print()
    print(f"  - |A × B| = |A| × |B| = {len(A)} × {len(B)} = {len(A_cross_B)}")
    print(f"  - |B × A| = |B| × |A| = {len(B)} × {len(A)} = {len(B_cross_A)}")
    print()
    print("  Example comparison:")
    print(f"    A × B contains: (1, 'x'), (1, 'y'), (2, 'x'), (2, 'y')")
    print(f"    B × A contains: ('x', 1), ('x', 2), ('y', 1), ('y', 2)")
    print("    These are completely different sets!")


if __name__ == "__main__":
    main()
