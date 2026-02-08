# -------------------------------------------------
# File Name: 09_find_and_membership.py
# Author: Florentino Báez
# Date: Variables - Lists
# Description: Find Elements and Check Membership.
#              'in' tests if a value exists in the list.
#              index(x) returns the position of the first
#              occurrence. 'not in' tests for absence.
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
