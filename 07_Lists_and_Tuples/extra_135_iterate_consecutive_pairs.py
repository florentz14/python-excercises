# ---------------------------------------------------------------------------
# 135. Iterate Over All Pairs of Consecutive Items
# ---------------------------------------------------------------------------
# Descripción: Iterate Over All Pairs of Consecutive Items
# Entrada/Salida: Según el ejercicio.
# ---------------------------------------------------------------------------

def consecutive_pairs(lst: list) -> list[tuple]:
    # Se construye list/set/dict a partir del iterable (elimina duplicados en set/dict).
    return list(zip(lst[:-1], lst[1:]))


sample = [1, 1, 2, 3, 3, 4, 4, 5]
print(consecutive_pairs(sample))
