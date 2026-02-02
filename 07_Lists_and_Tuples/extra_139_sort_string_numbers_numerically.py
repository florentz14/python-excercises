# 139. Sort List of String Numbers Numerically

def sort_numeric_strings(lst: list[str]) -> list[str]:
    return sorted(lst, key=lambda s: int(s))


sample = ['4', '12', '45', '7', '0', '100', '200', '-12', '-500']
print(sort_numeric_strings(sample))
