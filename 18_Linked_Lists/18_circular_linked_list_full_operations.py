# -------------------------------------------------
# File Name: 18_circular_linked_list_full_operations.py
# Author: Florentino Baez
# Date: 2026-03-09
# Description: Circular linked lists (singly and doubly) with full demos.
# -------------------------------------------------

"""
============================================================
  CIRCULAR LINKED LIST - Python 3.14
  The last node points BACK to the first node, forming
  a ring. There is no None terminator.

  SINGLY CIRCULAR:
    [10] -> [20] -> [30] -> [40] --+
      ^                             |
      +-----------------------------+

  DOUBLY CIRCULAR:
    [10] <-> [20] <-> [30] <-> [40]
      ^                           |
      +---------------------------+

  Two complete implementations in this file:
    A) SinglyCircularLinkedList
    B) DoublyCircularLinkedList

  Operations covered (both):
    - append         -> Insert at tail
    - prepend        -> Insert at head
    - insert_at      -> Insert at index
    - delete_head    -> Remove head
    - delete_tail    -> Remove tail
    - delete_at      -> Remove at index
    - delete_value   -> Remove first occurrence
    - get            -> Retrieve at index
    - update         -> Replace at index
    - search         -> First index of value
    - contains       -> Check existence
    - count          -> Count occurrences
    - rotate         -> Rotate the ring
    - reverse        -> Reverse the ring
    - sort           -> Sort ascending
    - length / is_empty
    - to_list        -> Export as Python list
    - split          -> Split into two halves
    - display        -> Print the circular ring
    - josephus       -> Josephus problem solver
============================================================
"""

SEPARATOR = "=" * 64


def title(text: str) -> None:
    print(f"\n{SEPARATOR}\n  {text}\n{SEPARATOR}")


def subtitle(text: str) -> None:
    print(f"\n  --- {text} ---")


# A) Singly circular linked list.
class SCNode:
    def __init__(self, value) -> None:
        self.value = value
        self.next: "SCNode | None" = None


