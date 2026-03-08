# -------------------------------------------------
# File Name: 63_priority_queue_heapq.py
# Author: Florentino Báez
# Date: 05_Data_Structures
# Description: Priority queue using heapq. Min-heap operations in Python.
# -------------------------------------------------

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
