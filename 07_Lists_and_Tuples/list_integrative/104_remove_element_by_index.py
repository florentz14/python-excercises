# -------------------------------------------------
# File Name: 104_remove_element_by_index.py
# Author: Florentino Báez
# Date: Lists and Tuples
# Description: Remove Element from List by Index
# -------------------------------------------------

def remove_at(lst: list, index: int) -> list:
    return lst[:index] + lst[index + 1:]


sample = ['Ricky Rivera', 98, 'Math', 90, 'Science']
print(remove_at(sample, 0))  # [98, 'Math', 90, 'Science']
