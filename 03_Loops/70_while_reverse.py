"""While loop: Reverse a name/string.
User enters a string; prints it reversed using a while loop.
"""
# Author: Florentino Báez


name = input("Enter your name: ")

# Build reversed string by iterating from end to start
reversed_name = ""
i = len(name) - 1

while i >= 0:
    reversed_name += name[i]
    i -= 1

print(f"Reversed: {reversed_name}")
