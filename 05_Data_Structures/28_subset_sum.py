# -------------------------------------------------
# File: 28_subset_sum.py (Subset Sum - Backtracking)
# -------------------------------------------------
# Author: Florentino Báez
# Module: Data Structures - Backtracking
#
# Description:
#   Subset Sum: find all subsets whose sum equals the target. For each
#   element, include or exclude; prune when sum exceeds target.
#
# Complexity: O(2^n) worst case.
# -------------------------------------------------


def subset_sum_backtracking(numbers, target):
    """Returns list of all subsets that sum exactly to target."""
    result = []
    n = len(numbers)

    def backtrack(current, idx, total):
        if total == target:
            result.append(current[:])
            return
        if total > target or idx >= n:
            return
        current.append(numbers[idx])
        backtrack(current, idx + 1, total + numbers[idx])
        current.pop()
        backtrack(current, idx + 1, total)

    backtrack([], 0, 0)
    return result


if __name__ == "__main__":
    print("=== Backtracking: Subset Sum ===\n")

    numbers = [3, 34, 4, 12, 5, 2]
    target = 9
    solutions = subset_sum_backtracking(numbers, target)

    print(f"Numbers: {numbers}")
    print(f"Target: {target}")
    print(f"Subsets that sum to {target}:")
    for sol in solutions:
        print(f"  {sol} (sum = {sum(sol)})")
