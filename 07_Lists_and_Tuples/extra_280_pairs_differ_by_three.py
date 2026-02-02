# 280. Find All Pairs of Integers That Differ by 3

def pairs_differ_by_k(lst: list[int], k: int = 3) -> list[list[int]]:
    result = []
    for i in range(len(lst)):
        for j in range(i + 1, len(lst)):
            if abs(lst[i] - lst[j]) == k:
                result.append(sorted([lst[i], lst[j]]))
    return result


print(pairs_differ_by_k([0, 3, 4, 7, 9]))       # [[0, 3], [4, 7]]
print(pairs_differ_by_k([0, -3, -5, -7, -8]))   # [[-3, 0], [-8, -5]]
print(pairs_differ_by_k([1, 2, 3, 4, 5]))       # [[1, 4], [2, 5]]
print(pairs_differ_by_k([100, 102, 103, 114, 115]))  # [[100, 103]]
