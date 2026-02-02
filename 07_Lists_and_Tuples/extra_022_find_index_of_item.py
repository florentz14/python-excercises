# 22. Find Index of an Item in a List

def find_index(lst: list, item) -> int:
    return lst.index(item) if item in lst else -1


# Or use lst.index(item) directly
sample = [10, 20, 30, 40]
print(sample.index(30))  # 2
