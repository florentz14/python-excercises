# -------------------------------------------------
# File Name: 31_min_of_three.py
# Author: Florentino Báez
# Date: 02_Conditionals
# Description: Minimum of three numbers
# -------------------------------------------------

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
