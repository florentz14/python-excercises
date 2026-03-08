# -------------------------------------------------
# File Name: 08_keys_values.py
# Author: Florentino Báez
# Date: 01_Variables_and_Types
# Description: Get all keys and values with keys() and values().
# -------------------------------------------------

print("Example 8: Get all keys and values")
print("-" * 40)

courses = {"Math": "A", "Science": "B", "English": "A"}
print("Dictionary:", courses)

print("Keys:", list(courses.keys()))     # All dictionary keys as a list
print("Values:", list(courses.values())) # All dictionary values as a list
