# -------------------------------------------------
# File Name: 02_shuffle_list.py
# Author: Florentino Báez
# Date: Lists and Tuples
# Description: Demonstrates shuffle list.
# -------------------------------------------------

import random

def shuffle_list(lst: list) -> list:
    result = lst.copy()
    random.shuffle(result)
    return result


sample = [1, 2, 3, 4, 5]
print(shuffle_list(sample))
