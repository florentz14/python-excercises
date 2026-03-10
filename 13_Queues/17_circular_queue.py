# -------------------------------------------------
# File Name: 17_circular_queue.py
# Author: Florentino Baez
# Date: 2026-03-09
# Description: Circular queue (fixed buffer) and full operation demos.
# -------------------------------------------------

"""
============================================================
  CIRCULAR QUEUE - Python 3.14
  Fixed-size circular buffer where the rear connects
  back to the start, maximizing space usage.

        front -> [10 | 20 | 30 | 40 | __ ]
                  ^                        ^
                front                    rear
               (read)                   (write)

  Advantage over linear queue: it reuses positions
  freed by dequeue without shifting elements.

  Operations:
    - enqueue   -> Insert at rear (with wrap-around)
    - dequeue   -> Remove from front (with wrap-around)
    - peek      -> View front
    - rear      -> View rear
    - is_empty  -> Is it empty?
    - is_full   -> Is it full?
    - size      -> Current size
    - clear     -> Empty queue
    - display   -> Show full physical buffer
============================================================
"""

SEPARATOR = "=" * 60


def title(text: str) -> None:
    print(f"\n{SEPARATOR}\n  {text}\n{SEPARATOR}")


def subtitle(text: str) -> None:
    print(f"\n  --- {text} ---")


# Circular queue with fixed-size array and modulo index updates.
class CircularQueue:
    """Fixed-size circular queue using wrap-around indexing."""

    def __init__(self, capacity: int = 8) -> None:
        self._capacity: int = capacity
        self._buffer: list = [None] * capacity
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
            raise IndexError("Circular queue is empty.")
        return self._buffer[self._front]

    def rear(self):
        """Return last inserted element."""
        if self.is_empty():
            raise IndexError("Circular queue is empty.")
        idx = (self._rear - 1) % self._capacity
        return self._buffer[idx]

    # Modification methods.
    def enqueue(self, value) -> None:
        if self.is_full():
            raise OverflowError("Circular queue is full.")
        self._buffer[self._rear] = value
        self._rear = (self._rear + 1) % self._capacity
        self._size += 1

    def dequeue(self):
        if self.is_empty():
            raise IndexError("Circular queue is empty.")
        value = self._buffer[self._front]
        self._buffer[self._front] = None
        self._front = (self._front + 1) % self._capacity
        self._size -= 1
        return value

    def clear(self) -> None:
        self._buffer = [None] * self._capacity
        self._front = 0
        self._rear = 0
        self._size = 0

    # Show physical buffer and marker positions.
    def display(self, name: str = "Circular Queue") -> None:
        buffer_str = []
        for i, value in enumerate(self._buffer):
            marker = ""
            if self._size > 0:
                rear_idx = (self._rear - 1) % self._capacity
                if i == self._front and i == rear_idx and self._size == 1:
                    marker = "F/R"
                elif i == self._front:
                    marker = "F"
                elif i == rear_idx:
                    marker = "R"
            cell = f"[{value if value is not None else '__':^4}]{marker}"
            buffer_str.append(cell)
        print(f"  {name}:")
        print("  " + " ".join(buffer_str))
        if not self.is_empty():
            print(
                f"  F=front(idx={self._front})  R=rear(idx={(self._rear - 1) % self._capacity})  "
                f"size={self._size}/{self._capacity}"
            )
        else:
            print(f"  (empty)  capacity={self._capacity}")

    # Show logical queue order from front to rear.
    def display_logical(self, name: str = "") -> None:
        if self.is_empty():
            print(f"  {name} FRONT -> [ empty ] <- REAR")
            return
        elems = []
        idx = self._front
        for _ in range(self._size):
            elems.append(str(self._buffer[idx]))
            idx = (idx + 1) % self._capacity
        print(f"  {name} FRONT -> [ {' | '.join(elems)} ] <- REAR")

    def __repr__(self) -> str:
        return f"CircularQueue(size={self._size}/{self._capacity})"


def demo_enqueue() -> CircularQueue:
    title("1. ENQUEUE - Insert at rear with wrap-around")
    queue = CircularQueue(capacity=5)

    for value in [10, 20, 30, 40, 50]:
        queue.enqueue(value)
        print(f"  enqueue({value:2d})")
        queue.display()
        print()

    subtitle("Try inserting into a full queue")
    try:
        queue.enqueue(99)
    except OverflowError as error:
        print(f"  OverflowError: {error}")

    return queue


def demo_dequeue(queue: CircularQueue) -> CircularQueue:
    title("2. DEQUEUE - Remove from front (front advances with wrap-around)")
    queue.display("Initial state")

    for _ in range(3):
        value = queue.dequeue()
        print(f"\n  dequeue() -> {value}")
        queue.display()

    subtitle("Insert after freeing space (visible wrap-around)")
    for value in [60, 70, 80]:
        queue.enqueue(value)
        print(f"\n  enqueue({value})")
        queue.display()

    return queue


