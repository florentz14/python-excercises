# ---------------------------------------------------------------------------
# 43. Split List into Different Variables
# ---------------------------------------------------------------------------
# Descripción: Split List into Different Variables
# Entrada/Salida: Según el ejercicio.
# ---------------------------------------------------------------------------

lst = [1, 2, 3, 4]
a, b, c, d = lst
print(a, b, c, d)  # 1 2 3 4

# Or with * for rest
first, *rest = lst
print(first, rest)  # 1 [2, 3, 4]
