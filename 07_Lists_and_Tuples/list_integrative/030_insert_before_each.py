# -------------------------------------------------
# File Name: 030_insert_before_each.py
# Author: Florentino Báez
# Date: Lists and Tuples
# Description: Insert Element Before Each List Item
# -------------------------------------------------

def insert_before(lst: list, elem) -> list:
    result = []
    for x in lst:
        result.append(elem)
        result.append(x)
    return result


print(insert_before([1, 2, 3], 0))  # [0, 1, 0, 2, 0, 3]
