# 64. Iterate Over Two Lists Simultaneously

def iterate_together(a: list, b: list):
    for x, y in zip(a, b):
        yield x, y


list1 = [1, 2, 3]
list2 = ['a', 'b', 'c']
for i, j in zip(list1, list2):
    print(i, j)
