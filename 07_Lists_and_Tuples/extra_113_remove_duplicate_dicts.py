# 113. Remove Duplicate Dictionaries from List (by content)

def unique_dicts(lst: list[dict]) -> list[dict]:
    seen = []
    result = []
    for d in lst:
        key = tuple(sorted((k, v) for k, v in d.items()))
        if key not in seen:
            seen.append(key)
            result.append(d)
    return result


sample = [{'Green': '#008000'}, {'Black': '#000000'}, {'Blue': '#0000FF'}, {'Green': '#008000'}]
print(unique_dicts(sample))
