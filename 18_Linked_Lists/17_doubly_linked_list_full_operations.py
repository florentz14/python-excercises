# -------------------------------------------------
# File Name: 17_doubly_linked_list_full_operations.py
# Author: Florentino Baez
# Date: 2026-03-09
# Description: Doubly linked list with full operation set and demos.
# -------------------------------------------------

"""
============================================================
  DOUBLY LINKED LIST - Python 3.14
  Each node holds a value, a pointer to the NEXT node,
  and a pointer to the PREVIOUS node.

  None <- [10|*|*] <-> [20|*|*] <-> [30|*|*] <-> [40|None]
          HEAD                                  TAIL

  Advantages over singly linked list:
    - O(1) delete_tail (no full traversal needed)
    - Bidirectional traversal
    - Easier insertion/deletion with node references

  Operations covered:
    - append           -> Insert at tail              O(1)
    - prepend          -> Insert at head              O(1)
    - insert_at        -> Insert at index             O(n)
    - insert_before    -> Insert before a value       O(n)
    - insert_after     -> Insert after a value        O(n)
    - delete_head      -> Remove head                 O(1)
    - delete_tail      -> Remove tail                 O(1)
    - delete_at        -> Remove at index             O(n)
    - delete_value     -> Remove first occurrence     O(n)
    - delete_all       -> Remove all occurrences      O(n)
    - get              -> Retrieve value at index     O(n)
    - update           -> Replace value at index      O(n)
    - search           -> First index of value        O(n)
    - search_backward  -> Search from tail            O(n)
    - contains         -> Check existence             O(n)
    - count            -> Count occurrences           O(n)
    - reverse          -> Reverse in-place            O(n)
    - sort             -> Sort ascending              O(n^2)
    - rotate           -> Rotate k positions          O(n)
    - to_list          -> Export forward              O(n)
    - to_list_reversed -> Export backward             O(n)
    - merge_sorted     -> Merge two sorted lists      O(n+m)
    - clear            -> Remove all nodes            O(1)
    - length / is_empty
    - display / display_backward
============================================================
"""

SEPARATOR = "=" * 64


def title(text: str) -> None:
    print(f"\n{SEPARATOR}\n  {text}\n{SEPARATOR}")


def subtitle(text: str) -> None:
    print(f"\n  --- {text} ---")


class Node:
    """A single node in a doubly linked list."""

    def __init__(self, value) -> None:
        self.value = value
        self.prev: "Node | None" = None
        self.next: "Node | None" = None

    def __repr__(self) -> str:
        return f"Node({self.value})"


