# -------------------------------------------------
# File Name: 25_variable_swapping.py
# Author: Florentino Báez
# Date: 01_Variables_and_Types
# Description: Variable swapping and compound assignment
# -------------------------------------------------

print("Swapping Variables")
# Initial values
x = 5
print(f"Initial value of x: {x}")
x += 3  # Equivalent to x = x + 3
print(f"After x += 3: {x}")
x *= 2  # Equivalent to x = x * 2
print(f"After x *= 2: {x}")
# Second variable for swap demo
y = 10
print(f"Initial value of y: {y}")
x, y = y, x  # Swapping values
print(f"After swapping, x: {x}, y: {y}")
print("*" * 30)
