# -------------------------------------------------
# File Name: 089_iterate_cyclically_at_index.py
# Author: Florentino Báez
# Date: Lists and Tuples
# Description: Iterate List Cyclically Starting at Given Index
# -------------------------------------------------

def iterate_from_index(lst: list, start: int) -> list:
    return lst[start:] + lst[:start]


sample = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
print(iterate_from_index(sample, 3))  # ['d', 'e', 'f', 'g', 'h', 'a', 'b', 'c']
print(iterate_from_index(sample, 5))  # ['f', 'g', 'h', 'a', 'b', 'c', 'd', 'e']
