# 156. Add Two Lists from Right (align by last element, pad left)

def add_lists_right(a: list[int], b: list[int]) -> list[int]:
    na, nb = len(a), len(b)
    if na >= nb:
        b_padded = [0] * (na - nb) + b
        return [a[i] + b_padded[i] for i in range(na)]
    else:
        a_padded = [0] * (nb - na) + a
        return [a_padded[i] + b[i] for i in range(nb)]


print(add_lists_right([2, 4, 7, 0, 5, 8], [3, 3, -1, 7]))  # [2, 4, 10, 3, 4, 15]
