# -------------------------------------------------
# File Name: 18_double_stack_destack.py
# Author: Florentino Baez
# Date: 2026-03-09
# Description: Double stack in shared array + double-ended stack.
# -------------------------------------------------

"""
============================================================
  DOUBLE STACK - Python 3.14
  Two stacks sharing one array, growing from opposite ends.

  Shared array (cap=10):
  Stack 1 -> [A|B|C|__|__|__|__|X|Y|Z] <- Stack 2
             top1=2                top2=7

  Advantage: memory is used more efficiently when one stack
  grows while the other shrinks.

  Also includes a Double-Ended Stack (DeStack):
  insertion/removal from BOTH top and base.

  Operations:
    - push1 / push2       -> Insert into stack 1 or 2
    - pop1  / pop2        -> Remove from stack 1 or 2
    - peek1 / peek2       -> View top without removing
    - push_top/push_base  -> DeStack insert on both sides
    - pop_top / pop_base  -> DeStack remove on both sides
    - is_empty1/2, is_full -> Queries
    - size1, size2, size_total
    - clear, clear1, clear2
    - transfer            -> Move items between stacks
    - display             -> Full visualization
============================================================
"""

SEPARATOR = "=" * 60


def title(text: str) -> None:
    print(f"\n{SEPARATOR}\n  {text}\n{SEPARATOR}")


def subtitle(text: str) -> None:
    print(f"\n  --- {text} ---")


# Part 1: Two stacks in one shared array.
class DoubleStack:
    """Stack 1 grows left->right, stack 2 grows right->left."""

    def __init__(self, capacity: int = 10) -> None:
        self._cap = capacity
        self._arr = [None] * capacity
        self._t1 = -1
        self._t2 = capacity

    # Query methods.
    def is_empty1(self) -> bool:
        return self._t1 == -1

    def is_empty2(self) -> bool:
        return self._t2 == self._cap

    def is_full(self) -> bool:
        return self._t1 + 1 == self._t2

    def size1(self) -> int:
        return self._t1 + 1

    def size2(self) -> int:
        return self._cap - self._t2

    def size_total(self) -> int:
        return self.size1() + self.size2()

    def peek1(self):
        if self.is_empty1():
            raise IndexError("Stack 1 is empty.")
        return self._arr[self._t1]

    def peek2(self):
        if self.is_empty2():
            raise IndexError("Stack 2 is empty.")
        return self._arr[self._t2]

    # Modification methods.
    def push1(self, value) -> None:
        if self.is_full():
            raise OverflowError("Shared array is full.")
        self._t1 += 1
        self._arr[self._t1] = value

    def push2(self, value) -> None:
        if self.is_full():
            raise OverflowError("Shared array is full.")
        self._t2 -= 1
        self._arr[self._t2] = value

    def pop1(self):
        if self.is_empty1():
            raise IndexError("Stack 1 is empty.")
        value = self._arr[self._t1]
        self._arr[self._t1] = None
        self._t1 -= 1
        return value

    def pop2(self):
        if self.is_empty2():
            raise IndexError("Stack 2 is empty.")
        value = self._arr[self._t2]
        self._arr[self._t2] = None
        self._t2 += 1
        return value

    def clear1(self) -> None:
        for i in range(self._t1 + 1):
            self._arr[i] = None
        self._t1 = -1

    def clear2(self) -> None:
        for i in range(self._t2, self._cap):
            self._arr[i] = None
        self._t2 = self._cap

    def clear(self) -> None:
        self._arr = [None] * self._cap
        self._t1 = -1
        self._t2 = self._cap

    def transfer(self, source: int, amount: int) -> int:
        """Move `amount` elements from source stack to the other stack."""
        moved = 0
        try:
            for _ in range(amount):
                if source == 1:
                    self.push2(self.pop1())
                else:
                    self.push1(self.pop2())
                moved += 1
        except (IndexError, OverflowError):
            pass
        return moved

    # Visualization helpers.
    def display(self, name: str = "Double Stack") -> None:
        buf = []
        for i, v in enumerate(self._arr):
            marker = ""
            if i == self._t1 and not self.is_empty1():
                marker = "^1"
            if i == self._t2 and not self.is_empty2():
                marker = "^2"
            buf.append(f"[{v if v is not None else '__':^4}]{marker}")
        print(f"  {name}:")
        print("  " + " ".join(buf))
        print(
            f"    ^Stack1(t={self._t1})  <-free:{self._cap - self.size_total()}->  "
            f"Stack2^(t={self._t2})"
        )
        print(
            f"    Stack1 size={self.size1()} | Stack2 size={self.size2()} | "
            f"Total={self.size_total()}/{self._cap}"
        )

    def display_stacks(self) -> None:
        s1 = [self._arr[i] for i in range(self._t1 + 1)]
        s2 = [self._arr[i] for i in range(self._t2, self._cap)]
        s2_base_to_top = list(reversed(s2))
        print(f"  Stack 1 (base->top): [ {' | '.join(str(v) for v in s1) if s1 else 'empty'} ]")
        print(
            "  Stack 2 (base->top): [ "
            + (f"{' | '.join(str(v) for v in s2_base_to_top)}" if s2_base_to_top else "empty")
            + " ]"
        )


