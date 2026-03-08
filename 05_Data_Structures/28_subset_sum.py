# -------------------------------------------------
# File Name: 28_subset_sum.py
# Author: Florentino Báez
# Date: 05_Data_Structures
# Description: Subset Sum. Find all subsets whose sum equals target. Backtracking. O(2^n).
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
