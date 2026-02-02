# 56. Convert String to List (characters or by delimiter)

def string_to_list(s: str, split_by: str | None = None) -> list:
    if split_by is None:
        return list(s)  # list of chars
    return s.split(split_by)


print(string_to_list("hello"))           # ['h', 'e', 'l', 'l', 'o']
print(string_to_list("a,b,c", ","))     # ['a', 'b', 'c']
