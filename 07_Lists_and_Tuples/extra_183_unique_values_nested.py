# 183. Unique Values in List of Lists (flatten and unique)

def unique_in_nested(lists: list[list]) -> list:
    return sorted(set(x for L in lists for x in L))


sample = [[1, 2, 3, 5], [2, 3, 5, 4], [0, 5, 4, 1], [3, 7, 2, 1], [1, 2, 1, 2]]
print(unique_in_nested(sample))
