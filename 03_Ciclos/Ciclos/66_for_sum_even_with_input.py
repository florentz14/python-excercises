# -------------------------------------------------
# File Name: 66_for_sum_even_with_input.py
# Author: Florentino Báez
# Course: ITSE-1002: Python Programming
# Date: Module 04 Lab (added)
# Description: Prompt the user for a positive even number and compute the sum of even numbers up to it.
# -------------------------------------------------

print("=" * 40)
print("For #5 – Sum of Even Numbers (with input)")
print("=" * 40)

# Prompt the user for a positive even integer
n = int(input("Enter a positive even number: "))

# Initialize sum
s = 0

# Loop: iterate over even numbers from 2 to n (inclusive)
for x in range(2, n + 1, 2):
    s += x

# Print the result
print("Sum of evens:", s)
print("=" * 40)
