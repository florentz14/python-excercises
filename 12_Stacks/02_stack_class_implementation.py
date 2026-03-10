# -------------------------------------------------
# File Name: 02_stack_class_implementation.py
# Author: Florentino Baez
# Date: 2026-03-09
# Description: Stack class. Encapsulates push(), pop(), peek(), and empty().
# -------------------------------------------------


class Stack:
    def __init__(self):
        self._data = []

    def push(self, x):
        self._data.append(x)

    def pop(self):
        if self.empty():
            raise IndexError("Pop on empty stack")
        return self._data.pop()

    def peek(self):
        if self.empty():
            raise IndexError("Peek on empty stack")
        return self._data[-1]

    def empty(self):
        return len(self._data) == 0

    def __len__(self):
        return len(self._data)


# --- Demo ---
if __name__ == "__main__":
    stack = Stack()
    stack.push("A")
    stack.push("B")
    stack.push("C")
    print("Top:", stack.peek())
    print("Pop:", stack.pop())
    print("Pop:", stack.pop())
    print("Empty?", stack.empty())
