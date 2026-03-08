# -------------------------------------------------
# File Name: 04_common_member_two_lists.py
# Author: Florentino Báez
# Date: Lists and Tuples
# Description: Check Common Member Between Two Lists
# -------------------------------------------------

def have_common_member(a: list, b: list) -> bool:
    return bool(set(a) & set(b))


print(have_common_member([1, 2, 3], [3, 4, 5]))   # True
print(have_common_member([1, 2], [3, 4]))         # False
