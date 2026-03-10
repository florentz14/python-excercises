# -------------------------------------------------
# File Name: 19_priority_queue_heap.py
# Author: Florentino Baez
# Date: 2026-03-09
# Description: Priority queue with max-heap and min-heap variants.
# -------------------------------------------------

"""
============================================================
  PRIORITY QUEUE - Python 3.14
  Elements are removed by priority, not arrival order.

  - Higher number = higher priority (max-heap)
  - Lower number = higher priority (min-heap)
  This file implements BOTH variants.

  Internal structure: binary heap (complete tree).

  Operations:
    - enqueue         -> Insert with priority
    - dequeue         -> Remove highest-priority element
    - peek            -> View highest-priority element
    - change_priority -> Change an element priority
    - remove          -> Remove specific element
    - contains        -> Search element
    - is_empty        -> Is queue empty?
    - size            -> Current size
    - clear           -> Empty queue
    - merge           -> Merge two queues
    - display         -> Show sorted content
    - heapify         -> Build from existing list
============================================================
"""

SEPARATOR = "=" * 60


def title(text: str) -> None:
    print(f"\n{SEPARATOR}\n  {text}\n{SEPARATOR}")


def subtitle(text: str) -> None:
    print(f"\n  --- {text} ---")


# Max-heap priority queue with FIFO tie-breaker.
class PriorityQueue:
    """
    Max-heap based priority queue.
    Each stored item is (priority, insertion_order, value).
    """

    def __init__(self) -> None:
        self._heap: list[tuple] = []
        self._counter: int = 0

    # Heap helpers.
    def _parent(self, i: int) -> int:
        return (i - 1) // 2

    def _left(self, i: int) -> int:
        return 2 * i + 1

    def _right(self, i: int) -> int:
        return 2 * i + 2

    def _key(self, i: int) -> tuple:
        # Compare by priority first, then FIFO for same priority.
        priority, order, _ = self._heap[i]
        return (priority, -order)

    def _sift_up(self, i: int) -> None:
        while i > 0:
            p = self._parent(i)
            if self._key(i) > self._key(p):
                self._heap[i], self._heap[p] = self._heap[p], self._heap[i]
                i = p
            else:
                break

    def _sift_down(self, i: int) -> None:
        n = len(self._heap)
        while True:
            largest = i
            left = self._left(i)
            right = self._right(i)
            if left < n and self._key(left) > self._key(largest):
                largest = left
            if right < n and self._key(right) > self._key(largest):
                largest = right
            if largest == i:
                break
            self._heap[i], self._heap[largest] = self._heap[largest], self._heap[i]
            i = largest

    # Queries.
    def is_empty(self) -> bool:
        return len(self._heap) == 0

    def size(self) -> int:
        return len(self._heap)

    def peek(self) -> tuple:
        if self.is_empty():
            raise IndexError("Priority queue is empty.")
        priority, _, value = self._heap[0]
        return (priority, value)

    def contains(self, value) -> bool:
        return any(v == value for _, _, v in self._heap)

    def get_priority(self, value) -> int | None:
        for priority, _, v in self._heap:
            if v == value:
                return priority
        return None

    # Modifications.
    def enqueue(self, value, priority: int) -> None:
        self._heap.append((priority, self._counter, value))
        self._counter += 1
        self._sift_up(len(self._heap) - 1)

    def dequeue(self) -> tuple:
        if self.is_empty():
            raise IndexError("Priority queue is empty.")
        self._heap[0], self._heap[-1] = self._heap[-1], self._heap[0]
        priority, _, value = self._heap.pop()
        if self._heap:
            self._sift_down(0)
        return (priority, value)

    def change_priority(self, value, new_priority: int) -> bool:
        for i, (priority, order, v) in enumerate(self._heap):
            if v == value:
                self._heap[i] = (new_priority, order, v)
                if new_priority > priority:
                    self._sift_up(i)
                else:
                    self._sift_down(i)
                return True
        return False

    def remove(self, value) -> bool:
        for i, (_, _, v) in enumerate(self._heap):
            if v == value:
                self._heap[i], self._heap[-1] = self._heap[-1], self._heap[i]
                self._heap.pop()
                if i < len(self._heap):
                    self._sift_up(i)
                    self._sift_down(i)
                return True
        return False

    def clear(self) -> None:
        self._heap = []
        self._counter = 0

    def merge(self, other: "PriorityQueue") -> "PriorityQueue":
        merged = PriorityQueue()
        for priority, _, value in self._heap:
            merged.enqueue(value, priority)
        for priority, _, value in other._heap:
            merged.enqueue(value, priority)
        return merged

    @classmethod
    def heapify(cls, items: list[tuple]) -> "PriorityQueue":
        """
        Build queue from list of (value, priority) in O(n) time.
        """
        pq = cls()
        for value, priority in items:
            pq._heap.append((priority, pq._counter, value))
            pq._counter += 1
        for i in range(len(pq._heap) // 2 - 1, -1, -1):
            pq._sift_down(i)
        return pq

    # Visualization helpers.
    def display(self, name: str = "PriorityQueue") -> None:
        if self.is_empty():
            print(f"  {name}: [ empty ]")
            return
        ordered = sorted(self._heap, key=lambda x: (-x[0], x[1]))
        elems = " -> ".join(f"{value}(p={priority})" for priority, _, value in ordered)
        print(f"  {name} [high->low]: {elems}")
        print(f"  {'':20s}Size: {self.size()}")

    def display_heap(self, name: str = "Internal heap") -> None:
        if self.is_empty():
            print(f"  {name}: [ empty ]")
            return
        print(f"  {name}:")
        n = len(self._heap)
        level = 0
        i = 0
        while i < n:
            count = 2 ** level
            row = []
            for _ in range(count):
                if i >= n:
                    break
                priority, _, value = self._heap[i]
                row.append(f"{value}({priority})")
                i += 1
            indent = " " * max(0, 20 - level * 4)
            print(indent + "  ".join(row))
            level += 1

    def __repr__(self) -> str:
        return f"PriorityQueue(size={self.size()})"


# Min-heap variant where lower priority is removed first.
class MinPriorityQueue:
    def __init__(self) -> None:
        self._heap: list[tuple] = []
        self._counter: int = 0

    def _key(self, i: int) -> tuple:
        priority, order, _ = self._heap[i]
        return (-priority, -order)

    def _sift_up(self, i: int) -> None:
        while i > 0:
            p = (i - 1) // 2
            if self._key(i) > self._key(p):
                self._heap[i], self._heap[p] = self._heap[p], self._heap[i]
                i = p
            else:
                break

    def _sift_down(self, i: int) -> None:
        n = len(self._heap)
        while True:
            smallest = i
            left = 2 * i + 1
            right = 2 * i + 2
            if left < n and self._key(left) > self._key(smallest):
                smallest = left
            if right < n and self._key(right) > self._key(smallest):
                smallest = right
            if smallest == i:
                break
            self._heap[i], self._heap[smallest] = self._heap[smallest], self._heap[i]
            i = smallest

    def enqueue(self, value, priority: int) -> None:
        self._heap.append((priority, self._counter, value))
        self._counter += 1
        self._sift_up(len(self._heap) - 1)

    def dequeue(self) -> tuple:
        if not self._heap:
            raise IndexError("Priority queue is empty.")
        self._heap[0], self._heap[-1] = self._heap[-1], self._heap[0]
        priority, _, value = self._heap.pop()
        if self._heap:
            self._sift_down(0)
        return (priority, value)

    def peek(self) -> tuple:
        if not self._heap:
            raise IndexError("Priority queue is empty.")
        priority, _, value = self._heap[0]
        return (priority, value)

    def is_empty(self) -> bool:
        return not self._heap

    def size(self) -> int:
        return len(self._heap)

    def display(self, name: str = "MinHeap") -> None:
        if not self._heap:
            print(f"  {name}: [ empty ]")
            return
        ordered = sorted(self._heap, key=lambda x: (x[0], x[1]))
        elems = " -> ".join(f"{value}(p={priority})" for priority, _, value in ordered)
        print(f"  {name} [low->high]: {elems}")


def demo_enqueue() -> PriorityQueue:
    title("1. ENQUEUE - Insert elements with priority")
    pq = PriorityQueue()
    data = [
        ("Task C", 2),
        ("Task A", 5),
        ("Task D", 1),
        ("Task B", 4),
        ("Task E", 3),
        ("Urgent", 9),
    ]

    subtitle("1a. Insert elements (higher priority leaves first)")
    for value, priority in data:
        pq.enqueue(value, priority)
        print(f"  enqueue({value!r:10s}, p={priority})  ->  ", end="")
        pq.display()

    subtitle("1b. Internal binary heap view")
    pq.display_heap()
    return pq


def demo_dequeue(pq: PriorityQueue) -> PriorityQueue:
    title("2. DEQUEUE - Always remove highest priority")
    pq.display("Before:")

    subtitle("Remove one by one")
    while not pq.is_empty():
        priority, value = pq.dequeue()
        print(f"  dequeue() -> {value!r:12s} (priority={priority})  | remaining: {pq.size()}")

    subtitle("Error when removing from empty queue")
    try:
        pq.dequeue()
    except IndexError as error:
        print(f"  IndexError: {error}")
    return pq


def demo_peek() -> PriorityQueue:
    title("3. PEEK - View highest priority without removing")
    pq = PriorityQueue()
    for value, priority in [("alpha", 3), ("beta", 7), ("gamma", 1)]:
        pq.enqueue(value, priority)
    pq.display("Queue:")
    priority, value = pq.peek()
    print(f"  peek() -> {value!r} with priority {priority}  (not removed)")
    pq.display("Queue unchanged:")
    return pq


def demo_change_priority(pq: PriorityQueue) -> None:
    title("4. CHANGE_PRIORITY - Modify an existing element priority")
    for value, priority in [("process_A", 2), ("process_B", 5), ("process_C", 3)]:
        pq.enqueue(value, priority)
    pq.display("Before:")

    subtitle("Increase process_A from 2 -> 8")
    ok = pq.change_priority("process_A", 8)
    print(f"  change_priority('process_A', 8) -> {'OK' if ok else 'Not found'}")
    pq.display("After:")

    subtitle("Decrease process_B from 5 -> 1")
    ok = pq.change_priority("process_B", 1)
    print(f"  change_priority('process_B', 1) -> {'OK' if ok else 'Not found'}")
    pq.display("After:")

    subtitle("Try changing missing element")
    ok = pq.change_priority("process_Z", 10)
    print(f"  change_priority('process_Z', 10) -> {'OK' if ok else 'Not found (expected)'}")


def demo_remove(pq: PriorityQueue) -> None:
    title("5. REMOVE - Delete specific element by value")
    pq.display("Before:")

    for value in ["process_B", "process_C"]:
        ok = pq.remove(value)
        print(f"  remove({value!r}) -> {'removed [OK]' if ok else 'not found'}")
        pq.display()

    subtitle("Remove non-existing element")
    ok = pq.remove("process_X")
    print(f"  remove('process_X') -> {'removed' if ok else 'not found (expected)'}")


def demo_queries() -> None:
    title("6. QUERIES - contains, get_priority, is_empty, size")
    pq = PriorityQueue()
    for value, priority in [("ping", 1), ("pong", 5), ("boom", 3)]:
        pq.enqueue(value, priority)
    pq.display("Queue:")
    print(f"  is_empty()           -> {pq.is_empty()}")
    print(f"  size()               -> {pq.size()}")
    print(f"  contains('pong')     -> {pq.contains('pong')}")
    print(f"  contains('miss')     -> {pq.contains('miss')}")
    print(f"  get_priority('boom') -> {pq.get_priority('boom')}")
    print(f"  get_priority('miss') -> {pq.get_priority('miss')}")


def demo_heapify() -> None:
    title("7. HEAPIFY - Build queue from existing list in O(n)")
    items = [
        ("item_E", 5), ("item_B", 2), ("item_A", 8),
        ("item_D", 4), ("item_C", 1), ("item_F", 7),
    ]
    print("  Input list (value, priority):", items)
    pq = PriorityQueue.heapify(items)
    pq.display("Result queue:")
    pq.display_heap("Internal heap:")


def demo_merge() -> None:
    title("8. MERGE - Merge two priority queues")
    pq1 = PriorityQueue()
    pq2 = PriorityQueue()

    for value, priority in [("A", 3), ("B", 7), ("C", 1)]:
        pq1.enqueue(value, priority)
    for value, priority in [("X", 5), ("Y", 2), ("Z", 9)]:
        pq2.enqueue(value, priority)

    pq1.display("Queue 1:")
    pq2.display("Queue 2:")
    merged = pq1.merge(pq2)
    merged.display("Merged:")

    print("\n  Removing in priority order:")
    while not merged.is_empty():
        priority, value = merged.dequeue()
        print(f"     -> {value} (priority={priority})")


def demo_min_heap() -> None:
    title("9. MIN-HEAP - Lower priority removed first (e.g., Dijkstra)")
    pq_min = MinPriorityQueue()
    nodes = [("C", 4), ("A", 1), ("F", 6), ("B", 2), ("E", 5), ("D", 3)]
    for value, priority in nodes:
        pq_min.enqueue(value, priority)
    pq_min.display("Min-heap:")

    print("\n  Removing (smallest first):")
    while not pq_min.is_empty():
        priority, value = pq_min.dequeue()
        print(f"     -> Node {value} with distance {priority}")


def demo_fifo_tie_breaker() -> None:
    title("10. FIFO TIE-BREAKER - Same priority keeps arrival order")
    pq = PriorityQueue()
    data = [("Req-1", 5), ("Req-2", 5), ("Req-3", 3), ("Req-4", 5), ("Req-5", 3)]
    for value, priority in data:
        pq.enqueue(value, priority)
    pq.display("Queue:")

    print("\n  Removal order (same priority -> earliest inserted first):")
    while not pq.is_empty():
        priority, value = pq.dequeue()
        print(f"     -> {value} (priority={priority})")


def demo_practical_case() -> None:
    title("11. PRACTICAL CASE - Technical support ticket system")
    print("  Priorities: 1=Low  3=Medium  5=High  9=Critical\n")

    support = PriorityQueue()
    tickets = [
        ("T-101: Printer out of paper", 1),
        ("T-102: Server down", 9),
        ("T-103: Software error", 5),
        ("T-104: Keyboard broken", 1),
        ("T-105: Slow database", 5),
        ("T-106: Email not working", 3),
        ("T-107: Ransomware detected", 9),
    ]

    print("  [Receiving tickets]")
    for desc, priority in tickets:
        support.enqueue(desc, priority)
        label = {1: "LOW", 3: "MEDIUM", 5: "HIGH", 9: "CRITICAL"}[priority]
        print(f"  [*] [{label:8s}] {desc}")

    support.display("\n  Support queue:")

    subtitle("New urgent ticket while processing")
    support.enqueue("T-108: Fire in server room", 9)
    print("  [*] [CRITICAL] T-108: Fire in server room")
    support.display("Updated queue:")

    print("\n  [Processing tickets by priority]")
    turn = 1
    while not support.is_empty():
        priority, desc = support.dequeue()
        label = {1: "LOW", 3: "MEDIUM", 5: "HIGH", 9: "CRITICAL"}[priority]
        print(f"  #{turn:02d} [{label:8s}] {desc}")
        turn += 1


def main() -> None:
    print(f"\n{SEPARATOR}")
    print("  PRIORITY QUEUE - Python 3.14")
    print(f"{SEPARATOR}")

    pq = demo_enqueue()
    pq = demo_dequeue(pq)
    pq = demo_peek()
    demo_change_priority(pq)
    demo_remove(pq)
    demo_queries()
    demo_heapify()
    demo_merge()
    demo_min_heap()
    demo_fifo_tie_breaker()
    demo_practical_case()

    title("OPERATIONS SUMMARY")
    print("  Operation               Description                         Complexity")
    print("  " + "-" * 65)
    operations = [
        ("enqueue(v, p)", "Insert with priority",                 "O(log n)"),
        ("dequeue()", "Remove highest-priority element",          "O(log n)"),
        ("peek()", "View highest without removing",               "O(1)"),
        ("change_priority(v,p)", "Change element priority",       "O(n)"),
        ("remove(v)", "Remove specific element",                  "O(n)"),
        ("contains(v)", "Check if value exists",                  "O(n)"),
        ("get_priority(v)", "Get value priority",                 "O(n)"),
        ("is_empty()", "Check if empty",                          "O(1)"),
        ("size()", "Number of elements",                          "O(1)"),
        ("clear()", "Empty queue",                                "O(1)"),
        ("merge(other)", "Merge with another queue",              "O(n log n)"),
        ("heapify(items)", "Build from list",                     "O(n)"),
        ("display()", "Show in priority order",                   "O(n log n)"),
        ("display_heap()", "Show internal tree",                  "O(n)"),
    ]
    for op, desc, complexity in operations:
        print(f"  {op:24s}  {desc:36s}  {complexity}")

    print(f"\n{SEPARATOR}")
    print("  [OK] Priority queue - all operations demonstrated.")
    print(f"{SEPARATOR}\n")


if __name__ == "__main__":
    main()
