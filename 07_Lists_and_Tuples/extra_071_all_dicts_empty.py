# 71. Check If All Dictionaries in List Are Empty

def all_dicts_empty(lst: list[dict]) -> bool:
    return all(len(d) == 0 for d in lst)


print(all_dicts_empty([{}, {}, {}]))       # True
print(all_dicts_empty([{1: 2}, {}, {}]))   # False
