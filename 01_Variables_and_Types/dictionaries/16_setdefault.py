# -------------------------------------------------
# File Name: 16_setdefault.py
# Author: Florentino Báez
# Date: Variables - Dictionaries
# Description: The setdefault() Method.
#              Returns the value of a key if it exists.
#              If the key is missing, inserts it with the
#              given default value and returns that default.
# -------------------------------------------------

# Example 16: Dictionary methods - setdefault()
print("Example 16: Dictionary methods - setdefault()")
print("-" * 40)

employee = {"id": 101, "name": "Bob", "department": "IT"}
print("Original:", employee)

# Key "salary" doesn't exist -> inserts it with default 50000
print("setdefault('salary', 50000):", employee.setdefault("salary", 50000))
print("After setdefault:", employee)

# Key "name" already exists -> returns existing value, does NOT overwrite
print("setdefault('name', 'Unknown'):", employee.setdefault("name", "Unknown"))
print("Final dictionary:", employee)
