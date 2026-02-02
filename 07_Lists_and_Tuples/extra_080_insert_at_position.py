# 80. Insert Element at Specified Position

def insert_at(lst: list, index: int, value) -> list:
    result = lst.copy()
    result.insert(index, value)
    return result


sample = [1, 1, 2, 3, 4, 4, 5, 1]
print(insert_at(sample, 2, 12))  # [1, 1, 12, 2, 3, 4, 4, 5, 1]
