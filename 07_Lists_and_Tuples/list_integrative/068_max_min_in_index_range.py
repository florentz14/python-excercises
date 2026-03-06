# ---------------------------------------------------------------------------
# 151. Max and Min in List Within Index Range
# ---------------------------------------------------------------------------
# Descripción: Max and Min in List Within Index Range
# Entrada/Salida: Según el ejercicio.
# ---------------------------------------------------------------------------

def max_min_in_range(lst: list[int | float], start: int, end: int) -> tuple:
    sub = lst[start:end + 1]
    # Se devuelve un valor u otro según la condición.
    return (max(sub), min(sub)) if sub else (None, None)


sample = [4, 3, 0, 5, 3, 0, 2, 3, 4, 2, 4, 3, 5]
print(max_min_in_range(sample, 3, 8))  # (5, 0)
