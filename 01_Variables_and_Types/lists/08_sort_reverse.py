# -------------------------------------------------
# File Name: 08_sort_reverse.py
# Author: Florentino Báez
# Date: 01_Variables_and_Types
# Description: Sort and Reverse a List.
# -------------------------------------------------

print("Example 8: Sort and reverse")
print("-" * 40)

unsorted = [50, 10, 40, 20, 30]
print("Original list:", unsorted)

unsorted.sort()                           # Sort ascending in place
print("Sorted list:", unsorted)

unsorted.reverse()                        # Reverse in place
print("Reversed list:", unsorted)
