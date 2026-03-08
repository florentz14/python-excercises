# -------------------------------------------------
# File Name: 24_comprehension.py
# Author: Florentino Báez
# Date: 01_Variables_and_Types
# Description: Dictionary comprehension: {key: value for item in iterable}.
# -------------------------------------------------

print("Example 14: Dictionary comprehension")
print("-" * 40)

numbers = [1, 2, 3, 4, 5]

# Basic comprehension: map each number to its square
squared = {x: x**2 for x in numbers}
print("Numbers:", numbers)
print("Squared dictionary:", squared)

# Comprehension with condition: only include even numbers
even_squares = {x: x**2 for x in numbers if x % 2 == 0}
print("Even squared dictionary:", even_squares)
