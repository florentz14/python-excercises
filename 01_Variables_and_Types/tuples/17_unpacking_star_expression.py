# -------------------------------------------------
# File Name: 17_unpacking_star_expression.py
# Author: Florentino Báez
# Date: 01_Variables_and_Types
# Description: Advanced unpacking with * (star expression).
# -------------------------------------------------

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
