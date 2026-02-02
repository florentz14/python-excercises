# 134. Difference Between Two Lists Including Duplicates (multiset difference)

from collections import Counter

def difference_with_duplicates(a: list, b: list) -> list:
    ca, cb = Counter(a), Counter(b)
    result = []
    for x, count in ca.items():
        result.extend([x] * (count - cb.get(x, 0)))
    return result


list1 = [1, 1, 2, 3, 3, 4, 4, 5, 6, 7]
list2 = [1, 1, 2, 4, 5, 6]
print(difference_with_duplicates(list1, list2))  # [3, 3, 4, 7]
