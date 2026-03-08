# -------------------------------------------------
# File Name: 079_strings_to_single_char_list.py
# Author: Florentino Báez
# Date: Lists and Tuples
# Description: Convert List of Strings and Chars to Single List of Characters
# -------------------------------------------------

def to_single_char_list(lst: list) -> list[str]:
    result = []
    for x in lst:
        if isinstance(x, str) and len(x) > 1:
            # Si es lista se aplana recursivamente; si no, se añade el elemento.
            result.extend(list(x))
        else:
            # Según la condición: se añade un valor u otro (p. ej. lista [n,x] si n>1, si no solo x).
            result.append(str(x) if not isinstance(x, str) else x)
    return result


# Simpler: flatten each string to chars
def flatten_chars(lst: list[str]) -> list[str]:
    # Se devuelve un valor u otro según la condición.
    return [c for s in lst for c in (s if isinstance(s, str) else str(s))]


print(flatten_chars(['red', 'white', 'a', 'b', 'black', 'f']))
