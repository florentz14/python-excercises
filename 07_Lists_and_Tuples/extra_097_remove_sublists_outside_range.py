# 97. Remove Sublists That Contain Element Outside Given Range

def remove_sublists_outside_range(lists: list[list[int]], low: int, high: int) -> list[list[int]]:
    return [L for L in lists if all(low <= x <= high for x in L)]


sample = [[2], [0], [1, 2, 3], [0, 1, 2, 3, 6, 7], [9, 11], [13, 14, 15, 17]]
print(remove_sublists_outside_range(sample, 13, 17))  # [[13, 14, 15, 17]]
