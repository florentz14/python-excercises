"""For loop: Find minimum in list.
Iterates to find the smallest value in a list.
"""
# Author: Florentino Báez


numbers = [15, 42, 8, 99, 23]
min_num = numbers[0]

for num in numbers:
    if num < min_num:
        min_num = num

print("Minimum:", min_num)
