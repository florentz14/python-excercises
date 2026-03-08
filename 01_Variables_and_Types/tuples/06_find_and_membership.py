# -------------------------------------------------
# File Name: 06_find_and_membership.py
# Author: Florentino Báez
# Date: 01_Variables_and_Types
# Description: Find Elements and Check Membership.
# -------------------------------------------------

print("Example 6: Find element and check membership")
print("-" * 40)

items = ("pen", "pencil", "eraser", "ruler", "notebook")
print("Tuple:", items)

# 'in' checks membership (returns True/False)
if "pen" in items:
    print("'pen' is in the tuple")
    print("Index of 'pen':", items.index("pen"))  # Returns first occurrence index

# 'not in' checks absence
if "marker" not in items:
    print("'marker' is not in the tuple")
