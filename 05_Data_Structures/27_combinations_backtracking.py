# -------------------------------------------------
# File Name: 27_combinations_backtracking.py
# Author: Florentino Baez
# Date: 05_Data_Structures
# Description: Combination generation with backtracking. All ways to choose k from n. O(C(n,k)*k).
# -------------------------------------------------

print("=== 5. Combination Generation (Backtracking) ===\n")


def combinaciones_backtracking(elements, k):
    """Generate all combinations of k elements using backtracking."""
    result = []
    n = len(elements)

    def backtrack(current_combination, start):
        if len(current_combination) == k:
            # Complete combination → save copy
            result.append(current_combination[:])
            return
        # Only consider elements from 'start' to avoid duplicates
        for i in range(start, n):
            current_combination.append(elements[i])  # Include element
            backtrack(current_combination, i + 1)    # Next from i+1
            current_combination.pop()                # Backtrack: exclude

    backtrack([], 0)
    return result


if __name__ == "__main__":
    elements_set = ['A', 'B', 'C', 'D']
    k = 2
    combs = combinaciones_backtracking(elements_set, k)
    print(f"Combinations of {elements_set} taking {k} elements:")
    for i, comb in enumerate(combs, 1):
        print(f"  {i}. {comb}")
    print(f"Total: {len(combs)} combinations (C({len(elements_set)}, {k}) = {len(combs)})")
