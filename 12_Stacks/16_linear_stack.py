# -------------------------------------------------
# File Name: 16_linear_stack.py
# Author: Florentino Baez
# Date: 2026-03-09
# Description: Linear stack (LIFO) implementation and complete demos.
# -------------------------------------------------

"""
============================================================
  LINEAR STACK - Python 3.14
  LIFO structure: Last In, First Out
  The last element inserted is the first removed.

        TOP ->   [ 50 ]   <- last inserted
                 [ 40 ]
                 [ 30 ]
                 [ 20 ]
                 [ 10 ]   <- first inserted
                ---------

  Operations:
    - push     -> Insert at top
    - pop      -> Remove from top
    - peek/top -> View top without removing
    - is_empty -> Is empty?
    - is_full  -> Is full?
    - size     -> Current size
    - clear    -> Empty stack
    - search   -> Search item (position from top)
    - copy     -> Copy stack
    - display  -> Show content
============================================================
"""

SEPARATOR = "=" * 60


def title(text: str) -> None:
    print(f"\n{SEPARATOR}\n  {text}\n{SEPARATOR}")


def subtitle(text: str) -> None:
    print(f"\n  --- {text} ---")


# Linear stack backed by a fixed-size array.
class LinearStack:
    """Linear stack where top grows to higher indexes."""

    def __init__(self, capacity: int = 10) -> None:
        self._data: list = [None] * capacity
        self._capacity: int = capacity
        self._top: int = -1

    # Query methods.
    def is_empty(self) -> bool:
        return self._top == -1

    def is_full(self) -> bool:
        return self._top == self._capacity - 1

    def size(self) -> int:
        return self._top + 1

    def peek(self):
        """Return the top element without removing it."""
        if self.is_empty():
            raise IndexError("Stack is empty: no top element.")
        return self._data[self._top]

    def search(self, value) -> int:
        """
        Return position from top (1 = top).
        Return -1 if value does not exist.
        """
        for i in range(self._top, -1, -1):
            if self._data[i] == value:
                return self._top - i + 1
        return -1

    def contains(self, value) -> bool:
        return self.search(value) != -1

    def copy(self) -> "LinearStack":
        """Return an exact stack copy."""
        new_stack = LinearStack(self._capacity)
        new_stack._data = self._data[:]
        new_stack._top = self._top
        return new_stack

    # Modification methods.
    def push(self, value) -> None:
        if self.is_full():
            raise OverflowError("Stack is full: push is not possible.")
        self._top += 1
        self._data[self._top] = value

    def pop(self):
        if self.is_empty():
            raise IndexError("Stack is empty: pop is not possible.")
        value = self._data[self._top]
        self._data[self._top] = None
        self._top -= 1
        return value

    def clear(self) -> None:
        self._data = [None] * self._capacity
        self._top = -1

    # Visualization methods.
    def display(self, name: str = "Stack") -> None:
        if self.is_empty():
            print(f"  {name}: [ empty ]")
            return
        print(f"  {name} (TOP->BASE):")
        for i in range(self._top, -1, -1):
            top_mark = " <- TOP" if i == self._top else ""
            base_mark = " <- BASE" if i == 0 else ""
            print(f"    [{self._data[i]}]{top_mark}{base_mark}")
        print(f"    ---------  size: {self.size()}/{self._capacity}")

    def display_horizontal(self, name: str = "") -> None:
        if self.is_empty():
            print(f"  {name} BASE -> [  empty  ] <- TOP")
            return
        elems = " | ".join(str(self._data[i]) for i in range(self._top + 1))
        print(f"  {name} BASE -> [ {elems} ] <- TOP  (size={self.size()})")

    def __repr__(self) -> str:
        top = self.peek() if not self.is_empty() else "empty"
        return f"LinearStack(top={top}, size={self.size()})"


def demo_push() -> LinearStack:
    title("1. PUSH - Insert elements at top")
    stack = LinearStack(capacity=6)

    subtitle("1a. Push one by one")
    for value in [10, 20, 30, 40, 50]:
        stack.push(value)
        print(f"  push({value:2d})  ->  ", end="")
        stack.display_horizontal()

    subtitle("1b. Full stack - push with capacity=6")
    stack.push(60)
    stack.display_horizontal("Full stack:")
    try:
        stack.push(99)
    except OverflowError as error:
        print(f"  OverflowError: {error}")

    subtitle("1c. Vertical stack view")
    stack.display("Complete stack")
    return stack


