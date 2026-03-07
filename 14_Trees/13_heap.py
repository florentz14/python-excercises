"""
14_Trees - Heap (Min-Heap / Max-Heap)
=========================================
Complete binary tree with heap property.
Min-Heap: parent <= children. Max-Heap: parent >= children.

Complexity: insert O(log n), extract O(log n), peek O(1).
Used in: Priority Queue, Dijkstra, Heapsort.
"""


class MinHeap:
    """Min-Heap: smallest at root. Parent <= children."""

    def __init__(self):
        self.heap = []

    def parent(self, i):
        return (i - 1) // 2

    def left(self, i):
        return 2 * i + 1

    def right(self, i):
        return 2 * i + 2

    def insert(self, key):
        """Insert key and bubble up."""
        self.heap.append(key)
        i = len(self.heap) - 1
        while i > 0 and self.heap[self.parent(i)] > self.heap[i]:
            p = self.parent(i)
            self.heap[p], self.heap[i] = self.heap[i], self.heap[p]
            i = p

    def extract_min(self):
        """Remove and return minimum. O(log n)."""
        if not self.heap:
            return None
        if len(self.heap) == 1:
            return self.heap.pop()

        minimum = self.heap[0]
        self.heap[0] = self.heap.pop()
        self._heapify_down(0)
        return minimum

    def _heapify_down(self, i):
        """Bubble down to restore heap property."""
        smallest = i
        left = self.left(i)
        right = self.right(i)
        if left < len(self.heap) and self.heap[left] < self.heap[smallest]:
            smallest = left
        if right < len(self.heap) and self.heap[right] < self.heap[smallest]:
            smallest = right
        if smallest != i:
            self.heap[i], self.heap[smallest] = self.heap[smallest], self.heap[i]
            self._heapify_down(smallest)

    def peek(self):
        """Return minimum without removing. O(1)."""
        return self.heap[0] if self.heap else None

    def size(self):
        return len(self.heap)


class MaxHeap:
    """Max-Heap: largest at root. Parent >= children."""

    def __init__(self):
        self.heap = []

    def parent(self, i):
        return (i - 1) // 2

    def left(self, i):
        return 2 * i + 1

    def right(self, i):
        return 2 * i + 2

    def insert(self, key):
        """Insert key and bubble up."""
        self.heap.append(key)
        i = len(self.heap) - 1
        while i > 0 and self.heap[self.parent(i)] < self.heap[i]:
            p = self.parent(i)
            self.heap[p], self.heap[i] = self.heap[i], self.heap[p]
            i = p

    def extract_max(self):
        """Remove and return maximum. O(log n)."""
        if not self.heap:
            return None
        if len(self.heap) == 1:
            return self.heap.pop()
        maximum = self.heap[0]
        self.heap[0] = self.heap.pop()
        self._heapify_down(0)
        return maximum

    def _heapify_down(self, i):
        largest = i
        left = self.left(i)
        right = self.right(i)
        if left < len(self.heap) and self.heap[left] > self.heap[largest]:
            largest = left
        if right < len(self.heap) and self.heap[right] > self.heap[largest]:
            largest = right
        if largest != i:
            self.heap[i], self.heap[largest] = self.heap[largest], self.heap[i]
            self._heapify_down(largest)

    def peek(self):
        return self.heap[0] if self.heap else None


if __name__ == "__main__":
    print("=== Min-Heap ===\n")
    min_h = MinHeap()
    for v in [3, 2, 1, 5, 4]:
        min_h.insert(v)
    print("Extract min:", [min_h.extract_min() for _ in range(5)])

    print("\n=== Max-Heap ===\n")
    max_h = MaxHeap()
    for v in [3, 2, 1, 5, 4]:
        max_h.insert(v)
    print("Extract max:", [max_h.extract_max() for _ in range(5)])
    print("\nUsed in: Priority Queue, Dijkstra, Heapsort.")
