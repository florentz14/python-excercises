# -------------------------------------------------
# File Name: 16_singly_linked_list_full_operations.py
# Author: Florentino Baez
# Date: 2026-03-09
# Description: Singly linked list with full operation set and demos.
# -------------------------------------------------

"""
============================================================
  SINGLY LINKED LIST - Python 3.14
  Each node holds a value and a pointer to the NEXT node.
  The last node points to None.

    HEAD -> [10|*] -> [20|*] -> [30|*] -> [40|None]

  Operations covered:
    - append          -> Insert at the tail
    - prepend         -> Insert at the head
    - insert_at       -> Insert at a given index
    - delete_value    -> Remove first occurrence of a value
    - delete_at       -> Remove node at a given index
    - delete_head     -> Remove the head
    - delete_tail     -> Remove the tail
    - search          -> Find a value (returns index)
    - get             -> Retrieve value at index
    - update          -> Replace value at index
    - contains        -> Check if value exists
    - length          -> Number of nodes
    - is_empty        -> Check if list is empty
    - reverse         -> Reverse the list in-place
    - sort            -> Sort the list (bubble sort)
    - clear           -> Remove all nodes
    - to_list         -> Export as Python list
    - from_list       -> Build linked list from Python list
    - count           -> Count occurrences of a value
    - index_of        -> First index of a value
    - last_index_of   -> Last index of a value
    - merge           -> Merge two sorted linked lists
    - display         -> Print the list
============================================================
"""

SEPARATOR = "=" * 62


def title(text: str) -> None:
    print(f"\n{SEPARATOR}\n  {text}\n{SEPARATOR}")


def subtitle(text: str) -> None:
    print(f"\n  --- {text} ---")


class Node:
    """A single node in a singly linked list."""

    def __init__(self, value) -> None:
        self.value = value
        self.next: "Node | None" = None

    def __repr__(self) -> str:
        return f"Node({self.value})"


