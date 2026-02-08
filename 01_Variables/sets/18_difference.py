"""
Exercise 5: Difference of Sets
This exercise demonstrates the set difference operation.
The difference A - B contains elements in A but not in B.
"""

def main():
    # Define two sets
    M = {1, 2, 3, 4, 5, 6}
    N = {2, 4, 6, 8}
    
    print("Exercise 5: Difference of Sets")
    print("=" * 50)
    print(f"Set M = {sorted(M)}")
    print(f"Set N = {sorted(N)}")
    print()
    
    # a) Calculate M - N (elements in M but not in N)
    # The difference operator - or the difference() method can be used
    diff_M_N = M - N  # Alternative: M.difference(N)
    print(f"a) M - N = {sorted(diff_M_N)}")
    print(f"   (Elements in M that are NOT in N)")
    print()
    
    # b) Calculate N - M (elements in N but not in M)
    diff_N_M = N - M  # Alternative: N.difference(M)
    print(f"b) N - M = {sorted(diff_N_M)}")
    print(f"   (Elements in N that are NOT in M)")
    print()
    
    # c) Check if M - N equals N - M
    are_equal = diff_M_N == diff_N_M
    print(f"c) Is M - N = N - M? {are_equal}")
    
    print("\n" + "=" * 50)
    print("Explanation:")
    print("  - Set difference is NOT commutative: M - N ≠ N - M")
    print(f"  - M - N = {sorted(diff_M_N)} (elements only in M)")
    print(f"  - N - M = {sorted(diff_N_M)} (elements only in N)")
    print("  - The order matters in set difference operations!")


if __name__ == "__main__":
    main()
