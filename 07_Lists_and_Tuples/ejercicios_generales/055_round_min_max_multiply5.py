# ---------------------------------------------------------------------------
# 84. Round Numbers, Min, Max, Multiply by 5, Unique Ascending
# ---------------------------------------------------------------------------
# Descripción: Round Numbers, Min, Max, Multiply by 5, Unique Ascending
# Entrada/Salida: Según el ejercicio.
# ---------------------------------------------------------------------------

def process_round_min_max(lst: list[float]) -> list[int]:
    rounded = [round(x) for x in lst]
    print("Min:", min(rounded), "Max:", max(rounded))
    return sorted(set(r * 5 for r in rounded))


sample = [22.4, 4.0, 16.22, 9.1, 11.0, 12.22, 14.2, 5.2, 17.5]
print(process_round_min_max(sample))
