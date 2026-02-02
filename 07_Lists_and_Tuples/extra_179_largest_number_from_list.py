# 179. Create Largest Number from List of Positive Integers (concatenate sorted)

def largest_number(lst: list[int]) -> str:
    """Sort so concatenation is largest: a before b if a+b >= b+a."""
    from functools import cmp_to_key
    strs = [str(x) for x in lst]
    strs.sort(key=cmp_to_key(lambda a, b: -1 if (a + b >= b + a) else 1))
    return ''.join(strs)


print(largest_number([3, 40, 41, 43, 74, 9]))   # 9744341403
print(largest_number([10, 40, 20, 30, 50, 60])) # 605040302010
