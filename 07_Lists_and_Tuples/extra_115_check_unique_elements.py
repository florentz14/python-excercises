# 115. Check If All Elements in List Are Unique

def all_unique(lst: list) -> bool:
    return len(lst) == len(set(lst))


print(all_unique([1, 2, 4, 6, 8]))   # True
print(all_unique([1, 2, 4, 6, 8, 2]))  # False
