# -------------------------------------------------
# File: 58_cocktail_sort.py (Cocktail Sort - Bidirectional Bubble)
# -------------------------------------------------
# Author: Florentino Báez
# Module: Data Structures - Sorting Algorithms
#
# Description:
#   Cocktail Sort: bidirectional Bubble Sort. Traverses left-to-right
#   (bubble largest to end) then right-to-left (bubble smallest to start).
#   Solves the "turtles" problem by moving small elements faster.
#
# Complexity: O(n²). Stable. In-place.
# -------------------------------------------------

import random
import time


def cocktail_sort(arr):
    """
    Cocktail Sort: bidirectional Bubble Sort.
    Alternates left-to-right pass (bubbles largest right) with right-to-left
    pass (bubbles smallest left). Shrinks the active range each pass.
    Does not modify the original list.
    """
    arr = arr.copy()
    n = len(arr)
    start, end = 0, n - 1  # Active range shrinks from both ends
    swapped = True

    while swapped:
        swapped = False
        # Pass 1: left to right — bubble largest element to end
        for i in range(start, end):
            if arr[i] > arr[i + 1]:
                arr[i], arr[i + 1] = arr[i + 1], arr[i]
                swapped = True
        end -= 1  # Largest is now in place
        if not swapped:
            break
        swapped = False
        # Pass 2: right to left — bubble smallest element to start
        for i in range(end, start, -1):
            if arr[i] < arr[i - 1]:
                arr[i], arr[i - 1] = arr[i - 1], arr[i]
                swapped = True
        start += 1  # Smallest is now in place

    return arr


def cocktail_sort_visual(arr):
    """
    Cocktail Sort with step-by-step visualization.
    Prints each pass (right and left) so the sorting process is visible.
    """
    arr = arr.copy()
    n = len(arr)
    start, end = 0, n - 1
    swapped = True
    step = 0

    print(f"\nOriginal: {arr}")
    print("=" * 60)

    while swapped:
        swapped = False
        step += 1
        for i in range(start, end):
            if arr[i] > arr[i + 1]:
                arr[i], arr[i + 1] = arr[i + 1], arr[i]
                swapped = True
        end -= 1
        print(f"Step {step}a (-> right): {arr}")
        if not swapped:
            break
        swapped = False
        for i in range(end, start, -1):
            if arr[i] < arr[i - 1]:
                arr[i], arr[i - 1] = arr[i - 1], arr[i]
                swapped = True
        start += 1
        print(f"Step {step}b (<- left): {arr}")

    print("=" * 60)
    print(f"Sorted: {arr}")
    return arr


# ============================================================
# 3. Comparison: Cocktail Sort vs Bubble Sort
# ============================================================
def bubble_sort(arr):
    """Bubble Sort for comparison."""
    arr = arr.copy()
    n = len(arr)
    for i in range(n):
        swapped = False
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True
        if not swapped:
            break
    return arr


def compare_with_bubble(n=2000):
    """Compares Cocktail Sort vs Bubble Sort in different scenarios."""
    scenarios = {
        "Random":         [random.randint(1, 10000) for _ in range(n)],
        "Almost sorted":  list(range(n)),
        "Reverse":        list(range(n, 0, -1)),
    }

    # Slightly shuffle "almost sorted"
    casi = scenarios["Almost sorted"]
    for _ in range(n // 20):
        i, j = random.randint(0, n-1), random.randint(0, n-1)
        casi[i], casi[j] = casi[j], casi[i]

    print(f"\nCocktail Sort vs Bubble Sort ({n} elements):")
    print("=" * 60)
    print(f"{'Scenario':<18s} {'Cocktail':>12s} {'Bubble':>12s} {'Winner':>10s}")
    print("-" * 60)

    for name, data in scenarios.items():
        start_t = time.time()
        cocktail_sort(data)
        t_cocktail = time.time() - start_t

        start_t = time.time()
        bubble_sort(data)
        t_bubble = time.time() - start_t

        winner = "Cocktail" if t_cocktail < t_bubble else "Bubble"
        print(f"  {name:<18s} {t_cocktail*1000:10.2f} ms {t_bubble*1000:10.2f} ms"
              f" {winner:>10s}")


def cocktail_sort_stats(arr):
    """
    Cocktail Sort that returns (sorted_list, passes, swaps).
    Useful for analyzing performance on different input distributions.
    """
    arr = arr.copy()
    n = len(arr)
    start, end = 0, n - 1
    swapped = True
    passes = swaps = 0

    while swapped:
        swapped = False
        passes += 1
        for i in range(start, end):
            if arr[i] > arr[i + 1]:
                arr[i], arr[i + 1] = arr[i + 1], arr[i]
                swapped = True
                swaps += 1
        end -= 1
        if not swapped:
            break
        swapped = False
        passes += 1
        for i in range(end, start, -1):
            if arr[i] < arr[i - 1]:
                arr[i], arr[i - 1] = arr[i - 1], arr[i]
                swapped = True
                swaps += 1
        start += 1

    return arr, passes, swaps


if __name__ == "__main__":
    print("=== Cocktail Sort (Bidirectional Bubble Sort) ===\n")

    demo = [5, 1, 4, 2, 8, 0, 2, 7, 3, 6]
    cocktail_sort_visual(demo)

    print("\n--- Swap Statistics ---")
    stats_cases = {
        "Random":    [random.randint(1, 50) for _ in range(15)],
        "Reverse":   list(range(10, 0, -1)),
        "Sorted":    list(range(1, 11)),
    }

    for name, case in stats_cases.items():
        result, passes, swaps = cocktail_sort_stats(case)
        print(f"  {name:12s}: {passes:3d} passes, {swaps:3d} swaps -> {result[:8]}{'...' if len(result) > 8 else ''}")

    print("\n--- Tests ---")
    test_cases = {
        "Random":      [random.randint(1, 50) for _ in range(15)],
        "Sorted":      list(range(1, 11)),
        "Reverse":     list(range(10, 0, -1)),
        "All same":    [5] * 8,
        "Single":      [42],
        "Empty":       [],
    }

    for name, case in test_cases.items():
        result = cocktail_sort(case)
        ok = all(result[i] <= result[i + 1] for i in range(len(result) - 1)) if len(result) > 1 else True
        print(f"  {name:15s}: {str(case[:8])}{'...' if len(case) > 8 else ''} -> {str(result[:8])}{'...' if len(result) > 8 else ''} {'OK' if ok else 'FAIL'}")

    compare_with_bubble(1500)
