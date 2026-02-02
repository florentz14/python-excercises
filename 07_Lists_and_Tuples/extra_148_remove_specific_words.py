# 148. Remove Specific Words from List

def remove_words(lst: list[str], to_remove: list[str]) -> list[str]:
    remove_set = set(to_remove)
    return [w for w in lst if w not in remove_set]


sample = ['red', 'green', 'blue', 'white', 'black', 'orange']
print(remove_words(sample, ['white', 'orange']))
