# ---------------------------------------------------------------------------
# 12. Remove 0th, 4th and 5th elements
# ---------------------------------------------------------------------------
# Descripción: Remove 0th, 4th and 5th elements
# Entrada/Salida: Según el ejercicio.
# ---------------------------------------------------------------------------

sample = ['Red', 'Green', 'White', 'Black', 'Pink', 'Yellow']
# Remove indices 0, 4, 5 -> keep 1, 2, 3
result = [v for i, v in enumerate(sample) if i not in (0, 4, 5)]
print(result)  # ['Green', 'White', 'Black']
