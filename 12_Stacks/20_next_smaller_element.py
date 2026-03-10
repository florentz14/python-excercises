# -------------------------------------------------
# File Name: 20_next_smaller_element.py
# Author: Florentino Baez
# Date: 2026-03-09
# Description: Next Smaller Element using monotonic stack.
# -------------------------------------------------

"""
============================================================
  NEXT SMALLER ELEMENT - Python 3.14
  For each array position, find the closest smaller value
  to the right (or left), using a monotonic stack.

  Example (to the right):
    nums = [4, 8, 5, 2, 25]
    ans  = [2, 5, 2, -1, -1]

  Time complexity:
    - O(n) for each full pass
============================================================
"""

SEPARATOR = "=" * 60


def title(text: str) -> None:
    print(f"\n{SEPARATOR}\n  {text}\n{SEPARATOR}")


def next_smaller_to_right(nums: list[int]) -> list[int]:
    """Return nearest smaller element to the right for each index."""
    result = [-1] * len(nums)
    stack: list[int] = []  # store candidate values in increasing order

    # Traverse from right to left to maintain right-side candidates.
    for i in range(len(nums) - 1, -1, -1):
        while stack and stack[-1] >= nums[i]:
            stack.pop()
        result[i] = stack[-1] if stack else -1
        stack.append(nums[i])
    return result


def next_smaller_to_left(nums: list[int]) -> list[int]:
    """Return nearest smaller element to the left for each index."""
    result = [-1] * len(nums)
    stack: list[int] = []

    # Traverse left to right to maintain left-side candidates.
    for i, value in enumerate(nums):
        while stack and stack[-1] >= value:
            stack.pop()
        result[i] = stack[-1] if stack else -1
        stack.append(value)
    return result


def next_smaller_index_right(nums: list[int]) -> list[int]:
    """Return index of next smaller element to the right, or -1."""
    result = [-1] * len(nums)
    stack: list[int] = []  # stack stores indexes

    for i in range(len(nums) - 1, -1, -1):
        while stack and nums[stack[-1]] >= nums[i]:
            stack.pop()
        result[i] = stack[-1] if stack else -1
        stack.append(i)
    return result


def demo() -> None:
    title("NEXT SMALLER ELEMENT - Monotonic stack demos")

    test_cases = [
        [4, 8, 5, 2, 25],
        [13, 7, 6, 12],
        [5, 4, 3, 2, 1],
        [1, 2, 3, 4, 5],
        [2, 1, 2, 1, 2],
    ]

    for nums in test_cases:
        print(f"\n  Input: {nums}")
        print(f"  Next smaller to right: {next_smaller_to_right(nums)}")
        print(f"  Next smaller to left : {next_smaller_to_left(nums)}")
        print(f"  Next smaller index right: {next_smaller_index_right(nums)}")


if __name__ == "__main__":
    demo()
