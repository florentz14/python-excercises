# -------------------------------------------------
# File Name: 11_comprehension.py
# Author: Florentino Báez
# Date: Variables - Sets
# Description: Set Comprehension.
#              Create sets in one line with the syntax
#              {expr for item in iterable if condition}.
#              Duplicates from the source are automatically
#              removed in the resulting set.
# -------------------------------------------------

# Example 16: Set comprehension
print("Example 16: Set comprehension")
print("-" * 40)

numbers_list = [1, 2, 2, 3, 3, 3, 4, 4, 4, 4]

# Basic comprehension: square each number (duplicates removed in set)
squared_set = {x**2 for x in numbers_list}
print("Original numbers:", numbers_list)
print("Squared set (removes duplicates):", squared_set)

# Comprehension with filter: only square even numbers
even_squared = {x**2 for x in numbers_list if x % 2 == 0}
print("Even squared set:", even_squared)
