# 50. Sort List of Nested Dictionaries

def sort_nested_dicts(lst: list[dict], key: str) -> list[dict]:
    return sorted(lst, key=lambda d: d.get(key, 0))


sample = [{'a': 2, 'b': 1}, {'a': 1, 'b': 2}, {'a': 3, 'b': 0}]
print(sort_nested_dicts(sample, 'a'))