def demo_pop(stack: LinearStack) -> LinearStack:
    title("2. POP - Remove and return top element")
    stack.display_horizontal("Before:")

    subtitle("2a. Repeated pop")
    for _ in range(4):
        value = stack.pop()
        print(f"  pop() -> {value:3d}  |  ", end="")
        stack.display_horizontal()

    subtitle("2b. Empty stack then try pop")
    while not stack.is_empty():
        stack.pop()
    stack.display_horizontal("Empty:")
    try:
        stack.pop()
    except IndexError as error:
        print(f"  IndexError: {error}")

    return stack


def demo_peek(stack: LinearStack) -> None:
    title("3. PEEK / TOP - View top without modifying stack")
    for value in [100, 200, 300]:
        stack.push(value)
    stack.display_horizontal("Current stack:")
    top = stack.peek()
    print(f"  peek() -> {top}   (stack NOT modified)")
    stack.display_horizontal("Unchanged:")


def demo_queries(stack: LinearStack) -> None:
    title("4. QUERIES - is_empty, is_full, size")
    stack.display_horizontal("Current stack:")
    print(f"  is_empty() -> {stack.is_empty()}")
    print(f"  is_full()  -> {stack.is_full()}")
    print(f"  size()     -> {stack.size()}")

    subtitle("Empty stack")
    empty = LinearStack(5)
    print(f"  is_empty() -> {empty.is_empty()}")
    print(f"  is_full()  -> {empty.is_full()}")
    print(f"  size()     -> {empty.size()}")

    subtitle("Full stack (cap=4)")
    full = LinearStack(4)
    for x in [1, 2, 3, 4]:
        full.push(x)
    full.display_horizontal("Full:")
    print(f"  is_empty() -> {full.is_empty()}")
    print(f"  is_full()  -> {full.is_full()}")
    print(f"  size()     -> {full.size()}")


def demo_search(stack: LinearStack) -> None:
    title("5. SEARCH and CONTAINS - Find elements")
    stack.clear()
    search_stack = LinearStack(capacity=10)
    for value in [10, 20, 30, 40, 50]:
        search_stack.push(value)
    search_stack.display_horizontal("Stack (base->top):")

    subtitle("search(value) -> position from top (1 = top)")
    for value in [50, 30, 10, 99]:
        pos = search_stack.search(value)
        if pos != -1:
            print(f"  search({value:2d}) -> position {pos} from top")
        else:
            print(f"  search({value:2d}) -> not found (-1)")

    subtitle("contains(value) -> True/False")
    for value in [30, 99]:
        print(f"  contains({value}) -> {search_stack.contains(value)}")


def demo_copy(stack: LinearStack) -> None:
    title("6. COPY - Copy stack without changing original")
    copy_demo = LinearStack(capacity=10)
    for value in [10, 20, 30, 40, 50]:
        copy_demo.push(value)
    copy_demo.display_horizontal("Original:")
    copied = copy_demo.copy()
    copied.display_horizontal("Copy:")

    subtitle("Changing copy does not affect original")
    copied.push(999)
    copied.pop()
    copied.pop()
    print("  -> After push(999) and two pop() on COPY:")
    copy_demo.display_horizontal("  Original (unchanged):")
    copied.display_horizontal("  Copy (modified):")


def demo_clear(stack: LinearStack) -> None:
    title("7. CLEAR - Empty stack completely")
    stack.display_horizontal("Before clear():")
    stack.clear()
    stack.display_horizontal("After clear():")
    print(f"  is_empty() -> {stack.is_empty()}")


def demo_display() -> None:
    title("8. DISPLAY - Different stack views")
    stack = LinearStack(8)
    stack.display("New stack (vertical):")
    stack.display_horizontal("New stack (horizontal):")

    for value in [5, 15, 25, 35]:
        stack.push(value)

    stack.display("With 4 elements (vertical):")
    stack.display_horizontal("With 4 elements (horizontal):")


