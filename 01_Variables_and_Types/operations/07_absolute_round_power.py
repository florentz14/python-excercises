# -------------------------------------------------
# File Name: 07_absolute_round_power.py
# Author: Florentino Báez
# Date: 01_Variables_and_Types
# Description: Uses abs(), round(), and pow()/**. Covers absolute value,
# -------------------------------------------------

import math

# Absolute value
num1 = -5
num2 = 3.14
print(f"abs({num1}) = {abs(num1)}")
print(f"abs({num2}) = {abs(num2)}")

# Round function
num3 = 3.14159
num4 = 2.5
num5 = 2.6
print(f"round({num3}) = {round(num3)}")
print(f"round({num3}, 2) = {round(num3, 2)}")
print(f"round({num4}) = {round(num4)}")  # Banker's rounding
print(f"round({num5}) = {round(num5)}")

# Power function
base = 2
exp = 3
print(f"{base} ** {exp} = {base ** exp}")
print(f"pow({base}, {exp}) = {pow(base, exp)}")
print(f"math.pow({base}, {exp}) = {math.pow(base, exp)}")

# Square root using power
print(f"math.sqrt(16) = {math.sqrt(16)}")
print(f"16 ** 0.5 = {16 ** 0.5}")

# Other powers
print(f"10 ** 2 = {10 ** 2}")
print(f"2 ** 0.5 = {2 ** 0.5}")  # Square root