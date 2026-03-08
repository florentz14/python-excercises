# -------------------------------------------------
# File Name: 08_select_random_item.py
# Author: Florentino Báez
# Date: Lists and Tuples
# Description: Select Random Item from List
# -------------------------------------------------

import random

def random_item(lst: list):
    return random.choice(lst)


sample = [1, 2, 3, 4, 5]
print(random_item(sample))
