# -------------------------------------------------
# File Name: 19_skip_list_full_operations.py
# Author: Florentino Baez
# Date: 2026-03-09
# Description: Skip list implementation with full operation demos.
# -------------------------------------------------

"""
============================================================
  SKIP LIST - Python 3.14
  A probabilistic data structure that allows fast search,
  insertion, and deletion in O(log n) expected time.

  Built on top of a linked-list idea but adds multiple
  "express lanes" (upper levels), allowing binary-search-like
  traversal over ordered values.

  Operations:
    - insert       -> Insert a value
    - delete       -> Remove a value
    - search       -> Find a value
    - contains     -> Check if value exists
    - get_min      -> Smallest value
    - get_max      -> Largest value
    - range_query  -> All values in [lo, hi]
    - rank         -> Position of a value
    - size         -> Number of elements
    - is_empty     -> Check if empty
    - clear        -> Remove all elements
    - to_list      -> Export sorted values
    - display      -> Print skip-list levels
============================================================
"""

import random

SEPARATOR = "=" * 64
MAX_LEVEL = 8
PROBABILITY = 0.5


def title(text: str) -> None:
    print(f"\n{SEPARATOR}\n  {text}\n{SEPARATOR}")


def subtitle(text: str) -> None:
    print(f"\n  --- {text} ---")


class SkipNode:
    """A node with multiple forward pointers."""

    def __init__(self, value, level: int) -> None:
        self.value = value
        self.forward: list["SkipNode | None"] = [None] * (level + 1)

    def __repr__(self) -> str:
        return f"SkipNode({self.value})"


class SkipList:
    """
    Ordered skip list with O(log n) expected search/insert/delete.
    Stores unique values by default (duplicates are ignored).
    """

    def __init__(
        self,
        max_level: int = MAX_LEVEL,
        probability: float = PROBABILITY,
        seed: int | None = None,
    ) -> None:
        self._max_level = max_level
        self._prob = probability
        self._level = 0
        self._size = 0
        # Sentinel head node conceptually represents -infinity.
        self._head = SkipNode(None, max_level)
        if seed is not None:
            random.seed(seed)

    # Internal helpers.
    def _random_level(self) -> int:
        """Choose level for a new node using geometric probability."""
        lvl = 0
        while random.random() < self._prob and lvl < self._max_level:
            lvl += 1
        return lvl

    def _find_update(self, value) -> list:
        """
        For each level, find the rightmost node with node.value < value.
        These predecessors are where pointers may change on insert/delete.
        """
        update = [None] * (self._max_level + 1)
        current = self._head
        for i in range(self._level, -1, -1):
            while current.forward[i] and current.forward[i].value < value:
                current = current.forward[i]
            update[i] = current
        return update

    # Queries.
    def is_empty(self) -> bool:
        return self._size == 0

    def size(self) -> int:
        return self._size

    def contains(self, value) -> bool:
        current = self._head
        for i in range(self._level, -1, -1):
            while current.forward[i] and current.forward[i].value < value:
                current = current.forward[i]
        current = current.forward[0]
        return current is not None and current.value == value

    def search(self, value) -> bool:
        return self.contains(value)

    def get_min(self):
        if self.is_empty():
            raise ValueError("Skip list is empty.")
        return self._head.forward[0].value

    def get_max(self):
        if self.is_empty():
            raise ValueError("Skip list is empty.")
        current = self._head
        while current.forward[0]:
            current = current.forward[0]
        return current.value

    def range_query(self, lo, hi) -> list:
        result = []
        current = self._head
        for i in range(self._level, -1, -1):
            while current.forward[i] and current.forward[i].value < lo:
                current = current.forward[i]
        current = current.forward[0]
        while current and current.value <= hi:
            result.append(current.value)
            current = current.forward[0]
        return result

    def rank(self, value) -> int:
        """Return 0-based position in sorted order, or -1 if missing."""
        pos = 0
        current = self._head.forward[0]
        while current:
            if current.value == value:
                return pos
            pos += 1
            current = current.forward[0]
        return -1

    # Insertions.
    def insert(self, value) -> bool:
        update = self._find_update(value)
        current = update[0].forward[0]
        if current and current.value == value:
            return False

        new_level = self._random_level()
        if new_level > self._level:
            for i in range(self._level + 1, new_level + 1):
                update[i] = self._head
            self._level = new_level

        new_node = SkipNode(value, new_level)
        for i in range(new_level + 1):
            new_node.forward[i] = update[i].forward[i]
            update[i].forward[i] = new_node

        self._size += 1
        return True

    def insert_many(self, values) -> int:
        return sum(1 for v in values if self.insert(v))

    # Deletions.
    def delete(self, value) -> bool:
        update = self._find_update(value)
        current = update[0].forward[0]
        if current is None or current.value != value:
            return False

        for i in range(self._level + 1):
            if update[i].forward[i] is not current:
                break
            update[i].forward[i] = current.forward[i]

        while self._level > 0 and self._head.forward[self._level] is None:
            self._level -= 1

        self._size -= 1
        return True

    def clear(self) -> None:
        self._head = SkipNode(None, self._max_level)
        self._level = 0
        self._size = 0

    # Export.
    def to_list(self) -> list:
        result = []
        current = self._head.forward[0]
        while current:
            result.append(current.value)
            current = current.forward[0]
        return result

    # Display.
    def display(self, label: str = "Skip List") -> None:
        print(f"\n  {label}  (size={self._size}, active levels={self._level + 1})")
        if self.is_empty():
            print("  (empty)")
            return

        all_vals = self.to_list()
        col_w = max(len(str(v)) for v in all_vals) + 2

        for lvl in range(self._level, -1, -1):
            row = f"  L{lvl} | HEAD "
            lvl_ptr = self._head.forward[lvl]
            for val in all_vals:
                if lvl_ptr and lvl_ptr.value == val:
                    row += f"{'-' * (col_w - len(str(val)) - 1)}[{val}]"
                    lvl_ptr = lvl_ptr.forward[lvl]
                else:
                    row += "-" * col_w
            row += "-> None"
            print(row)
        print(f"  {'-' * 4}+{'-' * (8 + len(all_vals) * col_w + 8)}")

    def __repr__(self) -> str:
        return f"SkipList({self.to_list()})"


