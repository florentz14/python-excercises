# 59. Check if n-th Element Exists in List

def nth_exists(lst: list, n: int) -> bool:
    return 0 <= n < len(lst)


print(nth_exists([1, 2, 3], 2))   # True
print(nth_exists([1, 2], 5))      # False
