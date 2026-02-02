# 18. Generate All Permutations of a List

import itertools

def all_permutations(lst: list) -> list:
    return list(itertools.permutations(lst))


sample = [1, 2, 3]
print(all_permutations(sample))
