# 170. Insert Element After Every nth Position

def insert_after_nth(lst: list, n: int, elem) -> list:
    result = []
    for i, x in enumerate(lst):
        result.append(x)
        if (i + 1) % n == 0 and i != len(lst) - 1:
            result.append(elem)
    return result


sample = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
print(insert_after_nth(sample, 2, 'a'))
print(insert_after_nth(sample, 4, 'b'))
