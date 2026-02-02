# 150. Reverse List of Lists (reverse order of outer list)

def reverse_outer(lst: list[list]) -> list[list]:
    return lst[::-1]


sample = [['orange', 'red'], ['green', 'blue'], ['white', 'black', 'pink']]
print(reverse_outer(sample))
