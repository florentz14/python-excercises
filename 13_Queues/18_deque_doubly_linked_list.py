# -------------------------------------------------
# File Name: 18_deque_doubly_linked_list.py
# Author: Florentino Baez
# Date: 2026-03-09
# Description: Double-ended queue (deque) with doubly linked list.
# -------------------------------------------------

"""
============================================================
  DOUBLE-ENDED QUEUE (Deque) - Python 3.14
  Allows insertion and deletion from BOTH ends.

  FRONT <- [10 | 20 | 30 | 40 | 50] -> REAR
           ^                            ^
      push_front / pop_front      push_rear / pop_rear

  Operations:
    - push_front   -> Insert at front
    - push_rear    -> Insert at rear
    - pop_front    -> Remove from front
    - pop_rear     -> Remove from rear
    - peek_front   -> View front
    - peek_rear    -> View rear
    - is_empty     -> Is empty?
    - is_full      -> Is full?
    - size         -> Current size
    - clear        -> Empty deque
    - contains     -> Search element
    - rotate       -> Rotate deque
    - reverse      -> Reverse deque
    - display      -> Show content
============================================================
"""

SEPARATOR = "=" * 60


def title(text: str) -> None:
    print(f"\n{SEPARATOR}\n  {text}\n{SEPARATOR}")


def subtitle(text: str) -> None:
    print(f"\n  --- {text} ---")


# Internal node for doubly linked list.
class _Node:
    def __init__(self, value) -> None:
        self.value = value
        self.prev: "_Node | None" = None
        self.next: "_Node | None" = None


# Deque implemented with a doubly linked list.
class DoubleDeque:
    """Deque with optional capacity limit."""

    def __init__(self, capacity: int | None = None) -> None:
        self._head: _Node | None = None
        self._tail: _Node | None = None
        self._size: int = 0
        self._capacity = capacity

    # Query methods.
    def is_empty(self) -> bool:
        return self._size == 0

    def is_full(self) -> bool:
        if self._capacity is None:
            return False
        return self._size >= self._capacity

    def size(self) -> int:
        return self._size

    def peek_front(self):
        if self.is_empty():
            raise IndexError("Deque is empty.")
        return self._head.value

    def peek_rear(self):
        if self.is_empty():
            raise IndexError("Deque is empty.")
        return self._tail.value

    def contains(self, value) -> bool:
        current = self._head
        while current:
            if current.value == value:
                return True
            current = current.next
        return False

    def index_of(self, value) -> int:
        current = self._head
        idx = 0
        while current:
            if current.value == value:
                return idx
            current = current.next
            idx += 1
        return -1

    # Modification methods.
    def push_front(self, value) -> None:
        if self.is_full():
            raise OverflowError("Deque is full.")
        node = _Node(value)
        if self.is_empty():
            self._head = self._tail = node
        else:
            node.next = self._head
            self._head.prev = node
            self._head = node
        self._size += 1

    def push_rear(self, value) -> None:
        if self.is_full():
            raise OverflowError("Deque is full.")
        node = _Node(value)
        if self.is_empty():
            self._head = self._tail = node
        else:
            node.prev = self._tail
            self._tail.next = node
            self._tail = node
        self._size += 1

    def pop_front(self):
        if self.is_empty():
            raise IndexError("Deque is empty.")
        value = self._head.value
        if self._size == 1:
            self._head = self._tail = None
        else:
            self._head = self._head.next
            self._head.prev = None
        self._size -= 1
        return value

    def pop_rear(self):
        if self.is_empty():
            raise IndexError("Deque is empty.")
        value = self._tail.value
        if self._size == 1:
            self._head = self._tail = None
        else:
            self._tail = self._tail.prev
            self._tail.next = None
        self._size -= 1
        return value

    def clear(self) -> None:
        self._head = self._tail = None
        self._size = 0

    def rotate(self, k: int = 1) -> None:
        """Rotate right by k (k>0) or left by k (k<0)."""
        if self._size <= 1:
            return
        if k >= 0:
            steps = k % self._size
            for _ in range(steps):
                self.push_front(self.pop_rear())
        else:
            steps = (-k) % self._size
            for _ in range(steps):
                self.push_rear(self.pop_front())

    def reverse(self) -> None:
        """Reverse deque order in-place."""
        current = self._head
        while current:
            current.prev, current.next = current.next, current.prev
            current = current.prev
        self._head, self._tail = self._tail, self._head

    def to_list(self) -> list:
        result = []
        current = self._head
        while current:
            result.append(current.value)
            current = current.next
        return result

    # Visualization helper.
    def display(self, name: str = "") -> None:
        cap = f"cap={self._capacity}" if self._capacity else "no limit"
        if self.is_empty():
            print(f"  {name} FRONT <- [ empty ] -> REAR  ({cap})")
            return
        elems = " <-> ".join(str(v) for v in self.to_list())
        print(f"  {name} FRONT <- [ {elems} ] -> REAR  (size={self._size}, {cap})")

    def __repr__(self) -> str:
        return f"DoubleDeque({self.to_list()})"


