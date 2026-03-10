# -------------------------------------------------
# File Name: 10_priority_queue_class.py
# Author: Florentino Baez
# Date: 2026-03-09
# Description: Priority queue class. Heap-based implementation.
# -------------------------------------------------

import heapq


class PriorityQueue:
    """Priority queue using heapq. Lower value = higher priority."""

    def __init__(self):
        self._heap = []
        self._index = 0  # Tie-breaker for same priority

    def push(self, item, priority=0):
        """Add item with priority. Lower priority = served first."""
        heapq.heappush(self._heap, (priority, self._index, item))
        self._index += 1

    def pop(self):
        """Remove and return highest priority item."""
        if self.is_empty():
            raise IndexError("Priority queue is empty")
        _, _, item = heapq.heappop(self._heap)
        return item

    def peek(self):
        """Return highest priority item without removing."""
        if self.is_empty():
            raise IndexError("Priority queue is empty")
        return self._heap[0][2]

    def size(self):
        return len(self._heap)

    def is_empty(self):
        return len(self._heap) == 0


if __name__ == "__main__":
    print("=" * 55)
    print("Priority Queue Class")
    print("=" * 55)

    pq = PriorityQueue()
    pq.push("low", priority=3)
    pq.push("high", priority=1)
    pq.push("medium", priority=2)

    print(f"Size: {pq.size()}")
    print(f"Peek: {pq.peek()}")
    print("Pop order:")
    while not pq.is_empty():
        print(f"  {pq.pop()}")
