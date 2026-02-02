# 263. Move Last n Elements to Start

def move_n_to_start(lst: list, n: int) -> list:
    n = n % len(lst) if lst else 0
    return lst[-n:] + lst[:-n]


sample = [1, 2, 3, 4, 5, 6, 7, 8]
print(move_n_to_start(sample, 3))  # [6,7,8,1,2,3,4,5]
