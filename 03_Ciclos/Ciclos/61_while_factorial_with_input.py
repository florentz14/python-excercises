# -------------------------------------------------
# File Name: 61_while_factorial_with_input.py
# Author: Florentino Báez
# Course: ITSE-1002: Python Programming
# Date: Module 04 Lab (added)
# Description: Prompt the user for a number and compute its factorial using a while loop.
# -------------------------------------------------

print("=" * 40)
print("While #5 – Factorial (with input)")
print("=" * 40)

# Prompt the user for an integer
n = int(input("Enter a number: "))

# Initialize factorial and counter
fact = 1
k = 1

# Loop while k is less than or equal to n
while k <= n:
    fact *= k
    k += 1

# Print the result
print("Factorial:", fact)
print("=" * 40)
