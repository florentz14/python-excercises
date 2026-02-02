# 152. Merge Two Sorted Lists Using heapq

import heapq

def merge_sorted(a: list[int], b: list[int]) -> list[int]:
    return list(heapq.merge(a, b))


list1 = [1, 3, 5, 7, 9, 11]
list2 = [0, 2, 4, 6, 8, 10]
print(merge_sorted(list1, list2))
