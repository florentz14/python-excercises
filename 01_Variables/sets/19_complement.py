"""
Exercise 6: Complement of Sets
This exercise demonstrates the complement operation.
The complement A' contains all elements in the universal set U that are not in A.
"""

def main():
    # Define the universal set and subset A
    U = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10}  # Universal set
    A = {2, 4, 6, 8, 10}                 # Subset of U
    
    print("Exercise 6: Complement of Sets")
    print("=" * 50)
    print(f"Universal Set U = {sorted(U)}")
    print(f"Set A = {sorted(A)}")
    print()
    
    # a) Calculate A' (complement of A with respect to U)
    # The complement is U - A (all elements in U that are not in A)
    A_complement = U - A
    print(f"a) A' (complement of A) = {sorted(A_complement)}")
    print(f"   A' = U - A = {sorted(A_complement)}")
    print()
    
    # b) Calculate (A')' (complement of the complement)
    # This should give us back the original set A
    A_double_complement = U - A_complement
    print(f"b) (A')' (complement of complement) = {sorted(A_double_complement)}")
    
    # Verify that (A')' = A
    is_equal = A_double_complement == A
    print(f"   Is (A')' = A? {is_equal}")
    
    print("\n" + "=" * 50)
    print("Explanation:")
    print("  - The complement A' contains all elements in U that are NOT in A")
    print("  - A' = U - A")
    print("  - The complement of the complement returns the original set")
    print("  - (A')' = A (Law of Double Complement)")
    print(f"  - Verification: A ∪ A' = {sorted(A | A_complement)} = U")
    print(f"  - Verification: A ∩ A' = {sorted(A & A_complement)} = ∅ (empty set)")


if __name__ == "__main__":
    main()
