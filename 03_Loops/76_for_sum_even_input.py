# -------------------------------------------------
# File Name: 76_for_sum_even_input.py
# Author: Florentino Báez
# Date: 03_Loops
# Description: Sum of even numbers with input.
# -------------------------------------------------

print("=" * 40)
print("For #5 – Sum of Even Numbers (with input)")
print("=" * 40)

n = int(input("Enter a positive even number: "))

s = 0

# Even numbers from 2 to n inclusive
for x in range(2, n + 1, 2):
    s += x

print("Sum of evens:", s)
print("=" * 40)
