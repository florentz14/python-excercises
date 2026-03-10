# -------------------------------------------------
# File Name: 03_parentheses.py
# Author: Florentino Baez
# Date: 2026-03-09
# Description: Parenthesis balancing. Stack verifies ( ) [ ] { } are balanced.
# -------------------------------------------------

def is_balanced(text):
    stack = []
    pairs = {")": "(", "]": "[", "}": "{"}
    for char in text:
        if char in "([{":
            stack.append(char)
        elif char in ")]}":
            if not stack or stack[-1] != pairs[char]:
                return False
            stack.pop()
    return len(stack) == 0


print(is_balanced("(2+3)*[4-1]"))   # True
print(is_balanced("((())"))         # False
print(is_balanced("{[()]}"))        # True
print(is_balanced("{[)]}"))         # False
