# -------------------------------------------------
# File Name: 16_linear_queue.py
# Author: Florentino Baez
# Date: 2026-03-09
# Description: Linear queue (FIFO) implementation and demos.
# -------------------------------------------------

"""
============================================================
  LINEAR QUEUE (Queue) - Python 3.14
  FIFO structure: First In, First Out
  The first element inserted is the first removed.

  Operations:
    - enqueue   -> Insert at the end
    - dequeue   -> Remove from the front
    - peek/front -> View front without removing
    - is_empty  -> Check whether it is empty
    - is_full   -> Check whether it is full
    - size      -> Current size
    - clear     -> Empty the queue
    - display   -> Show content
============================================================
"""

SEPARATOR = "=" * 60


def title(text: str) -> None:
    print(f"\n{SEPARATOR}\n  {text}\n{SEPARATOR}")


def subtitle(text: str) -> None:
    print(f"\n  --- {text} ---")


# Fixed-capacity linear queue implemented with circular indexing.
class LinearQueue:
    """Linear queue with fixed maximum capacity."""

    def __init__(self, capacity: int = 10) -> None:
        self._data: list = [None] * capacity
        self._capacity: int = capacity
        self._front: int = 0
        self._rear: int = 0
        self._size: int = 0

    # Query methods.
    def is_empty(self) -> bool:
        return self._size == 0

    def is_full(self) -> bool:
        return self._size == self._capacity

    def size(self) -> int:
        return self._size

    def peek(self):
        """Return front element without removing it."""
        if self.is_empty():
            raise IndexError("Queue is empty: no front element available.")
        return self._data[self._front]

    # Modification methods.
    def enqueue(self, value) -> None:
        """Insert an element at the rear."""
        if self.is_full():
            raise OverflowError("Queue is full: cannot insert.")
        self._data[self._rear] = value
        self._rear = (self._rear + 1) % self._capacity
        self._size += 1

    def dequeue(self):
        """Remove and return the front element."""
        if self.is_empty():
            raise IndexError("Queue is empty: cannot remove.")
        value = self._data[self._front]
        self._data[self._front] = None
        self._front = (self._front + 1) % self._capacity
        self._size -= 1
        return value

    def clear(self) -> None:
        """Remove all elements from queue."""
        self._data = [None] * self._capacity
        self._front = 0
        self._rear = 0
        self._size = 0

    # Visualization helper.
    def display(self, name: str = "Queue") -> None:
        if self.is_empty():
            print(f"  {name}: [ empty ]")
            return
        elements = []
        idx = self._front
        for _ in range(self._size):
            elements.append(str(self._data[idx]))
            idx = (idx + 1) % self._capacity
        print(f"  {name}: FRONT -> [ {' | '.join(elements)} ] <- REAR")
        print(f"         Size: {self._size}/{self._capacity}")

    def __repr__(self) -> str:
        return f"LinearQueue(size={self._size}, capacity={self._capacity})"


# Demo: enqueue operation and overflow handling.
def demo_enqueue() -> LinearQueue:
    title("1. ENQUEUE - Insert elements at the rear")
    queue = LinearQueue(capacity=6)

    for value in [10, 20, 30, 40, 50]:
        queue.enqueue(value)
        print(f"  enqueue({value:2d})  ->  ", end="")
        queue.display()

    subtitle("Try inserting into a full queue")
    queue.enqueue(60)
    queue.display("Full queue")
    try:
        queue.enqueue(99)
    except OverflowError as error:
        print(f"  OverflowError: {error}")

    return queue


# Demo: dequeue operation and underflow handling.
def demo_dequeue(queue: LinearQueue) -> LinearQueue:
    title("2. DEQUEUE - Remove elements from the front")
    queue.display("Before")

    for _ in range(3):
        removed = queue.dequeue()
        print(f"  dequeue() -> removed: {removed}")
        queue.display()

    subtitle("Empty queue completely, then try removing again")
    while not queue.is_empty():
        queue.dequeue()
    queue.display("Empty queue")
    try:
        queue.dequeue()
    except IndexError as error:
        print(f"  IndexError: {error}")

    return queue


