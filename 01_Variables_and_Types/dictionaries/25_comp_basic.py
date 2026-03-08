# -------------------------------------------------
# File Name: 25_comp_basic.py
# Author: Florentino Báez
# Date: 01_Variables_and_Types
# Description: Basic dict comprehension: {key: value for item in iterable}.
# -------------------------------------------------

print("1. Basic Dictionary Comprehension:")
print("-" * 60)
# Create a dictionary mapping numbers to their squares
squares = {x: x**2 for x in range(1, 6)}
print(f"Squares: {squares}")
print("Comprehension: {x: x**2 for x in range(1, 6)}")
