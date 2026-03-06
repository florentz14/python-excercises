# -------------------------------------------------
# File Name: 03_negative_indexing.py
# Author: Florentino Báez
# Date: Variables - Tuples
# Description: Negative Indexing.
#              Negative indices count from the end:
#              -1 is the last element, -2 is second to last,
#              -3 is third from the end, and so on.
# -------------------------------------------------

print("Example 3: Negative indexing")
print("-" * 40)

colors = ("red", "green", "blue", "yellow")
print("Tuple:", colors)

print("Second to last element:", colors[-2])   # "blue"
print("Third from end:", colors[-3])           # "green"
