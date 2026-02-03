# ---------------------------------------------------------------------------
# 118. Difference (n+1)th - nth for Each Position
# ---------------------------------------------------------------------------
# Descripción: Difference (n+1)th - nth for Each Position
# Entrada/Salida: Según el ejercicio.
# ---------------------------------------------------------------------------

def diff_consecutive(lst: list[float]) -> list[float]:
    # Lista por comprensión: se construye la lista a partir del iterable.
    return [lst[i + 1] - lst[i] for i in range(len(lst) - 1)]


print(diff_consecutive([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))  # [1]*9
print(diff_consecutive([2, 4, 6, 8]))  # [2, 2, 2]
