# 61. Create List of Empty Dictionaries

def list_of_empty_dicts(n: int) -> list[dict]:
    return [{} for _ in range(n)]


print(list_of_empty_dicts(5))  # [{}, {}, {}, {}, {}]
