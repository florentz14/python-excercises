# -------------------------------------------------
# File Name: 41_for_find_max.py
# Author: Florentino Báez
# Date: 03_Loops
# Description: Find maximum in list.
# -------------------------------------------------

numbers = [15, 42, 8, 99, 23]
max_num = numbers[0]

for num in numbers:
    if num > max_num:
        max_num = num

print("Maximum:", max_num)
