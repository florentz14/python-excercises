# ---------------------------------------------------------------------------
# 32. Check if List Contains a Sublist
# ---------------------------------------------------------------------------
# Descripción: Check if List Contains a Sublist
# Entrada/Salida: Según el ejercicio.
# ---------------------------------------------------------------------------

def contains_sublist(lst: list, sub: list) -> bool:
    n, m = len(lst), len(sub)
    if m == 0 or m > n:
        return m == 0
    for i in range(n - m + 1):
        if lst[i:i + m] == sub:
            return True
    return False


print(contains_sublist([1, 2, 3, 4, 5], [3, 4]))  # True
