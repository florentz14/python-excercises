# -------------------------------------------------
# File Name: 28_while_sum_until_zero.py
# Author: Florentino Báez
# Date: 03_Loops
# Description: Sum until zero.
# -------------------------------------------------

total = 0

data = int(input("Enter a number (0 to exit): "))

while data != 0:
    total = total + data
    data = int(input("Enter a number (0 to exit): "))

print("The total sum is:", total)
