# 261. Most Frequent Element in List

from collections import Counter

def most_frequent_elem(lst: list):
    return Counter(lst).most_common(1)[0][0] if lst else None


print(most_frequent_elem([2, 3, 8, 4, 7, 9, 8, 2, 6, 5, 1, 6, 1, 2, 3, 2, 4, 6, 9, 1, 2]))  # 2
