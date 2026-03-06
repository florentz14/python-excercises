"""
Compound assignment operators in Python
=======================================
Topic: Operations (01_Variables_and_Types/operations)
Description: +=, -=, *=, /=, etc. - Shorthand for operate-and-assign in one step.

Complexity: O(1) for all operations (atomic operations).
"""

# Compound assignment operators: operate and assign in a single step
x = 10
x += 5   # x = x + 5
print("x += 5 ->", x)
x *= 2   # x = x * 2
print("x *= 2 ->", x)
x -= 10  # x = x - 10
print("x -= 10 ->", x)
x //= 3  # x = x // 3 (floor division)
print("x //= 3 ->", x)
