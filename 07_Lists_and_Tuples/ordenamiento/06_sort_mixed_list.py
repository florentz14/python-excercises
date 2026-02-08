# ---------------------------------------------------------------------------
# 138. Sort Mixed List (Numbers Before Strings, each group sorted)
# ---------------------------------------------------------------------------
# Descripción: Sort Mixed List (Numbers Before Strings, each group sorted)
# Entrada/Salida: Según el ejercicio.
# ---------------------------------------------------------------------------

def sort_mixed(lst: list) -> list:
    numbers = sorted([x for x in lst if isinstance(x, (int, float))])
    strings = sorted([x for x in lst if isinstance(x, str)])
    return numbers + strings


sample = [19, 'red', 12, 'green', 'blue', 10, 'white', 'green', 1]
print(sort_mixed(sample))
