# ------------------------------------------------------------
# Algorithm: Backtracking - Generate All Subsets
# Purpose:
#   Generate all subsets of a list using pure backtracking
#   (choose → explore → unchoose pattern). No itertools.
# Complexity:
#   Time  : O(2^n)
#   Space : O(n) recursion depth, excluding output
# ------------------------------------------------------------
# Author: Florentino Báez
# ------------------------------------------------------------


def subsets(nums: list[int]) -> list[list[int]]:
    """Generate all subsets of nums. Each subset is a list."""
    result = []

    def backtrack(index: int, path: list[int]) -> None:
        # Add a copy of the current subset
        result.append(path[:])

        # Try including each remaining element
        for i in range(index, len(nums)):
            # Choose
            path.append(nums[i])

            # Explore
            backtrack(i + 1, path)

            # Unchoose
            path.pop()

    backtrack(0, [])
    return result


if __name__ == "__main__":
    print("=== Backtracking: Generate All Subsets ===\n")

    examples = [[1, 2, 3], [1, 2]]
    for nums in examples:
        print(f"nums = {nums}")
        subs = subsets(nums)
        print(f"  Subsets ({len(subs)}): {subs}")
