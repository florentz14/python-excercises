# 236. Find Parity Outliers (majority even -> return odd; majority odd -> return even)

def parity_outliers(lst: list[int]) -> list[int]:
    even = [x for x in lst if x % 2 == 0]
    odd = [x for x in lst if x % 2 != 0]
    return odd if len(even) > len(odd) else even


print(parity_outliers([1, 2, 3, 4, 6, 8]))  # [1, 3]
print(parity_outliers([1, 2, 3, 5, 7]))     # [2]