class SinglyCircularLinkedList:
    """Singly circular linked list with head/tail pointers."""

    def __init__(self) -> None:
        self._head: SCNode | None = None
        self._tail: SCNode | None = None
        self._size: int = 0

    # Queries.
    def is_empty(self) -> bool:
        return self._head is None

    def length(self) -> int:
        return self._size

    def get(self, index: int):
        return self._get_node(index).value

    def _get_node(self, index: int) -> SCNode:
        if index < 0 or index >= self._size:
            raise IndexError(f"Index {index} out of range (size={self._size}).")
        current = self._head
        for _ in range(index):
            current = current.next
        return current

    def search(self, value) -> int:
        if self.is_empty():
            return -1
        current = self._head
        for i in range(self._size):
            if current.value == value:
                return i
            current = current.next
        return -1

    def contains(self, value) -> bool:
        return self.search(value) != -1

    def count(self, value) -> int:
        total, current = 0, self._head
        for _ in range(self._size):
            if current.value == value:
                total += 1
            current = current.next
        return total

    # Insertions.
    def append(self, value) -> None:
        node = SCNode(value)
        if self.is_empty():
            self._head = self._tail = node
            node.next = node
        else:
            node.next = self._head
            self._tail.next = node
            self._tail = node
        self._size += 1

    def prepend(self, value) -> None:
        node = SCNode(value)
        if self.is_empty():
            self._head = self._tail = node
            node.next = node
        else:
            node.next = self._head
            self._tail.next = node
            self._head = node
        self._size += 1

    def insert_at(self, index: int, value) -> None:
        if index < 0 or index > self._size:
            raise IndexError(f"Index {index} out of range.")
        if index == 0:
            self.prepend(value)
        elif index == self._size:
            self.append(value)
        else:
            node = SCNode(value)
            prev = self._get_node(index - 1)
            node.next = prev.next
            prev.next = node
            self._size += 1

    # Deletions.
    def delete_head(self):
        if self.is_empty():
            raise IndexError("List is empty.")
        value = self._head.value
        if self._size == 1:
            self._head = self._tail = None
        else:
            self._head = self._head.next
            self._tail.next = self._head
        self._size -= 1
        return value

    def delete_tail(self):
        if self.is_empty():
            raise IndexError("List is empty.")
        if self._size == 1:
            return self.delete_head()
        prev = self._get_node(self._size - 2)
        value = self._tail.value
        prev.next = self._head
        self._tail = prev
        self._size -= 1
        return value

    def delete_at(self, index: int):
        if index == 0:
            return self.delete_head()
        if index == self._size - 1:
            return self.delete_tail()
        prev = self._get_node(index - 1)
        value = prev.next.value
        prev.next = prev.next.next
        self._size -= 1
        return value

    def delete_value(self, value) -> bool:
        idx = self.search(value)
        if idx == -1:
            return False
        self.delete_at(idx)
        return True

    # Updates.
    def update(self, index: int, value) -> None:
        self._get_node(index).value = value

    # Structural operations.
    def rotate(self, k: int) -> None:
        if self._size <= 1:
            return
        k = k % self._size
        for _ in range(k):
            self._tail = self._head
            self._head = self._head.next

    def reverse(self) -> None:
        if self._size < 2:
            return
        prev = self._tail
        current = self._head
        for _ in range(self._size):
            nxt = current.next
            current.next = prev
            prev = current
            current = nxt
        self._head, self._tail = self._tail, self._head

    def sort(self) -> None:
        if self._size < 2:
            return
        swapped = True
        while swapped:
            swapped = False
            current = self._head
            for _ in range(self._size - 1):
                if current.value > current.next.value:
                    current.value, current.next.value = current.next.value, current.value
                    swapped = True
                current = current.next

    def split(self) -> tuple["SinglyCircularLinkedList", "SinglyCircularLinkedList"]:
        if self._size < 2:
            raise ValueError("List must have at least 2 elements to split.")
        mid = self._size // 2
        first = SinglyCircularLinkedList()
        second = SinglyCircularLinkedList()
        current = self._head
        for i in range(self._size):
            if i < mid:
                first.append(current.value)
            else:
                second.append(current.value)
            current = current.next
        return first, second

    def to_list(self) -> list:
        result, current = [], self._head
        for _ in range(self._size):
            result.append(current.value)
            current = current.next
        return result

    @classmethod
    def from_list(cls, items: list) -> "SinglyCircularLinkedList":
        scll = cls()
        for item in items:
            scll.append(item)
        return scll

    def display(self, label: str = "") -> None:
        if label:
            print(f"  {label}")
        if self.is_empty():
            print("  O (empty circular list)")
            return
        vals = self.to_list()
        chain = " -> ".join(f"[{v}]" for v in vals)
        print("  HEAD v")
        print(f"  {chain} -> (back to HEAD)  length={self._size}")


# B) Doubly circular linked list.
class DCNode:
    def __init__(self, value) -> None:
        self.value = value
        self.prev: "DCNode | None" = None
        self.next: "DCNode | None" = None


