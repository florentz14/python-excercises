# 30. Count Frequency of Elements in List

from collections import Counter

def frequency(lst: list) -> dict:
    return dict(Counter(lst))


# Or manual: {x: lst.count(x) for x in set(lst)}
print(frequency([1, 2, 2, 3, 3, 3, 4]))
