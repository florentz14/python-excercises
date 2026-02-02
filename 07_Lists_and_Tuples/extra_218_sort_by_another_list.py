# 218. Sort One List by Another (order list by indexes list)

def sort_by_indexes(lst: list, indexes: list[int]) -> list:
    return [lst[i] for i in indexes]


items = ['apples', 'bread', 'eggs', 'jam', 'milk', 'oranges']
order = [5, 4, 3, 2, 1, 0]
print(sort_by_indexes(items, order))  # ['oranges', 'milk', 'jam', 'eggs', 'bread', 'apples']
