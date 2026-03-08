# -------------------------------------------------
# File Name: 42_for_find_min.py
# Author: Florentino Báez
# Date: 03_Loops
# Description: Find minimum in list.
# -------------------------------------------------

numbers = [15, 42, 8, 99, 23]
min_num = numbers[0]

for num in numbers:
    if num < min_num:
        min_num = num

print("Minimum:", min_num)
