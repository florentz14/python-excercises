# -------------------------------------------------
# File Name: 01_queue_with_list.py
# Author: Florentino Baez
# Date: 2026-03-09
# Description: Queue with list (FIFO). append() and pop(0). Better: use deque.
# -------------------------------------------------

queue = []

# Enqueue: add to the end
queue.append("A")
queue.append("B")
queue.append("C")
print("Queue:", queue)

# Dequeue: remove the first element (pop(0) is O(n))
first = queue.pop(0)
print("Dequeue:", first, "-> Queue:", queue)
print("Dequeue:", queue.pop(0), "-> Queue:", queue)
