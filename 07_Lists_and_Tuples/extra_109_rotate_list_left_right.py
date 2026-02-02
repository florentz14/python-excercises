# 109. Rotate List Left or Right by N Items

def rotate_left(lst: list, n: int) -> list:
    n = n % len(lst)
    return lst[n:] + lst[:n]


def rotate_right(lst: list, n: int) -> list:
    n = n % len(lst)
    return lst[-n:] + lst[:-n]


sample = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print("Left 4:", rotate_left(sample, 4))
print("Right 4:", rotate_right(sample, 4))
