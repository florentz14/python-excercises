# -------------------------------------------------
# File Name: 31_trapping_rain_water_stack.py
# Author: Florentino Baez
# Date: 2026-03-09
# Description: Trapping Rain Water solved with monotonic stack.
# -------------------------------------------------

"""
============================================================
  TRAPPING RAIN WATER (STACK) - Python 3.14
  Given elevation bars, compute trapped water amount.

  Example:
    height = [0,1,0,2,1,0,1,3,2,1,2,1] -> 6

  Stack idea:
    - Keep indexes of bars in decreasing-height order.
    - When current bar is higher than stack top, a basin may form.
============================================================
"""

SEPARATOR = "=" * 60


def title(text: str) -> None:
    print(f"\n{SEPARATOR}\n  {text}\n{SEPARATOR}")


def trap(height: list[int]) -> int:
    """Return total trapped rain water using monotonic stack."""
    water = 0
    stack: list[int] = []  # indexes

    for i, h in enumerate(height):
        while stack and h > height[stack[-1]]:
            bottom = stack.pop()
            if not stack:
                break
            left = stack[-1]
            width = i - left - 1
            bounded_height = min(height[left], h) - height[bottom]
            water += width * bounded_height
        stack.append(i)

    return water


def trap_bruteforce(height: list[int]) -> int:
    """Reference O(n^2) solution for comparison."""
    total = 0
    n = len(height)
    for i in range(n):
        left_max = max(height[: i + 1])
        right_max = max(height[i:])
        total += min(left_max, right_max) - height[i]
    return total


def demo() -> None:
    title("TRAPPING RAIN WATER - Stack approach")

    tests = [
        ([0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1], 6),
        ([4, 2, 0, 3, 2, 5], 9),
        ([1, 0, 1], 1),
        ([5, 4, 3, 2, 1], 0),
        ([1, 2, 3, 4, 5], 0),
    ]

    for arr, expected in tests:
        fast = trap(arr)
        slow = trap_bruteforce(arr)
        print(f"\n  height  : {arr}")
        print(f"  fast    : {fast}")
        print(f"  brute   : {slow}")
        print(f"  expected: {expected}")
        print(f"  match   : {fast == expected and slow == expected}")


if __name__ == "__main__":
    demo()
