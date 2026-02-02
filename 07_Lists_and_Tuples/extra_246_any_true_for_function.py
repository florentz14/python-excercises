# 246. Check If Function Returns True for At Least One Element

def any_match(lst: list, predicate) -> bool:
    return any(predicate(x) for x in lst)


print(any_match([1, 2, 3, 4], lambda x: x > 3))   # True
print(any_match([1, 2, 3], lambda x: x > 5))      # False
