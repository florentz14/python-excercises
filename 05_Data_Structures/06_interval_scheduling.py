# -------------------------------------------------
# File Name: 06_interval_scheduling.py
# Author: Florentino Baez
# Date: 05_Data_Structures
# Description: Weighted Interval Scheduling. Select non-overlapping intervals to maximize sum of weights. Uses dynamic programming. O(n log n) with sorting.
# -------------------------------------------------

def weighted_interval_scheduling(intervals):
    """
    intervals: list of (start, end, weight) tuples.
    Returns: (selected_indices, total_weight).
    """
    intervals.sort(key=lambda x: x[1])
    n = len(intervals)
    # dp[i] = max total weight achievable using intervals 0..i
    dp = [0] * n

    for i, (start, end, w) in enumerate(intervals):
        best = w
        # Find last compatible interval (ends before current starts)
        for j in range(i - 1, -1, -1):
            if intervals[j][1] <= start:
                if dp[j] + w > best:
                    best = dp[j] + w
                break
        dp[i] = best

    # Reconstruct solution by backtracking
    selected = []
    i = n - 1
    while i >= 0:
        if i == 0 or dp[i] > dp[i - 1]:
            selected.append(i)
            curr_end = intervals[i][0]
            i -= 1
            while i >= 0 and intervals[i][1] > curr_end:
                i -= 1
        else:
            i -= 1

    selected.reverse()
    total = dp[-1] if dp else 0
    return selected, total


if __name__ == "__main__":
    print("=== Greedy/DP: Weighted Interval Scheduling ===\n")

    intervals = [
        (1, 4, 3),
        (3, 5, 4),
        (0, 6, 2),
        (5, 7, 1),
        (8, 9, 5),
        (5, 9, 2)
    ]

    print("Intervals (start, end, weight):")
    for i, (s, e, w) in enumerate(intervals):
        print(f"  Interval {i}: [{s}, {e}] weight={w}")

    selected, total = weighted_interval_scheduling(intervals)
    print(f"\nSelected intervals: {selected}")
    print(f"Total weight: {total}")
    for idx in selected:
        s, e, w = intervals[idx]
        print(f"  Interval {idx}: [{s}, {e}] weight={w}")