class DoublyCircularLinkedList:
    """Doubly circular linked list with head/tail pointers."""

    def __init__(self) -> None:
        self._head: DCNode | None = None
        self._tail: DCNode | None = None
        self._size: int = 0

    # Queries.
    def is_empty(self) -> bool:
        return self._head is None

    def length(self) -> int:
        return self._size

    def get(self, index: int):
        return self._get_node(index).value

    def _get_node(self, index: int) -> DCNode:
        if index < 0 or index >= self._size:
            raise IndexError(f"Index {index} out of range (size={self._size}).")
        if index <= self._size // 2:
            current = self._head
            for _ in range(index):
                current = current.next
        else:
            current = self._tail
            for _ in range(self._size - 1 - index):
                current = current.prev
        return current

    def search(self, value) -> int:
        current = self._head
        for i in range(self._size):
            if current.value == value:
                return i
            current = current.next
        return -1

    def contains(self, value) -> bool:
        return self.search(value) != -1

    def count(self, value) -> int:
        total, current = 0, self._head
        for _ in range(self._size):
            if current.value == value:
                total += 1
            current = current.next
        return total

    # Insertions.
    def append(self, value) -> None:
        node = DCNode(value)
        if self.is_empty():
            self._head = self._tail = node
            node.next = node.prev = node
        else:
            node.prev = self._tail
            node.next = self._head
            self._tail.next = node
            self._head.prev = node
            self._tail = node
        self._size += 1

    def prepend(self, value) -> None:
        node = DCNode(value)
        if self.is_empty():
            self._head = self._tail = node
            node.next = node.prev = node
        else:
            node.next = self._head
            node.prev = self._tail
            self._head.prev = node
            self._tail.next = node
            self._head = node
        self._size += 1

    def insert_at(self, index: int, value) -> None:
        if index < 0 or index > self._size:
            raise IndexError(f"Index {index} out of range.")
        if index == 0:
            self.prepend(value)
        elif index == self._size:
            self.append(value)
        else:
            node = DCNode(value)
            after = self._get_node(index)
            before = after.prev
            node.prev, node.next = before, after
            before.next = after.prev = node
            self._size += 1

    # Deletions.
    def _unlink(self, node: DCNode):
        if self._size == 1:
            self._head = self._tail = None
        else:
            node.prev.next = node.next
            node.next.prev = node.prev
            if node is self._head:
                self._head = node.next
            if node is self._tail:
                self._tail = node.prev
        self._size -= 1
        return node.value

    def delete_head(self):
        if self.is_empty():
            raise IndexError("List is empty.")
        return self._unlink(self._head)

    def delete_tail(self):
        if self.is_empty():
            raise IndexError("List is empty.")
        return self._unlink(self._tail)

    def delete_at(self, index: int):
        return self._unlink(self._get_node(index))

    def delete_value(self, value) -> bool:
        current = self._head
        for _ in range(self._size):
            if current.value == value:
                self._unlink(current)
                return True
            current = current.next
        return False

    # Updates.
    def update(self, index: int, value) -> None:
        self._get_node(index).value = value

    # Structural operations.
    def rotate(self, k: int) -> None:
        if self._size <= 1:
            return
        k = k % self._size
        for _ in range(k):
            self._tail = self._head
            self._head = self._head.next

    def reverse(self) -> None:
        if self._size < 2:
            return
        current = self._head
        for _ in range(self._size):
            current.prev, current.next = current.next, current.prev
            current = current.prev
        self._head, self._tail = self._tail, self._head

    def sort(self) -> None:
        if self._size < 2:
            return
        swapped = True
        while swapped:
            swapped = False
            current = self._head
            for _ in range(self._size - 1):
                if current.value > current.next.value:
                    current.value, current.next.value = current.next.value, current.value
                    swapped = True
                current = current.next

    def split(self) -> tuple["DoublyCircularLinkedList", "DoublyCircularLinkedList"]:
        if self._size < 2:
            raise ValueError("Need at least 2 elements.")
        mid = self._size // 2
        first, second = DoublyCircularLinkedList(), DoublyCircularLinkedList()
        current = self._head
        for i in range(self._size):
            if i < mid:
                first.append(current.value)
            else:
                second.append(current.value)
            current = current.next
        return first, second

    def to_list(self) -> list:
        result, current = [], self._head
        for _ in range(self._size):
            result.append(current.value)
            current = current.next
        return result

    def to_list_reversed(self) -> list:
        result, current = [], self._tail
        for _ in range(self._size):
            result.append(current.value)
            current = current.prev
        return result

    @classmethod
    def from_list(cls, items: list) -> "DoublyCircularLinkedList":
        dcll = cls()
        for item in items:
            dcll.append(item)
        return dcll

    def display(self, label: str = "") -> None:
        if label:
            print(f"  {label}")
        if self.is_empty():
            print("  O (empty doubly circular list)")
            return
        vals = self.to_list()
        chain = " <-> ".join(f"[{v}]" for v in vals)
        print(f"  <> {chain} <>  (HEAD=[{vals[0]}], TAIL=[{vals[-1]}], length={self._size})")


def demo_sc_insertion() -> SinglyCircularLinkedList:
    title("1. SINGLY CIRCULAR - Insertion: append, prepend, insert_at")
    scll = SinglyCircularLinkedList()

    subtitle("1a. append()")
    for v in [20, 30, 40, 50]:
        scll.append(v)
        print(f"  append({v:2d})  ->  ", end="")
        scll.display()

    subtitle("1b. prepend()")
    scll.prepend(10)
    print("  prepend(10)  ->  ", end="")
    scll.display()

    subtitle("1c. insert_at(2, 99)")
    scll.insert_at(2, 99)
    print("  insert_at(2, 99)  ->  ", end="")
    scll.display()
    return scll


