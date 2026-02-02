# 253. Get n Minimum Elements from List

def n_minimum(lst: list[int | float], n: int = 1) -> list:
    return sorted(lst)[:n]


print(n_minimum([1, 2, 3], 1))  # [1]
print(n_minimum([1, 2, 3], 2))  # [1, 2]
print(n_minimum([-2, -3, -1, -2, -4, 0, -5], 3))  # [-5, -4, -3]
