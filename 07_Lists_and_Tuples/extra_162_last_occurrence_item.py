# 162. Find Last Occurrence Index of Item in List

def last_index_of(lst: list, item) -> int:
    for i in range(len(lst) - 1, -1, -1):
        if lst[i] == item:
            return i
    return -1


# Or: len(lst) - 1 - lst[::-1].index(item) if item in lst else -1
sample = ['s', 'd', 'f', 's', 'd', 'f', 's', 'f', 'k', 'o', 'p', 'i', 'w', 'e', 'k', 'c']
print(last_index_of(sample, 'f'))   # 7
print(last_index_of(sample, 'k'))   # 14