def demo_push() -> DoubleDeque:
    title("1. PUSH_FRONT and PUSH_REAR - Insert at both ends")
    dq = DoubleDeque()

    subtitle("1a. Insert at REAR (push_rear)")
    for value in [20, 30, 40]:
        dq.push_rear(value)
        print(f"  push_rear({value:2d})   ->  ", end="")
        dq.display()

    subtitle("1b. Insert at FRONT (push_front)")
    for value in [10, 0]:
        dq.push_front(value)
        print(f"  push_front({value:2d})  ->  ", end="")
        dq.display()

    subtitle("1c. Alternate insertions")
    dq2 = DoubleDeque()
    for i, value in enumerate([5, 15, 25, 35, 45]):
        if i % 2 == 0:
            dq2.push_rear(value)
            print(f"  push_rear({value:2d})   ->  ", end="")
        else:
            dq2.push_front(value)
            print(f"  push_front({value:2d})  ->  ", end="")
        dq2.display()

    return dq


def demo_pop(dq: DoubleDeque) -> DoubleDeque:
    title("2. POP_FRONT and POP_REAR - Remove from both ends")
    dq.display("Before:")

    subtitle("2a. Remove from FRONT (pop_front)")
    for _ in range(2):
        value = dq.pop_front()
        print(f"  pop_front() -> {value}")
        dq.display()

    subtitle("2b. Remove from REAR (pop_rear)")
    for _ in range(2):
        value = dq.pop_rear()
        print(f"  pop_rear()  -> {value}")
        dq.display()

    subtitle("2c. Remove until empty")
    dq.push_rear(100)
    dq.push_rear(200)
    while not dq.is_empty():
        value = dq.pop_front()
        print(f"  pop_front() -> {value}  | remaining: {dq.size()}")

    subtitle("2d. Error when removing from empty deque")
    try:
        dq.pop_front()
    except IndexError as error:
        print(f"  IndexError (pop_front): {error}")
    try:
        dq.pop_rear()
    except IndexError as error:
        print(f"  IndexError (pop_rear): {error}")

    return dq


def demo_peek(dq: DoubleDeque) -> None:
    title("3. PEEK_FRONT and PEEK_REAR - View without removing")
    for value in [10, 20, 30, 40, 50]:
        dq.push_rear(value)
    dq.display("Current deque:")
    print(f"  peek_front() -> {dq.peek_front()}  (not removed)")
    print(f"  peek_rear()  -> {dq.peek_rear()}  (not removed)")
    dq.display("Deque unchanged:")


def demo_queries(dq: DoubleDeque) -> None:
    title("4. QUERIES - is_empty, is_full, size, contains, index_of")
    dq.display("Current deque:")
    print(f"  is_empty()      -> {dq.is_empty()}")
    print(f"  is_full()       -> {dq.is_full()}")
    print(f"  size()          -> {dq.size()}")

    subtitle("contains() and index_of()")
    for val in [30, 99]:
        print(f"  contains({val:2d})   -> {dq.contains(val)}")
        print(f"  index_of({val:2d})   -> {dq.index_of(val)}")

    subtitle("Capacity-limited deque")
    limited = DoubleDeque(capacity=3)
    for value in [1, 2, 3]:
        limited.push_rear(value)
    limited.display("Limited deque (cap=3):")
    print(f"  is_full()  -> {limited.is_full()}")
    try:
        limited.push_rear(4)
    except OverflowError as error:
        print(f"  OverflowError: {error}")


def demo_clear(dq: DoubleDeque) -> None:
    title("5. CLEAR - Empty the deque")
    dq.display("Before clear():")
    dq.clear()
    dq.display("After clear():")
    print(f"  is_empty() -> {dq.is_empty()}")


