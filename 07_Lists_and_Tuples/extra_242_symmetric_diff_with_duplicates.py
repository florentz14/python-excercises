# 242. Symmetric Difference Without Filtering Duplicates

def symmetric_diff_keep_dupes(a: list, b: list) -> list:
    result = [x for x in a if x not in b]
    result += [x for x in b if x not in a]
    return result


# For true multiset: use Counter
from collections import Counter
def symmetric_diff_multiset(a: list, b: list) -> list:
    ca, cb = Counter(a), Counter(b)
    result = []
    for x in (set(a) | set(b)):
        diff = ca[x] - cb[x]
        result.extend([x] * abs(diff))
    return result


print(symmetric_diff_keep_dupes([10, 20, 30], [20, 40, 30]))  # [10, 40]
