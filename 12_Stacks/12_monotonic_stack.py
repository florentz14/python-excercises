"""
12_Stacks - Monotonic Stack
============================
Generic monotonic stack: increasing or decreasing.
Used for: next greater/smaller, stock span, histogram problems.
"""

from typing import Callable


def next_greater_indices(nums: list[int]) -> list[int]:
    """Next greater element index for each position. Decreasing stack."""
    n = len(nums)
    result = [-1] * n
    stack = []

    for i in range(n):
        while stack and nums[stack[-1]] < nums[i]:
            idx = stack.pop()
            result[idx] = i
        stack.append(i)
    return result


def next_smaller_indices(nums: list[int]) -> list[int]:
    """Next smaller element index. Increasing stack."""
    n = len(nums)
    result = [-1] * n
    stack = []

    for i in range(n):
        while stack and nums[stack[-1]] > nums[i]:
            idx = stack.pop()
            result[idx] = i
        stack.append(i)
    return result


def prev_greater_indices(nums: list[int]) -> list[int]:
    """Previous greater element index. Decreasing stack, left-to-right."""
    n = len(nums)
    result = [-1] * n
    stack = []

    for i in range(n):
        while stack and nums[stack[-1]] <= nums[i]:
            stack.pop()
        if stack:
            result[i] = stack[-1]
        stack.append(i)
    return result


if __name__ == "__main__":
    print("=" * 55)
    print("Monotonic Stack")
    print("=" * 55)

    nums = [2, 1, 2, 4, 3]
    print(f"  nums = {nums}")
    print(f"  next_greater_indices: {next_greater_indices(nums)}")
    print(f"  next_smaller_indices: {next_smaller_indices(nums)}")
    print(f"  prev_greater_indices: {prev_greater_indices(nums)}")