def demo_rotate_reverse() -> None:
    title("6. ROTATE and REVERSE - Advanced operations")

    subtitle("6a. rotate(k) - shift by k positions")
    dq = DoubleDeque()
    for value in [1, 2, 3, 4, 5]:
        dq.push_rear(value)
    dq.display("Original:")
    for k in [1, 2, -1]:
        dq2 = DoubleDeque()
        for value in [1, 2, 3, 4, 5]:
            dq2.push_rear(value)
        dq2.rotate(k)
        print(f"  rotate({k:+d})  ->  ", end="")
        dq2.display()

    subtitle("6b. reverse() - invert deque")
    dq.display("Before reverse():")
    dq.reverse()
    dq.display("After reverse():")


def demo_dual_usage() -> None:
    title("7. USE AS QUEUE AND STACK - Deque is generic")

    subtitle("7a. Use as FIFO queue (push_rear + pop_front)")
    fifo = DoubleDeque()
    for value in ["A", "B", "C"]:
        fifo.push_rear(value)
    fifo.display("FIFO (front to rear):")
    while not fifo.is_empty():
        print(f"  dequeue -> {fifo.pop_front()}")

    subtitle("7b. Use as LIFO stack (push_rear + pop_rear)")
    lifo = DoubleDeque()
    for value in ["X", "Y", "Z"]:
        lifo.push_rear(value)
    lifo.display("LIFO (top = rear):")
    while not lifo.is_empty():
        print(f"  pop -> {lifo.pop_rear()}")


def demo_practical_case() -> None:
    title("8. PRACTICAL CASE - Web browser history")
    print("  Scenario: user navigates pages and can go back/forward.\n")

    history_back = DoubleDeque()
    history_forward = DoubleDeque()
    current_page = "home.com"

    def navigate(new_page: str) -> None:
        nonlocal current_page
        history_back.push_rear(current_page)
        history_forward.clear()
        current_page = new_page
        print(f"  -> Navigating to: {current_page}")

    def go_back() -> None:
        nonlocal current_page
        if history_back.is_empty():
            print("  <- No back history.")
            return
        history_forward.push_front(current_page)
        current_page = history_back.pop_rear()
        print(f"  <- Back to: {current_page}")

    def go_forward() -> None:
        nonlocal current_page
        if history_forward.is_empty():
            print("  -> No forward history.")
            return
        history_back.push_rear(current_page)
        current_page = history_forward.pop_front()
        print(f"  -> Forward to: {current_page}")

    def state() -> None:
        back = history_back.to_list()
        forward = history_forward.to_list()
        print(f"     Back: {back}  |  Current: [{current_page}]  |  Forward: {forward}")

    navigate("google.com")
    navigate("python.org")
    navigate("docs.python.org")
    state()
    print()
    go_back()
    state()
    go_back()
    state()
    print()
    go_forward()
    state()
    navigate("stackoverflow.com")
    state()


def main() -> None:
    print(f"\n{SEPARATOR}")
    print("  DOUBLE-ENDED QUEUE (DEQUE) - Python 3.14")
    print(f"{SEPARATOR}")

    dq = demo_push()
    dq = demo_pop(dq)
    demo_peek(dq)
    demo_queries(dq)
    demo_clear(dq)
    demo_rotate_reverse()
    demo_dual_usage()
    demo_practical_case()

    title("OPERATIONS SUMMARY")
    print("  Operation          Description                         Complexity")
    print("  " + "-" * 62)
    operations = [
        ("push_front(v)", "Insert at front",                    "O(1)"),
        ("push_rear(v)", "Insert at rear",                      "O(1)"),
        ("pop_front()", "Remove from front",                    "O(1)"),
        ("pop_rear()", "Remove from rear",                      "O(1)"),
        ("peek_front()", "View front without removing",         "O(1)"),
        ("peek_rear()", "View rear without removing",           "O(1)"),
        ("is_empty()", "Check if empty",                        "O(1)"),
        ("is_full()", "Check if full",                          "O(1)"),
        ("size()", "Number of elements",                        "O(1)"),
        ("contains(v)", "Check if value exists",                "O(n)"),
        ("index_of(v)", "Index of value",                       "O(n)"),
        ("rotate(k)", "Rotate k positions",                     "O(k)"),
        ("reverse()", "Reverse deque",                          "O(n)"),
        ("clear()", "Empty deque",                              "O(1)"),
        ("display()", "Show content",                           "O(n)"),
    ]
    for op, desc, complexity in operations:
        print(f"  {op:18s}  {desc:38s}  {complexity}")

    print(f"\n{SEPARATOR}")
    print("  [OK] Double-ended queue - all operations demonstrated.")
    print(f"{SEPARATOR}\n")


if __name__ == "__main__":
    main()