def demo_sc_deletion(scll: SinglyCircularLinkedList) -> SinglyCircularLinkedList:
    title("2. SINGLY CIRCULAR - Deletion: delete_head, delete_tail, delete_at, delete_value")
    scll.display("Before:")

    v = scll.delete_head()
    print(f"  delete_head() -> {v}")
    scll.display()

    v = scll.delete_tail()
    print(f"  delete_tail() -> {v}")
    scll.display()

    v = scll.delete_at(1)
    print(f"  delete_at(1)  -> {v}")
    scll.display()

    scll.delete_value(30)
    print("  delete_value(30):")
    scll.display()
    return scll


def demo_sc_search(scll: SinglyCircularLinkedList) -> None:
    title("3. SINGLY CIRCULAR - Search & Access: search, get, contains, count")
    scll2 = SinglyCircularLinkedList.from_list([10, 20, 30, 20, 40])
    scll2.display("List:")
    for val in [20, 40, 99]:
        print(f"  search({val:2d}) -> {scll2.search(val):2d}   contains -> {scll2.contains(val)}")
    print(f"  count(20)     -> {scll2.count(20)}")
    for i in [0, 2, scll2.length() - 1]:
        print(f"  get({i})       -> {scll2.get(i)}")


def demo_sc_structural() -> None:
    title("4. SINGLY CIRCULAR - Structural: rotate, reverse, sort, split")
    base = [1, 2, 3, 4, 5]

    subtitle("4a. rotate(k)")
    for k in [1, 2, -1]:
        scll = SinglyCircularLinkedList.from_list(base)
        scll.rotate(k)
        print(f"  rotate({k:+d}) -> {scll.to_list()}")

    subtitle("4b. reverse()")
    scll = SinglyCircularLinkedList.from_list(base)
    scll.display("Before reverse:")
    scll.reverse()
    scll.display("After reverse:")

    subtitle("4c. sort()")
    scll = SinglyCircularLinkedList.from_list([64, 25, 12, 22, 11])
    scll.display("Unsorted:")
    scll.sort()
    scll.display("Sorted:")

    subtitle("4d. split() into two halves")
    scll = SinglyCircularLinkedList.from_list([1, 2, 3, 4, 5, 6])
    scll.display("Original:")
    first, second = scll.split()
    first.display("First half:")
    second.display("Second half:")


def demo_dc_insertion() -> DoublyCircularLinkedList:
    title("5. DOUBLY CIRCULAR - Insertion: append, prepend, insert_at")
    dcll = DoublyCircularLinkedList()

    for v in [20, 30, 40, 50]:
        dcll.append(v)
        print(f"  append({v:2d})  ->  ", end="")
        dcll.display()

    dcll.prepend(10)
    print("  prepend(10)  ->  ", end="")
    dcll.display()

    dcll.insert_at(3, 777)
    print("  insert_at(3, 777)  ->  ", end="")
    dcll.display()
    return dcll


def demo_dc_deletion(dcll: DoublyCircularLinkedList) -> DoublyCircularLinkedList:
    title("6. DOUBLY CIRCULAR - Deletion: delete_head, delete_tail, delete_at, delete_value")
    dcll.display("Before:")

    v = dcll.delete_head()
    print(f"  delete_head() -> {v}")
    dcll.display()

    v = dcll.delete_tail()
    print(f"  delete_tail() -> {v}")
    dcll.display()

    v = dcll.delete_at(1)
    print(f"  delete_at(1)  -> {v}")
    dcll.display()

    dcll.delete_value(30)
    print("  delete_value(30):")
    dcll.display()
    return dcll


def demo_dc_structural() -> None:
    title("7. DOUBLY CIRCULAR - Structural: rotate, reverse, sort, split, to_list_reversed")
    base = [1, 2, 3, 4, 5]

    subtitle("7a. rotate(k) - forward and backward")
    for k in [2, -2]:
        dcll = DoublyCircularLinkedList.from_list(base)
        dcll.rotate(k)
        print(f"  rotate({k:+d}) -> {dcll.to_list()}")

    subtitle("7b. reverse()")
    dcll = DoublyCircularLinkedList.from_list(base)
    dcll.display("Before:")
    dcll.reverse()
    dcll.display("After reverse:")

    subtitle("7c. sort()")
    dcll = DoublyCircularLinkedList.from_list([7, 3, 9, 1, 5])
    dcll.display("Unsorted:")
    dcll.sort()
    dcll.display("Sorted:")
    print(f"  to_list_reversed() -> {dcll.to_list_reversed()}")

    subtitle("7d. split()")
    dcll = DoublyCircularLinkedList.from_list([10, 20, 30, 40, 50, 60])
    dcll.display("Original:")
    f, s = dcll.split()
    f.display("First half:")
    s.display("Second half:")


