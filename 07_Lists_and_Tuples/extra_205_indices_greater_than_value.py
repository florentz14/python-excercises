# 205. Indices of Elements Greater Than Specified Value

def indices_greater_than(lst: list[int | float], value: int | float) -> list[int]:
    return [i for i, x in enumerate(lst) if x > value]


sample = [1234, 1522, 1984, 19372, 1000, 2342, 7626]
print(indices_greater_than(sample, 3000))   # [3, 6]
print(indices_greater_than(sample, 20000))  # []
