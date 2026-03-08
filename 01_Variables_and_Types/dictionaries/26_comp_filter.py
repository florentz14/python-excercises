# -------------------------------------------------
# File Name: 26_comp_filter.py
# Author: Florentino Báez
# Date: 01_Variables_and_Types
# Description: Dict comprehension with 'if' to filter items.
# -------------------------------------------------

print("2. With Conditional Filter:")
print("-" * 60)
# Only include even numbers in the comprehension
even_squares = {x: x**2 for x in range(1, 11) if x % 2 == 0}
print(f"Even squares: {even_squares}")
print("Comprehension: {x: x**2 for x in range(1, 11) if x % 2 == 0}")
