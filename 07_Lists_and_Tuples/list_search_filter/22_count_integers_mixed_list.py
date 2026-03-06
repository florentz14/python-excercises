# ---------------------------------------------------------------------------
# 106. Count Integers in Mixed List
# ---------------------------------------------------------------------------
# Descripción: Count Integers in Mixed List
# Entrada/Salida: Según el ejercicio.
# ---------------------------------------------------------------------------

def count_integers(lst: list) -> int:
    # Se devuelve la suma de todos los elementos.
    return sum(1 for x in lst if isinstance(x, int) and not isinstance(x, bool))


sample = [1, 'abcd', 3, 1.2, 4, 'xyz', 5, 'pqr', 7, -5, -12.22]
print(count_integers(sample))  # 6
