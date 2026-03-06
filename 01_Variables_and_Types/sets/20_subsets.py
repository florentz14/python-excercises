# -------------------------------------------------
# File Name: 20_subsets.py
# Author: Florentino Báez
# Date: Variables - Sets
# Description: Subsets of a Set.
#              Generates all 2^n subsets of a given set using
#              itertools.combinations. Explains the difference
#              between proper subsets and improper subsets.
# -------------------------------------------------

"""
Exercise 7: Subsets
This exercise demonstrates how to find all possible subsets of a set.
For a set with n elements, there are 2^n possible subsets.
"""

from itertools import combinations


def get_all_subsets(input_set):
    """
    Generate all possible subsets of a given set.
    
    Args:
        input_set: The input set
    
    Returns:
        A list of all subsets (as sets)
    """
    # Convert set to list for iteration
    elements = list(input_set)
    all_subsets = []
    
    # Generate subsets of all possible sizes (0 to n)
    # Size 0 = empty set, Size n = the set itself
    for size in range(len(elements) + 1):
        # Use combinations to get all subsets of current size
        # combinations() generates all ways to choose 'size' elements
        for subset in combinations(elements, size):
            all_subsets.append(set(subset))
    
    return all_subsets


def main():
    # Define set S with three elements
    S = {'x', 'y', 'z'}
    
    print("Exercise 7: Subsets")
    print("=" * 50)
    print(f"Set S = {sorted(S)}")
    print()
    
    # Get all possible subsets using the helper function
    all_subsets = get_all_subsets(S)
    
    # Sort subsets by size for better visualization
    # First by length, then by sorted element order
    all_subsets.sort(key=lambda x: (len(x), sorted(x)))
    
    print("All possible subsets of S:")
    print("-" * 50)
    
    # Display each subset with proper formatting
    for i, subset in enumerate(all_subsets, 1):
        if len(subset) == 0:
            # Special formatting for the empty set
            print(f"{i}. ∅ (empty set) or {{}}")
        else:
            print(f"{i}. {sorted(subset)}")
    
    print()
    print(f"Total number of subsets: {len(all_subsets)}")
    
    print("\n" + "=" * 50)
    print("Explanation:")
    print(f"  - A set with n elements has 2^n subsets")
    print(f"  - |S| = {len(S)}, so number of subsets = 2^{len(S)} = {2**len(S)}")
    print("  - This includes:")
    print("    * The empty set ∅")
    print("    * All single-element subsets")
    print("    * All two-element subsets")
    print("    * The set itself (improper subset)")
    print()
    print("  - Proper subsets: All subsets except S itself")
    print(f"    Number of proper subsets = {len(all_subsets) - 1}")


if __name__ == "__main__":
    main()
