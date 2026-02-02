# 153. Check If Element Occurs at Least n Times in List

def occurs_at_least_n(lst: list, elem, n: int) -> bool:
    return lst.count(elem) >= n


sample = [0, 1, 3, 5, 0, 3, 4, 5, 0, 8, 0, 3, 6, 0, 3, 1, 1, 0]
print(occurs_at_least_n(sample, 3, 4))  # True
print(occurs_at_least_n(sample, 8, 3))  # False
