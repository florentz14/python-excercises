# -------------------------------------------------
# File Name: 19_priority_stack.py
# Author: Florentino Baez
# Date: 2026-03-09
# Description: Priority stack with heap and sorted-list variants.
# -------------------------------------------------

"""
============================================================
  PRIORITY STACK - Python 3.14
  Combines LIFO behavior with priorities: pop removes the
  highest-priority element; ties are resolved by LIFO
  (latest inserted first inside the same priority level).

  Two implementations:
    A) Max-Heap       -> pop O(log n), push O(log n)
    B) Sorted List    -> pop O(1), push O(n)

  Operations:
    - push            -> Insert with priority
    - pop             -> Remove highest priority
    - peek            -> View highest priority
    - pop_by_level    -> Remove all at one priority
    - push_many       -> Insert multiple items
    - change_priority -> Change element priority
    - remove          -> Remove specific element
    - contains        -> Search element
    - get_priority    -> Read priority of a value
    - is_empty        -> Is empty?
    - size            -> Current size
    - clear           -> Empty stack
    - merge           -> Merge two priority stacks
    - to_sorted_list  -> Export sorted by priority
    - display         -> Show grouped by priority levels
============================================================
"""

SEPARATOR = "=" * 60


def title(text: str) -> None:
    print(f"\n{SEPARATOR}\n  {text}\n{SEPARATOR}")


def subtitle(text: str) -> None:
    print(f"\n  --- {text} ---")


# Implementation A: max-heap priority stack.
class PriorityStack:
    """
    Max-heap based priority stack.
    Stored tuple: (priority, lifo_seq, value).
    Higher priority first; tie -> larger lifo_seq first.
    """

    def __init__(self) -> None:
        self._heap: list[tuple] = []
        self._seq: int = 0

    # Heap helper methods.
    def _key(self, i: int) -> tuple:
        pri, seq, _ = self._heap[i]
        return (pri, seq)

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
            largest = i
            left, right = 2 * i + 1, 2 * i + 2
            if left < n and self._key(left) > self._key(largest):
                largest = left
            if right < n and self._key(right) > self._key(largest):
                largest = right
            if largest == i:
                break
            self._heap[i], self._heap[largest] = self._heap[largest], self._heap[i]
            i = largest

    # Query methods.
    def is_empty(self) -> bool:
        return not self._heap

    def size(self) -> int:
        return len(self._heap)

    def peek(self) -> tuple:
        if self.is_empty():
            raise IndexError("Priority stack is empty.")
        pri, _, val = self._heap[0]
        return (pri, val)

    def contains(self, value) -> bool:
        return any(v == value for _, _, v in self._heap)

    def get_priority(self, value) -> int | None:
        for pri, _, v in self._heap:
            if v == value:
                return pri
        return None

    def to_sorted_list(self) -> list[tuple]:
        return [(p, v) for p, _, v in sorted(self._heap, key=lambda x: (-x[0], -x[1]))]

    # Modification methods.
    def push(self, value, priority: int) -> None:
        self._heap.append((priority, self._seq, value))
        self._seq += 1
        self._sift_up(len(self._heap) - 1)

    def push_many(self, items: list[tuple]) -> None:
        for value, pri in items:
            self.push(value, pri)

    def pop(self) -> tuple:
        if self.is_empty():
            raise IndexError("Priority stack is empty.")
        self._heap[0], self._heap[-1] = self._heap[-1], self._heap[0]
        pri, _, val = self._heap.pop()
        if self._heap:
            self._sift_down(0)
        return (pri, val)

    def pop_by_level(self, priority: int) -> list:
        """Remove all elements of one priority level."""
        removed = []
        temp = PriorityStack()
        all_items = []
        while not self.is_empty():
            all_items.append(self.pop())
        for pri, val in all_items:
            if pri == priority:
                removed.append((pri, val))
            else:
                temp.push(val, pri)
        while not temp.is_empty():
            p, v = temp.pop()
            self.push(v, p)
        return removed

    def change_priority(self, value, new_priority: int) -> bool:
        for i, (pri, seq, v) in enumerate(self._heap):
            if v == value:
                old = pri
                self._heap[i] = (new_priority, seq, v)
                if new_priority > old:
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
        self._seq = 0

    def merge(self, other: "PriorityStack") -> "PriorityStack":
        merged = PriorityStack()
        for pri, _, val in self._heap:
            merged.push(val, pri)
        for pri, _, val in other._heap:
            merged.push(val, pri)
        return merged

    # Display helpers.
    def display(self, name: str = "PriorityStack") -> None:
        if self.is_empty():
            print(f"  {name}: [ empty ]")
            return
        levels: dict[int, list] = {}
        for pri, seq, val in self._heap:
            levels.setdefault(pri, []).append((seq, val))
        print(f"  {name} (high->low priority):")
        for pri in sorted(levels, reverse=True):
            items = sorted(levels[pri], reverse=True)
            vals = ", ".join(str(v) for _, v in items)
            print(f"    [priority {pri:2d}]: {vals}")
        print(f"    Total: {self.size()} elements")

    def display_heap(self, name: str = "Internal heap") -> None:
        if self.is_empty():
            print(f"  {name}: [ empty ]")
            return
        print(f"  {name}:")
        n, level, i = len(self._heap), 0, 0
        while i < n:
            row = []
            for _ in range(2 ** level):
                if i >= n:
                    break
                pri, _, val = self._heap[i]
                row.append(f"{val}(p={pri})")
                i += 1
            indent = " " * max(0, 20 - level * 5)
            print(f"{indent}{'  '.join(row)}")
            level += 1

    def __repr__(self) -> str:
        return f"PriorityStack(size={self.size()})"


