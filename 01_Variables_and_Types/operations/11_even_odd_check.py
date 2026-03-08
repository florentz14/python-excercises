# -------------------------------------------------
# File Name: 11_even_odd_check.py
# Author: Florentino Báez
# Date: 01_Variables_and_Types
# Description: Provides is_even() and is_odd() functions using modulo.
# -------------------------------------------------

def is_even(num):
    return num % 2 == 0


def is_odd(num):
    return num % 2 != 0


# Test with various numbers
test_numbers = [-5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5, 100, 101]

print("Even/Odd Check:")
for num in test_numbers:
    if is_even(num):
        print(f"{num} is even")
    elif is_odd(num):
        print(f"{num} is odd")
    else:
        print(f"{num} is neither even nor odd")

# Alternative way using bitwise operator


def is_even_bitwise(num):
    return (num & 1) == 0


def is_odd_bitwise(num):
    return (num & 1) == 1


print("\nUsing bitwise operators:")
for num in [0, 1, 2, 3, 4, 5]:
    print(f"{num}: even={is_even_bitwise(num)}, odd={is_odd_bitwise(num)}")

# Check if number is divisible by other numbers


def check_divisibility(num, divisor):
    return num % divisor == 0


print("\nDivisibility checks:")
num = 15
for div in [2, 3, 5, 7]:
    result = "divisible" if check_divisibility(num, div) else "not divisible"
    print(f"{num} is {result} by {div}")

# Float numbers (modulo with floats)
print("\nFloat modulo:")
print(f"5.5 % 2 = {5.5 % 2}")
print(f"10.7 % 3 = {10.7 % 3}")