def demo_insert() -> SkipList:
    title("1. INSERT - Add values in O(log n) expected time")
    sl = SkipList(max_level=4, seed=42)

    subtitle("1a. Inserting individual values")
    for v in [30, 10, 50, 20, 40, 5, 45, 25]:
        inserted = sl.insert(v)
        print(f"  insert({v:2d}) -> {'inserted [OK]' if inserted else 'duplicate, skipped'}")

    sl.display("After insertions:")

    subtitle("1b. insert_many() - batch insertion")
    sl2 = SkipList(max_level=4, seed=7)
    vals = [8, 3, 12, 1, 6, 10, 14, 4, 7, 13]
    count = sl2.insert_many(vals)
    print(f"  insert_many({vals})")
    print(f"  -> {count} values inserted")
    sl2.display("Resulting skip list:")

    subtitle("1c. Duplicate insertion is ignored")
    print(f"  insert(30) again -> {sl.insert(30)}")
    print(f"  insert(10) again -> {sl.insert(10)}")
    return sl


def demo_search(sl: SkipList) -> None:
    title("2. SEARCH & CONTAINS - O(log n) lookup")
    sl.display("Skip list:")

    subtitle("2a. contains(value) / search(value)")
    for val in [30, 45, 99, 5, 50]:
        print(f"  contains({val:2d}) -> {sl.contains(val)}")

    subtitle("2b. get_min() and get_max()")
    print(f"  get_min() -> {sl.get_min()}")
    print(f"  get_max() -> {sl.get_max()}")


def demo_range_query(sl: SkipList) -> None:
    title("3. RANGE QUERY - All values in [lo, hi]")
    sl.display("Skip list:")
    for lo, hi in [(10, 35), (1, 50), (25, 25), (60, 99)]:
        result = sl.range_query(lo, hi)
        print(f"  range_query({lo:2d}, {hi:2d}) -> {result}")


def demo_rank(sl: SkipList) -> None:
    title("4. RANK - Position (0-based) of a value")
    sl.display("Skip list:")
    for val in [5, 10, 25, 45, 50, 99]:
        r = sl.rank(val)
        suffix = "  (not found)" if r == -1 else ""
        print(f"  rank({val:2d}) -> {r:2d}{suffix}")


def demo_delete(sl: SkipList) -> SkipList:
    title("5. DELETE - Remove values in O(log n) expected time")
    print(f"  Before: {sl.to_list()}")
    sl.display()

    subtitle("5a. Deleting existing values")
    for v in [10, 30, 50]:
        removed = sl.delete(v)
        print(f"  delete({v:2d}) -> {'removed [OK]' if removed else 'not found'}")

    sl.display("After deletions:")

    subtitle("5b. Deleting a non-existing value")
    print(f"  delete(99) -> {sl.delete(99)}")

    subtitle("5c. Delete all remaining values")
    remaining = sl.to_list()[:]
    for v in remaining:
        sl.delete(v)
    sl.display("Empty skip list:")
    print(f"  is_empty() -> {sl.is_empty()}")
    return sl


