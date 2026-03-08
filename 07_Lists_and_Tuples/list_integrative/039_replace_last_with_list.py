# -------------------------------------------------
# File Name: 039_replace_last_with_list.py
# Author: Florentino Báez
# Date: Lists and Tuples
# Description: Replace Last Element with Another List. [1,3,5,7,9,10], [2,4,6,8] -...
# -------------------------------------------------

def replace_last_with_list(lst: list, other: list) -> list:
    return lst[:-1] + other


print(replace_last_with_list([1, 3, 5, 7, 9, 10], [2, 4, 6, 8]))
