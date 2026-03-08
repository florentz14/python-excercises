# -------------------------------------------------
# File Name: 09_constants_assignment.py
# Author: Florentino Báez
# Date: 01_Variables_and_Types
# Description: Constants (UPPER_CASE convention), multiple assignment,
# -------------------------------------------------

PI = 3.14159
TAX_RATE = 0.16
MAX_ATTEMPTS = 3

print("Constants:")
print(f"PI = {PI}")
print(f"TAX_RATE = {TAX_RATE * 100}%")

# Multiple assignment
x, y = 10, 20
print(f"\nMultiple assignment: x, y = 10, 20 -> x={x}, y={y}")

# Same value to multiple variables
a = b = c = 0
print(f"Same value: a = b = c = 0 -> a={a}, b={b}, c={c}")

# Variable swap without temporary variable
a, b = 5, 10
print(f"\nBefore swap: a={a}, b={b}")
a, b = b, a
print(f"After swap: a={a}, b={b}")
