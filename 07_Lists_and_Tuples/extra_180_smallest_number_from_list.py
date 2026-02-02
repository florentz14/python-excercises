# 180. Create Smallest Number from List of Positive Integers

def smallest_number(lst: list[int]) -> str:
    strs = [str(x) for x in lst]
    from functools import cmp_to_key
    strs.sort(key=cmp_to_key(lambda a, b: (a + b > b + a) - (b + a > a + b)))
    return ''.join(strs)


print(smallest_number([3, 40, 41, 43, 74, 9]))   # 3404143749
print(smallest_number([8, 4, 2, 9, 5, 6, 1, 0]))  # 01245689
