# -------------------------------------------------
# File Name: 93_while_positive_sum.py
# Author: Florentino Báez
# Date: 03_Loops
# Description: Sum positive numbers until 0.
# -------------------------------------------------

total = 0
print("Enter positive numbers (0 or negative to stop):")
while True:
    num = int(input("Number: "))
    if num <= 0:
        break
    total += num
print(f"Sum of positives: {total}")
