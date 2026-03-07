# ------------------------------------------------------------
# File: 17_unpacking_star_expression.py
# Purpose: Advanced unpacking with * (star expression).
# Description: Capture multiple elements into a list.
# ------------------------------------------------------------

numbers = (1, 2, 3, 4, 5)

a, *b, c = numbers
print("a, *b, c = (1,2,3,4,5)")
print("a:", a)
print("b:", b)
print("c:", c)

# First and rest
first, *rest = numbers
print("\nfirst, *rest = numbers")
print("first:", first, "rest:", rest)
