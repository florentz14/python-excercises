# 252. Get n Maximum Elements from List

def n_maximum(lst: list[int | float], n: int = 1) -> list:
    return sorted(lst, reverse=True)[:n]


print(n_maximum([1, 2, 3], 1))       # [3]
print(n_maximum([1, 2, 3], 2))       # [3, 2]
print(n_maximum([-2, -3, -1, -2, -4, 0, -5], 3))  # [0, -1, -2]
