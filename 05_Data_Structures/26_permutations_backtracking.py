# -------------------------------------------------
# File Name: 26_permutations_backtracking.py
# Author: Florentino Baez
# Date: 05_Data_Structures
# Description: Permutation generation with backtracking. All orderings of a sequence.
# -------------------------------------------------

print("=== 4. Permutation Generation (Backtracking) ===\n")


def permutaciones_backtracking(elements):
    """Generate all permutations using backtracking."""
    result = []
    n = len(elements)

    def backtrack(current_permutation, used):
        if len(current_permutation) == n:
            # Complete permutation → save copy
            result.append(current_permutation[:])
            return
        for i in range(n):
            if not used[i]:
                current_permutation.append(elements[i])  # Choose element
                used[i] = True                           # Mark as used
                backtrack(current_permutation, used)     # Recursion
                current_permutation.pop()                # Backtrack: remove
                used[i] = False                          # Unmark

    backtrack([], [False] * n)
    return result


if __name__ == "__main__":
    elements = [1, 2, 3]
    perms = permutaciones_backtracking(elements)
    print(f"Permutations of {elements}:")
    for i, perm in enumerate(perms, 1):
        print(f"  {i}. {perm}")
    print(f"Total: {len(perms)} permutations")
