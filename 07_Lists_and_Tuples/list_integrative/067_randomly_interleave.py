# -------------------------------------------------
# File Name: 067_randomly_interleave.py
# Author: Florentino Báez
# Date: Lists and Tuples
# Description: Randomly Interleave Two Lists
# -------------------------------------------------

import random

def random_interleave(a: list, b: list) -> list:
    result = a + b
    random.shuffle(result)
    return result


print(random_interleave([1, 2, 7, 8], [4, 3, 8, 9]))
