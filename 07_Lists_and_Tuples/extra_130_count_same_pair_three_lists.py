# ---------------------------------------------------------------------------
# 130. Count Same Pair in Three Lists (same index, same value in all three)
# ---------------------------------------------------------------------------
# Descripción: Count Same Pair in Three Lists (same index, same value in all three)
# Entrada/Salida: Según el ejercicio.
# ---------------------------------------------------------------------------

def count_same_pair_three(a: list, b: list, c: list) -> int:
    # Se devuelve la suma de todos los elementos.
    return sum(1 for i in range(min(len(a), len(b), len(c))) if a[i] == b[i] == c[i])


list1 = [1, 2, 3, 4, 5, 6, 7, 8]
list2 = [2, 2, 3, 1, 2, 6, 7, 9]
list3 = [2, 1, 3, 1, 2, 6, 7, 9]
print(count_same_pair_three(list1, list2, list3))  # 3
