# 42. Find Missing and Additional Values in Two Lists

def missing_and_additional(a: list, b: list) -> tuple[list, list]:
    set_a, set_b = set(a), set(b)
    missing_in_b = list(set_a - set_b)   # in first, not in second
    additional_in_b = list(set_b - set_a)  # in second, not in first
    return (missing_in_b, additional_in_b)


# Sample: first=['a','b','c'], second=['a','b','c','g','h'] -> missing: [], additional: ['g','h']
# If first is ref: missing in second: b,a,c; additional in second: g,h
list1 = ['a', 'b', 'c', 'd', 'e']
list2 = ['a', 'd', 'e', 'f', 'g', 'h']
missing, additional = missing_and_additional(list1, list2)
print("Missing in second:", sorted(set(list1) - set(list2)))
print("Additional in second:", sorted(set(list2) - set(list1)))