class SinglyLinkedList:
    """Singly linked list with a full set of operations."""

    def __init__(self) -> None:
        self._head: Node | None = None
        self._size: int = 0

    # Basic queries.
    def is_empty(self) -> bool:
        return self._head is None

    def length(self) -> int:
        return self._size

    def get(self, index: int):
        node = self._get_node(index)
        return node.value

    def _get_node(self, index: int) -> Node:
        if index < 0 or index >= self._size:
            raise IndexError(f"Index {index} out of range (size={self._size}).")
        current = self._head
        for _ in range(index):
            current = current.next
        return current

    def contains(self, value) -> bool:
        return self.search(value) != -1

    def search(self, value) -> int:
        current = self._head
        idx = 0
        while current:
            if current.value == value:
                return idx
            current = current.next
            idx += 1
        return -1

    def index_of(self, value) -> int:
        return self.search(value)

    def last_index_of(self, value) -> int:
        current = self._head
        idx = 0
        last = -1
        while current:
            if current.value == value:
                last = idx
            current = current.next
            idx += 1
        return last

    def count(self, value) -> int:
        current = self._head
        total = 0
        while current:
            if current.value == value:
                total += 1
            current = current.next
        return total

    # Insertions.
    def append(self, value) -> None:
        new_node = Node(value)
        if self.is_empty():
            self._head = new_node
        else:
            current = self._head
            while current.next:
                current = current.next
            current.next = new_node
        self._size += 1

    def prepend(self, value) -> None:
        new_node = Node(value)
        new_node.next = self._head
        self._head = new_node
        self._size += 1

    def insert_at(self, index: int, value) -> None:
        if index < 0 or index > self._size:
            raise IndexError(f"Index {index} out of range for insert (size={self._size}).")
        if index == 0:
            self.prepend(value)
            return
        new_node = Node(value)
        prev = self._get_node(index - 1)
        new_node.next = prev.next
        prev.next = new_node
        self._size += 1

    # Deletions.
    def delete_head(self):
        if self.is_empty():
            raise IndexError("Cannot delete from an empty list.")
        value = self._head.value
        self._head = self._head.next
        self._size -= 1
        return value

    def delete_tail(self):
        if self.is_empty():
            raise IndexError("Cannot delete from an empty list.")
        if self._size == 1:
            return self.delete_head()
        prev = self._get_node(self._size - 2)
        value = prev.next.value
        prev.next = None
        self._size -= 1
        return value

    def delete_at(self, index: int):
        if index == 0:
            return self.delete_head()
        prev = self._get_node(index - 1)
        if prev.next is None:
            raise IndexError(f"Index {index} out of range.")
        value = prev.next.value
        prev.next = prev.next.next
        self._size -= 1
        return value

    def delete_value(self, value) -> bool:
        if self.is_empty():
            return False
        if self._head.value == value:
            self.delete_head()
            return True
        current = self._head
        while current.next:
            if current.next.value == value:
                current.next = current.next.next
                self._size -= 1
                return True
            current = current.next
        return False

    def delete_all(self, value) -> int:
        removed = 0
        while self.delete_value(value):
            removed += 1
        return removed

    # Updates.
    def update(self, index: int, value) -> None:
        node = self._get_node(index)
        node.value = value

    # Structural operations.
    def reverse(self) -> None:
        prev = None
        current = self._head
        while current:
            nxt = current.next
            current.next = prev
            prev = current
            current = nxt
        self._head = prev

    def sort(self) -> None:
        if self._size < 2:
            return
        swapped = True
        while swapped:
            swapped = False
            current = self._head
            while current.next:
                if current.value > current.next.value:
                    current.value, current.next.value = current.next.value, current.value
                    swapped = True
                current = current.next

    def clear(self) -> None:
        self._head = None
        self._size = 0

    # Import/export.
    def to_list(self) -> list:
        result = []
        current = self._head
        while current:
            result.append(current.value)
            current = current.next
        return result

    @classmethod
    def from_list(cls, items: list) -> "SinglyLinkedList":
        sll = cls()
        for item in items:
            sll.append(item)
        return sll

    # Merge.
    @staticmethod
    def merge_sorted(a: "SinglyLinkedList", b: "SinglyLinkedList") -> "SinglyLinkedList":
        result = SinglyLinkedList()
        ca, cb = a._head, b._head
        while ca and cb:
            if ca.value <= cb.value:
                result.append(ca.value)
                ca = ca.next
            else:
                result.append(cb.value)
                cb = cb.next
        while ca:
            result.append(ca.value)
            ca = ca.next
        while cb:
            result.append(cb.value)
            cb = cb.next
        return result

    # Display.
    def display(self, label: str = "") -> None:
        if label:
            print(f"  {label}")
        if self.is_empty():
            print("  HEAD -> [None]  (empty list)")
            return
        current = self._head
        parts = []
        while current:
            parts.append(f"[{current.value}]")
            current = current.next
        chain = " -> ".join(parts)
        print(f"  HEAD -> {chain} -> None  (length={self._size})")

    def __repr__(self) -> str:
        return f"SinglyLinkedList({self.to_list()})"


def demo_insertion() -> SinglyLinkedList:
    title("1. INSERTION - append, prepend, insert_at")
    sll = SinglyLinkedList()

    subtitle("1a. append() - insert at tail")
    for v in [20, 30, 40, 50]:
        sll.append(v)
        print(f"  append({v:2d})  ->  ", end="")
        sll.display()

    subtitle("1b. prepend() - insert at head")
    sll.prepend(10)
    print("  prepend(10) ->  ", end="")
    sll.display()

    subtitle("1c. insert_at(index, value) - insert at position")
    sll.insert_at(2, 99)
    print("  insert_at(2, 99)  ->  ", end="")
    sll.display()
    sll.insert_at(0, 0)
    print("  insert_at(0,  0)  ->  ", end="")
    sll.display()
    sll.insert_at(sll.length(), 999)
    print("  insert_at(last, 999) ->  ", end="")
    sll.display()

    subtitle("1d. Out-of-range insert")
    try:
        sll.insert_at(100, 42)
    except IndexError as e:
        print(f"  IndexError: {e}")
    return sll


