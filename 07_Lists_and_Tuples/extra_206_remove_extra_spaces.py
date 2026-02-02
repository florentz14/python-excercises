# 206. Remove Additional/Extra Spaces from List (strip each string)

def remove_extra_spaces(lst: list[str]) -> list[str]:
    return [s.strip() if isinstance(s, str) else s for s in lst]


sample = ['abc ', ' ', ' ', 'sdfds ', ' ', ' ', 'sdfds ', 'huy']
print(remove_extra_spaces(sample))
