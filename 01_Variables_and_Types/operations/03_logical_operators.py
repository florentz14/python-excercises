# -------------------------------------------------
# File Name: 03_logical_operators.py
# Author: Florentino Báez
# Date: 01_Variables_and_Types
# Description: Shows logical operators (and, or, not) with boolean and numeric
# -------------------------------------------------

a = True
b = False

print(f"a = {a}, b = {b}")

# AND operator
print(f"a and b: {a and b}")

# OR operator
print(f"a or b: {a or b}")

# NOT operator
print(f"not a: {not a}")
print(f"not b: {not b}")

# Combining with comparisons
x = 10
y = 5
z = 15

print(f"x > y and y < z: {x > y and y < z}")
print(f"x < y or y < z: {x < y or y < z}")
print(f"not (x == y): {not (x == y)}")