class DoublyLinkedList:
    """Doubly linked list with full set of operations."""

    def __init__(self) -> None:
        self._head: Node | None = None
        self._tail: Node | None = None
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
        # Start from nearest end for fewer hops.
        if index <= self._size // 2:
            current = self._head
            for _ in range(index):
                current = current.next
        else:
            current = self._tail
            for _ in range(self._size - 1 - index):
                current = current.prev
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

    def search_backward(self, value) -> int:
        current = self._tail
        idx = self._size - 1
        while current:
            if current.value == value:
                return idx
            current = current.prev
            idx -= 1
        return -1

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
        node = Node(value)
        if self.is_empty():
            self._head = self._tail = node
        else:
            node.prev = self._tail
            self._tail.next = node
            self._tail = node
        self._size += 1

    def prepend(self, value) -> None:
        node = Node(value)
        if self.is_empty():
            self._head = self._tail = node
        else:
            node.next = self._head
            self._head.prev = node
            self._head = node
        self._size += 1

    def insert_at(self, index: int, value) -> None:
        if index < 0 or index > self._size:
            raise IndexError(f"Index {index} out of range for insert.")
        if index == 0:
            self.prepend(value)
            return
        if index == self._size:
            self.append(value)
            return
        node = Node(value)
        after = self._get_node(index)
        before = after.prev
        node.prev = before
        node.next = after
        before.next = node
        after.prev = node
        self._size += 1

    def insert_before(self, target, value) -> bool:
        current = self._head
        while current:
            if current.value == target:
                node = Node(value)
                node.next = current
                node.prev = current.prev
                if current.prev:
                    current.prev.next = node
                else:
                    self._head = node
                current.prev = node
                self._size += 1
                return True
            current = current.next
        return False

    def insert_after(self, target, value) -> bool:
        current = self._head
        while current:
            if current.value == target:
                node = Node(value)
                node.prev = current
                node.next = current.next
                if current.next:
                    current.next.prev = node
                else:
                    self._tail = node
                current.next = node
                self._size += 1
                return True
            current = current.next
        return False

    # Deletions.
    def _unlink(self, node: Node):
        if node.prev:
            node.prev.next = node.next
        else:
            self._head = node.next
        if node.next:
            node.next.prev = node.prev
        else:
            self._tail = node.prev
        node.prev = node.next = None
        self._size -= 1
        return node.value

    def delete_head(self):
        if self.is_empty():
            raise IndexError("Cannot delete from an empty list.")
        return self._unlink(self._head)

    def delete_tail(self):
        if self.is_empty():
            raise IndexError("Cannot delete from an empty list.")
        return self._unlink(self._tail)

    def delete_at(self, index: int):
        node = self._get_node(index)
        return self._unlink(node)

    def delete_value(self, value) -> bool:
        current = self._head
        while current:
            if current.value == value:
                self._unlink(current)
                return True
            current = current.next
        return False

    def delete_all(self, value) -> int:
        removed = 0
        current = self._head
        while current:
            nxt = current.next
            if current.value == value:
                self._unlink(current)
                removed += 1
            current = nxt
        return removed

    # Updates.
    def update(self, index: int, value) -> None:
        self._get_node(index).value = value

    # Structural operations.
    def reverse(self) -> None:
        current = self._head
        while current:
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
            while current and current.next:
                if current.value > current.next.value:
                    current.value, current.next.value = current.next.value, current.value
                    swapped = True
                current = current.next

    def rotate(self, k: int) -> None:
        """Rotate right by k (k<0 works as left rotation)."""
        if self._size <= 1 or k == 0:
            return
        k = k % self._size
        if k == 0:
            return
        new_tail = self._get_node(self._size - k - 1)
        new_head = new_tail.next

        self._tail.next = self._head
        self._head.prev = self._tail
        new_tail.next = None
        new_head.prev = None
        self._head = new_head
        self._tail = new_tail

    def clear(self) -> None:
        self._head = self._tail = None
        self._size = 0

    # Import/export.
    def to_list(self) -> list:
        result = []
        current = self._head
        while current:
            result.append(current.value)
            current = current.next
        return result

    def to_list_reversed(self) -> list:
        result = []
        current = self._tail
        while current:
            result.append(current.value)
            current = current.prev
        return result

    @classmethod
    def from_list(cls, items: list) -> "DoublyLinkedList":
        dll = cls()
        for item in items:
            dll.append(item)
        return dll

    # Merge.
    @staticmethod
    def merge_sorted(a: "DoublyLinkedList", b: "DoublyLinkedList") -> "DoublyLinkedList":
        result = DoublyLinkedList()
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
            print("  HEAD <-> [None]  (empty list)")
            return
        parts = [f"[{n.value}]" for n in self._iter_nodes()]
        print(f"  HEAD <-> {' <-> '.join(parts)} <-> TAIL  (length={self._size})")

    def display_backward(self, label: str = "") -> None:
        if label:
            print(f"  {label}")
        if self.is_empty():
            print("  TAIL <-> [None]  (empty list)")
            return
        current = self._tail
        parts = []
        while current:
            parts.append(f"[{current.value}]")
            current = current.prev
        print(f"  TAIL <-> {' <-> '.join(parts)} <-> HEAD")

    def _iter_nodes(self):
        current = self._head
        while current:
            yield current
            current = current.next

    def __repr__(self) -> str:
        return f"DoublyLinkedList({self.to_list()})"


def demo_insertion() -> DoublyLinkedList:
    title("1. INSERTION - append, prepend, insert_at, insert_before, insert_after")
    dll = DoublyLinkedList()

    subtitle("1a. append() - O(1) insert at tail")
    for v in [20, 30, 40, 50]:
        dll.append(v)
        print(f"  append({v:2d})  ->  ", end="")
        dll.display()

    subtitle("1b. prepend() - O(1) insert at head")
    dll.prepend(10)
    print("  prepend(10)  ->  ", end="")
    dll.display()

    subtitle("1c. insert_at(index, value)")
    dll.insert_at(2, 999)
    print("  insert_at(2, 999)  ->  ", end="")
    dll.display()

    subtitle("1d. insert_before(target, value)")
    ok = dll.insert_before(30, 25)
    print(f"  insert_before(30, 25) -> {'inserted' if ok else 'target not found'}")
    dll.display()

    subtitle("1e. insert_after(target, value)")
    ok = dll.insert_after(40, 45)
    print(f"  insert_after(40, 45) -> {'inserted' if ok else 'target not found'}")
    dll.display()
    return dll


