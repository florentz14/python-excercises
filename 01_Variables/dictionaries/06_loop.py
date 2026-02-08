# -------------------------------------------------
# File Name: 06_loop.py
# Author: Florentino Báez
# Date: Variables - Dictionaries
# Description: Loop Through a Dictionary.
#              Iterating over a dict with 'for key in dict'
#              gives the keys. Use dict[key] to access the
#              corresponding value inside the loop.
# -------------------------------------------------

# Example 6: Loop through dictionary
print("Example 6: Loop through dictionary")
print("-" * 40)

scores = {"Alice": 85, "Bob": 92, "Charlie": 78, "Diana": 95}
print("Scores:", scores)

# Looping over a dict iterates through its keys by default
for key in scores:
    print(f"{key}: {scores[key]}")   # Access value using the key
