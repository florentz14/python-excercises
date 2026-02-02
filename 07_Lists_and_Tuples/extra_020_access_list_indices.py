# 20. Access the Index of a List

def with_index(lst: list) -> list[tuple[int, any]]:
    return list(enumerate(lst))


sample = ['a', 'b', 'c']
for i, v in with_index(sample):
    print(i, v)
