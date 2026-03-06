# -------------------------------------------------
# File Name: 07_comprehension.py
# Author: Florentino Báez
# Date: Variables - Lists
# Description: List Comprehension.
#              Create lists in one line with the syntax
#              [expr for item in iterable if condition].
#              More concise and often faster than a for loop.
# -------------------------------------------------

print("Example 7: List comprehension")
print("-" * 40)

numbers_list = [1, 2, 3, 4, 5]
print("Original numbers:", numbers_list)

# Basic comprehension: square each number
squared = [x ** 2 for x in numbers_list]
print("Squared numbers:", squared)

# Comprehension with filter: keep only even numbers
even_numbers = [x for x in numbers_list if x % 2 == 0]
print("Even numbers:", even_numbers)
