# 123. Reverse Each String in List

def reverse_strings(lst: list[str]) -> list[str]:
    return [s[::-1] for s in lst]


sample = ['Red', 'Green', 'Blue', 'White', 'Black']
print(reverse_strings(sample))  # ['deR', 'neerG', 'eulB', 'etihW', 'kcalB']
