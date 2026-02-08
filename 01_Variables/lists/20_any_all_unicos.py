# -------------------------------------------------
# File Name: 20_any_all_unicos.py
# Author: Florentino Báez
# Date: Variables - Lists
# Description: any(), all(), and Unique Elements.
#              any() returns True if at least one element
#              satisfies the condition. all() returns True
#              only if every element does. dict.fromkeys()
#              removes duplicates while preserving order.
# -------------------------------------------------

print("=== any and all ===")
numeros1 = [2, 4, 6, 8]
numeros2 = [2, 4, 5, 8]

print(f"List 1: {numeros1}")
# all() — True only if every element passes the test
print(f"  All even? {all(x % 2 == 0 for x in numeros1)}")     # True

print(f"List 2: {numeros2}")
# any() — True if at least one element passes the test
print(f"  Any even? {any(x % 2 == 0 for x in numeros2)}")     # True
# all() fails because 5 is odd
print(f"  All even? {all(x % 2 == 0 for x in numeros2)}\n")   # False

print("=== Unique elements (preserving order) ===")
con_duplicados = [1, 2, 2, 3, 3, 3, 4, 5]
# dict.fromkeys() keeps only the first occurrence of each value
sin_duplicados = list(dict.fromkeys(con_duplicados))
print(f"Original:          {con_duplicados}")
print(f"Without duplicates: {sin_duplicados}")
