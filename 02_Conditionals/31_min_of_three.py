"""
Simple conditional: Minimum of three numbers
============================================
Topic: Conditionals (02_Conditionals)
Description: Find the smallest of three numbers without min().
"""

a = float(input("Number 1: "))
b = float(input("Number 2: "))
c = float(input("Number 3: "))

if a <= b and a <= c:
    smallest = a
elif b <= a and b <= c:
    smallest = b
else:
    smallest = c

print(f"Smallest: {smallest}")
