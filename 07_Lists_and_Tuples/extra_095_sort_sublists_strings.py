# 95. Sort Each Sublist of Strings (and 96: sort by length and value)

def sort_sublists_by_length_and_value(lists: list[list]) -> list[list]:
    return sorted(lists, key=lambda L: (len(L), L))


sample = [[2], [0], [1, 3], [0, 7], [9, 11], [13, 15, 17]]
print(sort_sublists_by_length_and_value(sample))
