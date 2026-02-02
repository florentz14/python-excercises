# 112. Check If List Is Sorted

def is_sorted(lst: list, ascending: bool = True) -> bool:
    if ascending:
        return all(lst[i] <= lst[i + 1] for i in range(len(lst) - 1))
    return all(lst[i] >= lst[i + 1] for i in range(len(lst) - 1))


print(is_sorted([1, 2, 4, 6, 8]))   # True
print(is_sorted([1, 2, 4, 3, 8]))   # False
