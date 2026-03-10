# -------------------------------------------------
# File Name: 17_circular_stack.py
# Author: Florentino Baez
# Date: 2026-03-09
# Description: Circular stack variants (blocking and overwriting).
# -------------------------------------------------

"""
============================================================
  CIRCULAR STACK - Python 3.14
  Fixed-size stack where positions are reused in circular mode:
  when capacity is exceeded, the top wraps back to index 0.

  Two variants:
    A) BLOCKING     -> rejects push when full
    B) OVERWRITING  -> newest push overwrites the oldest
       element (circular history buffer)

  Internal structure: array + top pointer with modulo.

  Operations:
    - push      -> Insert at top (with wrap-around)
    - pop       -> Remove from top (with wrap-around)
    - peek      -> View top without removing
    - is_empty  -> Is empty?
    - is_full   -> Is full?
    - size      -> Current size
    - clear     -> Empty stack
    - search    -> Search from top
    - display   -> Show physical buffer and logical view
    - to_list   -> Export as list (top->base)
============================================================
"""

SEPARATOR = "=" * 60


def title(text: str) -> None:
    print(f"\n{SEPARATOR}\n  {text}\n{SEPARATOR}")


def subtitle(text: str) -> None:
    print(f"\n  --- {text} ---")


# Variant A: Blocking circular stack.
class CircularStackBlocking:
    """Circular stack that rejects push when full."""

    def __init__(self, capacity: int = 6) -> None:
        self._cap = capacity
        self._buf = [None] * capacity
        self._top = -1
        self._size = 0

    # Query methods.
    def is_empty(self) -> bool:
        return self._size == 0

    def is_full(self) -> bool:
        return self._size == self._cap

    def size(self) -> int:
        return self._size

    def peek(self):
        if self.is_empty():
            raise IndexError("Circular stack is empty.")
        return self._buf[self._top % self._cap]

    def search(self, value) -> int:
        """Position from top (1=top), or -1 if missing."""
        for i in range(self._size):
            idx = (self._top - i) % self._cap
            if self._buf[idx] == value:
                return i + 1
        return -1

    def contains(self, value) -> bool:
        return self.search(value) != -1

    def to_list(self) -> list:
        return [self._buf[(self._top - i) % self._cap] for i in range(self._size)]

    # Modification methods.
    def push(self, value) -> None:
        if self.is_full():
            raise OverflowError("Circular stack is full.")
        self._top = (self._top + 1) % self._cap
        self._buf[self._top] = value
        self._size += 1

    def pop(self):
        if self.is_empty():
            raise IndexError("Circular stack is empty.")
        value = self._buf[self._top % self._cap]
        self._buf[self._top % self._cap] = None
        self._top = (self._top - 1) % self._cap
        self._size -= 1
        return value

    def clear(self) -> None:
        self._buf = [None] * self._cap
        self._top = -1
        self._size = 0

    # Display helpers.
    def display_buffer(self, name: str = "Physical buffer") -> None:
        cells = []
        for i, v in enumerate(self._buf):
            marker = ""
            real_top = self._top % self._cap if self._size > 0 else -1
            if i == real_top and self._size > 0:
                marker = "T"
            cells.append(f"[{v if v is not None else '__':^4}]{marker}")
        print(f"  {name}: " + " ".join(cells))

    def display(self, name: str = "") -> None:
        if self.is_empty():
            print(f"  {name} TOP -> [ empty ]  cap={self._cap}")
            return
        elems = " | ".join(str(v) for v in self.to_list())
        print(f"  {name} TOP -> [ {elems} ] <- BASE  (size={self._size}/{self._cap})")


