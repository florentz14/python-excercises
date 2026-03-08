# -------------------------------------------------
# File Name: 11_next_greater_element.py
# Author: Florentino Báez
# Date: 12_Stacks
# Description: Next greater element. Monotonic stack pattern.
# -------------------------------------------------

def next_greater_element(nums: list[int]) -> list[int]:
    """
    Returns array where result[i] = next greater element of nums[i], or -1 if none.
    """
    n = len(nums)
    result = [-1] * n
    stack = []  # monotonic decreasing: indices

    for i in range(n):
        while stack and nums[stack[-1]] < nums[i]:
            idx = stack.pop()
            result[idx] = nums[i]
        stack.append(i)
    return result


def next_greater_element_circular(nums: list[int]) -> list[int]:
    """Variant: array is circular (wrap around)."""
    n = len(nums)
    result = [-1] * n
    stack = []

    for i in range(2 * n):
        idx = i % n
        while stack and nums[stack[-1]] < nums[idx]:
            popped = stack.pop()
            result[popped] = nums[idx]
        if i < n:
            stack.append(idx)
    return result


if __name__ == "__main__":
    print("=" * 55)
    print("Next Greater Element")
    print("=" * 55)

    nums = [2, 1, 2, 4, 3]
    result = next_greater_element(nums)
    print(f"  nums = {nums}")
    print(f"  NGE  = {result}")

    print("\n  Circular variant:")
    nums2 = [1, 2, 1]
    print(f"  nums = {nums2}")
    print(f"  NGE  = {next_greater_element_circular(nums2)}")