# Part 2: Double-ended stack (DeStack).
class DeStack:
    """Stack with access at both top and base."""

    class _Node:
        def __init__(self, value):
            self.value = value
            self.prev = None
            self.next = None

    def __init__(self) -> None:
        self._top: DeStack._Node | None = None
        self._base: DeStack._Node | None = None
        self._size = 0

    def is_empty(self) -> bool:
        return self._size == 0

    def size(self) -> int:
        return self._size

    def peek_top(self):
        if self.is_empty():
            raise IndexError("DeStack is empty.")
        return self._top.value

    def peek_base(self):
        if self.is_empty():
            raise IndexError("DeStack is empty.")
        return self._base.value

    def push_top(self, value) -> None:
        node = self._Node(value)
        if self.is_empty():
            self._top = self._base = node
        else:
            node.next = self._top
            self._top.prev = node
            self._top = node
        self._size += 1

    def push_base(self, value) -> None:
        node = self._Node(value)
        if self.is_empty():
            self._top = self._base = node
        else:
            node.prev = self._base
            self._base.next = node
            self._base = node
        self._size += 1

    def pop_top(self):
        if self.is_empty():
            raise IndexError("DeStack is empty.")
        value = self._top.value
        if self._size == 1:
            self._top = self._base = None
        else:
            self._top = self._top.next
            self._top.prev = None
        self._size -= 1
        return value

    def pop_base(self):
        if self.is_empty():
            raise IndexError("DeStack is empty.")
        value = self._base.value
        if self._size == 1:
            self._top = self._base = None
        else:
            self._base = self._base.prev
            self._base.next = None
        self._size -= 1
        return value

    def clear(self) -> None:
        self._top = self._base = None
        self._size = 0

    def to_list(self) -> list:
        out = []
        cur = self._top
        while cur:
            out.append(cur.value)
            cur = cur.next
        return out

    def display(self, name: str = "") -> None:
        if self.is_empty():
            print(f"  {name} TOP -> [ empty ] <- BASE")
            return
        elems = " | ".join(str(v) for v in self.to_list())
        print(f"  {name} TOP -> [ {elems} ] <- BASE  (size={self._size})")


def demo_double_stack_push() -> DoubleStack:
    title("1. PUSH1 and PUSH2 - Two stacks growing to the center")
    ds = DoubleStack(capacity=10)

    subtitle("1a. Push only on Stack 1 (left->right)")
    for v in [10, 20, 30]:
        ds.push1(v)
        print(f"  push1({v:2d})")
        ds.display()
        print()

    subtitle("1b. Push only on Stack 2 (right->left)")
    for v in [90, 80, 70]:
        ds.push2(v)
        print(f"  push2({v:2d})")
        ds.display()
        print()

    subtitle("1c. Alternate push1 and push2")
    for v1, v2 in [(40, 60), (50, None)]:
        ds.push1(v1)
        print(f"  push1({v1})")
        ds.display()
        print()
        if v2 is not None:
            ds.push2(v2)
            print(f"  push2({v2})")
            ds.display()
            print()

    return ds


