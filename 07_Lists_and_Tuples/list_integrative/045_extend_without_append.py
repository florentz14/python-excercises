# -------------------------------------------------
# File Name: 045_extend_without_append.py
# Author: Florentino Báez
# Date: Lists and Tuples
# Description: Extend List Without Append - prepend second to first: [10,20,30], [...
# -------------------------------------------------

def extend_left(a: list, b: list) -> list:
    return b + a


print(extend_left([10, 20, 30], [40, 50, 60]))
