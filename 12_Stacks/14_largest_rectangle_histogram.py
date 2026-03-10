# -------------------------------------------------
# File Name: 14_largest_rectangle_histogram.py
# Author: Florentino Baez
# Date: 2026-03-09
# Description: Largest rectangle in histogram. Monotonic stack. O(n).
# -------------------------------------------------

def largest_rectangle_area(heights: list[int]) -> int:
    """
    Returns the largest rectangle area using monotonic stack.
    For each bar, we find the rectangle with that bar as the shortest.
    """
    stack = []  # (index, height)
    max_area = 0
    n = len(heights)

    for i in range(n):
        start = i
        while stack and stack[-1][1] > heights[i]:
            idx, h = stack.pop()
            width = i - idx
            max_area = max(max_area, h * width)
            start = idx
        stack.append((start, heights[i]))

    # Process remaining bars (extend to end)
    while stack:
        idx, h = stack.pop()
        width = n - idx
        max_area = max(max_area, h * width)

    return max_area


if __name__ == "__main__":
    print("=== Largest Rectangle in Histogram ===\n")

    heights = [2, 1, 5, 6, 2, 3]
    result = largest_rectangle_area(heights)

    print(f"Heights: {heights}")
    print(f"Largest rectangle area: {result}")
    print("\nVisual: bars of heights [2,1,5,6,2,3]")
    print("  Max area 10 = height 5 * width 2 (bars at indices 2-3)")
