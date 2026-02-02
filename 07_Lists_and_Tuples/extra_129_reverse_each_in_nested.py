# 129. Reverse Each List in Nested List

def reverse_each(lst: list[list]) -> list[list]:
    return [sublist[::-1] for sublist in lst]


sample = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]]
print(reverse_each(sample))
