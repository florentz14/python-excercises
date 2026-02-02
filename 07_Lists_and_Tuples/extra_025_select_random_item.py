# 25. Select Random Item from List

import random

def random_item(lst: list):
    return random.choice(lst)


sample = [1, 2, 3, 4, 5]
print(random_item(sample))