# Implementation B: sorted-list priority stack.
class PriorityStackList:
    """Alternative: keep list sorted, push O(n), pop O(1)."""

    def __init__(self) -> None:
        self._list: list[tuple] = []
        self._seq = 0

    def push(self, value, priority: int) -> None:
        entry = (priority, self._seq, value)
        self._seq += 1
        i = 0
        # Keep ascending order so highest is at end.
        while i < len(self._list) and (self._list[i][0], self._list[i][1]) < (priority, entry[1]):
            i += 1
        self._list.insert(i, entry)

    def pop(self) -> tuple:
        if not self._list:
            raise IndexError("Priority stack is empty.")
        pri, _, val = self._list.pop()
        return (pri, val)

    def peek(self) -> tuple:
        if not self._list:
            raise IndexError("Priority stack is empty.")
        pri, _, val = self._list[-1]
        return (pri, val)

    def is_empty(self) -> bool:
        return not self._list

    def size(self) -> int:
        return len(self._list)

    def display(self, name: str = "PriorityStackList") -> None:
        if not self._list:
            print(f"  {name}: [ empty ]")
            return
        elems = " -> ".join(f"{v}(p={p})" for p, _, v in reversed(self._list))
        print(f"  {name} [high->low]: {elems}")


def demo_push() -> PriorityStack:
    title("1. PUSH - Insert with priority")
    ps = PriorityStack()

    subtitle("1a. Individual push")
    data = [
        ("task_low", 1), ("task_high", 8),
        ("task_medium", 4), ("task_critical", 10),
        ("task_normal", 4), ("task_urgent", 8),
    ]
    for val, pri in data:
        ps.push(val, pri)
        print(f"  push({val!r:18s}, pri={pri:2d})")
    ps.display()
    ps.display_heap("Internal heap after pushes:")

    subtitle("1b. push_many - batch insert")
    ps2 = PriorityStack()
    batch = [("A", 3), ("B", 7), ("C", 1), ("D", 5), ("E", 7)]
    ps2.push_many(batch)
    print(f"  push_many({batch})")
    ps2.display()
    return ps


def demo_pop(ps: PriorityStack) -> PriorityStack:
    title("2. POP - Remove highest priority (LIFO on ties)")
    ps.display("Before:")

    subtitle("Pop all in order")
    while not ps.is_empty():
        pri, val = ps.pop()
        print(f"  pop() -> {val!r:20s} (priority={pri:2d})  | remaining: {ps.size()}")

    subtitle("Pop from empty stack -> error")
    try:
        ps.pop()
    except IndexError as error:
        print(f"  IndexError: {error}")
    return ps


def demo_peek() -> PriorityStack:
    title("3. PEEK - View top without removing")
    ps = PriorityStack()
    for val, pri in [("alpha", 3), ("beta", 9), ("gamma", 6)]:
        ps.push(val, pri)
    ps.display("Stack:")
    pri, val = ps.peek()
    print(f"  peek() -> {val!r} with priority {pri}  (unchanged)")
    ps.display("Unmodified:")
    return ps


