# 166. Remove None from List

def remove_none(lst: list) -> list:
    return [x for x in lst if x is not None]


sample = [12, 0, None, 23, None, -55, 234, 89, None, 0, 6, -12]
print(remove_none(sample))
