# -------------------------------------------------
# File Name: 09_number_classification.py
# Author: Florentino Báez
# Date: 02_Conditionals
# Description: if/elif/else para clasificar un número.
# -------------------------------------------------

print("Example 1: Number Classification")
print("-" * 40)
number = 15

if number > 0:
    print(f"{number} is a positive number")
elif number < 0:
    print(f"{number} is a negative number")
else:
    print(f"{number} is zero")
