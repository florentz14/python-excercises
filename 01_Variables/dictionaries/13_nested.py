# -------------------------------------------------
# File Name: 13_nested.py
# Author: Florentino Báez
# Date: Variables - Dictionaries
# Description: Nested Dictionaries.
#              A dictionary can contain other dictionaries as
#              values, creating a hierarchical data structure.
#              Access nested values by chaining keys:
#              dict["outer"]["inner"].
# -------------------------------------------------

# Example 13: Dictionary with nested structures
print("Example 13: Dictionary with nested structures")
print("-" * 40)

# Each top-level key maps to another dictionary
nested = {
    "user1": {"name": "John", "age": 25},
    "user2": {"name": "Jane", "age": 23}
}
print("Nested dictionary:", nested)

# Chain keys to reach nested values
print("User 1 name:", nested["user1"]["name"])   # Access inner dict value
print("User 2 age:", nested["user2"]["age"])
