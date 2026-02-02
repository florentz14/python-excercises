# 111. Access Multiple Elements at Specified Indices

def elements_at_indices(lst: list, indices: list[int]) -> list:
    return [lst[i] for i in indices if 0 <= i < len(lst)]


sample = [2, 3, 8, 4, 7, 9, 8, 2, 6, 5, 1, 6]
print(elements_at_indices(sample, [0, 3, 5, 7, 10]))  # [2, 4, 9, 2, 1]
