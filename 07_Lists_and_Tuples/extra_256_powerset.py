# 256. Powerset of Iterable

import itertools

def powerset(iterable) -> list[tuple]:
    s = list(iterable)
    return [tuple(c) for r in range(len(s) + 1) for c in itertools.combinations(s, r)]


print(powerset([1, 2]))
print(len(powerset([1, 2, 3, 4])))  # 16