def demo_change_priority(ps: PriorityStack) -> None:
    title("4. CHANGE_PRIORITY - Update element priority")
    for val, pri in [("p_A", 3), ("p_B", 7), ("p_C", 2), ("p_D", 5)]:
        ps.push(val, pri)
    ps.display("Before:")

    subtitle("Increase p_A: 3 -> 10")
    ps.change_priority("p_A", 10)
    ps.display("After p_A increase:")

    subtitle("Decrease p_B: 7 -> 1")
    ps.change_priority("p_B", 1)
    ps.display("After p_B decrease:")

    subtitle("Missing element")
    ok = ps.change_priority("p_Z", 5)
    print(f"  change_priority('p_Z', 5) -> {'OK' if ok else 'not found'}")


def demo_remove(ps: PriorityStack) -> None:
    title("5. REMOVE - Delete a specific element")
    ps.display("Before:")
    for val in ["p_C", "p_D"]:
        ok = ps.remove(val)
        print(f"  remove({val!r}) -> {'removed [OK]' if ok else 'not found'}")
    ps.display("After:")
    ok = ps.remove("not_exists")
    print(f"  remove('not_exists') -> {'removed' if ok else 'not found (expected)'}")


def demo_pop_by_level(ps: PriorityStack) -> None:
    title("6. POP_BY_LEVEL - Remove all items from one priority")
    for val, pri in [("X1", 5), ("X2", 5), ("Y1", 3), ("X3", 5), ("Z1", 8)]:
        ps.push(val, pri)
    ps.display("Before:")

    level = 5
    removed = ps.pop_by_level(level)
    print(f"  pop_by_level({level}) -> {[(p, v) for p, v in removed]}")
    ps.display("After:")


def demo_queries(ps: PriorityStack) -> None:
    title("7. QUERIES - contains, get_priority, is_empty, size")
    for val, pri in [("sun", 4), ("moon", 8), ("star", 2)]:
        ps.push(val, pri)
    ps.display("Stack:")
    print(f"  is_empty()            -> {ps.is_empty()}")
    print(f"  size()                -> {ps.size()}")
    print(f"  contains('moon')      -> {ps.contains('moon')}")
    print(f"  contains('comet')     -> {ps.contains('comet')}")
    print(f"  get_priority('star')  -> {ps.get_priority('star')}")
    print(f"  get_priority('comet') -> {ps.get_priority('comet')}")


def demo_merge(ps: PriorityStack) -> None:
    title("8. MERGE - Merge two priority stacks")
    ps2 = PriorityStack()
    for val, pri in [("v_A", 6), ("v_B", 1), ("v_C", 9)]:
        ps2.push(val, pri)
    ps.display("Stack 1:")
    ps2.display("Stack 2:")
    merged = ps.merge(ps2)
    merged.display("Merged:")

    subtitle("Pop merged stack in order")
    while not merged.is_empty():
        pri, val = merged.pop()
        print(f"  pop() -> {val!r:12s} (priority={pri})")


def demo_to_sorted_list(ps: PriorityStack) -> None:
    title("9. TO_SORTED_LIST - Export in priority order")
    ps.display("Stack:")
    out = ps.to_sorted_list()
    print("  to_sorted_list():")
    for pri, val in out:
        print(f"    (priority={pri}, value={val!r})")


def demo_clear(ps: PriorityStack) -> None:
    title("10. CLEAR - Empty the priority stack")
    ps.display("Before:")
    ps.clear()
    ps.display("After:")
    print(f"  is_empty() -> {ps.is_empty()}")


def demo_sorted_list_impl() -> None:
    title("11. IMPLEMENTATION B - Sorted list (push O(n), pop O(1))")
    pl = PriorityStackList()
    data = [("req_1", 3), ("req_2", 8), ("req_3", 1), ("req_4", 5), ("req_5", 8)]

    subtitle("Push")
    for val, pri in data:
        pl.push(val, pri)
        print(f"  push({val!r}, {pri})  ->  ", end="")
        pl.display()

    subtitle("Pop (always highest)")
    while not pl.is_empty():
        pri, val = pl.pop()
        print(f"  pop() -> {val!r} (p={pri})")


