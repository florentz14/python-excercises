# -------------------------------------------------
# File Name: 66_prefix_sum.py
# Author: Florentino Báez
# Date: 05_Data_Structures
# Description: Prefix sum. Precompute cumulative sums for O(1) range queries.
# -------------------------------------------------

def build_prefix_sum(nums: list[int]) -> list[int]:
    """Build prefix array: prefix[i] = sum of nums[0..i-1]. prefix[0]=0."""
    # Prefix sum starts with 0 for easier range calculations
    prefix = [0]

    for num in nums:
        # Append cumulative sum
        prefix.append(prefix[-1] + num)

    return prefix


def range_sum(prefix: list[int], left: int, right: int) -> int:
    """Return sum of elements from index left to right inclusive."""
    # Sum from left to right inclusive
    return prefix[right + 1] - prefix[left]


if __name__ == "__main__":
    print("=== Prefix Sum - Range Queries ===\n")

    nums = [1, 2, 3, 4, 5]
    prefix = build_prefix_sum(nums)

    print(f"Array: {nums}")
    print(f"Prefix: {prefix}")
    print(f"range_sum(1, 3): {range_sum(prefix, 1, 3)}  (2+3+4 = 9)")
    print(f"range_sum(0, 4): {range_sum(prefix, 0, 4)}  (full sum = 15)")