def demo_deletion(dll: DoublyLinkedList) -> DoublyLinkedList:
    title("2. DELETION - delete_head, delete_tail, delete_at, delete_value, delete_all")
    dll.display("Before deletions:")

    subtitle("2a. delete_head() - O(1)")
    v = dll.delete_head()
    print(f"  delete_head() -> removed: {v}")
    dll.display()

    subtitle("2b. delete_tail() - O(1) (key doubly-linked advantage)")
    v = dll.delete_tail()
    print(f"  delete_tail() -> removed: {v}")
    dll.display()

    subtitle("2c. delete_at(index)")
    v = dll.delete_at(1)
    print(f"  delete_at(1)  -> removed: {v}")
    dll.display()

    subtitle("2d. delete_value(value) - first occurrence")
    dll.append(30)
    dll.append(30)
    dll.display("After appending two extra 30s:")
    dll.delete_value(30)
    print("  delete_value(30) - first 30 removed:")
    dll.display()

    subtitle("2e. delete_all(value)")
    n = dll.delete_all(30)
    print(f"  delete_all(30) -> {n} node(s) removed")
    dll.display()
    return dll


def demo_search_access(dll: DoublyLinkedList) -> None:
    title("3. SEARCH & ACCESS - search, search_backward, get, contains, count")
    dll2 = DoublyLinkedList.from_list([10, 20, 30, 20, 40, 20, 50])
    dll2.display("List:")

    subtitle("3a. get(index) - from nearest end")
    for i in [0, 3, dll2.length() - 1]:
        print(f"  get({i}) -> {dll2.get(i)}")

    subtitle("3b. search() forward / search_backward()")
    for val in [20, 40, 99]:
        fwd = dll2.search(val)
        bwd = dll2.search_backward(val)
        print(f"  search({val:2d}) fwd-> {fwd:2d}   search_backward({val:2d}) bwd-> {bwd:2d}")

    subtitle("3c. contains / count")
    for val in [20, 99]:
        print(f"  contains({val:2d}) -> {dll2.contains(val)}   count({val:2d}) -> {dll2.count(val)}")


def demo_update() -> None:
    title("4. UPDATE - Replace value at index")
    dll = DoublyLinkedList.from_list([1, 2, 3, 4, 5])
    dll.display("Before:")
    for i, v in [(0, 10), (2, 30), (4, 50)]:
        dll.update(i, v)
    dll.display("After update(0,10), update(2,30), update(4,50):")


def demo_bidirectional() -> None:
    title("5. BIDIRECTIONAL TRAVERSAL - forward and backward display")
    dll = DoublyLinkedList.from_list([10, 20, 30, 40, 50])
    dll.display("Forward  (HEAD -> TAIL):")
    dll.display_backward("Backward (TAIL -> HEAD):")

    subtitle("to_list() vs to_list_reversed()")
    print(f"  to_list()          -> {dll.to_list()}")
    print(f"  to_list_reversed() -> {dll.to_list_reversed()}")


def demo_reverse() -> None:
    title("6. REVERSE - Reverse in-place by swapping pointers")
    dll = DoublyLinkedList.from_list([1, 2, 3, 4, 5])
    dll.display("Before:")
    dll.reverse()
    dll.display("After reverse():")
    dll.display_backward("Backward confirm:")


def demo_sort() -> None:
    title("7. SORT - Bubble sort ascending (swap values)")
    dll = DoublyLinkedList.from_list([64, 25, 12, 22, 11, 90])
    dll.display("Unsorted:")
    dll.sort()
    dll.display("Sorted:")
    dll.display_backward("Backward (descending view):")


def demo_rotate() -> None:
    title("8. ROTATE - Rotate list k steps to the right")
    base = [1, 2, 3, 4, 5]
    for k in [1, 2, -1, 5]:
        dll = DoublyLinkedList.from_list(base)
        dll.rotate(k)
        print(f"  rotate({k:+d}) -> {dll.to_list()}")


