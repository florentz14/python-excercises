"""
13_Queues - Priority Queue using heapq
=========================================
Elements with highest (or lowest) priority are served first.
Used in: OS scheduling, Dijkstra, simulations.

Python's heapq is a min-heap: smallest value has highest priority.
For max-heap behavior: negate values or use (-priority, item).
"""

import heapq


def demo_min_heap():
    """Min-heap: smallest value pops first."""
    pq = []
    heapq.heappush(pq, (2, "Task B"))
    heapq.heappush(pq, (1, "Task A"))
    heapq.heappush(pq, (3, "Task C"))
    heapq.heappush(pq, (0, "Urgent"))

    print("Min-heap (priority queue) - pop order:")
    while pq:
        priority, task = heapq.heappop(pq)
        print(f"  {priority}: {task}")


def demo_max_heap_simulation():
    """Max-heap: negate values so largest pops first."""
    pq = []
    for val in [5, 2, 8, 1, 9]:
        heapq.heappush(pq, -val)
    print("Max-heap simulation (negated) - pop order:")
    while pq:
        print(f"  {-heapq.heappop(pq)}")


def demo_dijkstra_style():
    """Priority queue for Dijkstra: (distance, node)."""
    pq = []
    heapq.heappush(pq, (0, "A"))
    heapq.heappush(pq, (4, "B"))
    heapq.heappush(pq, (2, "C"))
    heapq.heappush(pq, (7, "D"))

    print("Dijkstra-style (distance, node) - process order:")
    while pq:
        dist, node = heapq.heappop(pq)
        print(f"  Process {node} (dist={dist})")


if __name__ == "__main__":
    print("=" * 55)
    print("Priority Queue with heapq")
    print("=" * 55)
    demo_min_heap()
    print()
    demo_max_heap_simulation()
    print()
    demo_dijkstra_style()
