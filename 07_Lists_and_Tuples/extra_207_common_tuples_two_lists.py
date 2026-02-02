# 207. Common Tuples Between Two Lists

def common_tuples(a: list[tuple], b: list[tuple]) -> list[tuple]:
    set_b = set(b)
    return [t for t in a if t in set_b]


list1 = [('red', 'green'), ('black', 'white'), ('orange', 'pink')]
list2 = [('red', 'green'), ('orange', 'pink')]
print(common_tuples(list1, list2))
