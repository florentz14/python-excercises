# -------------------------------------------------
# File Name: 14_comprehension.py
# Author: Florentino Báez
# Date: Variables - Dictionaries
# Description: Dictionary Comprehension.
#              Create dictionaries in one line using the syntax
#              {key_expr: value_expr for item in iterable}.
#              Supports optional 'if' filtering.
# -------------------------------------------------

# Example 14: Dictionary comprehension
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
