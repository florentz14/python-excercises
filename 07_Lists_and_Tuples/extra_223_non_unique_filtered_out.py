# 223. List with Non-Unique Values Filtered Out (keep only unique)

def only_unique(lst: list) -> list:
    return [x for x in lst if lst.count(x) == 1]


print(only_unique([1, 2, 2, 3, 4, 4, 5]))  # [1, 3, 5]
