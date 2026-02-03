# ---------------------------------------------------------------------------
# 62. Print List as Space-Separated Elements
# ---------------------------------------------------------------------------
# Descripción: Print List as Space-Separated Elements
# Entrada/Salida: Según el ejercicio.
# ---------------------------------------------------------------------------

def print_space_separated(lst: list) -> None:
    print(' '.join(str(x) for x in lst))


print_space_separated([1, 2, 3, 4])  # 1 2 3 4
