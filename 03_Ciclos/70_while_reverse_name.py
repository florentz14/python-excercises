# -------------------------------------------------
# File Name: 60_while_reverse_name.py
# Author: Florentino Báez
# Course: ITSE-1002: Python Programming
# Date: Module 04 Lab (added)
# Description: Prompt the user for a name and print it reversed using a while loop.
# -------------------------------------------------

print("=" * 40)
print("While #4 – Reverse a Name (with input)")
print("=" * 40)

# Prompt the user for a name
name = input("Enter your name: ")

# Start index at last character
i = len(name) - 1
rev = ""

# Loop while i is non-negative, append characters in reverse order
while i >= 0:
    rev += name[i]
    i -= 1

# Print the reversed name
print("Reversed:", rev)
print("=" * 40)
