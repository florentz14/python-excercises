"""
Exercise 8: Combined Set Operations
This exercise demonstrates how to perform multiple set operations in sequence.
It illustrates the use of parentheses and order of operations.
"""

def main():
    # Define three sets
    A = {1, 2, 3, 4}
    B = {3, 4, 5, 6}
    C = {5, 6, 7, 8}
    
    print("Exercise 8: Combined Set Operations")
    print("=" * 50)
    print(f"Set A = {sorted(A)}")
    print(f"Set B = {sorted(B)}")
    print(f"Set C = {sorted(C)}")
    print()
    
    # a) (A ∪ B) ∩ C
    # First compute the union of A and B, then intersect with C
    A_union_B = A | B
    result_a = A_union_B & C
    
    print("a) (A ∪ B) ∩ C")
    print(f"   Step 1: A ∪ B = {sorted(A_union_B)}")
    print(f"   Step 2: (A ∪ B) ∩ C = {sorted(result_a)}")
    print(f"   Result: {sorted(result_a)}")
    print()
    
    # b) A ∪ (B ∩ C)
    # First compute the intersection of B and C, then union with A
    B_intersect_C = B & C
    result_b = A | B_intersect_C
    
    print("b) A ∪ (B ∩ C)")
    print(f"   Step 1: B ∩ C = {sorted(B_intersect_C)}")
    print(f"   Step 2: A ∪ (B ∩ C) = {sorted(result_b)}")
    print(f"   Result: {sorted(result_b)}")
    print()
    
    # c) (A ∩ B) ∪ (B ∩ C)
    # Compute two intersections, then union them
    A_intersect_B = A & B
    B_intersect_C_again = B & C
    result_c = A_intersect_B | B_intersect_C_again
    
    print("c) (A ∩ B) ∪ (B ∩ C)")
    print(f"   Step 1: A ∩ B = {sorted(A_intersect_B)}")
    print(f"   Step 2: B ∩ C = {sorted(B_intersect_C_again)}")
    print(f"   Step 3: (A ∩ B) ∪ (B ∩ C) = {sorted(result_c)}")
    print(f"   Result: {sorted(result_c)}")
    
    print("\n" + "=" * 50)
    print("Summary of Results:")
    print(f"  (A ∪ B) ∩ C = {sorted(result_a)}")
    print(f"  A ∪ (B ∩ C) = {sorted(result_b)}")
    print(f"  (A ∩ B) ∪ (B ∩ C) = {sorted(result_c)}")
    print()
    print("Key Observations:")
    print("  - Parentheses determine the order of operations")
    print("  - Different groupings produce different results")
    print("  - ∩ (intersection) and ∪ (union) don't follow same precedence rules")


if __name__ == "__main__":
    main()
