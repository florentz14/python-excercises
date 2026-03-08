# -------------------------------------------------
# File Name: 10_modulo_examples.py
# Author: Florentino Báez
# Date: 01_Variables_and_Types
# Description: Shows modulo operator for even/odd check, 12-hour clock arithmetic,
# -------------------------------------------------

print("Basic modulo operations:")
print(f"10 % 3 = {10 % 3}")
print(f"15 % 4 = {15 % 4}")
print(f"20 % 7 = {20 % 7}")

# Even/Odd check
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print("\nEven/Odd check:")
for num in numbers:
    if num % 2 == 0:
        print(f"{num} is even")
    else:
        print(f"{num} is odd")

# Clock arithmetic (12-hour clock)
hours = [13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24]
print("\n24-hour to 12-hour conversion:")
for hour in hours:
    hour_12 = hour % 12
    if hour_12 == 0:
        hour_12 = 12
    print(f"{hour}:00 -> {hour_12}:00")

# Divisibility check
print("\nDivisibility checks:")
num = 24
divisors = [2, 3, 4, 5, 6, 8]
for div in divisors:
    if num % div == 0:
        print(f"{num} is divisible by {div}")
    else:
        print(f"{num} is not divisible by {div}")

# Negative modulo
print("\nNegative modulo:")
print(f"(-10) % 3 = {(-10) % 3}")
print(f"10 % (-3) = {10 % (-3)}")
print(f"(-10) % (-3) = {(-10) % (-3)}")

# Using modulo for cycling through lists
colors = ["red", "green", "blue"]
print("\nCycling through colors:")
for i in range(10):
    print(f"Index {i}: {colors[i % len(colors)]}")
