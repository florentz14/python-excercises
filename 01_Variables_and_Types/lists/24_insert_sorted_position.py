# -------------------------------------------------
# File Name: 24_insert_sorted_position.py
# Author: Florentino Báez
# Date: 01_Variables_and_Types
# Description: Inserts an item into a sorted list while
# -------------------------------------------------

def insert_sorted(lst, item):
    """Insert item into sorted list maintaining order."""
    for i in range(len(lst)):
        if item < lst[i]:
            lst.insert(i, item)
            return
    lst.append(item)

sorted_list = [1, 3, 5, 7]
print("Before insert:", sorted_list)
insert_sorted(sorted_list, 4)
print("After insert 4:", sorted_list)
insert_sorted(sorted_list, 0)
print("After insert 0:", sorted_list)