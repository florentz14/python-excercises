"""
Logical operators in Python
===========================
Topic: Operations (01_Variables_and_Types/operations)
Description: and, or, not - Combining and negating boolean values.

Complexity: O(1) - Boolean expression evaluation (short-circuit).
"""

# Logical operators: and, or, not
p = True
q = False
print("p =", p, ", q =", q)
print("p and q:", p and q)
print("p or q:", p or q)
print("not p:", not p)

# Practical application: verify combined conditions
age = 25
has_license = True
can_drive = age >= 18 and has_license
print("\nAge:", age, ", License:", has_license)
print("Can drive:", can_drive)
