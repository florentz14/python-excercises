# -------------------------------------------------
# File Name: 57_last_value_satisfying.py
# Author: Florentino Báez
# Date: Lists and Tuples
# Description: Last Value That Satisfies Function
# -------------------------------------------------

def last_value_where(lst: list, predicate):
    for x in reversed(lst):
        if predicate(x):
            return x
    return None


print(last_value_where([1, 2, 3, 4], lambda x: x < 4))  # 3
print(last_value_where([1, 2, 3, 4], lambda x: x % 2 == 0))  # 4
