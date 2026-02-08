"""
Exercise 3: Union of Sets
This exercise demonstrates the union operation between sets.
The union combines all unique elements from both sets.
"""

def main():
    # Define two sets
    A = {1, 3, 5, 7}
    B = {2, 3, 4, 5}
    
    print("Exercise 3: Union of Sets")
    print("=" * 50)
    print(f"Set A = {sorted(A)}")
    print(f"Set B = {sorted(B)}")
    print()
    
    # a) Calculate A ∪ B (union of A and B)
    # The union operator | or the union() method can be used
    union_AB = A | B  # Alternative: A.union(B)
    print(f"a) A ∪ B = {sorted(union_AB)}")
    print()
    
    # b) Count the number of elements in A ∪ B
    num_elements = len(union_AB)
    print(f"b) Number of elements in A ∪ B: {num_elements}")
    
    print("\n" + "=" * 50)
    print("Explanation:")
    print("  - The union (∪) combines all elements from both sets")
    print("  - Duplicate elements appear only once in the result")
    print(f"  - Elements 3 and 5 appear in both sets, but only once in the union")
    print(f"  - |A| = {len(A)}, |B| = {len(B)}, |A ∪ B| = {num_elements}")


if __name__ == "__main__":
    main()
