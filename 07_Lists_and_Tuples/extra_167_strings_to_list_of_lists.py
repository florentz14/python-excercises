# 167. Convert List of Strings to List of Lists (each string -> list of chars)

def strings_to_lists(lst: list[str]) -> list[list[str]]:
    return [list(s) for s in lst]


sample = ['Red', 'Maroon', 'Yellow', 'Olive']
print(strings_to_lists(sample))