def demo_deletion(sll: SinglyLinkedList) -> SinglyLinkedList:
    title("2. DELETION - delete_head, delete_tail, delete_at, delete_value")
    sll.display("Before deletions:")

    subtitle("2a. delete_head()")
    v = sll.delete_head()
    print(f"  delete_head() -> removed: {v}")
    sll.display()

    subtitle("2b. delete_tail()")
    v = sll.delete_tail()
    print(f"  delete_tail() -> removed: {v}")
    sll.display()

    subtitle("2c. delete_at(index)")
    v = sll.delete_at(2)
    print(f"  delete_at(2)  -> removed: {v}")
    sll.display()

    subtitle("2d. delete_value(value) - removes first occurrence")
    sll.append(30)
    sll.append(30)
    sll.display("After appending two 30s:")
    ok = sll.delete_value(30)
    print(f"  delete_value(30) -> removed: {ok}")
    sll.display()

    subtitle("2e. delete_all(value) - removes every occurrence")
    count = sll.delete_all(30)
    print(f"  delete_all(30) -> {count} occurrence(s) removed")
    sll.display()

    subtitle("2f. delete from empty list -> error")
    empty = SinglyLinkedList()
    try:
        empty.delete_head()
    except IndexError as e:
        print(f"  IndexError: {e}")
    return sll


def demo_search_access(sll: SinglyLinkedList) -> None:
    title("3. SEARCH & ACCESS - search, get, contains, index_of, last_index_of, count")
    for v in [10, 20, 30, 40, 20, 50, 20]:
        sll.append(v)
    sll.display("List:")

    subtitle("3a. get(index) - retrieve by position")
    for i in [0, 3, sll.length() - 1]:
        print(f"  get({i}) -> {sll.get(i)}")
    try:
        sll.get(99)
    except IndexError as e:
        print(f"  IndexError: {e}")

    subtitle("3b. search(value) - index of first occurrence")
    for val in [20, 40, 99]:
        print(f"  search({val:2d}) -> {sll.search(val)}")

    subtitle("3c. contains(value)")
    for val in [30, 99]:
        print(f"  contains({val}) -> {sll.contains(val)}")

    subtitle("3d. index_of / last_index_of / count")
    print(f"  index_of(20)      -> {sll.index_of(20)}")
    print(f"  last_index_of(20) -> {sll.last_index_of(20)}")
    print(f"  count(20)         -> {sll.count(20)}")


def demo_update() -> None:
    title("4. UPDATE - Replace value at index")
    sll = SinglyLinkedList.from_list([10, 20, 30, 40, 50])
    sll.display("Before update:")
    sll.update(0, 100)
    sll.update(2, 300)
    sll.update(4, 500)
    sll.display("After update(0,100), update(2,300), update(4,500):")
    try:
        sll.update(99, 0)
    except IndexError as e:
        print(f"  IndexError: {e}")


def demo_reverse() -> None:
    title("5. REVERSE - Reverse list in-place")
    sll = SinglyLinkedList.from_list([1, 2, 3, 4, 5])
    sll.display("Original:")
    sll.reverse()
    sll.display("Reversed:")

    subtitle("Single element - trivial case")
    one = SinglyLinkedList.from_list([42])
    one.display("Before:")
    one.reverse()
    one.display("After:")


def demo_sort() -> None:
    title("6. SORT - Bubble sort ascending")
    sll = SinglyLinkedList.from_list([64, 25, 12, 22, 11])
    sll.display("Unsorted:")
    sll.sort()
    sll.display("Sorted:")

    subtitle("Already sorted")
    sll2 = SinglyLinkedList.from_list([1, 2, 3, 4, 5])
    sll2.display("Already sorted:")
    sll2.sort()
    sll2.display("After sort (no change):")

    subtitle("Reverse sorted")
    sll3 = SinglyLinkedList.from_list([5, 4, 3, 2, 1])
    sll3.display("Reverse sorted:")
    sll3.sort()
    sll3.display("After sort:")


def demo_clear() -> None:
    title("7. CLEAR - Remove all nodes")
    sll = SinglyLinkedList.from_list([1, 2, 3, 4, 5])
    sll.display("Before clear():")
    sll.clear()
    sll.display("After clear():")
    print(f"  is_empty() -> {sll.is_empty()}")
    print(f"  length()   -> {sll.length()}")


