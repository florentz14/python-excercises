# 15. Shuffle List

import random

def shuffle_list(lst: list) -> list:
    result = lst.copy()
    random.shuffle(result)
    return result


sample = [1, 2, 3, 4, 5]
print(shuffle_list(sample))
