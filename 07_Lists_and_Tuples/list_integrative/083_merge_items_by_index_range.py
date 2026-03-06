# ---------------------------------------------------------------------------
# 173. Merge List Items in Index Range (join strings from start to end index)
# ---------------------------------------------------------------------------
# Descripción: Merge List Items in Index Range (join strings from start to end index)
# Entrada/Salida: Según el ejercicio.
# ---------------------------------------------------------------------------

def merge_range(lst: list[str], start: int, end: int) -> list:
    result = lst[:start] + [''.join(lst[start:end])] + lst[end:]
    return result


sample = ['a', 'b', 'c', 'd', 'e', 'f', 'g']
print(merge_range(sample, 2, 4))   # ['a', 'b', 'cd', 'e', 'f', 'g']
print(merge_range(sample, 3, 7))   # ['a', 'b', 'c', 'defg']