def demo_josephus() -> None:
    title("8. JOSEPHUS PROBLEM - Classic circular list application")
    print("  n people stand in a circle; every k-th person is eliminated.")
    print("  Last survivor wins.\n")

    def josephus(n: int, k: int) -> int:
        circle = SinglyCircularLinkedList.from_list(list(range(1, n + 1)))
        circle.display(f"  {n} people in a circle:")

        elimination_order = []
        idx = 0
        while circle.length() > 1:
            idx = (idx + k - 1) % circle.length()
            eliminated = circle.delete_at(idx)
            elimination_order.append(eliminated)
            if idx >= circle.length():
                idx = 0
        survivor = circle.get(0)

        print(f"\n  Elimination order (k={k}): {elimination_order}")
        print(f"  * Survivor: person #{survivor}")
        return survivor

    josephus(n=7, k=3)
    print()
    josephus(n=10, k=2)


def demo_practical() -> None:
    title("9. PRACTICAL EXAMPLE - Round-robin task scheduler")
    print("  Scenario: tasks rotate in a circular queue; each runs once per cycle.\n")

    tasks = DoublyCircularLinkedList.from_list(["render", "physics", "audio", "network", "input"])
    tasks.display("Task ring:")

    print("\n  Simulating 3 scheduling cycles:\n")
    current = tasks._head
    for cycle in range(1, 4):
        print(f"  [Cycle {cycle}]")
        ran = 0
        while True:
            print(f"    > Running: {current.value}")
            current = current.next
            ran += 1
            if ran == tasks.length():
                break
        print()


def main() -> None:
    print(f"\n{SEPARATOR}")
    print("  CIRCULAR LINKED LIST - Python 3.14")
    print("  A) Singly Circular   B) Doubly Circular")
    print(f"{SEPARATOR}")

    scll = demo_sc_insertion()
    scll = demo_sc_deletion(scll)
    demo_sc_search(scll)
    demo_sc_structural()

    dcll = demo_dc_insertion()
    dcll = demo_dc_deletion(dcll)
    demo_dc_structural()

    demo_josephus()
    demo_practical()

    title("OPERATION SUMMARY")
    print(f"  {'Operation':<22} {'Description':<32} {'Singly':<12} {'Doubly'}")
    print("  " + "-" * 72)
    ops = [
        ("append(v)", "Insert at tail",                "O(1)", "O(1)"),
        ("prepend(v)", "Insert at head",               "O(1)", "O(1)"),
        ("insert_at(i,v)", "Insert at index i",        "O(n)", "O(n)"),
        ("delete_head()", "Remove head",               "O(1)", "O(1)"),
        ("delete_tail()", "Remove tail",               "O(n)", "O(1)"),
        ("delete_at(i)", "Remove at index i",          "O(n)", "O(n)"),
        ("delete_value(v)", "Remove first occurrence", "O(n)", "O(n)"),
        ("get(i)", "Retrieve at index i",              "O(n)", "O(n/2)"),
        ("update(i,v)", "Replace at index i",          "O(n)", "O(n/2)"),
        ("search(v)", "First index of v",              "O(n)", "O(n)"),
        ("contains(v)", "Check existence",             "O(n)", "O(n)"),
        ("count(v)", "Count occurrences",              "O(n)", "O(n)"),
        ("rotate(k)", "Rotate ring k steps",           "O(k)", "O(k)"),
        ("reverse()", "Reverse the ring",              "O(n)", "O(n)"),
        ("sort()", "Sort ascending",                   "O(n^2)", "O(n^2)"),
        ("split()", "Split into two halves",           "O(n)", "O(n)"),
        ("to_list()", "Export forward",                "O(n)", "O(n)"),
        ("to_list_reversed()", "Export backward",      "-", "O(n)"),
        ("length()", "Number of nodes",                "O(1)", "O(1)"),
        ("is_empty()", "Check if empty",               "O(1)", "O(1)"),
    ]
    for op, desc, sc, dc in ops:
        print(f"  {op:<22} {desc:<32} {sc:<12} {dc}")

    print(f"\n{SEPARATOR}")
    print("  [OK] Circular Linked List - all operations demonstrated.")
    print(f"{SEPARATOR}\n")


if __name__ == "__main__":
    main()
