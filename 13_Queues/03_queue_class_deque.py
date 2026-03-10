# -------------------------------------------------
# File Name: 03_queue_class_deque.py
# Author: Florentino Baez
# Date: 2026-03-09
# Description: Queue class with deque. enqueue(), dequeue(), front(), empty().
# -------------------------------------------------

from collections import deque


class Queue:
    def __init__(self):
        self._data = deque()

    def enqueue(self, x):
        self._data.append(x)

    def dequeue(self):
        if self.empty():
            raise IndexError("Dequeue on empty queue")
        return self._data.popleft()

    def front(self):
        if self.empty():
            raise IndexError("Front on empty queue")
        return self._data[0]

    def empty(self):
        return len(self._data) == 0

    def __len__(self):
        return len(self._data)


# --- Demo ---
if __name__ == "__main__":
    queue = Queue()
    queue.enqueue(10)
    queue.enqueue(20)
    queue.enqueue(30)
    print("Front:", queue.front())
    print("Dequeue:", queue.dequeue())
    print("Dequeue:", queue.dequeue())
    print("Empty?", queue.empty())
