"""For loop: Average of list.
Sums list elements and divides by length for average.
"""
# Author: Florentino Báez


numbers = [85, 90, 78, 92, 88]
total = 0

for num in numbers:
    total = total + num

average = total / len(numbers)
print(f"Average: {average}")