# Variant B: Overwriting circular history stack.
class CircularStackHistory:
    """Circular stack that overwrites oldest value when full."""

    def __init__(self, capacity: int = 5) -> None:
        self._cap = capacity
        self._buf = [None] * capacity
        self._top = -1
        self._base = 0
        self._size = 0

    def is_empty(self) -> bool:
        return self._size == 0

    def is_full(self) -> bool:
        return self._size == self._cap

    def size(self) -> int:
        return self._size

    def peek(self):
        if self.is_empty():
            raise IndexError("History stack is empty.")
        return self._buf[self._top % self._cap]

    def push(self, value) -> None:
        # If full, overwrite the oldest element and advance base.
        self._top = (self._top + 1) % self._cap
        self._buf[self._top] = value
        if self._size < self._cap:
            self._size += 1
        else:
            self._base = (self._base + 1) % self._cap

    def pop(self):
        if self.is_empty():
            raise IndexError("History stack is empty.")
        value = self._buf[self._top]
        self._buf[self._top] = None
        self._top = (self._top - 1) % self._cap
        self._size -= 1
        return value

    def to_list(self) -> list:
        return [self._buf[(self._top - i) % self._cap] for i in range(self._size)]

    def clear(self) -> None:
        self._buf = [None] * self._cap
        self._top = -1
        self._base = 0
        self._size = 0

    def display_buffer(self, name: str = "Physical buffer") -> None:
        cells = []
        for i, v in enumerate(self._buf):
            marker = ""
            real_top = self._top % self._cap if self._size > 0 else -1
            if i == real_top and self._size > 0:
                marker = "T"
            if i == self._base and self._size > 0:
                marker += "B"
            cells.append(f"[{v if v is not None else '__':^4}]{marker}")
        print(f"  {name}: " + " ".join(cells))
        print("  (T=top, B=base/oldest)")

    def display(self, name: str = "") -> None:
        if self.is_empty():
            print(f"  {name} [ empty history ]  cap={self._cap}")
            return
        elems = " | ".join(str(v) for v in self.to_list())
        print(f"  {name} TOP -> [ {elems} ] <- OLDEST  (size={self._size}/{self._cap})")


def demo_push_blocking() -> CircularStackBlocking:
    title("1. PUSH - Insert in circular stack (blocking)")
    stack = CircularStackBlocking(capacity=5)

    subtitle("1a. Sequential push until full")
    for value in [10, 20, 30, 40, 50]:
        stack.push(value)
        print(f"  push({value:2d})")
        stack.display_buffer()
        stack.display()

    subtitle("1b. Push on full stack -> error")
    try:
        stack.push(99)
    except OverflowError as error:
        print(f"  OverflowError: {error}")

    return stack


def demo_pop_blocking(stack: CircularStackBlocking) -> CircularStackBlocking:
    title("2. POP - Remove from top (wrap-around visible)")
    stack.display("Before:")

    subtitle("2a. Pop x 3")
    for _ in range(3):
        value = stack.pop()
        print(f"  pop() -> {value}")
        stack.display_buffer()
        stack.display()

    subtitle("2b. Push into freed positions (wrap-around)")
    for value in [60, 70, 80]:
        stack.push(value)
        print(f"  push({value})")
        stack.display_buffer()
        stack.display()

    return stack


def demo_peek_blocking(stack: CircularStackBlocking) -> None:
    title("3. PEEK - View top without modifying stack")
    stack.display("Current stack:")
    print(f"  peek() -> {stack.peek()}   (unchanged)")
    stack.display("Unchanged:")


def demo_queries_blocking(stack: CircularStackBlocking) -> None:
    title("4. QUERIES - is_empty, is_full, size, search, contains")
    stack.display("Current stack:")
    print(f"  is_empty() -> {stack.is_empty()}")
    print(f"  is_full()  -> {stack.is_full()}")
    print(f"  size()     -> {stack.size()}")

    subtitle("search and contains")
    for value in [70, 80, 60, 99]:
        pos = stack.search(value)
        print(f"  search({value:2d}) -> {pos:2d}   contains({value:2d}) -> {stack.contains(value)}")


def demo_clear_blocking(stack: CircularStackBlocking) -> None:
    title("5. CLEAR - Empty circular stack")
    stack.display_buffer("Before:")
    stack.display()
    stack.clear()
    stack.display_buffer("After:")
    stack.display()
    print(f"  is_empty() -> {stack.is_empty()}")