# Demo: peek/front.
def demo_peek(queue: LinearQueue) -> None:
    title("3. PEEK / FRONT - View front without removing")
    for value in [100, 200, 300]:
        queue.enqueue(value)

    queue.display("Current queue")
    front = queue.peek()
    print(f"  peek() -> {front}  (queue is NOT modified)")
    queue.display("Queue after peek")


# Demo: query methods.
def demo_queries(queue: LinearQueue) -> None:
    title("4. QUERIES - is_empty, is_full, size")
    queue.display("Current queue")
    print(f"  is_empty() -> {queue.is_empty()}")
    print(f"  is_full()  -> {queue.is_full()}")
    print(f"  size()     -> {queue.size()}")

    subtitle("Empty queue state")
    empty_queue = LinearQueue(5)
    print(f"  is_empty() -> {empty_queue.is_empty()}")
    print(f"  is_full()  -> {empty_queue.is_full()}")
    print(f"  size()     -> {empty_queue.size()}")

    subtitle("Full queue state")
    full_queue = LinearQueue(3)
    for value in [1, 2, 3]:
        full_queue.enqueue(value)
    full_queue.display("Full queue (cap=3)")
    print(f"  is_empty() -> {full_queue.is_empty()}")
    print(f"  is_full()  -> {full_queue.is_full()}")
    print(f"  size()     -> {full_queue.size()}")


# Demo: clear operation.
def demo_clear(queue: LinearQueue) -> None:
    title("5. CLEAR - Empty the queue")
    queue.display("Before clear()")
    queue.clear()
    queue.display("After clear()")
    print(f"  is_empty() -> {queue.is_empty()}")


# Demo: display operation in several states.
def demo_display() -> None:
    title("6. DISPLAY - Visualize queue in different states")
    queue = LinearQueue(8)
    queue.display("Newly created queue")

    for value in [5, 15, 25, 35]:
        queue.enqueue(value)
    queue.display("With 4 elements")

    queue.dequeue()
    queue.dequeue()
    queue.display("After 2 dequeue()")

    for value in [45, 55, 65]:
        queue.enqueue(value)
    queue.display("After adding 3 more")


# Demo: practical customer service scenario.
def demo_practical_case() -> None:
    title("7. PRACTICAL CASE - Customer service line simulation")
    print("  Scenario: customers arrive and are served one by one.\n")

    customers = LinearQueue(capacity=10)
    arrivals = ["Ana", "Luis", "Maria", "Carlos", "Sofia"]

    print("  [Arrivals]")
    for name in arrivals:
        customers.enqueue(name)
        print(f"  -> {name} joins the line")
    customers.display("Current line")

    print("\n  [Service at desk]")
    while not customers.is_empty():
        served = customers.dequeue()
        pending = customers.size()
        print(f"  [OK] Serving: {served:8s}  |  Pending: {pending}")

    customers.display("\n  Line at end of day")


def main() -> None:
    print(f"\n{SEPARATOR}")
    print("  LINEAR QUEUE - Python 3.14")
    print(f"{SEPARATOR}")

    queue = demo_enqueue()
    queue = demo_dequeue(queue)
    demo_peek(queue)
    demo_queries(queue)
    demo_clear(queue)
    demo_display()
    demo_practical_case()

    title("OPERATIONS SUMMARY")
    print("  Operation      Description                        Complexity")
    print("  " + "-" * 56)
    operations = [
        ("enqueue(v)", "Insert at rear",                    "O(1)"),
        ("dequeue()",  "Remove from front",                 "O(1)"),
        ("peek()",     "View front without removing",       "O(1)"),
        ("is_empty()", "Check if queue is empty",           "O(1)"),
        ("is_full()",  "Check if queue is full",            "O(1)"),
        ("size()",     "Number of elements",                "O(1)"),
        ("clear()",    "Empty the queue",                   "O(n)"),
        ("display()",  "Show queue content",                "O(n)"),
    ]
    for op, desc, complexity in operations:
        print(f"  {op:14s}  {desc:35s}  {complexity}")

    print(f"\n{SEPARATOR}")
    print("  [OK] Linear Queue - all operations demonstrated.")
    print(f"{SEPARATOR}\n")


if __name__ == "__main__":
    main()
