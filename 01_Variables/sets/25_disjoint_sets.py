"""
Exercise 12: Disjoint Sets (Bonus)
This exercise demonstrates the concept of disjoint sets.
Two sets are disjoint if they have no elements in common (their intersection is empty).
"""

def are_disjoint(set_a, set_b):
    """
    Check if two sets are disjoint.
    
    Args:
        set_a: First set
        set_b: Second set
    
    Returns:
        True if sets are disjoint, False otherwise
    """
    # Two sets are disjoint if their intersection is empty
    return len(set_a & set_b) == 0


def main():
    print("Exercise 12: Disjoint Sets (Bonus)")
    print("=" * 50)
    
    # First pair of sets
    X = {2, 4, 6, 8}
    Y = {1, 3, 5, 7}
    
    print("a) First pair:")
    print(f"   X = {sorted(X)}")
    print(f"   Y = {sorted(Y)}")
    print()
    
    # Calculate intersection
    X_intersect_Y = X & Y
    disjoint_a = are_disjoint(X, Y)
    
    print(f"   X ∩ Y = {sorted(X_intersect_Y) if X_intersect_Y else '∅ (empty set)'}")
    print(f"   Are X and Y disjoint? {disjoint_a}")
    
    if disjoint_a:
        print("   ✓ These sets are DISJOINT (no common elements)")
    else:
        print(f"   ✗ These sets are NOT disjoint (common elements: {sorted(X_intersect_Y)})")
    
    print()
    print("-" * 50)
    print()
    
    # Second pair of sets
    R = {'a', 'b', 'c'}
    S = {'c', 'd', 'e'}
    
    print("b) Second pair:")
    print(f"   R = {sorted(R)}")
    print(f"   S = {sorted(S)}")
    print()
    
    # Calculate intersection
    R_intersect_S = R & S
    disjoint_b = are_disjoint(R, S)
    
    print(f"   R ∩ S = {sorted(R_intersect_S) if R_intersect_S else '∅ (empty set)'}")
    print(f"   Are R and S disjoint? {disjoint_b}")
    
    if disjoint_b:
        print("   ✓ These sets are DISJOINT (no common elements)")
    else:
        print(f"   ✗ These sets are NOT disjoint (common elements: {sorted(R_intersect_S)})")
    
    print("\n" + "=" * 50)
    print("Definition of Disjoint Sets:")
    print("  Two sets A and B are disjoint if and only if:")
    print("    A ∩ B = ∅ (their intersection is the empty set)")
    print()
    print("  In other words:")
    print("    - They share NO common elements")
    print("    - There is no element that belongs to both sets")
    print()
    print("Summary:")
    print(f"  - X and Y: {'DISJOINT' if disjoint_a else 'NOT disjoint'}")
    print(f"  - R and S: {'DISJOINT' if disjoint_b else 'NOT disjoint'}")
    print()
    print("Real-world example:")
    print("  - Even numbers and odd numbers are disjoint sets")
    print("  - Days of the week and months of the year are disjoint sets")


if __name__ == "__main__":
    main()
