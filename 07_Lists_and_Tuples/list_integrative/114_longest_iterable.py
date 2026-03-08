# -------------------------------------------------
# File Name: 114_longest_iterable.py
# Author: Florentino Báez
# Date: Lists and Tuples
# Description: Longest Iterable Among Arguments
# -------------------------------------------------

def longest(*args) -> list | str:
    return max(args, key=len)


print(longest('Red', 'Green', 'Blue'))  # Green
print(longest([1, 2, 3], [1, 2, 3, 4], [1, 2, 3, 4, 5]))  # [1,2,3,4,5]
