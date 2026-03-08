# -------------------------------------------------
# File Name: 06_loop.py
# Author: Florentino Báez
# Date: 01_Variables_and_Types
# Description: Loop through dictionary keys, values, and items().
# -------------------------------------------------

print("Example 6: Loop through dictionary")
print("-" * 40)

# Create a dictionary
scores = {"Alice": 85, "Bob": 92, "Charlie": 78, "Diana": 95}
print("Scores:", scores)

# Loop through the dictionary
for key in scores:
    print(f"{key}: {scores[key]}")   # Access value using the key

print("-" * 60)

# loop through the dictionary and print the key and value
print("Loop through the dictionary and print the only the values")
for value in scores.values():
    print(f"Value: {value}")
print("-" * 60)

# loop through the dictionary and print the keys
print("Loop through the dictionary and print the keys")
for key in scores.keys():
    print(f"Key: {key}")
print("-" * 60)

# loop through the dictionary and print the values and the keys
print("Loop through the dictionary and print the values and the keys")
for key, value in scores.items():
    print(f"Key: {key}, Value: {value}")
print("-" * 60)

