# ---------------------------------------------------------------------------
# 83. Round Every Number, Print Total Sum * Length
# ---------------------------------------------------------------------------
# Descripción: Round Every Number, Print Total Sum * Length
# Entrada/Salida: Según el ejercicio.
# ---------------------------------------------------------------------------

def round_sum_times_length(lst: list[float]) -> int | float:
    rounded = [round(x) for x in lst]
    # Se devuelve la suma de todos los elementos.
    return sum(rounded) * len(rounded)


sample = [22.4, 4.0, -16.22, -9.1, 11.0, -12.22, 14.2, -5.2, 17.5]
print(round_sum_times_length(sample))  # 243