def demo_peek_rear(queue: CircularQueue) -> None:
    title("3. PEEK and REAR - View front and rear without modifying queue")
    queue.display_logical("State:")
    print(f"  peek() -> {queue.peek()}   (front, not removed)")
    print(f"  rear() -> {queue.rear()}   (last inserted)")
    queue.display_logical("State after queries (unchanged):")


def demo_queries(queue: CircularQueue) -> None:
    title("4. QUERIES - is_empty, is_full, size")
    queue.display_logical("Current queue:")
    print(f"  is_empty() -> {queue.is_empty()}")
    print(f"  is_full()  -> {queue.is_full()}")
    print(f"  size()     -> {queue.size()}")

    subtitle("Empty queue (new)")
    empty_queue = CircularQueue(4)
    print(f"  is_empty() -> {empty_queue.is_empty()}")
    print(f"  is_full()  -> {empty_queue.is_full()}")
    print(f"  size()     -> {empty_queue.size()}")

    subtitle("Full queue (capacity=4)")
    full_queue = CircularQueue(4)
    for x in [1, 2, 3, 4]:
        full_queue.enqueue(x)
    full_queue.display()
    print(f"  is_empty() -> {full_queue.is_empty()}")
    print(f"  is_full()  -> {full_queue.is_full()}")
    print(f"  size()     -> {full_queue.size()}")


def demo_clear(queue: CircularQueue) -> None:
    title("5. CLEAR - Empty the circular queue")
    queue.display("Before clear()")
    queue.clear()
    queue.display("After clear()")
    print(f"  is_empty() -> {queue.is_empty()}")


def demo_wrap_around() -> None:
    title("6. WRAP-AROUND - The key advantage of circular queue")
    print("  In a LINEAR queue, freed slots after dequeue() are wasted.")
    print("  In a CIRCULAR queue, those slots are reused.\n")

    queue = CircularQueue(capacity=5)
    print("  Step 1: Fill the queue")
    for value in [1, 2, 3, 4, 5]:
        queue.enqueue(value)
    queue.display()

    print("\n  Step 2: Remove 3 elements (front moves)")
    for _ in range(3):
        queue.dequeue()
    queue.display()

    print("\n  Step 3: Insert 3 new values (reuses starting positions)")
    for value in [6, 7, 8]:
        queue.enqueue(value)
        queue.display()
        print()

    queue.display_logical("Final logical view:")


def demo_practical_case() -> None:
    title("7. PRACTICAL CASE - Print spooler buffer")
    print("  Scenario: printer with circular buffer of 4 jobs.\n")

    spooler = CircularQueue(capacity=4)
    jobs = ["Doc1.pdf", "Photo.png", "Report.docx", "Image.jpg"]

    print("  [Sending jobs to printer]")
    for job in jobs:
        spooler.enqueue(job)
        print(f"  -> Queued: {job}")
    spooler.display_logical("Buffer:")

    print("\n  [Printer processing]")
    cycles = 0
    new_jobs = ["Letter.txt", "Table.xlsx", "Summary.pdf"]
    new_idx = 0
    while not spooler.is_empty() or new_idx < len(new_jobs):
        if not spooler.is_empty():
            printed = spooler.dequeue()
            print(f"  [OK] Printing: {printed}")
        if new_idx < len(new_jobs) and not spooler.is_full():
            incoming = new_jobs[new_idx]
            spooler.enqueue(incoming)
            print(f"  -> New queued job: {incoming}")
            new_idx += 1
        cycles += 1

    print(f"\n  Total print cycles: {cycles}")
    spooler.display_logical("Buffer at end:")


def main() -> None:
    print(f"\n{SEPARATOR}")
    print("  CIRCULAR QUEUE - Python 3.14")
    print(f"{SEPARATOR}")

    queue = demo_enqueue()
    queue = demo_dequeue(queue)
    demo_peek_rear(queue)
    demo_queries(queue)
    demo_clear(queue)
    demo_wrap_around()
    demo_practical_case()

    title("OPERATIONS SUMMARY")
    print("  Operation        Description                             Complexity")
    print("  " + "-" * 62)
    operations = [
        ("enqueue(v)", "Insert at rear (with wrap-around)",      "O(1)"),
        ("dequeue()", "Remove from front (with wrap-around)",    "O(1)"),
        ("peek()", "View front without removing",                "O(1)"),
        ("rear()", "View last inserted element",                 "O(1)"),
        ("is_empty()", "Check if queue is empty",                "O(1)"),
        ("is_full()", "Check if queue is full",                  "O(1)"),
        ("size()", "Number of elements",                         "O(1)"),
        ("clear()", "Empty the queue",                           "O(n)"),
        ("display()", "Show full physical buffer",               "O(n)"),
    ]
    for op, desc, comp in operations:
        print(f"  {op:16s}  {desc:42s}  {comp}")

    print(f"\n{SEPARATOR}")
    print("  [OK] Circular Queue - all operations demonstrated.")
    print(f"{SEPARATOR}\n")


if __name__ == "__main__":
    main()
