# 196. Move Specified Element to End of List

def move_to_end(lst: list, elem) -> list:
    return [x for x in lst if x != elem] + [x for x in lst if x == elem]


sample = ['red', 'green', 'white', 'black', 'orange']
print(move_to_end(sample, 'white'))  # ['red', 'green', 'black', 'orange', 'white']
print(move_to_end(sample, 'red'))
