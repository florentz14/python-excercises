# 82. Generate Combinations of n Distinct Objects from List

import itertools

def combinations_from_list(lst: list, r: int) -> list:
    return list(itertools.combinations(lst, r))


sample = [1, 2, 3, 4, 5]
for c in combinations_from_list(sample, 2)[:5]:
    print(list(c))
