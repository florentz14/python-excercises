# -------------------------------------------------
# File Name: 49_for_average_list.py
# Author: Florentino Báez
# Date: 03_Loops
# Description: Average of list.
# -------------------------------------------------

numbers = [85, 90, 78, 92, 88]
total = 0

for num in numbers:
    total = total + num

average = total / len(numbers)
print(f"Average: {average}")
