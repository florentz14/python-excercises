# -------------------------------------------------
# File Name: 19_power_and_roots.py
# Author: Florentino Báez
# Date: 01_Variables_and_Types
# Description: Power and root calculations (square, cube, nth root).
# -------------------------------------------------

import math


def calculate_power(base, exponent):
    """Calculate base raised to the power of exponent"""
    return base ** exponent


def calculate_square_root(number):
    """Calculate square root"""
    if number < 0:
        return "Error: Square root of negative number"
    return math.sqrt(number)


def calculate_cube_root(number):
    """Calculate cube root"""
    if number < 0:
        return -((-number) ** (1/3))
    return number ** (1/3)


# Examples
print("Power and Roots Calculations:")
print("=" * 30)

# Basic powers
print("Basic Powers:")
print(f"2^3 = {calculate_power(2, 3)}")
print(f"5^2 = {calculate_power(5, 2)}")
print(f"10^0 = {calculate_power(10, 0)}")
print(f"2^-1 = {calculate_power(2, -1)}")

# Using built-in pow
print(f"\nUsing pow(2, 3): {pow(2, 3)}")
print(f"Using math.pow(2, 3): {math.pow(2, 3)}")

# Square roots
print("\nSquare Roots:")
print(f"√4 = {calculate_square_root(4)}")
print(f"√9 = {calculate_square_root(9)}")
print(f"√2 ≈ {calculate_square_root(2):.4f}")
print(f"√(-1) = {calculate_square_root(-1)}")

# Cube roots
print("\nCube Roots:")
print(f"∛8 = {calculate_cube_root(8)}")
print(f"∛27 = {calculate_cube_root(27)}")
print(f"∛-8 = {calculate_cube_root(-8)}")

# Other roots
print("\nOther Roots:")
print(f"4th root of 16 = {16 ** (1/4)}")
print(f"5th root of 32 = {32 ** (1/5)}")

# Powers of 10
print("\nPowers of 10:")
for i in range(-3, 4):
    result = 10 ** i
    print(f"10^{i} = {result}")

# Exponential growth
print("\nExponential Growth:")
initial = 100
rate = 0.05  # 5%
years = 5
final = initial * (1 + rate) ** years
print(f"Initial: ${initial}")
print(f"Growth rate: {rate*100}% per year")
print(f"After {years} years: ${final:.2f}")

# Compound interest formula: A = P(1 + r/n)^(nt)
principal = 1000
rate = 0.07
time = 3
compounded = principal * (1 + rate) ** time
print(f"\nCompound Interest:")
print(f"Principal: ${principal}")
print(f"Rate: {rate*100}%")
print(f"Time: {time} years")
print(f"Final amount: ${compounded:.2f}")

# Pythagorean theorem
print("\nPythagorean Theorem:")
a, b = 3, 4
c = math.sqrt(a**2 + b**2)
print(f"Right triangle: a={a}, b={b}")
print(f"Hypotenuse c = √({a}² + {b}²) = {c}")

# Distance formula
print("\nDistance Formula:")
x1, y1 = 0, 0
x2, y2 = 3, 4
distance = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)
print(f"Distance between ({x1},{y1}) and ({x2},{y2}): {distance}")
