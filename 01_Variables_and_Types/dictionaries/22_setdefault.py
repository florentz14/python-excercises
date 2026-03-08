# -------------------------------------------------
# File Name: 22_setdefault.py
# Author: Florentino Báez
# Date: 01_Variables_and_Types
# Description: setdefault() returns value if key exists; otherwise inserts
# -------------------------------------------------

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
