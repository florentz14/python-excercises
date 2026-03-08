# -------------------------------------------------
# File Name: 12_membership.py
# Author: Florentino Báez
# Date: 01_Variables_and_Types
# Description: Membership operators in and not in to check if an
# -------------------------------------------------

text = "Python is great"
print("'es' in text:", "es" in text)
print("'Java' in text:", "Java" in text)
print("'xyz' not in text:", "xyz" not in text)

# With characters
print("\n'P' in 'Python':", "P" in "Python")

# With lists
numbers = [1, 2, 3, 4, 5]
print("\n3 in numbers:", 3 in numbers)
print("10 not in numbers:", 10 not in numbers)

# Application: validate input
valid_options = ["y", "n", "yes", "no"]
response = "y"
if response.lower() in valid_options:
    print("\nValid response")