def demo_double_stack_pop(ds: DoubleStack) -> DoubleStack:
    title("2. POP1 and POP2 - Remove from each stack")
    ds.display_stacks()

    subtitle("2a. Pop from Stack 1")
    for _ in range(2):
        v = ds.pop1()
        print(f"  pop1() -> {v}")
        ds.display()
        print()

    subtitle("2b. Pop from Stack 2")
    for _ in range(2):
        v = ds.pop2()
        print(f"  pop2() -> {v}")
        ds.display()
        print()

    return ds


def demo_peek_queries(ds: DoubleStack) -> None:
    title("3. PEEK and QUERIES - Stack 1 and Stack 2")
    ds.display_stacks()
    print(f"  peek1()      -> {ds.peek1()}")
    print(f"  peek2()      -> {ds.peek2()}")
    print(f"  is_empty1()  -> {ds.is_empty1()}")
    print(f"  is_empty2()  -> {ds.is_empty2()}")
    print(f"  is_full()    -> {ds.is_full()}")
    print(f"  size1()      -> {ds.size1()}")
    print(f"  size2()      -> {ds.size2()}")
    print(f"  size_total() -> {ds.size_total()}/{ds._cap}")

    subtitle("Shared array completely full (cap=6)")
    full = DoubleStack(6)
    for v in [1, 2, 3]:
        full.push1(v)
    for v in [6, 5, 4]:
        full.push2(v)
    full.display("Full:")
    print(f"  is_full() -> {full.is_full()}")
    try:
        full.push1(99)
    except OverflowError as error:
        print(f"  OverflowError on push1: {error}")


def demo_clear(ds: DoubleStack) -> None:
    title("4. CLEAR - Empty one or both stacks")
    ds.display("Before:")

    subtitle("4a. clear1() - empty only stack 1")
    ds.clear1()
    ds.display("After clear1():")

    subtitle("4b. clear2() - empty only stack 2")
    ds.clear2()
    ds.display("After clear2():")

    subtitle("4c. clear() - empty both")
    for v in [1, 2, 3]:
        ds.push1(v)
    for v in [9, 8, 7]:
        ds.push2(v)
    ds.display("Before full clear:")
    ds.clear()
    ds.display("After clear():")


def demo_transfer() -> None:
    title("5. TRANSFER - Move elements between stacks")
    ds = DoubleStack(10)
    for v in [1, 2, 3, 4, 5]:
        ds.push1(v)
    ds.display("Before (all in Stack 1):")
    ds.display_stacks()

    n = ds.transfer(source=1, amount=3)
    print(f"\n  transfer(source=1, amount=3) -> moved: {n}")
    ds.display("After:")
    ds.display_stacks()


def demo_destack() -> None:
    title("6. DESTACK - Double-ended stack (top and base access)")
    ds = DeStack()

    subtitle("6a. push_top and push_base")
    for v in [30, 20, 10]:
        ds.push_top(v)
        print(f"  push_top({v:2d})  ->  ", end="")
        ds.display()
    for v in [40, 50]:
        ds.push_base(v)
        print(f"  push_base({v:2d}) ->  ", end="")
        ds.display()

    subtitle("6b. peek_top and peek_base")
    ds.display("State:")
    print(f"  peek_top()  -> {ds.peek_top()}")
    print(f"  peek_base() -> {ds.peek_base()}")

    subtitle("6c. pop_top and pop_base")
    for _ in range(2):
        v = ds.pop_top()
        print(f"  pop_top()  -> {v}")
        ds.display()
    for _ in range(2):
        v = ds.pop_base()
        print(f"  pop_base() -> {v}")
        ds.display()

    subtitle("6d. Queries")
    print(f"  is_empty() -> {ds.is_empty()}")
    print(f"  size()     -> {ds.size()}")
    ds.clear()
    print(f"  After clear(): is_empty() -> {ds.is_empty()}")


