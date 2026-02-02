# 70. Find Items Starting with Specific Character

def items_starting_with(lst: list[str], char: str) -> list[str]:
    return [s for s in lst if s.startswith(char)]


sample = ['abcd', 'abc', 'bcd', 'bkie', 'cder', 'dagfa', 'acjd']
print("Start with 'a':", items_starting_with(sample, 'a'))
print("Start with 'd':", items_starting_with(sample, 'd'))
