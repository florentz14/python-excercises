# -------------------------------------------------
# File Name: 46_for_count_item.py
# Author: Florentino Báez
# Date: 03_Loops
# Description: Count occurrences in list.
# -------------------------------------------------

fruits = ["apple", "banana", "apple", "orange", "apple", "banana"]
item = "apple"
count = 0

for fruit in fruits:
    if fruit == item:
        count = count + 1

print(f"'{item}' appears {count} times")
