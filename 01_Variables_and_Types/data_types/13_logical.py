# -------------------------------------------------
# File Name: 13_logical.py
# Author: Florentino Báez
# Date: 01_Variables_and_Types
# Description: Logical operators (and, or, not), short-circuit
# -------------------------------------------------

p = True
q = False
print("p =", p, ", q =", q)
print("p and q:", p and q)
print("p or q:", p or q)
print("not p:", not p)
print("not q:", not q)

# Combine with comparisons
print("\n--- With comparisons ---")
age = 20
has_license = True
print("age >= 18 and has_license:", age >= 18 and has_license)

# Multiple conditions
x = 5
print("1 < x < 10:", 1 < x < 10)
print("x > 3 and x < 7:", x > 3 and x < 7)

# or: at least one true
is_weekend = False
is_holiday = True
print("\nis_weekend or is_holiday:", is_weekend or is_holiday)

# not: negation
raining = True
print("not raining:", not raining)

# Short-circuit: or returns the first truthy value
print("\n--- Short-circuit ---")
print("0 or 42:", 0 or 42)
print("'' or 'default':", "" or "default")
print("1 and 2:", 1 and 2)