def demo_import_export() -> None:
    title("8. IMPORT / EXPORT - from_list & to_list")
    python_list = [10, 20, 30, 40, 50]
    print(f"  Python list:   {python_list}")
    sll = SinglyLinkedList.from_list(python_list)
    sll.display("Linked list:")
    exported = sll.to_list()
    print(f"  to_list()  ->   {exported}")
    print(f"  Round-trip OK: {python_list == exported}")


def demo_merge() -> None:
    title("9. MERGE - Merge two sorted linked lists")
    a = SinglyLinkedList.from_list([1, 3, 5, 7, 9])
    b = SinglyLinkedList.from_list([2, 4, 6, 8, 10])
    a.display("List A (sorted):")
    b.display("List B (sorted):")
    merged = SinglyLinkedList.merge_sorted(a, b)
    merged.display("Merged (sorted):")


def demo_practical() -> None:
    title("10. PRACTICAL EXAMPLE - Text editor line buffer")
    print("  Scenario: each node holds one line of text.\n")

    doc = SinglyLinkedList()
    for line in ["def hello():", "    pass"]:
        doc.append(line)
    doc.display("Initial document:")

    doc.insert_at(1, '    """Greet the user."""')
    doc.delete_value("    pass")
    doc.insert_at(1, '    print("Hello, World!")')
    doc.display("After edits:")

    subtitle("Navigate lines by index")
    for i in range(doc.length()):
        print(f"  Line {i}: {doc.get(i)}")


def main() -> None:
    print(f"\n{SEPARATOR}")
    print("  SINGLY LINKED LIST - Python 3.14")
    print(f"{SEPARATOR}")

    sll = demo_insertion()
    sll = demo_deletion(sll)
    demo_search_access(sll)
    demo_update()
    demo_reverse()
    demo_sort()
    demo_clear()
    demo_import_export()
    demo_merge()
    demo_practical()

    title("OPERATION SUMMARY")
    print(f"  {'Operation':<24} {'Description':<36} {'Time'}")
    print("  " + "-" * 66)
    ops = [
        ("append(v)", "Insert at tail",                    "O(n)"),
        ("prepend(v)", "Insert at head",                   "O(1)"),
        ("insert_at(i, v)", "Insert at index i",           "O(n)"),
        ("delete_head()", "Remove head",                   "O(1)"),
        ("delete_tail()", "Remove tail",                   "O(n)"),
        ("delete_at(i)", "Remove node at index i",         "O(n)"),
        ("delete_value(v)", "Remove first occurrence of v","O(n)"),
        ("delete_all(v)", "Remove all occurrences of v",   "O(n)"),
        ("get(i)", "Retrieve value at index i",            "O(n)"),
        ("update(i, v)", "Replace value at index i",       "O(n)"),
        ("search(v)", "First index of v",                  "O(n)"),
        ("last_index_of(v)", "Last index of v",            "O(n)"),
        ("count(v)", "Count occurrences of v",             "O(n)"),
        ("contains(v)", "Check if v exists",               "O(n)"),
        ("reverse()", "Reverse list in-place",             "O(n)"),
        ("sort()", "Sort ascending (bubble sort)",         "O(n^2)"),
        ("merge_sorted(a,b)", "Merge two sorted lists",    "O(n+m)"),
        ("clear()", "Remove all nodes",                    "O(1)"),
        ("to_list()", "Export to Python list",             "O(n)"),
        ("from_list(lst)", "Build from Python list",       "O(n)"),
        ("length()", "Number of nodes",                    "O(1)"),
        ("is_empty()", "Check if list is empty",           "O(1)"),
        ("display()", "Print the list",                    "O(n)"),
    ]
    for op, desc, tm in ops:
        print(f"  {op:<24} {desc:<36} {tm}")

    print(f"\n{SEPARATOR}")
    print("  [OK] Singly Linked List - all operations demonstrated.")
    print(f"{SEPARATOR}\n")


if __name__ == "__main__":
    main()