def demo_clear() -> None:
    title("6. CLEAR - Remove all elements in O(1)")
    sl = SkipList(seed=1)
    sl.insert_many([5, 10, 15, 20, 25])
    sl.display("Before clear():")
    sl.clear()
    sl.display("After clear():")
    print(f"  is_empty() -> {sl.is_empty()}")
    print(f"  size()     -> {sl.size()}")


def demo_performance() -> None:
    title("7. PERFORMANCE - Level occupancy view")
    print("  Promotion probability p=0.5, max_level=8\n")

    random.seed(0)
    sl = SkipList(max_level=8, probability=0.5)
    sl.insert_many(list(range(1, 33)))
    sl.display("32-element skip list:")

    print("\n  Level occupancy:")
    for lvl in range(sl._level + 1):
        count = 0
        node = sl._head.forward[lvl]
        while node:
            count += 1
            node = node.forward[lvl]
        bar = "#" * count
        print(f"  L{lvl}: {bar}  ({count} nodes)")


def demo_to_list() -> None:
    title("8. TO_LIST - Export values in sorted order")
    sl = SkipList(seed=5)
    unsorted = [42, 7, 19, 3, 55, 11, 28]
    sl.insert_many(unsorted)
    print(f"  Inserted (unordered): {unsorted}")
    print(f"  to_list() (sorted)  : {sl.to_list()}")


def demo_practical() -> None:
    title("9. PRACTICAL EXAMPLE - Sorted leaderboard")
    print("  Skip list stores scores; search/delete in O(log n).\n")

    board = SkipList(max_level=4, seed=99)
    players = {
        "Alice": 8500,
        "Bob": 7200,
        "Carol": 9100,
        "Dave": 6800,
        "Eve": 9100,
        "Frank": 7850,
    }

    subtitle("9a. Inserting scores")
    for name, score in players.items():
        board.insert(score)
        print(f"  {name:6s}: {score}")

    board.display("\n  Leaderboard (unique scores):")

    subtitle("9b. Range query [7000, 9000]")
    top_scores = board.range_query(7000, 9000)
    print(f"  Scores in [7000, 9000]: {top_scores}")

    subtitle("9c. Fast exact score lookup")
    print(f"  contains(9100) -> {board.contains(9100)}")
    print(f"  contains(8000) -> {board.contains(8000)}")

    subtitle("9d. Remove a score")
    board.delete(6800)
    print("  delete(6800) -> removed")
    board.display("Updated leaderboard:")


def main() -> None:
    print(f"\n{SEPARATOR}")
    print("  SKIP LIST - Python 3.14")
    print(f"{SEPARATOR}")

    sl = demo_insert()
    demo_search(sl)
    demo_range_query(sl)
    demo_rank(sl)
    sl = demo_delete(sl)
    demo_clear()
    demo_performance()
    demo_to_list()
    demo_practical()

    title("OPERATION SUMMARY")
    print(f"  {'Operation':<24} {'Description':<36} {'Expected Time'}")
    print("  " + "-" * 70)
    ops = [
        ("insert(v)", "Insert value (unique)",           "O(log n)"),
        ("insert_many(vals)", "Batch insert",            "O(k log n)"),
        ("delete(v)", "Remove value",                    "O(log n)"),
        ("contains(v)", "Check existence",               "O(log n)"),
        ("search(v)", "Check existence (alias)",         "O(log n)"),
        ("get_min()", "Smallest value",                  "O(1)"),
        ("get_max()", "Largest value",                   "O(n)"),
        ("range_query(lo,hi)", "All values in [lo, hi]", "O(log n + k)"),
        ("rank(v)", "0-based position of v",             "O(n)"),
        ("size()", "Number of elements",                 "O(1)"),
        ("is_empty()", "Check if empty",                 "O(1)"),
        ("clear()", "Remove all elements",               "O(1)"),
        ("to_list()", "Export sorted values",            "O(n)"),
        ("display()", "Print multi-level structure",     "O(n * L)"),
    ]
    for op, desc, tm in ops:
        print(f"  {op:<24} {desc:<36} {tm}")

    print("\n  Space complexity: O(n log n) expected")
    print(f"\n{SEPARATOR}")
    print("  [OK] Skip List - all operations demonstrated.")
    print(f"{SEPARATOR}\n")


if __name__ == "__main__":
    main()
