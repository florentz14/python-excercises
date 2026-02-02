# 271. Check If List Has Duplicate Values

def has_duplicates(lst: list) -> bool:
    return len(lst) != len(set(lst))


print(has_duplicates([1, 2, 3, 4, 5, 6, 7]))   # False
print(has_duplicates([1, 2, 3, 3, 4, 5, 5]))  # True
