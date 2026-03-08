# -------------------------------------------------
# File Name: 10_shuffle_new_list.py
# Author: Florentino Báez
# Date: Lists and Tuples
# Description: Shuffle List and Return New List
# -------------------------------------------------

import random

def shuffle_new(lst: list) -> list:
    result = lst.copy()
    random.shuffle(result)
    return result


print(shuffle_new([1, 2, 3, 4, 5, 6]))
