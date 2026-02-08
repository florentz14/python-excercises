"""
Exercise 9: Cardinality (Size) of Sets
This exercise demonstrates set cardinality and the inclusion-exclusion principle.
Cardinality refers to the number of elements in a set.
"""

def main():
    # Define two sets
    A = {2, 4, 6, 8}
    B = {1, 3, 5, 7, 9}
    
    print("Exercise 9: Cardinality of Sets")
    print("=" * 50)
    print(f"Set A = {sorted(A)}")
    print(f"Set B = {sorted(B)}")
    print()
    
    # a) Calculate n(A), n(B), and n(A ∪ B)
    n_A = len(A)
    n_B = len(B)
    
    # Calculate the union
    A_union_B = A | B
    n_A_union_B = len(A_union_B)
    
    print("a) Cardinalities:")
    print(f"   n(A) = |A| = {n_A}")
    print(f"   n(B) = |B| = {n_B}")
    print(f"   A ∪ B = {sorted(A_union_B)}")
    print(f"   n(A ∪ B) = |A ∪ B| = {n_A_union_B}")
    print()
    
    # b) Check if n(A ∪ B) = n(A) + n(B)
    sum_cardinalities = n_A + n_B
    are_equal = (n_A_union_B == sum_cardinalities)
    
    print("b) Does n(A ∪ B) = n(A) + n(B)?")
    print(f"   n(A) + n(B) = {n_A} + {n_B} = {sum_cardinalities}")
    print(f"   n(A ∪ B) = {n_A_union_B}")
    print(f"   Are they equal? {are_equal}")
    print()
    
    # Calculate intersection to explain
    A_intersect_B = A & B
    n_A_intersect_B = len(A_intersect_B)
    
    print("   Why?")
    if n_A_intersect_B == 0:
        print(f"   - A ∩ B = ∅ (empty set)")
        print("   - Sets A and B are DISJOINT (no common elements)")
        print("   - For disjoint sets: n(A ∪ B) = n(A) + n(B)")
        print("   - This is why the equality holds in this case!")
    else:
        print(f"   - A ∩ B = {sorted(A_intersect_B)}")
        print(f"   - n(A ∩ B) = {n_A_intersect_B}")
        print("   - Sets A and B have common elements")
        print("   - For sets with overlap:")
        print("     n(A ∪ B) = n(A) + n(B) - n(A ∩ B)")
        print(f"     n(A ∪ B) = {n_A} + {n_B} - {n_A_intersect_B} = {n_A + n_B - n_A_intersect_B}")
    
    print("\n" + "=" * 50)
    print("Inclusion-Exclusion Principle:")
    print("  For any two sets A and B:")
    print("  n(A ∪ B) = n(A) + n(B) - n(A ∩ B)")
    print()
    print(f"  In this example:")
    print(f"  {n_A_union_B} = {n_A} + {n_B} - {n_A_intersect_B}")
    print(f"  {n_A_union_B} = {n_A + n_B - n_A_intersect_B} ✓")


if __name__ == "__main__":
    main()