def demo_practical_cases() -> None:
    title("9. PRACTICAL CASES")

    subtitle("9a. Check balanced parentheses")
    def is_balanced(expression: str) -> bool:
        st = LinearStack(capacity=max(1, len(expression)))
        pairs = {')': '(', ']': '[', '}': '{'}
        for ch in expression:
            if ch in "([{":
                st.push(ch)
            elif ch in ")]}":
                if st.is_empty() or st.pop() != pairs[ch]:
                    return False
        return st.is_empty()

    for expr in ["({[a+b]})", "((a+b)", "{[(a)]}", "([)]", ""]:
        ok = is_balanced(expr)
        print(f"  {expr!r:20s} -> {'[OK] Balanced' if ok else '[X] Unbalanced'}")

    subtitle("9b. Reverse a string with stack")
    def reverse_text(text: str) -> str:
        st = LinearStack(capacity=max(1, len(text)))
        for ch in text:
            st.push(ch)
        out = []
        while not st.is_empty():
            out.append(st.pop())
        return "".join(out)

    for word in ["Python", "Hello World", "abcde"]:
        print(f"  {word!r:15s} -> {reverse_text(word)!r}")

    subtitle("9c. Decimal to binary conversion")
    def decimal_to_binary(n: int) -> str:
        if n == 0:
            return "0"
        st = LinearStack(64)
        while n > 0:
            st.push(n % 2)
            n //= 2
        bits = []
        while not st.is_empty():
            bits.append(str(st.pop()))
        return "".join(bits)

    for num in [0, 5, 10, 42, 255]:
        print(f"  decimal {num:4d}  ->  binary {decimal_to_binary(num)}")

    subtitle("9d. Evaluate postfix expression (RPN)")
    def eval_rpn(tokens: list[str]) -> float:
        st = LinearStack(capacity=20)
        ops = {"+", "-", "*", "/"}
        for tok in tokens:
            if tok not in ops:
                st.push(float(tok))
            else:
                b = st.pop()
                a = st.pop()
                if tok == "+":
                    st.push(a + b)
                elif tok == "-":
                    st.push(a - b)
                elif tok == "*":
                    st.push(a * b)
                elif tok == "/":
                    st.push(a / b)
        return st.pop()

    expr1 = ["3", "4", "+", "2", "*"]  # (3 + 4) * 2 = 14
    print(f"  {' '.join(expr1)!r:25s} -> {eval_rpn(expr1):.1f}  (=(3+4)*2)")
    expr2 = ["5", "1", "2", "+", "*"]  # 5 * (1 + 2) = 15
    print(f"  {' '.join(expr2)!r:25s} -> {eval_rpn(expr2):.1f}  (=5*(1+2))")


def main() -> None:
    print(f"\n{SEPARATOR}")
    print("  LINEAR STACK - Python 3.14")
    print(f"{SEPARATOR}")

    stack = demo_push()
    stack = demo_pop(stack)
    demo_peek(stack)
    demo_queries(stack)
    demo_search(stack)
    demo_copy(stack)
    demo_clear(stack)
    demo_display()
    demo_practical_cases()

    title("OPERATIONS SUMMARY")
    print(f"  {'Operation':<18} {'Description':<38} {'Complexity'}")
    print("  " + "-" * 60)
    operations = [
        ("push(v)", "Insert at top",                     "O(1)"),
        ("pop()", "Remove from top",                     "O(1)"),
        ("peek()", "View top without removing",          "O(1)"),
        ("is_empty()", "Check if empty",                 "O(1)"),
        ("is_full()", "Check if full",                   "O(1)"),
        ("size()", "Number of elements",                 "O(1)"),
        ("search(v)", "Position from top",               "O(n)"),
        ("contains(v)", "Check value existence",         "O(n)"),
        ("copy()", "Exact stack copy",                   "O(n)"),
        ("clear()", "Empty stack",                       "O(n)"),
        ("display()", "Show content",                    "O(n)"),
    ]
    for op, desc, complexity in operations:
        print(f"  {op:<18} {desc:<38} {complexity}")

    print(f"\n{SEPARATOR}")
    print("  [OK] Linear stack - all operations demonstrated.")
    print(f"{SEPARATOR}\n")


if __name__ == "__main__":
    main()
