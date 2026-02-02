# 102. Extract Strings of Specified Length from List

def strings_of_length(lst: list[str], n: int) -> list[str]:
    return [s for s in lst if len(s) == n]


sample = ['Python', 'list', 'exercises', 'practice', 'solution']
print(strings_of_length(sample, 8))  # ['practice', 'solution']
