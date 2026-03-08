# -------------------------------------------------
# File Name: 075_strictly_increasing.py
# Author: Florentino Báez
# Date: Lists and Tuples
# Description: Check If List Is Strictly Increasing (or can be by removing one ele...
# -------------------------------------------------

def is_strictly_increasing(lst: list[int]) -> bool:
    return all(lst[i] < lst[i + 1] for i in range(len(lst) - 1))


def strictly_increasing_after_one_removal(lst: list[int]) -> bool:
    if is_strictly_increasing(lst):
        return True
    for i in range(len(lst)):
        if is_strictly_increasing(lst[:i] + lst[i + 1:]):
            return True
    return False


print(strictly_increasing_after_one_removal([1, 2, 3]))
print(strictly_increasing_after_one_removal([1, 3, 2, 4]))
