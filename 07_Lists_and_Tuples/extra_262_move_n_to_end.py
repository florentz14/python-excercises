# 262. Move First n Elements to End

def move_n_to_end(lst: list, n: int) -> list:
    n = n % len(lst) if lst else 0
    return lst[n:] + lst[:n]


sample = [1, 2, 3, 4, 5, 6, 7, 8]
print(move_n_to_end(sample, 3))  # [4,5,6,7,8,1,2,3]
print(move_n_to_end(sample, 2))  # [3,4,5,6,7,8,1,2]
