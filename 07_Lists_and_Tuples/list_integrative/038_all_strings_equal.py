# -------------------------------------------------
# File Name: 038_all_strings_equal.py
# Author: Florentino Báez
# Date: Lists and Tuples
# Description: Check If All Items in List Equal Given String
# -------------------------------------------------

def all_equal_to(lst: list[str], s: str) -> bool:
    return all(x == s for x in lst)


print(all_equal_to(['a', 'a', 'a'], 'a'))   # True
print(all_equal_to(['a', 'b', 'a'], 'a'))   # False
