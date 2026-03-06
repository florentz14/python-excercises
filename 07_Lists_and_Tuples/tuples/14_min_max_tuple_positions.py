# ---------------------------------------------------------------------------
# 175. Min and Max for Each Tuple Position in List of Tuples
# ---------------------------------------------------------------------------
# Descripción: Min and Max for Each Tuple Position in List of Tuples
# Entrada/Salida: Según el ejercicio.
# ---------------------------------------------------------------------------

def min_max_by_position(tuples: list[tuple]) -> tuple[list, list]:
    if not tuples:
        return [], []
    n = len(tuples[0])
    max_vals = [max(t[i] for t in tuples) for i in range(n)]
    min_vals = [min(t[i] for t in tuples) for i in range(n)]
    return max_vals, min_vals


sample = [(2, 3), (2, 4), (0, 6), (7, 1)]
max_v, min_v = min_max_by_position(sample)
print("Max by position:", max_v)  # [7, 6]
print("Min by position:", min_v)  # [0, 1]
