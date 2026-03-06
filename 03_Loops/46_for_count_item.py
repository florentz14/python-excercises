"""For loop: Count occurrences in list.
Counts how many times an item appears in a list.
"""
# Author: Florentino Báez


fruits = ["apple", "banana", "apple", "orange", "apple", "banana"]
item = "apple"
count = 0

for fruit in fruits:
    if fruit == item:
        count = count + 1

print(f"'{item}' appears {count} times")
