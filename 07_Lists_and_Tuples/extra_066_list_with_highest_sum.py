# 66. Find List in List of Lists with Highest Sum

def list_with_max_sum(lists: list[list[int]]) -> list[int]:
    return max(lists, key=sum)


sample = [[1, 2, 3], [4, 5, 6], [10, 11, 12], [7, 8, 9]]
print(list_with_max_sum(sample))  # [10, 11, 12]
