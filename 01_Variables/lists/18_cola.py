# -------------------------------------------------
# File Name: 18_cola.py
# Author: Florentino Báez
# Date: Variables - Lists
# Description: List as a Queue (FIFO) with deque.
#              First In, First Out. collections.deque is
#              preferred over list for O(1) popleft().
#              append() enqueues, popleft() dequeues.
# -------------------------------------------------

from collections import deque

print("=== List as a queue (FIFO) ===")
print("Use deque for efficiency: append() to enqueue, popleft() to dequeue")
print()

cola = deque()
print(f"Empty queue: {cola}")

# Enqueue — add to the back
cola.append(1)
cola.append(2)
cola.append(3)
print(f"After append(1), append(2), append(3): {cola}")

# Dequeue — remove from the front (O(1) with deque)
primero = cola.popleft()
print(f"popleft() returns: {primero}")
print(f"Queue after popleft: {cola}")

# More enqueue/dequeue operations
cola.append(4)
cola.append(5)
print(f"After append(4), append(5): {cola}")

print(f"popleft(): {cola.popleft()}")
print(f"popleft(): {cola.popleft()}")
print(f"Final queue: {cola}")

# Peek — view the front element without removing it
print(f"\nPeek (front without removing): cola[0] = {cola[0]}")

# appendleft() inserts at the front (opposite end)
cola.appendleft(0)
print(f"After appendleft(0): {cola}")
