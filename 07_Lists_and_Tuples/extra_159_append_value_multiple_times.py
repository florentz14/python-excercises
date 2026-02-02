# 159. Append Same Value/List Multiple Times

def append_times(value, n: int) -> list:
    return [value] * n


def append_list_times(lst: list, n: int) -> list[list]:
    return [lst[:] for _ in range(n)]


print(append_times(7, 5))  # [7, 7, 7, 7, 7]
print(append_list_times([1, 2, 5], 4))