def demo_history_variant() -> None:
    title("6. OVERWRITING CIRCULAR STACK - History (last N states)")
    print("  When full, it overwrites the oldest state.\n")

    hist = CircularStackHistory(capacity=4)

    subtitle("6a. Fill history")
    for value in ["state_1", "state_2", "state_3", "state_4"]:
        hist.push(value)
        print(f"  push({value!r})")
        hist.display_buffer()
        hist.display()
        print()

    subtitle("6b. Exceed capacity -> overwrite oldest")
    for value in ["state_5", "state_6"]:
        hist.push(value)
        print(f"  push({value!r})  <- overwrites oldest")
        hist.display_buffer()
        hist.display()
        print()

    subtitle("6c. Pop (undo)")
    for _ in range(3):
        value = hist.pop()
        print(f"  pop() -> {value!r}  (undo)")
        hist.display()


def demo_wrap_around_visual() -> None:
    title("7. WRAP-AROUND - Step-by-step visualization")
    print("  Circular stack cap=4: top wraps around.\n")
    stack = CircularStackBlocking(capacity=4)

    steps = [
        ("push", "A"), ("push", "B"), ("push", "C"), ("push", "D"),
        ("pop", None), ("pop", None),
        ("push", "E"), ("push", "F"),
    ]
    for op, value in steps:
        if op == "push":
            stack.push(value)
            print(f"  push('{value}')  ->  buffer: ", end="")
        else:
            popped = stack.pop()
            print(f"  pop()->'{popped}'  ->  buffer: ", end="")
        buf_str = " ".join(f"[{x if x else '__':^3}]" for x in stack._buf)
        print(f"{buf_str}  top_idx={(stack._top) % stack._cap}")


def demo_practical_case() -> None:
    title("8. PRACTICAL CASE - Undo history in text editor")
    print("  Scenario: editor keeps last 5 changes. Undo reverts.\n")

    undo = CircularStackHistory(capacity=5)
    actions = [
        "Type 'Hello'",
        "Type ' world'",
        "Apply bold",
        "Change font",
        "Set red color",
        "Underline",
        "Set size 14pt",
    ]

    print("  [Applying actions]")
    for action in actions:
        undo.push(action)
        print(f"  [*] {action}")
    undo.display("\n  Available history:")

    print("\n  [Pressing Ctrl+Z - undo]")
    for _ in range(4):
        action = undo.pop()
        print(f"  <- Undo: {action}")
        if not undo.is_empty():
            undo.display("  History:")

    undo.display("\n  History at end:")


def main() -> None:
    print(f"\n{SEPARATOR}")
    print("  CIRCULAR STACK - Python 3.14")
    print("  Variant A: Blocking | Variant B: Overwriting")
    print(f"{SEPARATOR}")

    stack = demo_push_blocking()
    stack = demo_pop_blocking(stack)
    demo_peek_blocking(stack)
    demo_queries_blocking(stack)
    demo_clear_blocking(stack)
    demo_history_variant()
    demo_wrap_around_visual()
    demo_practical_case()

    title("OPERATIONS SUMMARY")
    print(f"  {'Operation':<18} {'Description':<40} {'Complexity'}")
    print("  " + "-" * 62)
    operations = [
        ("push(v)", "Insert at top (with wrap-around)",      "O(1)"),
        ("pop()", "Remove from top (with wrap-around)",      "O(1)"),
        ("peek()", "View top without removing",              "O(1)"),
        ("is_empty()", "Check if empty",                     "O(1)"),
        ("is_full()", "Check if full",                       "O(1)"),
        ("size()", "Number of elements",                     "O(1)"),
        ("search(v)", "Position from top",                   "O(n)"),
        ("contains(v)", "Check value existence",             "O(n)"),
        ("clear()", "Empty stack",                           "O(n)"),
        ("to_list()", "Export top->base list",               "O(n)"),
        ("display()", "Show content",                        "O(n)"),
    ]
    for op, desc, complexity in operations:
        print(f"  {op:<18} {desc:<40} {complexity}")

    print(f"\n{SEPARATOR}")
    print("  [OK] Circular stack - all operations demonstrated.")
    print(f"{SEPARATOR}\n")


if __name__ == "__main__":
    main()
