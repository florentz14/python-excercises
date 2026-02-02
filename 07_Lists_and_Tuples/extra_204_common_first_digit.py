# 204. Check If First Digit/Character Same for All Elements

def same_first_digit(lst: list) -> bool:
    if not lst:
        return True
    first = str(lst[0])[0]
    return all(str(x)[0] == first for x in lst)


print(same_first_digit([1234, 122, 1984, 19372, 100]))   # True
print(same_first_digit([1234, 922, 1984, 19372, 100]))   # False
print(same_first_digit(['aabc', 'abc', 'ab', 'a']))       # True
