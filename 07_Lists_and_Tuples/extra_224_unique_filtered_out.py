# 224. List with Unique Values Filtered Out (keep only duplicates)

def only_duplicates(lst: list) -> list:
    return [x for x in set(lst) if lst.count(x) > 1]


# Or preserve order: [x for x in lst if lst.count(x) > 1] then remove dupes
def only_duplicates_ordered(lst: list) -> list:
    seen = set()
    result = []
    for x in lst:
        if lst.count(x) > 1 and x not in seen:
            seen.add(x)
            result.append(x)
    return result


print(only_duplicates_ordered([1, 2, 2, 3, 4, 4, 5]))  # [2, 4]
