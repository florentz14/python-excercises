# -------------------------------------------------
# File Name: 10_none.py
# Author: Florentino Báez
# Date: 01_Variables_and_Types
# Description: None type represents absence of value; verification
# -------------------------------------------------

result = None
print("result =", result)
print("type(None):", type(None))

# Typical use: default value, indicate "no value"
def search(name):
    # Simulates search that may find nothing
    if name == "Ana":
        return 25
    return None  # Not found

age = search("Ana")
print(f"\nsearch('Ana'): {age}")

age = search("X")
print(f"search('X'): {age}")

# Check None with 'is' (not with ==)
if age is None:
    print("Age not found.")

# None is falsy (evaluated as False in boolean context)
print(f"\nbool(None): {bool(None)}")
