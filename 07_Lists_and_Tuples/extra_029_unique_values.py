# 29. Get Unique Values from List (preserve order)

def unique_values(lst: list) -> list:
    return list(dict.fromkeys(lst))


print(unique_values([1, 2, 2, 3, 3, 3, 4]))  # [1, 2, 3, 4]
