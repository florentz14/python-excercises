# -------------------------------------------------
# File Name: 70_while_reverse.py
# Author: Florentino Báez
# Date: 03_Loops
# Description: Reverse a name/string.
# -------------------------------------------------

name = input("Enter your name: ")

# Build reversed string by iterating from end to start
reversed_name = ""
i = len(name) - 1

while i >= 0:
    reversed_name += name[i]
    i -= 1

print(f"Reversed: {reversed_name}")
