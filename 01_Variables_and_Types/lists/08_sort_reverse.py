# -------------------------------------------------
# File Name: 08_sort_reverse.py
# Author: Florentino Báez
# Date: Variables - Lists
# Description: Sort and Reverse a List.
#              sort() sorts in place (ascending by default).
#              reverse() reverses in place. Both modify the
#              original list and return None.
# -------------------------------------------------

print("Example 8: Sort and reverse")
print("-" * 40)

unsorted = [50, 10, 40, 20, 30]
print("Original list:", unsorted)

unsorted.sort()                           # Sort ascending in place
print("Sorted list:", unsorted)

unsorted.reverse()                        # Reverse in place
print("Reversed list:", unsorted)
