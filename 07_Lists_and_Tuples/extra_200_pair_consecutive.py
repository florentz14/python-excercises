# ---------------------------------------------------------------------------
# 200. Pair Consecutive Elements: [1,2,3,4,5,6] -> [[1,2],[2,3],[3,4],[4,5],[5,6]]
# ---------------------------------------------------------------------------
# Descripción: Pair Consecutive Elements: [1,2,3,4,5,6] -> [[1,2],[2,3],[3,4],[4,5...
# Entrada/Salida: Según el ejercicio.
# ---------------------------------------------------------------------------

def pair_consecutive(lst: list) -> list[list]:
    # Lista por comprensión: se construye la lista a partir del iterable.
    return [[lst[i], lst[i + 1]] for i in range(len(lst) - 1)]


print(pair_consecutive([1, 2, 3, 4, 5, 6]))
print(pair_consecutive([1, 2, 3, 4, 5]))
