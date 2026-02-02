# 241. Frequency Dict from List (unique values as keys, count as value)

from collections import Counter

def frequency_dict(lst: list) -> dict:
    return dict(Counter(lst))


print(frequency_dict(['a', 'b', 'a', 'c', 'a', 'b', 'f', 'e', 'e']))