def demo_merge() -> None:
    title("9. MERGE - Merge two sorted doubly linked lists")
    a = DoublyLinkedList.from_list([1, 3, 5, 9])
    b = DoublyLinkedList.from_list([2, 4, 6, 7, 8])
    a.display("List A:")
    b.display("List B:")
    merged = DoublyLinkedList.merge_sorted(a, b)
    merged.display("Merged:")
    merged.display_backward("Merged backward:")


def demo_practical() -> None:
    title("10. PRACTICAL EXAMPLE - Browser history (back/forward navigation)")
    print("  Each node is a URL. Navigate backward and forward.\n")

    history = DoublyLinkedList()
    current_node = None

    def visit(url: str) -> None:
        nonlocal current_node
        history.append(url)
        current_node = history._tail
        print(f"  -> Visited: {url}")

    def go_back() -> str | None:
        nonlocal current_node
        if current_node and current_node.prev:
            current_node = current_node.prev
            print(f"  <- Back to: {current_node.value}")
            return current_node.value
        print("  <- No previous page.")
        return None

    def go_forward() -> str | None:
        nonlocal current_node
        if current_node and current_node.next:
            current_node = current_node.next
            print(f"  -> Forward to: {current_node.value}")
            return current_node.value
        print("  -> No next page.")
        return None

    visit("home.com")
    visit("news.com")
    visit("sports.com")
    visit("tech.com")

    history.display("\n  Full history:")
    print(f"  Current page: {current_node.value}\n")

    go_back()
    go_back()
    go_forward()
    go_forward()
    go_forward()


def main() -> None:
    print(f"\n{SEPARATOR}")
    print("  DOUBLY LINKED LIST - Python 3.14")
    print(f"{SEPARATOR}")

    dll = demo_insertion()
    dll = demo_deletion(dll)
    demo_search_access(dll)
    demo_update()
    demo_bidirectional()
    demo_reverse()
    demo_sort()
    demo_rotate()
    demo_merge()
    demo_practical()

    title("OPERATION SUMMARY")
    print(f"  {'Operation':<26} {'Description':<36} {'Time'}")
    print("  " + "-" * 68)
    ops = [
        ("append(v)", "Insert at tail",                    "O(1)"),
        ("prepend(v)", "Insert at head",                   "O(1)"),
        ("insert_at(i, v)", "Insert at index i",           "O(n)"),
        ("insert_before(t, v)", "Insert before first t",   "O(n)"),
        ("insert_after(t, v)", "Insert after first t",     "O(n)"),
        ("delete_head()", "Remove head",                   "O(1)"),
        ("delete_tail()", "Remove tail",                   "O(1)"),
        ("delete_at(i)", "Remove at index i",              "O(n)"),
        ("delete_value(v)", "Remove first occurrence",     "O(n)"),
        ("delete_all(v)", "Remove all occurrences",        "O(n)"),
        ("get(i)", "Retrieve value at index i",            "O(n)"),
        ("update(i, v)", "Replace value at index i",       "O(n)"),
        ("search(v)", "First index (forward)",             "O(n)"),
        ("search_backward(v)", "First index (from tail)",  "O(n)"),
        ("count(v)", "Count occurrences",                  "O(n)"),
        ("contains(v)", "Check existence",                 "O(n)"),
        ("reverse()", "Reverse in-place",                  "O(n)"),
        ("sort()", "Sort ascending",                       "O(n^2)"),
        ("rotate(k)", "Rotate k steps right",              "O(n)"),
        ("merge_sorted(a,b)", "Merge two sorted lists",    "O(n+m)"),
        ("to_list()", "Forward export",                    "O(n)"),
        ("to_list_reversed()", "Backward export",          "O(n)"),
        ("clear()", "Remove all nodes",                    "O(1)"),
        ("length()", "Number of nodes",                    "O(1)"),
        ("is_empty()", "Check if empty",                   "O(1)"),
    ]
    for op, desc, tm in ops:
        print(f"  {op:<26} {desc:<36} {tm}")

    print(f"\n{SEPARATOR}")
    print("  [OK] Doubly Linked List - all operations demonstrated.")
    print(f"{SEPARATOR}\n")


if __name__ == "__main__":
    main()
