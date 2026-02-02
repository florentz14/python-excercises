# 169. Convert List of Strings and Chars to Single List of Characters

def to_single_char_list(lst: list) -> list[str]:
    result = []
    for x in lst:
        if isinstance(x, str) and len(x) > 1:
            result.extend(list(x))
        else:
            result.append(str(x) if not isinstance(x, str) else x)
    return result


# Simpler: flatten each string to chars
def flatten_chars(lst: list[str]) -> list[str]:
    return [c for s in lst for c in (s if isinstance(s, str) else str(s))]


print(flatten_chars(['red', 'white', 'a', 'b', 'black', 'f']))
