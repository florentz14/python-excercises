# -------------------------------------------------
# File Name: 09_find_and_membership.py
# Author: Florentino Báez
# Date: 01_Variables_and_Types
# Description: Find Elements and Check Membership.
# -------------------------------------------------

print("Example 9: Find element and check membership")
print("-" * 40)

items = ["pen", "pencil", "eraser", "ruler", "notebook"]
print("List:", items)

# 'in' checks membership (O(n) for lists)
if "pen" in items:
    print("'pen' is in the list")
    print("Index of 'pen':", items.index("pen"))  # Returns first match index

# 'not in' checks absence
if "marker" not in items:
    print("'marker' is not in the list")
