# 116. Sort List of Lists by Given Index of Inner List

def sort_by_inner_index(lst: list[tuple], index: int) -> list:
    return sorted(lst, key=lambda t: t[index])


sample = [('Greyson Fulton', 98, 99), ('Brady Kent', 97, 96), ('Wyatt Knott', 91, 94)]
print(sort_by_inner_index(sample, 0))  # by name
print(sort_by_inner_index(sample, 2))  # by third element
