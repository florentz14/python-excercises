# 199. Convert Unicode List to List of Strings (ensure str type)

def unicode_to_strings(lst: list) -> list[str]:
    return [str(x) for x in lst]


sample = ['S001', 'S002', 'S003', 'S004']
print(unicode_to_strings(sample))
