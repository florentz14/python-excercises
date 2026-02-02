# 149. Generate All Combinations of List Elements (powerset)

import itertools

def all_combinations(lst: list) -> list[list]:
    return [list(c) for r in range(len(lst) + 1) for c in itertools.combinations(lst, r)]


sample = ['orange', 'red', 'green', 'blue']
print(len(all_combinations(sample)))  # 16
