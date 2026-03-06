# ------------------------------------------------------------
# File: 61_k_closest_points_to_origin.py
# LeetCode 973 - K Closest Points to Origin (Heap)
#
# Purpose:
#   Return the k closest points to the origin (0,0).
#   Distance = sqrt(x^2 + y^2). Use squared distance to avoid sqrt.
#
# Pattern: Min-heap (heapq). Alternative: QuickSelect.
# Complexity: O(n log k) with heap; O(n) average with QuickSelect.
#
# Author: Florentino Baez
# ------------------------------------------------------------

import heapq


def k_closest(points: list[list[int]], k: int) -> list[list[int]]:
    """
    Return k closest points to origin. Uses min-heap with (-dist, point)
    to simulate max-heap of size k, or store (dist, point) and pop k times.
    """
    # Min-heap: (distance_squared, point). Pop k smallest.
    heap = []
    for x, y in points:
        dist_sq = x * x + y * y
        heapq.heappush(heap, (dist_sq, [x, y]))

    return [heapq.heappop(heap)[1] for _ in range(k)]


def k_closest_heapq_nsmallest(points: list[list[int]], k: int) -> list[list[int]]:
    """Alternative: use heapq.nsmallest. Cleaner for small k."""
    return heapq.nsmallest(k, points, key=lambda p: p[0] * p[0] + p[1] * p[1])


if __name__ == "__main__":
    points = [[1, 3], [-2, 2], [5, -1], [0, 0]]
    k = 2
    print("K Closest (k=2):", k_closest([p[:] for p in points], k))
    print("Expected: [[0,0], [-2,2]] or similar order")
