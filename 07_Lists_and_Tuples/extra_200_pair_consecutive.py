# 200. Pair Consecutive Elements: [1,2,3,4,5,6] -> [[1,2],[2,3],[3,4],[4,5],[5,6]]

def pair_consecutive(lst: list) -> list[list]:
    return [[lst[i], lst[i + 1]] for i in range(len(lst) - 1)]


print(pair_consecutive([1, 2, 3, 4, 5, 6]))
print(pair_consecutive([1, 2, 3, 4, 5]))
