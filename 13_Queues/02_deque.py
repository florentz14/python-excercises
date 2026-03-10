# -------------------------------------------------
# File Name: 02_deque.py
# Author: Florentino Baez
# Date: 2026-03-09
# Description: Queue with collections.deque. append and popleft. O(1) at both ends.
# -------------------------------------------------

from collections import deque

queue = deque()

# Enqueue
queue.append("A")
queue.append("B")
queue.append("C")
print("Queue:", list(queue))

# Dequeue (popleft = O(1))
first = queue.popleft()
print("Dequeue:", first, "-> Queue:", list(queue))
print("Dequeue:", queue.popleft(), "-> Queue:", list(queue))

# Peek front without removing
if queue:
    print("Front:", queue[0])
