# 202. Find Indexes of All None Items in List

def indexes_of_none(lst: list) -> list[int]:
    return [i for i, x in enumerate(lst) if x is None]


sample = [1, None, 5, 4, None, 0, None, None]
print(indexes_of_none(sample))  # [1, 4, 6, 7]
