# -------------------------------------------------
# File Name: 06_loop.py
# Author: Florentino Báez
# Date: Variables - Lists
# Description: Loop Through a List.
#              Use a for loop to iterate over each element.
#              Lists maintain insertion order, so elements
#              are visited in the order they were added.
# -------------------------------------------------

print("Example 6: Loop through a list")
print("-" * 40)

scores = [85, 92, 78, 95, 88]
print("Scores:", scores)

# Iterate over each element in the list
for score in scores:
    print(f"Score: {score}")
