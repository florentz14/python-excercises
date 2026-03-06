# ------------------------------------------------------------
# File: 63_priority_queue_heapq.py
# Priority Queue using heapq
#
# Purpose:
#   Python's heapq implements a min-heap. Use it as a priority queue:
#   - heappush(heap, (priority, item))
#   - heappop(heap) returns smallest priority
#
# For max-heap: negate priorities, or use (-priority, item).
#
# Author: Florentino Baez
# ------------------------------------------------------------

import heapq


def demo_priority_queue():
    """Simple priority queue: (priority, task). Lower number = higher priority."""
    pq = []
    heapq.heappush(pq, (2, "Task B"))
    heapq.heappush(pq, (1, "Task A"))
    heapq.heappush(pq, (3, "Task C"))

    print("Process in order:")
    while pq:
        priority, task = heapq.heappop(pq)
        print(f"  {priority}: {task}")


def demo_max_heap_simulation():
    """Max-heap: negate values. Largest pops first."""
    heap = []
    for x in [5, 3, 8, 1, 9]:
        heapq.heappush(heap, -x)

    print("Extract max (using -value):")
    while heap:
        print(f"  {-heapq.heappop(heap)}")


if __name__ == "__main__":
    print("=== Priority Queue (min-heap) ===")
    demo_priority_queue()
    print("\n=== Max-heap simulation ===")
    demo_max_heap_simulation()
