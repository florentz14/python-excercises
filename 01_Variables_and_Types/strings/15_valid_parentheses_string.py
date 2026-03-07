# ------------------------------------------------------------
# File: 15_valid_parentheses_string.py
# Purpose: Valid parentheses in string.
# Description: Stack-based. O(n).
# ------------------------------------------------------------

def is_valid(s: str) -> bool:
    stack = []
    pairs = {")": "(", "]": "[", "}": "{"}
    for c in s:
        if c in "([{":
            stack.append(c)
        elif c in ")]}":
            if not stack or stack[-1] != pairs[c]:
                return False
            stack.pop()
    return len(stack) == 0

if __name__ == "__main__":
    print(is_valid("()[]{}"))   # True
    print(is_valid("(]"))       # False