def demo_practical_case() -> None:
    title("7. PRACTICAL CASE - Shared resource management")

    subtitle("7a. Double stack: CPU and GPU tasks sharing RAM")
    print("  CPU and GPU share a 12-slot memory buffer.\n")
    ram = DoubleStack(capacity=12)

    cpu_tasks = ["cpu_render", "cpu_physics", "cpu_audio", "cpu_ai"]
    gpu_tasks = ["gpu_shader1", "gpu_shader2", "gpu_texture", "gpu_shadow"]

    for cpu, gpu in zip(cpu_tasks, gpu_tasks):
        ram.push1(cpu)
        ram.push2(gpu)

    ram.display("Shared RAM:")
    ram.display_stacks()

    print("\n  Processing tasks (alternating CPU and GPU):")
    while not ram.is_empty1() or not ram.is_empty2():
        if not ram.is_empty1():
            task = ram.pop1()
            print(f"  [CPU] Executed: {task}")
        if not ram.is_empty2():
            task = ram.pop2()
            print(f"  [GPU] Executed: {task}")

    subtitle("7b. DeStack: bidirectional history navigation")
    print("  Code inspector: navigate changes backward and forward.")
    hist = DeStack()
    changes = ["add_class", "refactor_method", "rename_variable", "remove_duplicates"]
    for c in changes:
        hist.push_top(c)
        print(f"  [*] {c}")
    hist.display("\n  History (top=most recent):")

    print("\n  [Move backward in history]")
    for _ in range(2):
        print(f"  <- {hist.pop_top()}")
    hist.display("  History after 2 undo:")

    print("\n  [Look toward oldest side]")
    print(f"  -> Oldest visible: {hist.peek_base()}")


def main() -> None:
    print(f"\n{SEPARATOR}")
    print("  DOUBLE STACK - Python 3.14")
    print("  Part 1: DoubleStack (shared array)")
    print("  Part 2: DeStack    (top and base access)")
    print(f"{SEPARATOR}")

    ds = demo_double_stack_push()
    ds = demo_double_stack_pop(ds)
    demo_peek_queries(ds)
    demo_clear(ds)
    demo_transfer()
    demo_destack()
    demo_practical_case()

    title("OPERATIONS SUMMARY")
    print(f"  {'Operation':<22} {'Description':<38} {'Complexity'}")
    print("  " + "-" * 65)
    operations = [
        ("-- DOUBLE STACK --", "", ""),
        ("push1(v)/push2(v)", "Insert in stack 1 or 2",            "O(1)"),
        ("pop1()/pop2()", "Remove from stack 1 or 2",              "O(1)"),
        ("peek1()/peek2()", "View top of stack 1 or 2",            "O(1)"),
        ("is_empty1/2()", "Check whether stack 1/2 is empty",      "O(1)"),
        ("is_full()", "Check if shared array is full",              "O(1)"),
        ("size1/2/total()", "Individual and total sizes",          "O(1)"),
        ("transfer(src,n)", "Move n elements between stacks",       "O(n)"),
        ("clear1/2/clear()", "Empty one or both stacks",           "O(n)"),
        ("-- DESTACK --", "", ""),
        ("push_top(v)", "Insert at top",                            "O(1)"),
        ("push_base(v)", "Insert at base",                          "O(1)"),
        ("pop_top()", "Remove from top",                            "O(1)"),
        ("pop_base()", "Remove from base",                          "O(1)"),
        ("peek_top/base()", "View top/base without removing",      "O(1)"),
        ("clear()", "Empty the DeStack",                            "O(1)"),
        ("display()", "Show content",                               "O(n)"),
    ]
    for op, desc, comp in operations:
        if desc == "":
            print(f"\n  {op}")
        else:
            print(f"  {op:<22} {desc:<38} {comp}")

    print(f"\n{SEPARATOR}")
    print("  [OK] Double stack - all operations demonstrated.")
    print(f"{SEPARATOR}\n")


if __name__ == "__main__":
    main()
