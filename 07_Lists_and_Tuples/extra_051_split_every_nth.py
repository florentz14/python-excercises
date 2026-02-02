# 51. Split List Every Nth Element
# ['a','b','c','d','e','f','g','h','i','j','k','l','m','n'] -> [['a','d','g','j','m'], ['b','e','h','k','n'], ['c','f','i','l']]

def split_every_nth(lst: list, n: int) -> list[list]:
    return [lst[i::n] for i in range(n)]


sample = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n']
print(split_every_nth(sample, 3))
