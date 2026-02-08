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
    elements = list(input_set)
    all_subsets = []
    
    # Generate subsets of all possible sizes (0 to n)
    for size in range(len(elements) + 1):
        # Use combinations to get all subsets of current size
        for subset in combinations(elements, size):
            all_subsets.append(set(subset))
    
    return all_subsets


def main():
    # Define set S
    S = {'x', 'y', 'z'}
    
    print("Exercise 7: Subsets")
    print("=" * 50)
    print(f"Set S = {sorted(S)}")
    print()
    
    # Get all possible subsets
    all_subsets = get_all_subsets(S)
    
    # Sort subsets by size for better visualization
    all_subsets.sort(key=lambda x: (len(x), sorted(x)))
    
    print("All possible subsets of S:")
    print("-" * 50)
    
    for i, subset in enumerate(all_subsets, 1):
        if len(subset) == 0:
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
