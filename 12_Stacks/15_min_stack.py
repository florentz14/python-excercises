"""
12_Stacks - Min Stack
======================
Stack that supports getMin() in O(1) time.
All operations: push, pop, top, getMin in O(1).

LeetCode 155 - Min Stack

Idea: Keep a parallel stack of minimums.
When we push x, min_stack pushes min(x, current_min).
When we pop, min_stack pops too.
"""


class MinStack:
    """Stack with O(1) getMin."""

    def __init__(self):
        self.stack = []
        self.min_stack = []

    def push(self, val: int) -> None:
        self.stack.append(val)
        if not self.min_stack or val <= self.min_stack[-1]:
            self.min_stack.append(val)
        else:
            self.min_stack.append(self.min_stack[-1])

    def pop(self) -> None:
        if self.stack:
            self.stack.pop()
            self.min_stack.pop()

    def top(self) -> int:
        return self.stack[-1] if self.stack else None

    def get_min(self) -> int:
        return self.min_stack[-1] if self.min_stack else None


if __name__ == "__main__":
    print("=== Min Stack ===\n")

    ms = MinStack()
    ms.push(-2)
    ms.push(0)
    ms.push(-3)

    print(f"push(-2), push(0), push(-3)")
    print(f"getMin(): {ms.get_min()}")  # -3

    ms.pop()
    print(f"\npop()")
    print(f"top(): {ms.top()}")  # 0
    print(f"getMin(): {ms.get_min()}")  # -2
