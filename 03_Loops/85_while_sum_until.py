# -------------------------------------------------
# File Name: 85_while_sum_until.py
# Author: Florentino Báez
# Date: 03_Loops
# Description: Sum numbers until -1.
# -------------------------------------------------

print("Example: Sum numbers (enter -1 to stop)")
print("-" * 40)

total = 0
while True:
    num = int(input("Enter a number (-1 to stop): "))
    if num == -1:
        break
    total += num

print(f"Total sum: {total}")
