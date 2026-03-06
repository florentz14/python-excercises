"""For loop: Find maximum in list.
Iterates to find the largest value in a list.
"""
# Author: Florentino Báez


numbers = [15, 42, 8, 99, 23]
max_num = numbers[0]

for num in numbers:
    if num > max_num:
        max_num = num

print("Maximum:", max_num)