def demo_lifo_tie() -> None:
    title("12. LIFO ON TIES - Same priority pops latest first")
    ps = PriorityStack()
    for val, pri in [("first", 5), ("second", 5), ("third", 5), ("fourth", 5)]:
        ps.push(val, pri)
    ps.display("All with priority 5:")

    print("\n  Pop order (same priority -> LIFO):")
    while not ps.is_empty():
        pri, val = ps.pop()
        print(f"  pop() -> {val!r} (priority={pri})")


def demo_practical_case() -> None:
    title("13. PRACTICAL CASE - OS process scheduler")
    print("  Priorities: 1=Idle  3=Normal  6=High  10=Real-Time\n")

    scheduler = PriorityStack()
    processes = [
        ("idle_daemon", 1),
        ("update_service", 3),
        ("user_browser", 3),
        ("music_player", 3),
        ("antivirus_scan", 6),
        ("database_query", 6),
        ("kernel_interrupt", 10),
        ("video_driver", 6),
        ("system_monitor", 3),
        ("rt_control_loop", 10),
    ]

    print("  [Incoming scheduler processes]")
    for name, pri in processes:
        scheduler.push(name, pri)
        label = {1: "IDLE", 3: "NORMAL", 6: "HIGH", 10: "RT"}[pri]
        print(f"  [+] [{label:6s}] {name}")

    scheduler.display("\n  Scheduler state:")

    subtitle("Urgent real-time process arrives")
    scheduler.push("rt_emergency", 10)
    print("  [+] [RT    ] rt_emergency (urgent arrival)")
    scheduler.display("Scheduler updated:")

    print("\n  [CPU running by priority]")
    tick = 1
    while not scheduler.is_empty():
        pri, name = scheduler.pop()
        label = {1: "IDLE", 3: "NORMAL", 6: "HIGH", 10: "RT"}.get(pri, f"p={pri}")
        print(f"  [*] tick {tick:02d} [{label:6s}] {name}")
        tick += 1


def main() -> None:
    print(f"\n{SEPARATOR}")
    print("  PRIORITY STACK - Python 3.14")
    print(f"{SEPARATOR}")

    ps = demo_push()
    ps = demo_pop(ps)
    ps = demo_peek()
    demo_change_priority(ps)
    demo_remove(ps)
    demo_pop_by_level(ps)
    demo_queries(ps)
    demo_merge(ps)
    demo_to_sorted_list(ps)
    demo_clear(ps)
    demo_sorted_list_impl()
    demo_lifo_tie()
    demo_practical_case()

    title("OPERATIONS SUMMARY")
    print(f"  {'Operation':<26} {'Description':<36} {'Heap':<10} {'List'}")
    print("  " + "-" * 72)
    operations = [
        ("push(v, pri)", "Insert with priority",               "O(log n)", "O(n)"),
        ("push_many(items)", "Insert multiple",                "O(k log n)", "O(kn)"),
        ("pop()", "Remove highest priority",                   "O(log n)", "O(1)"),
        ("peek()", "View highest without removing",            "O(1)", "O(1)"),
        ("pop_by_level(p)", "Remove all in level p",           "O(n log n)", "O(n)"),
        ("change_priority(v,p)", "Change priority",            "O(n)", "O(n)"),
        ("remove(v)", "Remove specific element",               "O(n)", "O(n)"),
        ("contains(v)", "Check if value exists",               "O(n)", "O(n)"),
        ("get_priority(v)", "Get value priority",              "O(n)", "O(n)"),
        ("is_empty()", "Check if empty",                       "O(1)", "O(1)"),
        ("size()", "Number of elements",                       "O(1)", "O(1)"),
        ("clear()", "Empty stack",                             "O(1)", "O(1)"),
        ("merge(other)", "Merge with another stack",           "O(n log n)", "O(n^2)"),
        ("to_sorted_list()", "Export sorted",                  "O(n log n)", "O(n)"),
        ("display()", "Show by priority levels",               "O(n log n)", "O(n)"),
    ]
    for op, desc, heap, lst in operations:
        print(f"  {op:<26} {desc:<36} {heap:<10} {lst}")

    print(f"\n{SEPARATOR}")
    print("  [OK] Priority stack - all operations demonstrated.")
    print(f"{SEPARATOR}\n")


if __name__ == "__main__":
    main()
