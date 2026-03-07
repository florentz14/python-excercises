# Floor, Ceil, and Square Root Functions in Python

import math

# Floor function - rounds down to nearest integer
num1 = 3.7
num2 = -2.3
print(f"math.floor({num1}) = {math.floor(num1)}")
print(f"math.floor({num2}) = {math.floor(num2)}")

# Ceil function - rounds up to nearest integer
num3 = 3.2
num4 = -2.8
print(f"math.ceil({num3}) = {math.ceil(num3)}")
print(f"math.ceil({num4}) = {math.ceil(num4)}")

# Square root function
num5 = 16
num6 = 2
print(f"math.sqrt({num5}) = {math.sqrt(num5)}")
print(f"math.sqrt({num6}) = {math.sqrt(num6)}")

# Square root of negative number (will raise ValueError)
try:
    print(f"math.sqrt(-1) = {math.sqrt(-1)}")
except ValueError as e:
    print(f"Error: {e}")

# Using ** 0.5 for square root
print(f"25 ** 0.5 = {25 ** 0.5}")
print(f"10 ** 0.5 = {10 ** 0.5}")

# Examples with decimals
print(f"math.floor(5.9) = {math.floor(5.9)}")
print(f"math.ceil(5.1) = {math.ceil(5.1)}")