# -------------------------------------------------
# File Name: 08_keys_values.py
# Author: Florentino Báez
# Date: Variables - Dictionaries
# Description: Get All Keys and Values.
#              keys() returns a view of all keys.
#              values() returns a view of all values.
#              Wrap with list() to get a regular list.
# -------------------------------------------------

# Example 8: Get all keys and values
print("Example 8: Get all keys and values")
print("-" * 40)

courses = {"Math": "A", "Science": "B", "English": "A"}
print("Dictionary:", courses)

print("Keys:", list(courses.keys()))     # All dictionary keys as a list
print("Values:", list(courses.values())) # All dictionary values as a list
