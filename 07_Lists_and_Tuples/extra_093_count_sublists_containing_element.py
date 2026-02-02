# 93. Count Sublists Containing a Particular Element

def count_sublists_containing(lists: list[list], elem) -> int:
    return sum(1 for L in lists if elem in L)


sample = [[1, 3], [5, 7], [1, 11], [1, 15, 7]]
print("Count 1:", count_sublists_containing(sample, 1))  # 3
print("Count 7:", count_sublists_containing(sample, 7))   # 2
