# 215. Merge Lists into List of Lists (zip by position)

def merge_into_list_of_lists(*lists: list) -> list[list]:
    return [list(t) for t in zip(*lists)]


print(merge_into_list_of_lists(['a', 'b'], [1, 2], [True, False]))  # [['a', 1, True], ['b', 2, False]]
